# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['savit', 'savit.config']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['savit = savit.main:app']}

setup_kwargs = {
    'name': 'savit',
    'version': '0.1.2',
    'description': 'Saves your commands as you use them',
    'long_description': '# `savit`\n\nHelping you to write docs by saving your commands\n\n**Usage**:\n\n```console\n$ savit [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `config`: Saves your configurations to ~/.config/savit/config.toml\n* `start`: Start saving your commands\n* `stop`: Stop saving your commands and writes them to a file\n\n## `savit config`\n\nSaves your configurations to ~/.config/savit/config.toml\n\n**Usage**:\n\n```console\n$ savit config [OPTIONS]\n```\n\n**Options**:\n\n* `--open-file`: Opens the config file  [default: False]\n* `--help`: Show this message and exit.\n\n## `savit start`\n\nStart saving your commands\n\n**Usage**:\n\n```console\n$ savit start [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n## `savit stop`\n\nStop saving your commands and writes them to a file\n\n**Usage**:\n\n```console\n$ savit stop [OPTIONS]\n```\n\n**Options**:\n\n* `--txt`: Saves your commands to a .txt file  [default: False]\n* `--md`: Saves your commands to a .md file  [default: False]\n* `--file PATH`: File (may include path) to save your commands\n* `--help`: Show this message and exit.\n\n\n**Points of attention**\n* Don\'t use aliases to savit commands, since savit works by reading your shell history, the app will work in an unexpected way if aliases are used;\n* Make sure to have your config file at `~/.config/savit/config.toml` correctly set up;\n\n\n**Config file structure**\n```toml\n[savit]\nhistory_path = "" # path to your shell history file\noutput_format = "" # output format to use by deafault (txt or md)\noutput_folder = "" # folder to save your commands by default (use ./ to save commands from the location where savit runs)\n```',
    'author': 'ivansantiagojr',
    'author_email': 'ivansantiago.junior@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
