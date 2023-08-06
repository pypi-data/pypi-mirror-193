# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mcpdf', 'mcpdf.cli', 'mcpdf.fit', 'mcpdf.nnpdf']

package_data = \
{'': ['*'],
 'mcpdf.fit': ['runcard-base/*', 'runcard-full/*', 'runcard-short/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'a3b2bbc3ced97675ac3a71df45f55ba>=6.4.0,<7.0.0',
 'click>=8.1.3,<9.0.0',
 'eko[box]>=0.10.0,<0.11.0',
 'numpy>=1.22.3,<2.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['mcpdf = mcpdf.cli:command']}

setup_kwargs = {
    'name': 'mcpdf',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Alessandro Candido',
    'author_email': 'candido.ale@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
