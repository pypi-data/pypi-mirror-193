import pathlib
import argparse

from . import context, rfc


def create_parser() -> argparse.ArgumentParser:
    config_dir = str((pathlib.Path.home() / '.rfcctl').absolute())

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--overwrite-config',
        help='Overwrite global configuration directory path',
        default=config_dir
    )
    sp = parser.add_subparsers()
    context.create_parser(sp.add_parser('context'))
    rfc.create_create_parser(sp.add_parser('create'))
    rfc.create_update_parser(sp.add_parser('update'))

    return parser
