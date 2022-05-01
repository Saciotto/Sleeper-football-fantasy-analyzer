from sleeper_analyzer.context import Context
from sleeper_cli.initializer import initialize
from sleeper_cli.main import main


def console_entry():
    context = Context()
    if context.username is None:
        initialize(context)
    else:
        main(context)


if __name__ == '__main__':
    console_entry()
