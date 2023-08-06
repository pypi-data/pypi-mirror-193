# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asbestos']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'asbestos-snow',
    'version': '1.0.4',
    'description': 'An easy way to mock Snowflake connections in Python!',
    'long_description': '# asbestos\nAn easy way to mock Snowflake connections in Python!\n\n## What is this?\n\n`asbestos` is a library to allow easy mocking of Snowflake calls during local development or testing to save on costs and time. The docs have more information, but here\'s a quick example:\n\n```python\nfrom asbestos import asbestos_cursor, config as asbestos_config\n\n\ndef snowflake_cursor() -> SnowflakeCursor | AsbestosCursor:\n    # Use a flag to decide whether it returns the test cursor\n    # or the real thing\n    if settings.ENABLE_ASBESTOS:\n        return asbestos_cursor()\n    return snowflake_connection().cursor(DictCursor)\n\n\nasbestos_config.register(\n    query="your sql goes %s",\n    data=("here",),\n    response={"It\'s a": "response!"}\n)\n\nwith snowflake_cursor() as cursor:\n    cursor.execute("your sql goes %s", (\'here\',))\n    assert cursor.fetchall() == {"It\'s a": "response!"}\n```\n\n`asbestos` is not a 1:1 mocking of the full Snowflake API, but includes synchronous and async query mocking that handle most use cases. Check out [some fun things you can do with it here][usage]!\n\n## Installation:\n\n```shell\npoetry add asbestos-snow\n```\n\nThe installation name is slightly different from the usage name due to someone claiming the name with no releases on PyPI; with luck, we will be able to finish the name requisition process to be able to use `asbestos` soon. If you\'re interested, you can [see how well that\'s going here](https://github.com/pypi/support/issues/2621).\n\n## Docs\n\n[Check out the documentation here!][docs]\n\nTo work on the docs locally, ensure that your `python3` version is up-to-date ([pyenv](https://github.com/pyenv/pyenv) is a great way of managing this) and run `make docs`. This will create a dedicated documentation environment and serve the docs locally for testing. To remove the environment, run `make docs_clean`.\n\n## Development\n\n`asbestos` uses `pre-commit` to help us keep the repo clean. To get started, make sure [you have `poetry` installed](https://python-poetry.org/) and follow these steps:\n\n* clone the respository:\n  * `git clone git@github.com:SpotOnInc/asbestos.git` (preferred)\n  * OR `git clone https://github.com/SpotOnInc/asbestos`\n* `poetry install`\n* `poetry shell`\n* `pre-commit install`\n\nAfter that, you\'re ready to go!\n\n[usage]: https://spotoninc.github.io/asbestos/usage/\n[docs]: https://spotoninc.github.io/asbestos/\n',
    'author': 'Joe Kaufeld',
    'author_email': 'jkaufeld@spoton.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/spotoninc/asbestos',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
