# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snapccess']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.1,<2.0.0',
 'pynvml>=11.4.1,<12.0.0',
 'torch>=1.13.0,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'snapccess',
    'version': '0.1.9',
    'description': 'Ensemble deep learning of embeddings for clustering multimodal single-cell omics data',
    'long_description': '## SnapCCESS\n\n\n',
    'author': 'Lijia Yu',
    'author_email': 'yulj2010@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
