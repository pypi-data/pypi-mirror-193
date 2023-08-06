# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['biblelib', 'biblelib.books', 'biblelib.words']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'biblelib',
    'version': '0.2.4',
    'description': 'Utilities for working with metadata for Bible books, references, pericopes, and other units.',
    'long_description': '# Biblelib\n\n[![Release](https://img.shields.io/github/v/release/sboisen/Biblelib)](https://img.shields.io/github/v/release/sboisen/Biblelib)\n[![Build status](https://img.shields.io/github/workflow/status/sboisen/Biblelib/merge-to-main)](https://img.shields.io/github/workflow/status/sboisen/Biblelib/merge-to-main)\n[![codecov](https://codecov.io/gh/sboisen/Biblelib/branch/main/graph/badge.svg)](https://codecov.io/gh/sboisen/Biblelib)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/sboisen/Biblelib)](https://img.shields.io/github/commit-activity/m/sboisen/Biblelib)\n[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://sboisen.github.io/Biblelib/)\n[![Code style with black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports with isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)\n[![License](https://img.shields.io/github/license/sboisen/Biblelib)](https://img.shields.io/github/license/sboisen/Biblelib)\n\nUtilities for working with Bible books, references, pericopes, and\nother units. Note this does _not_ include any actual Bible texts.\n\n- **Github repository**: <https://github.com/Clear-Bible/Biblelib\n- **Documentation** may *eventually* arrive at\n  <https://clear-bible.github.io/Biblelib/> but can be found in the\n  `docs` directory, and built using `mkdocs`.\n\n## Installation\n\n```bash\n$ pip install biblelib\n```\n',
    'author': 'Sean Boisen',
    'author_email': 'sean.boisen@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Clear-Bible/Biblelib/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<=3.11',
}


setup(**setup_kwargs)
