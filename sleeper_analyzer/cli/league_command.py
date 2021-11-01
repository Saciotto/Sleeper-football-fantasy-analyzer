from pandas import DataFrame

from ..models.league import League


def _players_scoring(context, args):
    league = League(context, args.league)
    data, columns = league.scoring(league.players)
    scoring = DataFrame(data, columns=columns)
    print(scoring)


def league_parser(parser):
    sub_parser = parser.add_parser('players')
    sub_parser.add_argument("-l", "--league", nargs="?", default=None)
    sub_parser.set_defaults(func=_players_scoring)
