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
    'name': 'pengue-brain-games',
    'version': '0.1.1',
    'description': '',
    'long_description': '### Hexlet tests and linter status:\n[![Actions Status](https://github.com/Pengue/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Pengue/python-project-49/actions)\n[![Maintainability](https://api.codeclimate.com/v1/badges/26cbe53cff2aa1026fef/maintainability)](https://codeclimate.com/github/Pengue/python-project-49)\n\n# Brain Games. Level 1 project on [Hexlet](https://ru.hexlet.io/professions/python/projects/49), program: Python developer.\n\nInstallation:\n\n`pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pengue-brain-games`\n\n## Installing package and playing in brain-even\n<a href="https://asciinema.org/a/560367" target="_blank"><img src="https://asciinema.org/a/560367.svg" /></a>\n\n## Playing in brain-calc\n<a href="https://asciinema.org/a/560369" target="_blank"><img src="https://asciinema.org/a/560369.svg" /></a>\n\n## Playing in brain-gcd\n<a href="https://asciinema.org/a/560376" target="_blank"><img src="https://asciinema.org/a/560376.svg" /></a>\n\n## Playing in brain-progression\n<a href="https://asciinema.org/a/560350" target="_blank"><img src="https://asciinema.org/a/560350.svg" /></a>\n\n## Playing in brain-prime\n<a href="https://asciinema.org/a/560358" target="_blank"><img src="https://asciinema.org/a/560358.svg" /></a>',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
