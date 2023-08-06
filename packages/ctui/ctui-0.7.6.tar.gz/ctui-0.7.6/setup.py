# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ctui']

package_data = \
{'': ['*'], 'ctui': ['kaitai/*']}

install_requires = \
['Pygments>=2.14.0,<3.0.0',
 'prompt-toolkit>=3.0.36,<4.0.0',
 'six>=1.16.0,<2.0.0',
 'tabulate>=0.8.0,<0.9.0',
 'tinydb>=4.7.1,<5.0.0']

setup_kwargs = {
    'name': 'ctui',
    'version': '0.7.6',
    'description': "The ctui library is similar to Python's built in cmd library, but with a curses-like user interface",
    'long_description': "# Control Things Serial\n\nThe `ctui` is a library for creating terminal-based user interfaces, and is used in all the ControlThings tools at controlthings.io.  It is similar to using Click or Python's standard Cmd library, but with a curses-like interface written in pure Python.\n\n# Installation\n\nCtui is primarily developed on Linux, but should work in both Mac and Windows as well.\n\nAs long as you have git and Python 3.6 or later installed, all you should need to do is:\n\n```\npip3 install ctui\n```\n\n# Usage\n\nImport the library, instantiate a Ctui object, and start the ctui application, like:\n\n```\nfrom ctui import Ctui\n\nmyapp = Ctui()\nmyapp.run()\n```\n\nOf course you can configure you app in a number of different ways by modifying your app's attributes or by adding your own custom commands.   Check out the `examples` folder to walk you through some of these.  For more complex examples how to use ctui, check out the various ControlThings Tools, most of which use ctui.  You can find these at <https://github.com/ControlThingsTools>.\n\n# Fork and Develop\n\nTo set up a development environment for ctui, you will first need to install [Python Poetry](<https://python-poetry.org>) which is used to manage all the project dependencies and publish the pypi packages.  I strongly recommend checking out the website and at least reading through the [Basic Usage](https://python-poetry.org/docs/basic-usage/) page, but if you want the TLDR, just run:\n\n    curl -sSL https://install.python-poetry.org | python3 -\n\nOnce Poetry is installed, pull the repo and :\n\n    git clone https://github.com/ControlThings-io/ctui.git\n    cd ctui\n    poetry install\n    poetry shell\n\nThat last command will open a shell in a python virtual environment where you can do live edits to the code.  If you are a VS Code user, VS Code will automatically load the repo configs with all the linting rules I use through the repo, and should automatically open the debug tools and terminal inside the virtual environment.\n\n# Author\n\n* Justin Searle <justin@controlthings.io>\n",
    'author': 'Justin Searle',
    'author_email': 'justin@controlthings.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.controlthings.io',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
