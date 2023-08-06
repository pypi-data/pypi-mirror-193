# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['epss_api']

package_data = \
{'': ['*']}

install_requires = \
['urllib3>=1.26.13,<2.0.0']

entry_points = \
{'console_scripts': ['push = tools.push:main',
                     'release = tools.release:main',
                     'sbom = tools.sbom:main',
                     'sphinx = tools.sphinx:main']}

setup_kwargs = {
    'name': 'epss-api',
    'version': '0.2.0',
    'description': 'EPSS API Python Client',
    'long_description': '=================\nEPSS API Client\n=================\n\n.. image:: https://badge.fury.io/py/epss-api.svg\n    :target: https://badge.fury.io/py/epss-api\n\n.. image:: https://github.com/kannkyo/epss-api/actions/workflows/python-ci.yml/badge.svg\n    :target: https://github.com/kannkyo/epss-api/actions/workflows/python-ci.yml\n\n.. image:: https://codecov.io/gh/kannkyo/epss-api/branch/main/graph/badge.svg?token=R40FT0KITO \n :target: https://codecov.io/gh/kannkyo/epss-api\n\n.. image:: https://github.com/kannkyo/epss-api/actions/workflows/scorecards.yml/badge.svg\n    :target: https://github.com/kannkyo/epss-api/actions/workflows/scorecards.yml\n\nEPSS API client.\n',
    'author': 'kannkyo',
    'author_email': '15080890+kannkyo@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kannkyo/epss-api',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
