from argparse import ArgumentParser

from .. import __version__
from ..sleeper import Sleeper


def initialize(context, args):
    print('Updating {} data...'.format(args.username))
    sleeper = Sleeper()
    sleeper.download_statistics(args.username)
    context.username = args.username
    print('Done!')


def uninitialized_main(context):
    parser = ArgumentParser(prog='sleeper')
    subparsers = parser.add_subparsers(title='commands', metavar='command', help='description')

    init_parser = subparsers.add_parser('init', help='Initializes a sleeper analyzer workbench')
    init_parser.add_argument("username", help="Sleeper username")
    init_parser.set_defaults(func=initialize)

    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    if 'func' in args:
        args.func(context, args)
    else:
        parser.print_usage()
