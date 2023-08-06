# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xbridge_cli',
 'xbridge_cli.bridge',
 'xbridge_cli.misc',
 'xbridge_cli.server',
 'xbridge_cli.server.config',
 'xbridge_cli.utils',
 'xbridge_cli.utils.config_file']

package_data = \
{'': ['*'], 'xbridge_cli.server.config': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'click>=8.1.3,<9.0.0',
 'docker>=6.0.0,<7.0.0',
 'httpx>=0.18.1,<0.24.0',
 'psutil>=5.9.2,<6.0.0',
 'pycryptodome>=3.17,<4.0',
 'tabulate>=0.8.9,<0.10.0',
 'websockets>=10.3,<11.0',
 'xrpl-py==1.8.0b1']

entry_points = \
{'console_scripts': ['xbridge-cli = xbridge_cli.main:main']}

setup_kwargs = {
    'name': 'xbridge-cli',
    'version': '0.1.0',
    'description': 'A CLI that helps you set up an XRPL-XRPL bridge.',
    'long_description': "# xbridge-cli\n\n## Install\n\n```bash\npip install xbridge-cli\n```\n\nNOTE: if you're looking at the repo before it's published, this won't work. Instead, you'll do this:\n\n```bash\ngit clone https://github.com/xpring-eng/xbridge-cli.git\ncd xbridge-cli\n# install poetry\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -\npoetry install\npoetry shell\n```\n\nInstall rippled and the xbridge witness.\n\nrippled: https://xrpl.org/install-rippled.html\n\nwitness: https://github.com/seelabs/xbridge_witness\n\n## Get started\n\n```bash\nexport XCHAIN_CONFIG_DIR={filepath where you want your config files stored}\nexport RIPPLED_EXE={rippled exe filepath}\nexport WITNESSD_EXE={witnessd exe filepath}\n./scripts/tutorial.sh\n```\n\nTo stop the servers:\n\n```bash\nxbridge-cli server stop --all\n```\n\n## Use Commands\n\n```bash\nxbridge-cli --help\n```\n\nEach subcommand also has a `--help` flag, to tell you what fields you'll need.\n",
    'author': 'Mayukha Vadari',
    'author_email': 'mvadari@ripple.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xpring-eng/xbridge-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
