# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edge_ai', 'edge_ai.common']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.3,<2.0.0', 'requests>=2.28.2,<3.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['ei = edge_ai.main:app']}

setup_kwargs = {
    'name': 'edge-ai',
    'version': '0.1.1',
    'description': '',
    'long_description': '# edge-ai\n\n`edge-ai` is a python package and CLI to transform data into hardware-agnostic, embedded AI models, using the Edge Impulse API.\n\nFull documentation for this package is available at https://docs.edgeimpulse.com/notebooks/edge-ai',
    'author': 'Jorge Silva',
    'author_email': 'jorge@edgeimpulse.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
