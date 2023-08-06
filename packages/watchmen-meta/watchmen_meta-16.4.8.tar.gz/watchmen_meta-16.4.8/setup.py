# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_meta',
 'watchmen_meta.admin',
 'watchmen_meta.analysis',
 'watchmen_meta.auth',
 'watchmen_meta.common',
 'watchmen_meta.console',
 'watchmen_meta.dqc',
 'watchmen_meta.gui',
 'watchmen_meta.system',
 'watchmen_meta.webhook']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome>=3.14.1,<4.0.0',
 'watchmen-auth==16.4.8',
 'watchmen-storage==16.4.8']

extras_require = \
{'mongodb': ['watchmen-storage-mongodb==16.4.8'],
 'mssql': ['watchmen-storage-mssql==16.4.8'],
 'mysql': ['watchmen-storage-mysql==16.4.8'],
 'oracle': ['watchmen-storage-oracle==16.4.8'],
 'postgresql': ['watchmen-storage-postgresql==16.4.8']}

setup_kwargs = {
    'name': 'watchmen-meta',
    'version': '16.4.8',
    'description': '',
    'long_description': 'None',
    'author': 'botlikes',
    'author_email': '75356972+botlikes456@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
