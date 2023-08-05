# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbcl']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.46,<2.0.0',
 'prompt-toolkit>=2.0.10,<3.0.0',
 'pygments>=2.2.0,<3.0.0',
 'terminaltables>=3.1.0,<4.0.0']

entry_points = \
{'console_scripts': ['dbcl = dbcl.command_line:command_loop']}

setup_kwargs = {
    'name': 'dbcl',
    'version': '0.1.23',
    'description': 'A database command line interface that is engine-agnostic.',
    'long_description': "# dbcl - Database Command Line\n[![Build Status](https://travis-ci.org/ksofa2/dbcl.svg?branch=master)](https://travis-ci.org/ksofa2/dbcl)\n[![Maintainability](https://api.codeclimate.com/v1/badges/e4663675580964433469/maintainability)](https://codeclimate.com/github/ksofa2/dbcl/maintainability)\n\n\nAn engine-agnostic database command line interface.\n\n\n## Installation\n\nUse `pip` to install the dbcl tool:\n\n```\npip install dbcl\n```\n\nAlso install the necessary packages for your database, for example: `cx_Oracle`, `pg8000` or `PyMySQL`.\n\n\n## Database connection\n\nDatabase connections are specified using [SQLAlchemy database URLs](http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls). The database URL can be given as an argument to the `dbcl` command:\n\n```\ndbcl sqlite:///database.db\n```\n\nIf the URL isn't given as an argument, a prompt will ask for the URL to use for the connection:\n\n```\n$ dbcl\nConnect to [sqlite:///database.db]:\n```\n\nIf the DATABASE_URL environmental variable is set, that value will be the default for the database prompt:\n\n```\n$ export DATABASE_URL=sqlite:///database.db\n$ dbcl\nConnect to [sqlite:///database.db]:\n```\n\nExample of a connection to a PostgreSQL database using wht `pg8000` package:\n\n```\ndbcl postgresql+pg8000://username:password@127.0.0.1:5432/dbname\n```\n",
    'author': 'Kris Steinhoff',
    'author_email': 'ksteinhoff@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
