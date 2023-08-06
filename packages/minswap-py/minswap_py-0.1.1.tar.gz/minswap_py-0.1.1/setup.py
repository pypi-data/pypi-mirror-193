# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['minswap', 'minswap.models']

package_data = \
{'': ['*']}

install_requires = \
['blockfrost-python==0.5.2',
 'pycardano==0.7.2',
 'pydantic==1.10.4',
 'python-dotenv==0.21.1']

setup_kwargs = {
    'name': 'minswap-py',
    'version': '0.1.1',
    'description': '',
    'long_description': '# minswap-py (v0.1.1)\n<p align="center">\n    <img src="https://img.shields.io/pypi/status/minswap-py?style=flat-square" />\n    <img src="https://img.shields.io/pypi/dm/minswap-py?style=flat-square" />\n    <img src="https://img.shields.io/pypi/l/minswap-py?style=flat-square"/>\n    <img src="https://img.shields.io/pypi/v/minswap-py?style=flat-square"/>\n    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n</p>\n\n`minswap-py` is a tool to interact with [Minswap](https://minswap.org/).  The current version has feature parity with the minswap [blockfrost-adapter](https://github.com/minswap/blockfrost-adapter).\n\nDocumentation and additional features coming soon.\n\n## Quickstart\n\nIn order to use this package:\n1. Install with `pip install minswap-py`\n2. Sign up for blockfrost and get an API key.\n3. In your working directory, save a `.env` file. In this file, save your blockfrost API key as follows:\n```bash\nPROJECT_ID=YOUR_BLOCKFROST_ID\n```\n\nOnce you do this, you can try out the code in the `examples` folder on the Github repository.\n',
    'author': 'eldermillenial',
    'author_email': 'eldermillenial@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/theeldermillenial/minswap-py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
