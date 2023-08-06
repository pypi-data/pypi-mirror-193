# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['understory']
install_requires = \
['webint-auth>0.0',
 'webint-code>0.0',
 'webint-data>0.0',
 'webint-editor>0.0',
 'webint-guests>0.0',
 'webint-media>0.0',
 'webint-mentions>0.0',
 'webint-owner>0.0',
 'webint-player>0.0',
 'webint-posts>0.0',
 'webint-search>0.0',
 'webint-system>0.0',
 'webint-tracker>0.0']

entry_points = \
{'websites': ['understory = understory:app']}

setup_kwargs = {
    'name': 'understory',
    'version': '0.1.6',
    'description': 'a decentralized social platform',
    'long_description': 'None',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ragt.ag/code/projects/understory',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
