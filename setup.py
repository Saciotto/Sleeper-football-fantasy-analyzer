import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def find_version(*file_paths):
    with open(os.path.join(here, *file_paths), encoding='latin1') as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string')


setup(
    name='sleeper',
    version=find_version('sleeper_analyzer', '__init__.py'),
    packages=find_packages(include=['sleeper_analyzer', 'sleeper_analyzer.*', 'sleeper_cli', 'sleeper_cli.*',
                                    'sleeper_gui', 'sleeper_gui.*']),
    url='https://github.com/Saciotto/Sleeper-football-fantasy-analyzer',
    license='MIT',
    author='Matheus Rossi Saciotto',
    author_email='saciotto@gmail.com',
    description='CLI application to analyze sleeper football fantasy leagues',
    entry_points={
        'console_scripts': [
            'sleeper = sleeper_cli.__main__:console_entry',
        ]
    }
)
