# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['customtex']

package_data = \
{'': ['*'], 'customtex': ['presets/*']}

install_requires = \
['string-color>=1.2.3,<2.0.0']

entry_points = \
{'console_scripts': ['customtex = customtex.main:customtex']}

setup_kwargs = {
    'name': 'customtex',
    'version': '0.1.1',
    'description': 'A CLI utility for setting up LaTeX projects',
    'long_description': "# CustomTeX v0.1.1\n\n### A CLI utility for setting up LaTeX projects\nCustomTeX is a command line utility for setting up LaTeX projects based on some predefined styles for titles, section headers, theorems, etc.\n\nFor the moment, the utility is intended for a personal use, since there aren't many options for customization. However, we aim to design a more general system for creating LaTeX projects based on dynamic and fully customizable templates.\n\n## Installation\nCustomTeX is a Python library and can be installed using pip:\n\n    pip install customtex\n\nNo additional dependencies are required.\n\n## Usage\nTo generate the main files of a LaTeX project with CustomTeX, you have to run the `customtex` command followed by the path, main file name and language options and the `init` or the `template` subcommand. For example:\n\n    customtex --path /path/to/directory --name main --lang english init [options]\n\nThis will create a LaTeX project with the following structure in the `path/to/directory` directory:\n\n    /path/to/directory\n    ├── main.tex\n    └── tex\n        ├── macros.tex\n        └── preamble.tex\n\n\n### The `init` subcommand\nThe `init` subcommand creates a project based on the options that the utility provides. Run `customtex init --help` to see the available options.\n\n### The `template` subcommand\nThe `template` subcommand creates a project based on a template. A template consist of a list of options from the `init` subcommand that are run when invoking the `template` option followed by the name of the template.\n\nRun `customtex template --help` to see the available templates.\n\n## License\nCustomTeX is licensed under the MIT license. See the LICENSE file for more information.\n",
    'author': 'Mario Vago Marzal',
    'author_email': 'mariovagomarzal@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mariovagomarzal/customtex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
