class SleeperAnalizerException(Exception):
    pass


class UninitializedExeception(SleeperAnalizerException):
    pass


class LeagueNotFoundException(SleeperAnalizerException):
    pass


class UserNotFoundException(SleeperAnalizerException):
    pass


class RosterNotFoundException(SleeperAnalizerException):
    pass
