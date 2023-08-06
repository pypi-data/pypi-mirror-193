# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['localnow']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'localnow',
    'version': '0.1.0',
    'description': 'Drop-in replacement for `datetime.datetime.now()` explicitly set with the local timezone.',
    'long_description': "# localnow\n\n## Description\n\nThis small Python package is a drop-in replacement for `datetime.datetime.now` that returns the current time in the \nlocal timezone.\n\n## Usage\n\nSuppose you want the current date and time. You could do this:\n\n```python\nimport datetime\n\nx = datetime.datetime.now()\n```\n\nBy default, `x` will be in UTC. `datetime.datetime.now` takes an optional `tz` argument that you can use to specify a\ndifferent timezone. However, if you want to use your *local* timezone, wherever that may be, you need an extra step:\n\n```python\nimport datetime\n\ntz = datetime.datetime.utcnow().astimezone().tzinfo\nx = datetime.datetime.now(tz=tz)\n```\n\nPersonally, I find the `tz = ...` line to be a bit of a distraction and difficult to remember, so I made this package.\nIt provides a drop-in replacement for `datetime.datetime.now` that is essentially does the same as the code above but\nwith a little less code:\n\n```python\nfrom localnow import now\n\nx = now()\n```\n\nThat's it.\n\n## Installation\n\nYou can install this package from PyPI:\n\n```bash\npip install localnow\n```\n\n## License\n\nMIT\n\n",
    'author': 'Sam Mathias',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sammosummo/localnow',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
