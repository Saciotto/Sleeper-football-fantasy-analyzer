from sleeper_analyzer.sleeper import Sleeper
from sleeper_gui.app import App


def console_entry():
    sleeper = Sleeper()
    app = App(sleeper)
    app.mainloop()


if __name__ == '__main__':
    console_entry()
