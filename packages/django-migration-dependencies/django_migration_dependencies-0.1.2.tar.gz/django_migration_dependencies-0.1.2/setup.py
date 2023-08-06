# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'dmdg'}

packages = \
['migrations_graph']

package_data = \
{'': ['*'], 'migrations_graph': ['templates/migrations_graph/*']}

setup_kwargs = {
    'name': 'django-migration-dependencies',
    'version': '0.1.2',
    'description': 'A Django app to visualise the migrations graph',
    'long_description': '# Django Migration Dependency Graph\nThis is an app that helps developers understand how their migrations are interconnected across their apps, serving as a tool to identify possible circular dependencies when squashing them.\n\n## Quick start\n\n1. Add "migrations-graph" to your INSTALLED_APPS setting like this:\n\n\n    INSTALLED_APPS = [\n        ...\n        \'migrations-graph\',\n    ]\n\n\n2. Include the polls URLconf in your project urls.py like this::\n\n\n    path(\'migrations-graph/\', include(\'migrations_graph.urls\')),\n\n\n3. Start the development server.\n\n4. Visit http://127.0.0.1:8000/migrations_graph/ to see the graph.\n',
    'author': 'Eugenio Doñaque',
    'author_email': 'eugenio@donaque.xyz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/edg956/django-migration-dependencies',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
