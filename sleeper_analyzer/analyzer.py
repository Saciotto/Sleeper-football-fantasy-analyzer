from argparse import ArgumentParser
from types import SimpleNamespace

from . import __version__
from .models.league import League
from .models.team import Team
from .initializer import initialize


def _leagues(context, _):
    leagues = [league['name'] for league in context.sleeper.user_leagues]
    print(leagues)


def _users(context, args):
    league = League(context, args.league)
    users = [user['display_name'] for user in league.users]
    print(users)


def _players(context, args):
    team = Team(context, args.user, args.league)
    print(team.players)


def _update(context, _):
    args = SimpleNamespace()
    args.username = context.username
    initialize(context, args)


def _team_statistics(context, args):
    team = Team(context, args.user, args.league)
    print(team.scoring())


def _best_projected_lineup(context, args):
    team = Team(context, args.user, args.league)
    print(team.best_projected_lineup())


def main(context):
    parser = ArgumentParser(prog='sleeper')
    subparsers = parser.add_subparsers(title='commands', metavar='command', help='description')

    sub_parser = subparsers.add_parser('leagues', help='List user leagues')
    sub_parser.set_defaults(func=_leagues)

    sub_parser = subparsers.add_parser('users', help='List of users for a league')
    sub_parser.add_argument("league")
    sub_parser.set_defaults(func=_users)

    sub_parser = subparsers.add_parser('players', help='List of players')
    sub_parser.add_argument("user")
    sub_parser.add_argument("league")
    sub_parser.set_defaults(func=_players)

    sub_parser = subparsers.add_parser('update', help='Update statistics')
    sub_parser.set_defaults(func=_update)

    sub_parser = subparsers.add_parser('team', help='Show team statistics')
    sub_parser.add_argument("user")
    sub_parser.add_argument("league")
    sub_parser.set_defaults(func=_team_statistics)

    sub_parser = subparsers.add_parser('lineup', help='Show best projected lineup')
    sub_parser.add_argument("user")
    sub_parser.add_argument("league")
    sub_parser.set_defaults(func=_best_projected_lineup)

    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    if 'func' in args:
        args.func(context, args)
    else:
        parser.print_usage()
