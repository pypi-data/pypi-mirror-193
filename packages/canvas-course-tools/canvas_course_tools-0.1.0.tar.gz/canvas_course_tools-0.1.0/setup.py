# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['canvas_course_tools']

package_data = \
{'': ['*'], 'canvas_course_tools': ['templates/*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'canvasapi>=2.2.0,<3.0.0',
 'click>=8.1.3,<9.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'nameparser>=1.1.1,<2.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'rich-click>=1.5.2,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'tomli-w>=1.0.0,<2.0.0',
 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['canvas = canvas_course_tools.cli:cli']}

setup_kwargs = {
    'name': 'canvas-course-tools',
    'version': '0.1.0',
    'description': 'Canvas course tools',
    'long_description': 'None',
    'author': 'David Fokkema',
    'author_email': 'd.b.r.a.fokkema@vu.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
