# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chat_companion', 'toolbox']

package_data = \
{'': ['*']}

install_requires = \
['inquirerpy>=0.3.4,<0.4.0',
 'openai>=0.26.5,<0.27.0',
 'plac>=1.3.5,<2.0.0',
 'pysimplelog>=4.0.0,<5.0.0']

entry_points = \
{'console_scripts': ['companion = chat_companion.companion:main']}

setup_kwargs = {
    'name': 'chat-companion',
    'version': '0.1.5',
    'description': 'A chat gpt command line client with extra features"',
    'long_description': '# CLI Companion\n\nCLI Companion is a command line tool that you can use to ask questions and get responses back from a virtual companion. You can also review previous questions and responses.\n\n## Installation\n\nUsing pip\n\n`pip install chat-companion`\n\nUsing Poetry\n\n`poetry add chat-companion`\n\n## Usage\n\nrun \n`companion --help` \n\nTo see the list of commands.\n\n```\ncustom commands\n===============\ngenerate_response  proof_read   review     talk     \nhelp               resummarize  summarize  translate\n```\n\n### Talk\n\nTo ask a question, use the `talk` subcommand. For example:\n\n```\ncompanion talk "What is your name?"\n```\n\n### Review\n\nTo review previous questions and responses, use the `review` subcommand. This will bring up a list of previous questions. You can then select a question to view the response.',
    'author': 'daniel-davee',
    'author_email': 'daniel.v.davee@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
