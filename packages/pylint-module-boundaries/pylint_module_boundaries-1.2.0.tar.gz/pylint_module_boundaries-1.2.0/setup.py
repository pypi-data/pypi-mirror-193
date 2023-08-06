# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylint_module_boundaries']

package_data = \
{'': ['*']}

install_requires = \
['pylint>=2,<3']

setup_kwargs = {
    'name': 'pylint-module-boundaries',
    'version': '1.2.0',
    'description': '',
    'long_description': '# pylint module boundaries\n\na pylint plugin to enforce boundaries between modules in your project. similar to nx\'s\n[enforce-module-boundaries](https://nx.dev/core-features/enforce-project-boundaries) eslint plugin\n\n## example\n\nsay you have three packages in your project - `common`, `package1`, and `package2` - you can use the `banned-imports` rule to prevent `common` from importing anything from `package1` or `package2`, thus avoiding issues such as circular dependencies.\n\nPylint can then be used to detect any violations of this rule:\n\n![](readme-images/img.png)\n\nsee [usage](/#usage) below for a config example\n\n## installing\n\n```\npoetry install pylint-module-boundaries\n```\n\n## usage\n\n```toml\n# pyproject.toml\n[tool.pylint.MASTER]\nload-plugins = "pylint_module_boundaries"\n# (currently uses regex but i want to replace it with something better in the future)\nbanned-imports = \'\'\'\n{\n    "common(\\\\..*)?": ["package1(\\\\..*)?", "package2(\\\\..*)?"],\n    "scripts(\\\\..*)?": ["package1(\\\\..*)?", "package2(\\\\..*)?"]\n}\n\'\'\'\n```\n',
    'author': 'DetachHead',
    'author_email': 'detachhead@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
