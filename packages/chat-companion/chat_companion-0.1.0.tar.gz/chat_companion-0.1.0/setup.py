# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chat_companion', 'chat_companion.toolbox']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.26.5,<0.27.0',
 'plac>=1.3.5,<2.0.0',
 'pyinstaller>=5.8.0,<6.0.0',
 'pysimplelog>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'chat-companion',
    'version': '0.1.0',
    'description': 'A cli client for chat gpt with some extra features',
    'long_description': '# CLI Companion\n\nCLI Companion is a command line tool that you can use to ask questions and get responses back from a virtual companion. You can also review previous questions and responses.\n\n## Installation\n\nYou can install CLI Companion using [PyInstaller](https://www.pyinstaller.org/).\n\nTo install using PyInstaller, first clone this repository. Then, in the repository directory, run the following command:\n\n```\npyinstaller -D companion.py\n```\n\nThis will create a standalone executable in the `dist` directory.\n\n## Usage\n\n### Talk\n\nTo ask a question, use the `talk` subcommand. For example:\n\n```\ncompanion talk "What is your name?"\n```\n\n### Review\n\nTo review previous questions and responses, use the `review` subcommand. This will bring up a list of previous questions. You can then select a question to view the response.',
    'author': 'daniel-davee',
    'author_email': 'daniel.v.davee@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.10.9',
}


setup(**setup_kwargs)
