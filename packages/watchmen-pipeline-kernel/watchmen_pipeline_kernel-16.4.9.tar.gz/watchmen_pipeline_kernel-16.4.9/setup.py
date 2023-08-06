# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_pipeline_kernel',
 'watchmen_pipeline_kernel.boot',
 'watchmen_pipeline_kernel.cache',
 'watchmen_pipeline_kernel.common',
 'watchmen_pipeline_kernel.external_writer',
 'watchmen_pipeline_kernel.monitor_log',
 'watchmen_pipeline_kernel.pipeline',
 'watchmen_pipeline_kernel.pipeline_schema',
 'watchmen_pipeline_kernel.pipeline_schema_interface',
 'watchmen_pipeline_kernel.topic',
 'watchmen_pipeline_kernel.topic_snapshot']

package_data = \
{'': ['*']}

install_requires = \
['APScheduler>=3.9.1,<4.0.0',
 'dask>=2022.9.1,<2023.0.0',
 'distributed>=2022.9.1,<2023.0.0',
 'watchmen-data-kernel==16.4.9']

extras_require = \
{'mongodb': ['watchmen-storage-mongodb==16.4.9'],
 'mssql': ['watchmen-storage-mssql==16.4.9'],
 'mysql': ['watchmen-storage-mysql==16.4.9'],
 'oracle': ['watchmen-storage-oracle==16.4.9'],
 'postgresql': ['watchmen-storage-postgresql==16.4.9'],
 'standard-ext-writer': ['requests>=2.27.1,<3.0.0']}

setup_kwargs = {
    'name': 'watchmen-pipeline-kernel',
    'version': '16.4.9',
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
