import argparse
import dataclasses
import datetime
import json
import pathlib
import re
import typing

import jinja2

from .data import contexts
from .data.rfcs import Rfcs, RfcMetadata


def create_create_parser(parser: argparse.ArgumentParser):
    parser.add_argument(
        '--category-tree',
        '--category',
        '-c',
        nargs='+',
        help='Category tree'
    )
    parser.add_argument(
        '--obsoletes',
        help='Obsolete other RFCs',
        nargs='*',
        default=()
    )
    parser.add_argument(
        '--number',
        help='Specify number of new RFC explicitly',
        type=int,
        default=None
    )
    parser.add_argument(
        '--title',
        '-t',
        help='RFC title'
    )
    parser.set_defaults(handler=__context_wrapper(__handle_create))


def create_update_parser(parser: argparse.ArgumentParser):
    parser.set_defaults(handler=__context_wrapper(__handle_update))


def __context_wrapper(f: typing.Callable[[argparse.Namespace, contexts.Context], None]):
    def wrapper(args: argparse.Namespace):
        base_dir = pathlib.Path(args.overwrite_config)
        ctxs = contexts.Contexts.load(base_dir, empty_if_not_exists=True)
        ctx = ctxs.current_context
        f(args, ctx)
    return wrapper


def __string_with_marker(target: str, value: str):
    return f'<!-- {target} --> {value}'


def __timestamp(now: datetime.datetime) -> str:
    return now.strftime('%Y/%m/%d')


def __handle_create(args: argparse.Namespace, ctx: contexts.Context):
    directory = pathlib.Path(ctx.directory)
    number = args.number
    if number is None:
        rfcs = enumerate_rfcs(directory, only_metadata=True)
        number = rfcs.get_latest_number()

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(directory),
        autoescape=jinja2.select_autoescape()
    )

    now = datetime.datetime.now()
    timestamp = __timestamp(now)

    template = env.get_template('skeleton.md')
    generated = template.render(
        title=args.title,
        number=number,
        status=__string_with_marker('status', ctx.initial_status),
        category=' &gt; '.join(args.category_tree),
        created_by=ctx.user,
        updated_by=__string_with_marker('updated by', ctx.user),
        created_at=timestamp,
        last_modified_at=__string_with_marker('last modified', timestamp),
        last_modified_at_json=now.isoformat(),
        obsoletes=__string_with_marker('obsoletes', ', '.join(args.obsoletes)),
        obsoletes_json=json.dumps([int(o) for o in args.obsoletes]),
        obsoleted_by_json=[],
        obsoleted_by=__string_with_marker('obsoleted by', '')
    )
    target = directory.joinpath('rfcs/' + '/'.join(args.category_tree))
    target.mkdir(parents=True, exist_ok=True)
    target = target / f'rfc{number}-{args.title}.md'
    with open(target, 'w') as fp:
        fp.write(generated)


def __handle_update(_: argparse.Namespace, ctx: contexts.Context):
    __update(ctx)


def __update(ctx: contexts.Context):
    directory = pathlib.Path(ctx.directory)
    rfcs = enumerate_rfcs(directory, only_metadata=False)

    need_updates: typing.Dict[int, typing.Tuple[typing.List[int], typing.List[int], typing.Optional[str]]] = {}
    for rfc in rfcs.rfcs:
        number = rfc.number

        obsoletes_in_md = rfc.get_content_obsoletes()
        obsoletes = rfc.obsoletes

        if obsoletes_in_md != obsoletes:
            if number not in need_updates:
                need_updates[number] = rfc.obsoleted_by, rfc.obsoletes, None
            oby, obs, status = need_updates[number]
            obs.extend(rfc.obsoletes)
            need_updates[number] = oby, obs, status

        for obsolete in obsoletes:
            obsoleted_rfc = rfcs.find(obsolete)
            if number not in obsoleted_rfc.obsoleted_by:
                if obsolete not in need_updates:
                    need_updates[obsolete] = obsoleted_rfc.obsoleted_by, obsoleted_rfc.obsoletes, None
                oby, obs, _ = need_updates[obsolete]
                oby.append(number)
                need_updates[obsolete] = oby, obs, ctx.obsolete_status

    now = datetime.datetime.now()
    for number, new_data in need_updates.items():
        new_obsoleted_rfcs, new_obsoletes_by_this, status = new_data
        print(new_obsoleted_rfcs)
        rfc = rfcs.find(number)
        __update_single_file(
            old_rfc=rfc,
            status=status,
            obsoleted_by=sorted(set(new_obsoleted_rfcs)),
            obsoletes=sorted(set(new_obsoletes_by_this)),
            updated_by=ctx.user,
            updated_at=now
        )


def __update_single_file(
        old_rfc: RfcMetadata,
        status: typing.Optional[str],
        obsoleted_by: typing.List[int],
        obsoletes: typing.List[int],
        updated_by: str, updated_at: datetime.datetime
):
    new_rfc = dataclasses.replace(old_rfc, obsoleted_by=obsoleted_by, obsoletes=obsoletes)
    content = old_rfc.content

    content = re.sub(r'<!--\s*updated\s+by\s*-->[^\n\r]*', f'<!-- updated by --> {updated_by}', content)

    timestamp = __timestamp(updated_at)
    content = re.sub(r'<!--\s*last\s+modified\s*-->[^\n\r]*', f'<!-- last modified --> {timestamp}', content)

    obsoleted_by = ', '.join((str(o) for o in sorted(new_rfc.obsoleted_by)))
    content = re.sub(r'<!--\s*obsoleted\s+by\s*-->[^\n\r]*', f'<!-- obsoleted by --> {obsoleted_by}', content)

    obsoletes = ', '.join((str(o) for o in sorted(new_rfc.obsoletes)))
    content = re.sub(r'<!--\s*obsoletes\s*-->[^\n\r]*', f'<!-- obsoletes --> {obsoletes}', content)

    if status is not None:
        content = re.sub(r'<!--\s*status\s*-->[^\n\r]*', f'<!-- status --> {status}', content)

    metadata = json.dumps(new_rfc.to_json_dict(updated_at), indent=2)
    output = f'<!-- BEGIN METADATA\n{metadata}\nEND METADATA -->\n{content}'
    with open(new_rfc.file, 'w') as fp:
        fp.write(output)


def enumerate_rfcs(base_dir: pathlib.Path, *, only_metadata=True) -> Rfcs:
    begin_metadata_regex = re.compile(r'<!--\s*BEGIN\s+METADATA\s*', flags=re.RegexFlag.IGNORECASE)
    end_metadata_regex = re.compile(r'\s*END\s+METADATA\s*-->\s*', flags=re.RegexFlag.IGNORECASE)

    rfcs: typing.Dict[int, RfcMetadata] = {}
    base_dir = base_dir / 'rfcs'
    for md in base_dir.rglob('*.md'):
        with open(md) as fp:
            values = ''
            while begin_metadata_regex.match(fp.readline()) is None:
                pass
            while True:
                line = fp.readline()
                if end_metadata_regex.match(line) is not None:
                    break
                values += line
            content = None
            content_lines = None
            if not only_metadata:
                content_lines = list(fp.readlines())
                content = ''.join(content_lines)
            meta = json.loads(values)
            meta = RfcMetadata(
                file=md,
                number=meta['number'],
                obsoletes=sorted(meta['obsoletes']),
                obsoleted_by=sorted(meta['obsoletedBy']),
                content=content,
                content_lines=content_lines
            )
            rfcs[meta.number] = meta
    return Rfcs(rfcs)
