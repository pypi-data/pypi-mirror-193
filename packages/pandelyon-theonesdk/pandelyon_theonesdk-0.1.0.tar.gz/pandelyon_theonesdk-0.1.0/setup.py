# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tor']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'pandelyon-theonesdk',
    'version': '0.1.0',
    'description': 'Prototype SDK built against The One API',
    'long_description': '# adyates-SDK\n\nSample SDK against The One Ring API.  Developed with (and requires) Python3.\n\n# Using the SDK\n\n## Keys\n\nYou will need have an API key from [The One API](https://the-one-api.dev/).\n\n## Environment Variables\n\n| Name | Required | Purpose |\n|------|----------|---------|\n| TOR_ONEAPIKEY | Yes | To make authenticated requests against the The One API |\n| TOR_BASEURI | No (Default: `https://the-one-api.dev/v2`) | Base URL for all issued API requests |\n\n\n## Installation\nInstall from PyPI using the following command\n\n```\npython -m pip install pandelyon-theonesdk\n```\n\nOr whatever package manager you choose to use.\n\n\nTo use the SDK, import as follows:\n\n```\nimport tor\n```\n\n## Querying\n\nSuccessful results are returned as a list of dicts with the direct API values along with meta information about\nthe query, useful for pagination (if needed).\n\n```\n## Fetching the list of Lord of the Rings movies\nmovies = tor.Movies().get()\n\nmovies.results  # [{"_id": "5cd95395de30eff6ebccde5b","name": "The Two Towers", ...]\nmovies.meta     # {"total": 8, "limit": 1000, "offset": 0, "page": 1, "pages": 1}\n\n\n## Fetching only The Two Towers\n\ntwo_towers = tor.Movies("5cd95395de30eff6ebccde5b")\n\n## Fetching quotes from The Two Towers\ntwo_towers = tor.Movies(\n    "5cd95395de30eff6ebccde5b",\n    quotes=True\n).get()\n\n## ...in a specific order\ntwo_towers = tor.Movies(\n    "5cd95395de30eff6ebccde5b",\n    quotes=True,\n    sortby="character:asc"  # Or "character:desc"\n).get()\n\n## Paging through quotes from The Two Towers\n\n#### Using offsets\ntwo_towers = tor.Movies(\n    "5cd95395de30eff6ebccde5b",\n    quotes=True,\n    pagination={"limit": 10, "offset": 30}\n).get()\n\n#### .. Or by page\ntwo_towers = tor.Movies(\n    "5cd95395de30eff6ebccde5b",\n    quotes=True,\n    pagination={"limit": 10, "page": 4}\n).get()\n\n## Filtering the results (But see the Notes below)\n\ntwo_towers = tor.Movies(\n    "5cd95395de30eff6ebccde5b",\n    quotes=True,\n    filters=[\n        "character!=5cd99d4bde30eff6ebccfc15",\n        "dialog=/Dwarf/"\n    ]\n).get()\n```\n\n## Exceptions\n\nWhen executing a query, the following exceptions may occur prior to `requests` making the query:\n\n* `RuntimeError`: If the SDK environment variables (e.g. the API Key) are not properly set\n* `requests.RequestError`: If the parameters for any request are incorrectly formed\n\nAny other errors thrown by `requests.get()` will be passed to the user.\n\n\n# Notes about the behavior of API itself\n\n* When building a paginated query, `offset` and `page` cannot be used at the same time.  If both are present, the `offset` parameter will take priority over `page`.\n* Although the filtering API will work on other queries, `/movies` seems to ignore them (e.g. Attempting to regex quotes only containing Dwarf or to a specific character will not work). This isn\'t apparent in this SDK but is more obvious when performing the same examples on `/character`. \n\n\n# Contributing and Development\n\nDevelopment is done with [`poetry`](https://python-poetry.org/).  \n\nInstall with test dependecies included:\n\n```poetry install --with test```\n\nRun tests with `poe`:\n\n```poe test```\n\n\nBy default, test coverage results are located in two places:\n\n* Human-readable `htmlcov/index.html`\n* Machine-interpretable `test-reports/coverage.xml`\n',
    'author': 'A Y',
    'author_email': 'github@pandelyon.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/adyates/adyates-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
