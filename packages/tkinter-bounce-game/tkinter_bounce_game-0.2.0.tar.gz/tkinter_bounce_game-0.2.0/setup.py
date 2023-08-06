# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tkinter_bounce_game']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tkinter-bounce-game',
    'version': '0.2.0',
    'description': 'Simple bounce game with Python and tkinter',
    'long_description': '# tkinter-bounce-game\n\n[![PyPI](https://img.shields.io/pypi/v/tkinter-bounce-game?color=blue)](https://pypi.org/project/tkinter-bounce-game/)\n\nSimple bounce game with Python and tkinter\n\n## Usage\n\n```sh\npython -m tkinter_bounce_game\n```\n\nPress `<Space>` to start and press `<Left>`/`<Right>` to move paddle.\n\n## Installation\n\ntkinter-bounce-game requires Python 3.10 or later with `tkinter` module.\n\n```sh\npip install tkinter-bounce-game\n```\n',
    'author': '4513ECHO',
    'author_email': '4513echo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/4513ECHO/tkinter-bounce-game',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
