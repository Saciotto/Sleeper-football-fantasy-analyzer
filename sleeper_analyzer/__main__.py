from .context import Context
from .initializer import uninitialized_main
from .analyzer import main


def console_entry():
    context = Context()
    if context.username is None:
        uninitialized_main(context)
    else:
        main(context)


if __name__ == '__main__':
    console_entry()
