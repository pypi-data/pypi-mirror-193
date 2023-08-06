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
    'version': '0.1.2',
    'description': '',
    'long_description': '# edge-ai\n\n`edge-ai` is a python module and CLI to transform data into hardware-agnostic AI models, using the Edge Impulse API.\n\n## Installation\n\n```console\npip install edge-ai\n```\n\n## CLI Usage\n\n### `ei`\n\nTransform data into hardware-agnostic AI models, using the Edge Impulse API\n\n**Usage**:\n\n```console\n$ ei [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `portals`: Work with Edge Impulse Upload Portals\n* `transformations`: Manage organization data transformations...\n\n#### `ei portals`\n\nWork with Edge Impulse Upload Portals\n\n**Usage**:\n\n```console\n$ ei portals [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `create`: Create an organization data upload portal...\n* `delete`: Delete an organization portal from Edge...\n* `download`: Download the contents of an Edge Impulse...\n* `show`: Show upload portal details of an Edge...\n\n##### `ei portals create`\n\nCreate an organization data upload portal on Edge Impulse\n\n**Usage**:\n\n```console\n$ ei portals create [OPTIONS]\n```\n\n**Options**:\n\n* `--org-id INTEGER`: the ID of the Edge Impulse organization that the portal belongs to  [env var: EI_ORG_ID; required]\n* `--org-key TEXT`: an Edge Impulse Organization API key  [env var: EI_ORG_KEY; required]\n* `--name TEXT`: the name of the portal to create  [required]\n* `--help`: Show this message and exit.\n\n##### `ei portals delete`\n\nDelete an organization portal from Edge Impulse\n\n**Usage**:\n\n```console\n$ ei portals delete [OPTIONS]\n```\n\n**Options**:\n\n* `--org-id INTEGER`: the ID of the Edge Impulse organization that the portal belongs to  [env var: EI_ORG_ID; required]\n* `--org-key TEXT`: an Edge Impulse Organization API key  [env var: EI_ORG_KEY; required]\n* `--portal-id INTEGER`: the ID of the portal to download files from  [required]\n* `--help`: Show this message and exit.\n\n##### `ei portals download`\n\nDownload the contents of an Edge Impulse organization portal\n\n**Usage**:\n\n```console\n$ ei portals download [OPTIONS]\n```\n\n**Options**:\n\n* `--org-id INTEGER`: the ID of the Edge Impulse organization that the portal belongs to  [env var: EI_ORG_ID; required]\n* `--username TEXT`: the Edge Impulse username to login with  [env var: EI_USERNAME; required]\n* `--password TEXT`: the Edge Impulse user password  [env var: EI_PASSWORD; required]\n* `--portal-id INTEGER`: the ID of the portal to download files from  [required]\n* `--path TEXT`: the path where the portal files should be downloaded  [required]\n* `--help`: Show this message and exit.\n\n##### `ei portals show`\n\nShow upload portal details of an Edge Impulse organization\n\nIf --portal-id is provided, only the details for that portal will be shown\n\n**Usage**:\n\n```console\n$ ei portals show [OPTIONS]\n```\n\n**Options**:\n\n* `--org-id INTEGER`: the ID of the Edge Impulse organization that the portal belongs to  [env var: EI_ORG_ID; required]\n* `--org-key TEXT`: an Edge Impulse Organization API key  [env var: EI_ORG_KEY; required]\n* `--portal-id INTEGER`: the ID of the portal to download files from\n* `--contents / --no-contents`: Show the contents of the portal  [default: no-contents]\n* `--help`: Show this message and exit.\n\n#### `ei transformations`\n\nManage organization data transformations on Edge Impulse\n\n**Usage**:\n\n```console\n$ ei transformations [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `create`: Create a data transformation block on Edge...\n* `delete`: Delete a data transformation block for an...\n* `list`: List data transformation blocks for an...\n\n##### `ei transformations create`\n\nCreate a data transformation block on Edge Impulse\n\nOrganization portals and buckets are mounted as /portals/<id> and /buckets/<id> respectively.\n\n**Usage**:\n\n```console\n$ ei transformations create [OPTIONS]\n```\n\n**Options**:\n\n* `--org-id INTEGER`: the ID of the Edge Impulse organization that the portal belongs to  [env var: EI_ORG_ID; required]\n* `--org-key TEXT`: an Edge Impulse Organization API key  [env var: EI_ORG_KEY; required]\n* `--container TEXT`: the URI of the Docker container to run (may include version tag)  [required]\n* `--name TEXT`: the name of the transformation block\n* `--description TEXT`: a summary describing the transformation block\n* `--help`: Show this message and exit.\n\n##### `ei transformations delete`\n\nDelete a data transformation block for an Edge Impulse organization\n\n**Usage**:\n\n```console\n$ ei transformations delete [OPTIONS]\n```\n\n**Options**:\n\n* `--org-id INTEGER`: the ID of the Edge Impulse organization that the portal belongs to  [env var: EI_ORG_ID; required]\n* `--org-key TEXT`: an Edge Impulse Organization API key  [env var: EI_ORG_KEY; required]\n* `--transformation-id TEXT`: the ID of the data transformation to delete  [required]\n* `--help`: Show this message and exit.\n\n##### `ei transformations list`\n\nList data transformation blocks for an Edge Impulse organization\n\n**Usage**:\n\n```console\n$ ei transformations list [OPTIONS]\n```\n\n**Options**:\n\n* `--org-id INTEGER`: the ID of the Edge Impulse organization that the portal belongs to  [env var: EI_ORG_ID; required]\n* `--org-key TEXT`: an Edge Impulse Organization API key  [env var: EI_ORG_KEY; required]\n* `--help`: Show this message and exit.\n',
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
