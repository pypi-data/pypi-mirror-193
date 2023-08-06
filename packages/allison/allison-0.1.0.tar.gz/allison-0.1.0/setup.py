# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['allison',
 'allison.clustering',
 'allison.linear_models',
 'allison.nn',
 'allison.utils',
 'allison.utils.functions']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0']

setup_kwargs = {
    'name': 'allison',
    'version': '0.1.0',
    'description': 'A Machine Learning library for begainers',
    'long_description': '# Allison\nAllison: is a library  of Artificial Intelligence\n\n# About Allison\n\nThis project implements the main machine learning and deep learning architectures in Python, \nusing libraries such as Numpy, Scipy and Matplotlib for the visualizations. \nits objective is to show how machine learning works\ninside and not be a black box for many people.\n\n## Requirements\n- Numpy\n- Matplotlib\n- Scipy\n- Pandas\n## Install\n- clone the repository `git clone https://github.com/Mitchell-Mirano/Allison.git`\n- install a virtual environment `python -m virtualenv env`\n- install the requirements `pip install -r requirements.txt`\n\nNow you can use Allison\n\n## Examples in Allison\n- for examples review examples directory\n',
    'author': 'Mitchell Mirano',
    'author_email': 'mitchellmirano25@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
