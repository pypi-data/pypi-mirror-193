# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tkinter_bounce_game']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tkinter-bounce-game',
    'version': '0.1.0',
    'description': 'Simple bounce game with Python and tkinter',
    'long_description': '# tkinter-bounce-game\n\nSimple bounce game with Python and tkinter\n\n## Usage\n\n```sh\npython -m tkinter-bounce-game\n```\n\nPress `<Space>` to start and press `<Left>`/`<Right>` to move paddle.\n',
    'author': '4513ECHO',
    'author_email': '4513echo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
