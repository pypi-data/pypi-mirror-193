# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eincheck', 'eincheck.checks', 'eincheck.parser']

package_data = \
{'': ['*']}

install_requires = \
['lark>=1.1,<1.2']

setup_kwargs = {
    'name': 'eincheck',
    'version': '0.1.3',
    'description': 'Tensor shape checks inspired by einstein notation',
    'long_description': '# eincheck\n\n[![CI](https://github.com/epronovost/eincheck/actions/workflows/pr.yaml/badge.svg)](https://github.com/epronovost/eincheck/actions/workflows/pr.yaml)\n[![Documentation Status](https://readthedocs.org/projects/eincheck/badge/?version=main)](https://eincheck.readthedocs.io/en/main/?badge=main)\n[![PyPI version](https://badge.fury.io/py/eincheck.svg)](https://badge.fury.io/py/eincheck)\n\nTensor shape checks inspired by einstein notation\n\n\n## Overview\n\nThis library has three main functions:\n\n* `check_shapes` takes tuples of `(Tensor, shape)` and checks that all the Tensors match the shapes\n\n```\ncheck_shapes((x, "i 3"), (y, "i 3"))\n```\n\n* `check_func` is a function decorator to check the input and output shapes of a function\n\n```\n@check_func("*i x, *i y -> *i (x + y)")\ndef concat(a, b):\n    return np.concatenate([a, b], -1)\n```\n\n* `check_data` is a class decorator to check the fields of a data class\n\n```\n@check_data(start="i 2", end="i 2")\nclass LineSegment2D(NamedTuple):\n    start: torch.Tensor\n    end: torch.Tensor\n```\n\nFor more info, [read the docs!](https://eincheck.readthedocs.io/en/main)\n',
    'author': 'Ethan Pronovost',
    'author_email': 'epronovo1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/EPronovost/eincheck',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4',
}


setup(**setup_kwargs)
