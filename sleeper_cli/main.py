from argparse import ArgumentParser
from types import SimpleNamespace

from sleeper_analyzer import __version__
from sleeper_analyzer.models.league import League
from sleeper_analyzer.models.team import Team
from sleeper_cli.initializer import update_command
from sleeper_cli.league_command import league_parser


def _default_league(sleeper):
    default_league = sleeper.config.get('default_league', None)
    if default_league is None:
        try:
            default_league = sleeper.db.user_leagues[0]
            default_league = default_league['league_id']
        except (IndexError, FileNotFoundError):
            default_league = None
    return default_league


def _add_default_options(sleeper, args):
    if 'user' in args and args.user is None:
        args.user = sleeper.db.username
    if 'league' in args and args.league is None:
        args.league = _default_league(sleeper)


def _leagues(sleeper, _):
    leagues = [league['name'] for league in sleeper.db.user_leagues]
    print(leagues)


def _users(sleeper, args):
    league = sleeper.get_league(args.league)
    users = [user['display_name'] for user in league.users]
    print(users)


def _players(sleeper, args):
    team = sleeper.get_team(args.user, args.league)
    print(team.players)


def _update(sleeper, _):
    args = SimpleNamespace()
    args.username = sleeper.db.username
    update_command(sleeper, args)


def _team_statistics(sleeper, args):
    team = sleeper.get_team(args.user, args.league)
    print(team.scoring_dataframe())


def _best_projected_lineup(sleeper, args):
    team = sleeper.get_team(args.user, args.league)
    print(team.best_projected_lineup())


def _set_user(sleeper, args):
    sleeper.config['username'] = args.user


def _set_league(sleeper, args):
    sleeper.config['default_league'] = args.league


def main(sleeper):
    parser = ArgumentParser(prog='sleeper')
    subparsers = parser.add_subparsers(title='commands', metavar='command', help='description')

    sub_parser = subparsers.add_parser('leagues', help='List user leagues')
    sub_parser.add_argument("-u", "--user", nargs="?", default=None)
    sub_parser.set_defaults(func=_leagues)

    sub_parser = subparsers.add_parser('users', help='List of users for a league')
    sub_parser.add_argument("-l", "--league", nargs="?", default=None)
    sub_parser.set_defaults(func=_users)

    sub_parser = subparsers.add_parser('players', help='List of players')
    sub_parser.add_argument("-u", "--user", nargs="?", default=None)
    sub_parser.add_argument("-l", "--league", nargs="?", default=None)
    sub_parser.set_defaults(func=_players)

    sub_parser = subparsers.add_parser('update', help='Update statistics')
    sub_parser.set_defaults(func=_update)

    sub_parser = subparsers.add_parser('team', help='Show team statistics')
    sub_parser.add_argument("-u", "--user", nargs="?", default=None)
    sub_parser.add_argument("-l", "--league", nargs="?", default=None)
    sub_parser.set_defaults(func=_team_statistics)

    sub_parser = subparsers.add_parser('lineup', help='Show best projected lineup')
    sub_parser.add_argument("-u", "--user", nargs="?", default=None)
    sub_parser.add_argument("-l", "--league", nargs="?", default=None)
    sub_parser.set_defaults(func=_best_projected_lineup)

    sub_parser = subparsers.add_parser('set_user', help='Set the default user')
    sub_parser.add_argument("user")
    sub_parser.set_defaults(func=_set_user)

    sub_parser = subparsers.add_parser('set_league', help='Set the default user')
    sub_parser.add_argument("league")
    sub_parser.set_defaults(func=_set_league)

    sub_parser = subparsers.add_parser('league', help='League commands')
    sub_parser = sub_parser.add_subparsers(title='league', metavar='league', help='description')
    league_parser(sub_parser)

    parser.add_argument('--version', action='version', version=__version__)
    args = parser.parse_args()
    if 'func' in args:
        _add_default_options(sleeper, args)
        args.func(sleeper, args)
    else:
        parser.print_usage()
