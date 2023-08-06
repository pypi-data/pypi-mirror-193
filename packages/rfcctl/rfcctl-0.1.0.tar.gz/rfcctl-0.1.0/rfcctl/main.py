import argparse
import pathlib

from .parser import create_parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        __initialize_if_needed(args)
        args.handler(args)
    else:
        parser.print_help()


def __initialize_if_needed(args: argparse.Namespace):
    base_dir = pathlib.Path(args.overwrite_config)
    base_dir.mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    main()
