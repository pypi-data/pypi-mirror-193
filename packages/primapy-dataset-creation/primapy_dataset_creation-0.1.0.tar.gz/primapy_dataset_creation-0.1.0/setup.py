# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['primapy_dataset_creation']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'primapy-dataset-creation',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'condensatore',
    'author_email': 'annamatteoli.93@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
