# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rfcctl', 'rfcctl.data']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=3.1.2,<4.0.0']

entry_points = \
{'console_scripts': ['rfcctl = rfcctl.main:main']}

setup_kwargs = {
    'name': 'rfcctl',
    'version': '0.1.1',
    'description': 'RFC like documents management tool',
    'long_description': "# rfcctl: RFC like document manager\n\n&cop; 2023 SiLeader.\n\n## How to use\n### 1. Add context\nAdd context to use `context add` subcommand.\n\n```bash\nrfcctl context add --name <CONTEXT_NAME> --user <USER NAME> /path/to/directory\n```\n\n- `--name` is context name alias\n- `--user` is writer username\n- `--switch` option is switch this context as default context\n- `--initial-status` is RFC's initial status. default is Draft\n- `--obsoleted-status` is obsoleted RFC's status. default is Obsoleted\n- `--init` option is create `skeleton.md` in this directory\n\n### 2. Create new RFC\nCreate new RFC file from `skeleton.md` to use `create` subcommand.\n\n```bash\nrfcctl create --category-tree <CATEGORY> <SUBCATEGORY in CATEGORY> ... --title 'My new RFC'\n```\n\n### 3. Update RFC metadata\nUpdate RFC's obsoleted metadata to use `update` subcommand.\n\n```bash\nrfcctl update\n```\n\n\n## License\nApache License 2.0\n\nSee LICENSE",
    'author': 'SiLeader',
    'author_email': 'sileader.dev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SiLeader/rfcctl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
