# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['vivlio']

package_data = \
{'': ['*'],
 'vivlio': ['Clients/CSV/*',
            'Clients/HTML/*',
            'Clients/JSON/*',
            'Clients/Markdown/*',
            'Clients/Mindmap/*',
            'Clients/YAML/*',
            'Devices/CSV/*',
            'Devices/HTML/*',
            'Devices/JSON/*',
            'Devices/Markdown/*',
            'Devices/Mindmap/*',
            'Devices/YAML/*',
            'Networks/CSV/*',
            'Networks/HTML/*',
            'Networks/JSON/*',
            'Networks/Markdown/*',
            'Networks/Mindmap/*',
            'Networks/YAML/*',
            'Organizations/CSV/*',
            'Organizations/HTML/*',
            'Organizations/JSON/*',
            'Organizations/Markdown/*',
            'Organizations/Mindmap/*',
            'Organizations/YAML/*']}

install_requires = \
['aiofiles>=23.1.0,<24.0.0',
 'aiohttp>=3.8.4,<4.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.28.2,<3.0.0',
 'rich-click>=1.6.1,<2.0.0']

entry_points = \
{'console_scripts': ['vivlio = vivlio.script:run']}

setup_kwargs = {
    'name': 'vivlio',
    'version': '0.1.1',
    'description': 'Business ready documents from Meraki',
    'long_description': '# vivlio\n\nBusiness Ready Documents for Meraki\n\n## Current API Coverage\n\nOrganizations\n\nOrganization Devices\n\nOrganization Networks\n\n## Installation\n\n```console\n$ python3 -m venv meraki\n$ source meraki/bin/activate\n(meraki) $ pip install vivlio\n```\n\n## Usage - Help\n\n```console\n(meraki) $ vivlio --help\n```\n\n![vivlio Help](/images/help.png)\n\n## Usage - In-line\n\n```console\n(meraki) $ vivlio --token <Meraki Token>\n```\n\n## Usage - Interactive\n\n```console\n(meraki) $ vivlio\nMeraki Token: <Meraki Token>\n```\n\n## Usage - Environment Variables\n\n```console\n(meraki) $ export TOKEN=<Meraki API Token>\n\n```\n\n## Recommended VS Code Extensions\n\nExcel Viewer - CSV Files\n\nMarkdown Preview - Markdown Files\n\nMarkmap - Mindmap Files\n\nOpen in Default Browser - HTML Files\n\n## Always On Sandbox\n\nThis code works with the always on sandbox! \n\nhttps://devnetsandbox.cisco.com/RM/Diagram/Index/a9487767-deef-4855-b3e3-880e7f39eadc?diagramType=Topology\n\n```console\nexport TOKEN=\n\n(venv)$ pip install vivlio\n(venv)$ mkdir vivlio_output\n(venv)$ cd vivlio_output\n(venv)/vivlio_output$ vivlio\n(venv)/vivlio_output$ code . \n(Launches VS Code and you can view the output with the recommended VS Code extensions)\n```\n## Contact\n\nPlease contact John Capobianco if you need any assistance\n',
    'author': 'John Capobianco',
    'author_email': 'ptcapo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
