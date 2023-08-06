# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stablerandom']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22,<2.0']

setup_kwargs = {
    'name': 'stablerandom',
    'version': '0.4.27',
    'description': 'Create stable/repeatable numpy.random applications',
    'long_description': '# stablerandom\nstablerandom provides a stable and repeatable implementation of \nthe NumPy random number generator (numpy.random). With this package, \nyou can generate the same sequence of random numbers across different \nplatforms and Python environments, ensuring reproducibility \nin scientific computing, machine learning, and unit testing.\n\nstablerandom can decorate any function or method and provide a \ncall-stack scoped seeded random generator. It is thread safe and \nsupports nested scopes.\n\n## Example\nUsing the `@stablerandom` decorator to get a stable output for numpy.random.triangular\n\n ```\nimport numpy.random\nfrom stablerandom import stablerandom\n\n@stablerandom\ndef random_triangular(samples):\n    return numpy.random.triangular(1, 5, 10, samples)\n\nprint(random_triangular(3))\n>>> [1.99882862 7.95097645 7.68974243]\nprint(random_triangular(3))\n>>> [1.99882862 7.95097645 7.68974243]\n```\n\n## Installing\n```bash\n$ pip install stablerandom\n```\nThe source code is currently hosted on GitHub at \nhttps://github.com/GistLabs/stablerandom\nand published in PyPI at https://pypi.org/project/stablerandom/ \n\nThe versioning scheme currently used is {major}.{minor}.{auto build number}\nfrom `git rev-list --count HEAD`. \n\nWe recommend picking a version like:\n\n`stablerandom = "^0.3"`\n\n## Dependencies\nThis library has been tested with [NumPy](https://www.numpy.org) back to version 1.22\n\n## Community guidelines\nWe welcome contributions and questions. Please head over to github and \nsend us pull requests or create issues!\n',
    'author': 'John Heintz',
    'author_email': 'john@gistlabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
