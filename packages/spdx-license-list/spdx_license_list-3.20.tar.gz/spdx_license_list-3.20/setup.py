# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['spdx_license_list']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'spdx-license-list',
    'version': '3.20',
    'description': 'SPDX License List as a Python dictionary',
    'long_description': "[![Latest PyPI release](https://img.shields.io/pypi/v/spdx-license-list?logo=pypi)](https://pypi.org/project/spdx-license-list) ![Latest GitHub release](https://img.shields.io/github/v/release/JJMC89/spdx-license-list?logo=github) ![Latest tag](https://img.shields.io/github/v/tag/JJMC89/spdx-license-list?logo=git)\n\n![License](https://img.shields.io/pypi/l/spdx-license-list?color=blue) ![Python versions](https://img.shields.io/pypi/pyversions/spdx-license-list?logo=python)\n\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/JJMC89/spdx-license-list/main.svg)](https://results.pre-commit.ci/latest/github/JJMC89/pywikibot-extensions/main)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# SPDX License List\n\nProvides the SPDX License List as a Python dictionary\n\nData source: [spdx/license-list-data](https://github.com/spdx/license-list-data)\n\nDesigned as a replacement for [Michael Pöhn's spdx-license-list](https://gitlab.com/uniqx/spdx-license-list) but does not have the same API\n\n## Installation\n\n```console\npip install spdx-license-list\n```\n\n## API\n\n`spdx_license_list.LICENSES` is a dictionary of all the licenses.\n\nThe dictionary uses the identifier (**id**) as the keys, and the values are (typed) named tuples with the following attributes:\n- **id** (*str*) - short identifier to identify a match to licenses in the context of an SPDX file, a source file, or elsewhere\n- **name** (*str*) - full name that should be the title found in the license file or consistent with naming from other well-known sources\n- **deprecated_id** (*bool*) - idendifier is deprecated\n- **fsf_libre** (*bool*) - license is [listed as free by the FSF](https://www.gnu.org/licenses/license-list.en.html)\n- **osi_approved** (*bool*) - license is [OSI-approved](https://opensource.org/licenses)\n",
    'author': 'JJMC89',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JJMC89/spdx-license-list',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
