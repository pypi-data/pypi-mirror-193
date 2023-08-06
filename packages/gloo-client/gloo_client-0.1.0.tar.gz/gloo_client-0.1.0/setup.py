# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gloo', 'gloo.db', 'gloo.tasks']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.74,<2.0.0',
 'fastapi>=0.85.0,<0.86.0',
 'google-cloud-firestore>=2.9.1,<3.0.0',
 'langchain>=0.0.83,<0.0.84',
 'mypy-boto3-dynamodb>=1.26.24,<2.0.0',
 'openai>=0.26.5,<0.27.0',
 'pinecone-client>=2.1.0,<3.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'sentence-transformers>=2.2.2,<3.0.0',
 'types-boto3>=1.0.2,<2.0.0',
 'unidecode>=1.3.6,<2.0.0',
 'uvicorn>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['gloo_cli = gloo_cli:cli', 'start = gloo.main:start']}

setup_kwargs = {
    'name': 'gloo-client',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
