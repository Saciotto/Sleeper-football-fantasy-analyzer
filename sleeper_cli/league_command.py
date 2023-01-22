from pandas import DataFrame


def _players_scoring(sleeper, args):
    league = sleeper.get_league(args.league)
    data, columns = league.scoring(league.players)
    scoring = DataFrame(data, columns=columns)
    print(scoring)


def league_parser(parser):
    sub_parser = parser.add_parser('players')
    sub_parser.add_argument("-l", "--league", nargs="?", default=None)
    sub_parser.set_defaults(func=_players_scoring)
