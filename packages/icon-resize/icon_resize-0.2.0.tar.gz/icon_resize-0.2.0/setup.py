# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['icon_resize']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['icon-resize = icon_resize:entry', 'pump = pump:main']}

setup_kwargs = {
    'name': 'icon-resize',
    'version': '0.2.0',
    'description': 'CLI to create lossless icons in multiple sizes',
    'long_description': '# Icon Resize CLI\n\n![py-badge] [![black-badge]][black-url] ![mit]\n\n![screenshot](https://i.imgur.com/K00hCxN.png)\n\n> CLI to create lossless icons in multiple sizes\n\n🔗 [source code]\n\n[mit]: https://img.shields.io/github/license/hoishing/icon-resize\n[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg\n[black-url]: https://github.com/psf/black\n[py-badge]: https://img.shields.io/badge/python-3.10%20%7C%203.11-blue\n[source code]: https://github.com/hoishing/icon-resize-cli/\n\n## Features\n\n- resize icon file(png/jpg) to multiple sizes\n- lossless compression for png files\n- maintain aspect ratio and transparency\n\n## Prerequisite\n\n- macOS or Linux (Windows not tested)\n- python3.10+\n- [Image Magick][magick] `brew install imagemagick`\n\n## Installation\n\n`pip install icon-resize`\n\n## Usage\n\n```shell\n# default resize to 256, 128, 64\nicon-resize mic-512\n\n# specify resize to 128, 64\nicon-resize mic-512 --sizes "128,64"\n\n# save to \'mic\' folder with default sizes\nicon-resize mic-512 --out-folder mic/\n\n# enable autocomplete in current session\neval "$(_ICON_RESIZE_COMPLETE=zsh_source icon_resize)"\n```\n\n## Technical Details\n\n- use [Typer][typer] for CLI and help docs generation\n- use [Image Magick][magick] for both resize and compress images\n\n## Questions?\n\nOpen a [github issue] or ping me on [Twitter ![twitter-icon]][Twitter]\n\n[github issue]: https://github.com/hoishing/icon-resize-cli/issues\n[Twitter]: https://twitter.com/intent/tweet?text=https://github.com/hoishing/icon-resize-cli/%20%0D@hoishing\n[twitter-icon]: https://api.iconify.design/logos/twitter.svg?width=20\n[typer]: https://typer.tiangolo.com\n[magick]: https://imagemagick.org\n[poetry]: https://python-poetry.org/\n',
    'author': 'Kelvin Ng',
    'author_email': 'hoishing@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://hoishing.github.io/proj/icon-resize-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
