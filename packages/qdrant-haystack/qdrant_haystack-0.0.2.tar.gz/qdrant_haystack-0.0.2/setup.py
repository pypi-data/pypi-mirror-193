# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qdrant_haystack', 'qdrant_haystack.document_stores']

package_data = \
{'': ['*']}

install_requires = \
['farm-haystack>=1.13.0,<2.0.0', 'qdrant-client>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'qdrant-haystack',
    'version': '0.0.2',
    'description': 'An integration of Qdrant ANN vector database backend with Haystack',
    'long_description': '# qdrant-haystack\n\nAn integration of Qdrant ANN vector database backend with Haystack \n',
    'author': 'Kacper Łukawski',
    'author_email': 'kacper.lukawski@qdrant.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<=3.11',
}


setup(**setup_kwargs)
