# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hits',
 'hits.parallel',
 'hits.serialize',
 'hits.test',
 'hits.visualize',
 'hits.visualize.interactive']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.4.0,<10.0.0',
 'biopython>=1.81,<2.0',
 'bokeh>=3.0.3,<4.0.0',
 'ipython>=8.10.0,<9.0.0',
 'ipywidgets>=8.0.4,<9.0.0',
 'matplotlib>=3.7.0,<4.0.0',
 'numpy>=1.24.2,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'pysam>=0.20.0,<0.21.0',
 'pyyaml>=6.0,<7.0',
 'seaborn>=0.12.2,<0.13.0',
 'statsmodels>=0.13.5,<0.14.0']

setup_kwargs = {
    'name': 'hits-x',
    'version': '0.1.3',
    'description': "Updated and modified from Jeff's version.",
    'long_description': 'utilities for processing high-throughput sequencing experiments (v0.3.3)\n',
    'author': 'hukai916',
    'author_email': '31452631+hukai916@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
