# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['board_game_bot']

package_data = \
{'': ['*']}

install_requires = \
['board-game-utils<0.2.0',
 'html2text',
 'mastodon-py',
 'pretty-errors',
 'python-dotenv',
 'pytility',
 'requests',
 'tweepy<4.0.0',
 'urllib3']

setup_kwargs = {
    'name': 'board-game-bot',
    'version': '0.4.0',
    'description': 'Board game recommender bots 🤖',
    'long_description': '# 🎲 Board Game Bot 🤖\n',
    'author': 'Markus Shepherd',
    'author_email': 'markus@recommend.games',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://recommend.games/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
