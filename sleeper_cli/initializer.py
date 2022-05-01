from argparse import ArgumentParser

from sleeper_analyzer import __version__
from sleeper_analyzer.sleeper import Sleeper


def download_updates(context, args):
    sleeper = Sleeper()
    sleeper.download_statistics(args.username)
    context.username = args.username
    print('Done!')


def initialize_command(context, args):
    print('Initializing {} data...'.format(args.username))
    download_updates(context, args)


def update_command(context, args):
    print('Updating {} data...'.format(args.username))
    download_updates(context, args)


def initialize(context):
    parser = ArgumentParser(prog='sleeper')
    subparsers = parser.add_subparsers(title='commands', metavar='command', help='description')

    init_parser = subparsers.add_parser('init', help='Initializes a sleeper analyzer workbench')
    init_parser.add_argument("username", help="Sleeper username")
    init_parser.set_defaults(func=initialize_command)

    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    if 'func' in args:
        args.func(context, args)
    else:
        parser.print_usage()
