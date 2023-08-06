# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wom',
 'wom.models',
 'wom.models.competitions',
 'wom.models.deltas',
 'wom.models.groups',
 'wom.models.names',
 'wom.models.players',
 'wom.models.records',
 'wom.services']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['aiohttp>3.8.1', 'attrs>=22']

entry_points = \
{'console_scripts': ['wompy = wom._cli:info']}

setup_kwargs = {
    'name': 'wom-py',
    'version': '0.1.1',
    'description': 'An asynchronous wrapper for the Wise Old Man API.',
    'long_description': "# wom.py\n\nAn asynchronous wrapper for the [Wise Old Man API](https://docs.wiseoldman.net/).\n\nThe library aims to make it easy to interact with the Wise Old Man API by\nproviding service methods for all available endpoints and model classes\nfor data consistency.\n\n## Disclaimer\n\nThe library is in early development, and as such features or public interfaces\nmay change at any time. Thanks for following our progress!\n\n## Documentation\n\n- [Stable](https://jonxslays.github.io/wom.py/)\n- [Development](https://jonxslays.github.io/wom.py/dev/)\n\n## Installation\n\n### Stable\n\n```sh\npip install -U wom.py\n```\n\n### Development\n\n```sh\npip install -U git+https://github.com/Jonxslays/wom.py\n```\n\nFor more information on using `pip`, check out the [pip documentation](https://pip.pypa.io/en/stable/).\n\n## What is Wise Old Man\n\nWise Old Man is an open source Oldschool Runescape player progress tracker.\n\nIf you're interested in learning more about the Wise Old Man project, consider checking out any of these links:\n\n- [Website](https://wiseoldman.net/)\n- [API documentation](https://docs.wiseoldman.net/)\n- [Github repository](https://wiseoldman.net/github)\n- [Discord community](https://wiseoldman.net/discord)\n- [Support the developers on Patreon](https://wiseoldman.net/patreon)\n\nSome of the popular features include:\n\n- Experience tracking\n- Boss killcounts\n- Player achievements\n- Group competitions\n- Global leaderboards\n- A discord bot for interacting with the API\n\n## Problems\n\nIf you're experiencing a problem with the library, please open an issue\n[here](https://github.com/Jonxslays/wom.py/issues), after first confirming\na similar issue was not already created.\n\n## Contributing\n\nwom.py is open to contributions.\n\nCome back soon™ once I've written the contributing guide.\n\n## License\n\nwom.py is licensed under the\n[MIT License](https://github.com/Jonxslays/wom.py/blob/master/LICENSE).\n",
    'author': 'Jonxslays',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Jonxslays/wom.py',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
