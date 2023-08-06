# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['versionedfunction']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'versionedfunction',
    'version': '0.8.45',
    'description': 'Sometimes you want to be able to dynamically call different versions of a function',
    'long_description': '# versionedfunction\nSometimes you want to be able to dynamically call different \nversions of a function.\n* testing alternatives against each other\n* runtime "always on" support for versions code changes\n\n## Example\n```python\nfrom versionedfunction import versionedfunction, versionContext\n\nclass Foo():\n    @versionedfunction\n    def algo(self):\n        return 0\n\n    @algo.version\n    def algo1(self):\n        return 1\n\n    @algo.default\n    @algo.version\n    def algo2(self):\n        return 2\nfoo = Foo()\n\nassert foo.algo() == 2\n\nversionContext[\'Foo.algo\'] = "1"\nassert foo.algo() == 1\n```\n\n## Installing\n```bash\n$ pip install versionedfunction\n```\nThe source code is currently hosted on GitHub at \nhttps://github.com/GistLabs/versionedfunction\nand published in PyPI at https://pypi.org/project/versionedfunction/ \n\nThe versioning scheme currently used is {major}.{minor}.{auto build number}\nfrom `git rev-list --count HEAD`. \n\nWe recommend picking a version like:\n\n`versionedfunction = "^0.8"`\n\n## Community guidelines\nWe welcome contributions and questions. Please head over to github and \nsend us pull requests or create issues!\n',
    'author': 'John Heintz',
    'author_email': 'john@gistlabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
