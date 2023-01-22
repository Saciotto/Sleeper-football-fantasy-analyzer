from sleeper_analyzer.sleeper import Sleeper
from sleeper_cli.initializer import initialize
from sleeper_cli.main import main


def console_entry():
    sleeper = Sleeper()
    if sleeper.db.initialized:
        main(sleeper)
    else:
        initialize(sleeper)


if __name__ == '__main__':
    console_entry()
