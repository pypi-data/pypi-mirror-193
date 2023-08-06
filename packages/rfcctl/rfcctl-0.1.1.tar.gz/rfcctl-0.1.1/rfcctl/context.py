import argparse
import pathlib

from .data.contexts import Contexts, Context
from .data.skeleton import RFC_SKELETON


def create_parser(parser: argparse.ArgumentParser):
    sp = parser.add_subparsers()
    __create_context_add_parser(sp.add_parser('add'))
    __create_context_switch_parser(sp.add_parser('switch'))


def __create_context_add_parser(parser: argparse.ArgumentParser):
    parser.set_defaults(handler=__handle_context_add)
    parser.add_argument('directory', help='Context directory')
    parser.add_argument('--name', '-n', help='Context name')
    parser.add_argument('--user', '-u', help='User name for context')
    parser.add_argument('--switch', '-s', action='store_true', help='Switch to created context')
    parser.add_argument('--initial-status', '-i', help='Initial RFC status', default='Draft')
    parser.add_argument('--obsoleted-status', '-o', help='Obsoleted RFC status', default='Obsoleted')
    parser.add_argument('--init', action='store_true', help='Create skeleton.md')


def __create_context_switch_parser(parser: argparse.ArgumentParser):
    parser.set_defaults(handler=__handle_context_switch)
    parser.add_argument('name', help='Context name')


def __handle_context_add(args: argparse.Namespace):
    base_dir = pathlib.Path(args.overwrite_config)
    ctxs = Contexts.load(base_dir, empty_if_not_exists=True)
    directory = pathlib.Path(args.directory).absolute()
    if not directory.exists():
        raise FileNotFoundError(f'Context directory {directory} not found')
    if args.init:
        with open(directory / 'skeleton.md', 'w') as fp:
            fp.write(RFC_SKELETON)
    ctx = Context(
        user=args.user,
        name=args.name,
        directory=str(directory),
        initial_status=args.initial_status,
        obsoleted_status=args.obsoleted_status,
    )
    ctxs = ctxs.add(ctx)
    if args.switch:
        ctxs = ctxs.switch(args.name)
    ctxs.save(base_dir)


def __handle_context_switch(args: argparse.Namespace):
    base_dir = pathlib.Path(args.overwrite_config)
    ctx = Contexts.load(base_dir)
    ctx.switch(args.name).save(base_dir)
    pass
