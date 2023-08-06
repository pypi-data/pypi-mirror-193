# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tgr_wdn_query_lang', 'tgr_wdn_query_lang.generated']

package_data = \
{'': ['*']}

install_requires = \
['antlr4-python3-runtime>=4.9.2,<5.0.0']

setup_kwargs = {
    'name': 'tgr-wdn-query-lang',
    'version': '1.1.5',
    'description': 'A library for parsing simple query expression.',
    'long_description': 'None',
    'author': 'Ivan Choo',
    'author_email': 'ivan@horangi.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
