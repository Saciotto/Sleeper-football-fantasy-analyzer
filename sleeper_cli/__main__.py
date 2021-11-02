from sleeper_analyzer.context import Context
from sleeper_cli.initializer import uninitialized_main
from sleeper_cli.main import main


def console_entry():
    context = Context()
    if context.username is None:
        uninitialized_main(context)
    else:
        main(context)


if __name__ == '__main__':
    console_entry()
