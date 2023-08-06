# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['houdini_package_manager']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'houdini-package-manager',
    'version': '0.0.1',
    'description': 'GUI package manager for Houdini',
    'long_description': '# houdini-package-manager\n\n[![Release](https://img.shields.io/github/v/release/ariffjeff/houdini-package-manager)](https://img.shields.io/github/v/release/ariffjeff/houdini-package-manager)\n[![Build status](https://img.shields.io/github/actions/workflow/status/ariffjeff/houdini-package-manager/main.yml?branch=main)](https://github.com/ariffjeff/houdini-package-manager/actions/workflows/main.yml?query=branch%3Amain)\n[![codecov](https://codecov.io/gh/ariffjeff/houdini-package-manager/branch/main/graph/badge.svg)](https://codecov.io/gh/ariffjeff/houdini-package-manager)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/ariffjeff/houdini-package-manager)](https://img.shields.io/github/commit-activity/m/ariffjeff/houdini-package-manager)\n[![License](https://img.shields.io/github/license/ariffjeff/houdini-package-manager)](https://img.shields.io/github/license/ariffjeff/houdini-package-manager)\n\nGUI package manager for Houdini\n\n- **Github repository**: <https://github.com/ariffjeff/houdini-package-manager/>\n- **Documentation** <https://ariffjeff.github.io/houdini-package-manager/>\n\n## Usage\n\n\n\n---\n\nRepository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).',
    'author': 'Ariff Jeff',
    'author_email': 'fariffjeff@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ariffjeff/houdini-package-manager',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
