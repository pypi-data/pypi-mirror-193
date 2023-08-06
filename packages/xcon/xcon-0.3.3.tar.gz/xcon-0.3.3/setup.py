# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xcon',
 'xcon.providers',
 'xcon.serverless_files',
 'xcon.serverless_files.config_manager']

package_data = \
{'': ['*']}

install_requires = \
['ciso8601>=2.3.0,<3.0.0',
 'xbool>=1.0.0,<2.0.0',
 'xboto>=1.0.2,<2.0.0',
 'xinject>=1.3.0,<2.0.0',
 'xloop>=1.0.1,<2.0.0',
 'xsentinels>=1.2.1,<2.0.0',
 'xsettings>=1.1.2,<2.0.0']

entry_points = \
{'pytest11': ['xcon_pytest_plugin = xcon.pytest_plugin']}

setup_kwargs = {
    'name': 'xcon',
    'version': '0.3.3',
    'description': 'Dynamic configuration retreiver.',
    'long_description': '![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.8|%203.9|%203.10|%203.11|%203.12&color=blue?style=flat-square&logo=python)\n![PyPI version](https://badge.fury.io/py/xcon.svg?)\n\n- [Introduction](#introduction)\n- [Documentation](#documentation)\n- [Install](#install)\n- [Licensing](#licensing)\n\n# Introduction\n\nHelps retrieve configuration information from aws/boto services such as Ssm\'s Param Store and Secrets Manager,\nwith the ability the cache a flattened list into a dynamodb table.\n\nRight now this is **pre-release software**, as the dynamo cache table and related need further documentation and testing.\n\nRetrieving values from Param Store and Secrets Manager should work and be relatively fast, as we bulk-grab values\nat the various directory-levels that are checked.\n\n**More documentation and testing will be coming soon, for a full 1.0.0 release sometime in the next month or so.**\n\nSee **[xsettings docs](https://xyngular.github.io/py-xcon/latest/)**.\n\n# Documentation\n\n**[📄 Detailed Documentation](https://xyngular.github.io/py-xcon/latest/)** | **[🐍 PyPi](https://pypi.org/project/xcon/)**\n\n# Install\n\n```bash\n# via pip\npip install xcon\n\n# via poetry\npoetry add xcon\n```\n\n# Licensing\n\nThis library is licensed under the "The Unlicense" License. See the LICENSE file.\n',
    'author': 'Josh Orr',
    'author_email': 'josh@orr.blue',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xyngular/py-xsettings',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
