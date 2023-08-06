# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tailwind_colors']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tailwind-colors',
    'version': '0.1.0',
    'description': '',
    'long_description': "# Python Tailwind Colors\n\nUse the default color palette from TailwindCSS (https://tailwindcss.com/docs/customizing-colors) in your python code for plotting, image generation, etc..\n\n**Usage:**\n\n```python\nfrom tailwind_colors import TAILWIND_COLORS\n\nprint(TAILWIND_COLORS.FUCHSIA_600)  # prints '#c026d3'\n```\n",
    'author': 'Moritz Makowski',
    'author_email': 'moritz@dostuffthatmatters.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
