# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_lineage',
 'watchmen_lineage.ml',
 'watchmen_lineage.model',
 'watchmen_lineage.router',
 'watchmen_lineage.service',
 'watchmen_lineage.service.builder',
 'watchmen_lineage.service.memory',
 'watchmen_lineage.service.table',
 'watchmen_lineage.storage',
 'watchmen_lineage.utils']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.8.8,<3.0.0',
 'watchmen-data-surface==16.4.8',
 'watchmen-indicator-surface==16.4.8',
 'watchmen-inquiry-surface==16.4.8',
 'watchmen-pipeline-surface==16.4.8']

setup_kwargs = {
    'name': 'watchmen-lineage',
    'version': '16.4.8',
    'description': '',
    'long_description': '# Watchmen Lineage\n\nLineage of _**Watchmen**_.',
    'author': 'luke0623',
    'author_email': 'luke0623@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
