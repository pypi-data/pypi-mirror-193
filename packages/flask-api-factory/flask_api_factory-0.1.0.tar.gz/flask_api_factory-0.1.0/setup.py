# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_api_factory', 'flask_api_factory.actions', 'flask_api_factory.filter']

package_data = \
{'': ['*']}

install_requires = \
['flask-migrate>=4.0.4,<5.0.0',
 'flask-sqlalchemy>=3.0.3,<4.0.0',
 'flask>=2.2.2,<3.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'pika>=1.3.1,<2.0.0',
 'prometheus-flask-exporter>=0.21.0,<0.22.0',
 'pydantic[dotenv]>=1.10.4,<2.0.0']

extras_require = \
{'mysql': ['mysql>=0.0.3,<0.0.4'],
 'postgres': ['psycopg2-binary>=2.9.5,<3.0.0']}

setup_kwargs = {
    'name': 'flask-api-factory',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Rodrigo Pinheiro Matias',
    'author_email': 'rodrigopmatias@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
