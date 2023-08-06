# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amberdata']

package_data = \
{'': ['*']}

install_requires = \
['gql[requests]>=3.4.0,<4.0.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['typing-extensions>=4.0.1,<5.0.0'],
 'docs': ['sphinx>=4.3.2,<5.0.0', 'sphinx-rtd-theme>=1.0.0,<2.0.0']}

setup_kwargs = {
    'name': 'amberdata',
    'version': '0.1.1',
    'description': 'Amberdata is a Python library to access the Amberdata API',
    'long_description': '## Demo\n\n## Install\n\n```bash\npip install amberdata\n```\n## for reference\n\n```python\nfrom amberdata import Amberdata\n\nad_client = Amberdata(x_api_key="ENTER YOUR API KEY HERE")\n\nblockchain_address_logs = ad_client.blockchain_address_logs(\n    address="0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", topic="0x58e5d5a525e3b40bc15abaa38b5882678db1ee68befd2f60bafe3a7fd06db9e3"\n)\n\nprint(blockchain_address_logs)\n```\n',
    'author': 'Patrick Doyle',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/amberdata/amberdata-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
