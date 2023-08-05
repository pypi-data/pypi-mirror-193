# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datagen_protocol',
 'datagen_protocol.schema',
 'datagen_protocol.schema.assets',
 'datagen_protocol.schema.environment',
 'datagen_protocol.schema.hic',
 'datagen_protocol.schema.humans',
 'datagen_protocol.schemas.validation.humans']

package_data = \
{'': ['*'], 'datagen_protocol': ['resources/*']}

setup_kwargs = {
    'name': 'datagen-validation-protocol',
    'version': '0.4.1',
    'description': 'Datagen Validation Protocol',
    'long_description': 'None',
    'author': 'ShayZ',
    'author_email': 'shay.zilberman@datagen.tech',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
