# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_pipeline_surface',
 'watchmen_pipeline_surface.connectors',
 'watchmen_pipeline_surface.data']

package_data = \
{'': ['*']}

install_requires = \
['watchmen-pipeline-kernel==16.4.8', 'watchmen-rest==16.4.8']

extras_require = \
{'kafka': ['kafka-python>=2.0.2,<3.0.0', 'aiokafka>=0.7.2,<0.8.0'],
 'mongodb': ['watchmen-storage-mongodb==16.4.8'],
 'mssql': ['watchmen-storage-mssql==16.4.8'],
 'mysql': ['watchmen-storage-mysql==16.4.8'],
 'oracle': ['watchmen-storage-oracle==16.4.8'],
 'postgresql': ['watchmen-storage-postgresql==16.4.8'],
 'rabbitmq': ['aio-pika>=7.1.2,<8.0.0'],
 'standard-ext-writer': ['requests>=2.27.1,<3.0.0']}

setup_kwargs = {
    'name': 'watchmen-pipeline-surface',
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
