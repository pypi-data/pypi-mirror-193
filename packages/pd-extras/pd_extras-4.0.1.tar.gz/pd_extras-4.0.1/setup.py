# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pd_extras',
 'pd_extras.check',
 'pd_extras.extra',
 'pd_extras.optimize',
 'pd_extras.write']

package_data = \
{'': ['*']}

install_requires = \
['dnspython',
 'mysqlclient',
 'pandas>=1.5.3',
 'psycopg2',
 'pyarrow',
 'pymongo',
 'pymssql',
 'pymysql',
 'sqlalchemy-utils',
 'sqlalchemy>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'pd-extras',
    'version': '4.0.1',
    'description': 'Some utility functions on top of pandas.',
    'long_description': '# Pandas Extras\n\n![Build](https://github.com/proafxin/pandas-utils/actions/workflows/tox_build.yml/badge.svg)\n![Workflow for Codecov Action](https://github.com/proafxin/pd-extras/actions/workflows/codecov.yml/badge.svg)\n[![codecov](https://codecov.io/gh/proafxin/pd-extras/branch/develop/graph/badge.svg?token=AQA0IJY4N1)](https://codecov.io/gh/proafxin/pd-extras)[![Documentation Status](https://readthedocs.org/projects/pd-extras/badge/?version=latest)](https://pd-extras.readthedocs.io/en/latest/?badge=latest)\n\nSome functions on top of pandas.\n\n## Install Environment\n\nRun `python -m pip install -U pip` and `pip install -U pip poetry`. Then run `poetry install`. If you are facing issues installing `mysqlclient` or `psycopg2` on Ubuntu, it\'s because you are missing some libraries. Please check their pages. Usually for `psycopg2`, it\'s `libpq-dev` and for `mysqlclient`, it\'s `python3-dev default-libmysqlclient-dev build-essential`. Check the pages for more specific and accurate commands.\n\n## Generate Documentation Source Files\n\nYou should not have to do this but in case you want to generate the source ReStructuredText files yourself, here is how. Skip to the next section to simply generate html documentation locally.\n\nChange to docs directory `cd docs/`. Run `sphinx-quickstart`. Choose `y` when it asks to seperate build and source directories.\n\nChange to `docs/source` directory. In `conf.py`, add the following lines at the start of the script.\n\n```python\nimport os\nimport sys\n\nsys.path.insert(0, os.path.abspath("../.."))\n```\n\nand save it. Add `"sphinx.ext.autodoc",` to the `extensions` list. Run `python -m pip install -U sphinx_rtd_theme` and set `html_theme = "sphinx_rtd_theme"` (or whatever theme you want).\n\nIn `index.rst`, add `modules` to toctree. The structure should look like this:\n\n```markdown\n.. toctree::\n:maxdepth: 2\n:caption: Contents:\n\nmodules\n```\n\nRun the following to generate the source files.\n\n```markdown\npoetry install --with docs\npoetry run sphinx-apidoc -f -o source/ ../ ../tests/\n```\n\n## Generating HTML Documentation\n\nChange to `docs/` using `cd ..` then run `.\\make clean` and `.\\make html`. Output should be built with no errors or warnings. You will get the html documenation in `docs/build/html` directory. Open `index.html`.\n',
    'author': 'Masum Billal',
    'author_email': 'billalmasum93@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/proafxin/pandas-utils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
