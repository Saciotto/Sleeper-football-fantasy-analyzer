import os
from pathlib import Path
from PySide6.QtCore import QUrl, QtInfoMsg, QtWarningMsg, QtCriticalMsg, QtFatalMsg, qInstallMessageHandler


def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'Info'
    elif mode == QtWarningMsg:
        mode = 'Warning'
    elif mode == QtCriticalMsg:
        mode = 'critical'
    elif mode == QtFatalMsg:
        mode = 'fatal'
    else:
        mode = 'Debug'
    print("%s: %s (%s:%d, %s)" % (mode, message, context.file, context.line, context.file))


def enable_qml_logs():
    qInstallMessageHandler(qt_message_handler)


def get_qrc_root():
    qrc_root = Path(__file__).parent
    return qrc_root.as_uri()


def get_view(name):
    gui_folder = Path(__file__).parent
    qml_file = gui_folder / 'views' / name
    return QUrl(qml_file.as_uri())


def compile_resources():
    gui_folder = Path(__file__).parent.absolute()
    os.system(f'pyside6-rcc.exe "{gui_folder}/assets.qrc" -o "{gui_folder}/resources/assets_rc.py"')
    os.system(f'pyside6-rcc.exe "{gui_folder}/components.qrc" -o "{gui_folder}/resources/components_rc.py"')
    os.system(f'pyside6-rcc.exe "{gui_folder}/views.qrc" -o "{gui_folder}/resources/views_rc.py"')
