# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['einorm']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'einorm',
    'version': '0.1.1',
    'description': 'An einops-style generalized normalization layer.',
    'long_description': '# einorm\n\n[![Test](https://github.com/junhsss/einorm/actions/workflows/test.yml/badge.svg)](https://github.com/junhsss/einorm/actions/workflows/test.yml)\n[![PyPI Version](https://badge.fury.io/py/einorm.svg)](https://badge.fury.io/py/einorm)\n\nAn [einops](https://github.com/arogozhnikov/einops)-style generalized normalization layer.\n\n## Installation\n\nYou need `torch` >= 1.13 or `functorch` to be installed:\n\n```\npip install einorm\n```\n\n## Usage\n\n```python\nfrom einorm import Einorm\n\n# Equivalent to nn.LayerNorm(1024)\nEinorm("b n d", "d", d=1024)\n\n# Specify the dimensions and sizes to normalize along.\nEinorm("a b c d e", "b d", b=3, d=4)\n```\n\nAccording to [ViT-22B](https://arxiv.org/abs/2302.05442), normalizing query and key in a head-wise fashion can help stabilize the training dynamics. This can be achieved by providing additional grouping arguments to `Einorm`:\n\n```python\nEinorm("b h n d", "d", "h", h=16, d=64)  # num_heads=16, head_dim=64\n```\n',
    'author': 'junhsss',
    'author_email': 'junhsssr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
