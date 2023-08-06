# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['profyle',
 'profyle.database',
 'profyle.deps',
 'profyle.middleware',
 'profyle.models',
 'profyle.web']

package_data = \
{'': ['*'],
 'profyle.web': ['static/*', 'static/images/*', 'static/libs/*', 'templates/*']}

install_requires = \
['fastapi>=0.92.0,<0.93.0',
 'jinja2>=3.1.2,<4.0.0',
 'snakeviz>=2.1.1,<3.0.0',
 'typer[all]>=0.7.0,<0.8.0',
 'uvicorn[standard]>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['profyle = profyle.main:app']}

setup_kwargs = {
    'name': 'profyle',
    'version': '0.0.1',
    'description': 'Analyze and profiling code',
    'long_description': 'Analyze and profiling code',
    'author': 'Carlos Valdivia',
    'author_email': 'vpcarlos97@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
