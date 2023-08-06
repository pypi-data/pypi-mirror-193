# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brain_games', 'brain_games.games', 'brain_games.scripts']

package_data = \
{'': ['*']}

install_requires = \
['prompt>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['brain-calc = brain_games.scripts.brain_calc:main',
                     'brain-even = brain_games.scripts.brain_even:main',
                     'brain-games = brain_games.scripts.brain_games:main',
                     'brain-gcd = brain_games.scripts.brain_gcd:main',
                     'brain-prime = brain_games.scripts.brain_prime:main',
                     'brain-progression = '
                     'brain_games.scripts.brain_progression:main']}

setup_kwargs = {
    'name': 'sterphius-brain-games',
    'version': '0.1.1',
    'description': 'Brain-games: several terminal games that will allow you to stretch your brain',
    'long_description': '### Hexlet tests and linter status:\n[![Actions Status](https://github.com/Sterphius/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Sterphius/python-project-49/actions)\n[![Maintainability](https://api.codeclimate.com/v1/badges/032bf7df2200568ae9b6/maintainability)](https://codeclimate.com/github/Sterphius/python-project-49/maintainability)\n\n## Description\n\nThis is the training project at Python Developer course at [Hexlet](hexlet.io). \\\nIt contains five mathematic games:\n- Brain-calc\n- Brain-even\n- Brain-gcd\n- Brain-prime\n- Brain-progression\n\n## Install\n\nYou can install Brain Games, using [pip](https://pypi.org/project/pip/): \\\n`pip install sterphius-brain-games`\n[![asciicast](https://asciinema.org/a/561422.svg)](https://asciinema.org/a/561422)\n\n## Brain-calc\n\nIn this game you have to calculate result of the expression.\n[![asciicast](https://asciinema.org/a/561428.svg)](https://asciinema.org/a/561428)\n\n## Brain-even\n\nIn this game you have to answer whether the number is even or not.\n[![asciicast](https://asciinema.org/a/561431.svg)](https://asciinema.org/a/561431)\n\n## Brain-gcd\n\nIn this game it is required to find greatest common divider of 2 numbers.\n[![asciicast](https://asciinema.org/a/561432.svg)](https://asciinema.org/a/561432)\n\n## Brain-prime\n\nIn this game you have to tell if the number is prime or not.\n[![asciicast](https://asciinema.org/a/561433.svg)](https://asciinema.org/a/561433)\n\n## Brain-progression\n\nIn this game you have to fill in the missing number in arithmetic progression\n[![asciicast](https://asciinema.org/a/561434.svg)](https://asciinema.org/a/561434)',
    'author': 'Aleksei Malyshev',
    'author_email': 'malyshff@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Sterphius/python-project-49',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
