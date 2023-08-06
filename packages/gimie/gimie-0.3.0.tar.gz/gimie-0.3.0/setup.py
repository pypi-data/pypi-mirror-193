# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gimie', 'gimie.graph', 'gimie.sources']

package_data = \
{'': ['*']}

install_requires = \
['PyDriller>=2.3,<3.0',
 'calamus>=0.4.1,<0.5.0',
 'pre-commit>=3.0.0,<4.0.0',
 'pyshacl>=0.20.0,<0.21.0',
 'python-dotenv>=0.21.1,<0.22.0',
 'requests>=2.28.2,<3.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['gimie = gimie.cli:app']}

setup_kwargs = {
    'name': 'gimie',
    'version': '0.3.0',
    'description': 'Extract structured metadata from git repositories.',
    'long_description': '# Gimie\n\n[![PyPI version](https://badge.fury.io/py/gimie.svg)](https://badge.fury.io/py/gimie) [![Python Poetry Test](https://github.com/SDSC-ORD/gimie/actions/workflows/poetry-pytest.yml/badge.svg)](https://github.com/SDSC-ORD/gimie/actions/workflows/poetry-pytest.yml)\n\nGimie (GIt Meta Information Extractor) is a python library and command line tool to extract structured metadata from git repositories.\n\n:warning: Gimie is at an early development stage. It is not yet functional.\n\n## Context\nScientific code repositories contain valuable metadata which can be used to enrich existing catalogues, platforms or databases. This tool aims to easily extract structured metadata from a generic git repositories. The following sources of information are used:\n\n* [x] Github API\n* [ ] Gitlab API\n* [ ] Local Git metadata\n* [ ] License text\n* [ ] Free text in README\n* [ ] Renku project metadata\n\n## Installation\n\nTo install the stable version on PyPI:\n\n```shell\npip install gimie\n```\n\nTo install the dev version from github:\n\n```shell\npip install git+https://github.com/SDSC-ORD/gimie.git@main#egg=gimie\n```\n\nGimie is also available as a docker container hosted on the [Github container registry](https://github.com/SDSC-ORD/gimie/pkgs/container/gimie):\n\n```shell\ndocker pull ghcr.io/sdsc-ord/gimie:latest\n\n# The access token can be provided as an environment variable\ndocker run -e ACCESS_TOKEN=$ACCESS_TOKEN ghcr.io/sdsc-ord/gimie:latest gimie data <repo>\n```\n\n\n### For development:\n\nactivate a conda or virtual environment with Python 3.8 or higher\n\n```shell\ngit clone https://github.com/SDSC-ORD/gimie && cd gimie\nmake install\n```\n\nrun tests:\n\n```shell\nmake test\n```\n\nrun checks:\n\n```shell\nmake check\n```\n\n## Usage\n\n### Set your github credentials\n\nIn order to avoid rate limits with the github api, you need to provide your github\nusername and a github token: see\n[here ](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)\non how to generate a github token.\n\nThere are 2 options for setting up your github token in your local environment:\n\n**Option 1:**\n\n```\ncp .env.dist .env\n```\n\nAnd then edit the `.env` file and put your github token in.\n\n**Option 2:**\n\nAdd your github token in your terminal:\n\n```bash\nexport ACCESS_TOKEN=\n```\n\nAfter the github token has been added, you can run the command without running into an github api limit.\nOtherwise you can still run the command, but might hit that limit after running the command several times.\n\n### Run the command\n\nAs a command line tool:\n```shell\ngimie data https://github.com/numpy/numpy\n```\nAs a python library:\n\n```python\nfrom gimie.project import Project\nproj = Project("https://github.com/numpy/numpy)\n\n# To retrieve the rdflib.Graph object\ng = proj.to_graph()\n\n# To retrieve the serialized graph\nproj.serialize(format=\'ttl\')\n```\n\nOr to extract only from a specific source:\n```python\nfrom gimie.sources.remote import GithubExtractor\ngh = GithubExtractor(\'https://github.com/SDSC-ORD/gimie\')\ngh.extract()\n\n# To retrieve the rdflib.Graph object\ng = gh.to_graph()\n\n# To retrieve the serialized graph\ngh.serialize(format=\'ttl\')\n```\n\n## Outputs\n\nThe default output is JSON-ld, a JSON serialization of the [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework) data model. We follow the schema recommended by [codemeta](https://codemeta.github.io/).\nSupported formats are json-ld, turtle and n-triples.\n\n## Contributing\n\nAll contributions are welcome. New functions and classes should have associated tests and docstrings following the [numpy style guide](https://numpydoc.readthedocs.io/en/latest/format.html).\n\nThe code formatting standard we use is [black](https://github.com/psf/black), with `--line-length=79` to follow [PEP8](https://peps.python.org/pep-0008/) recommendations. We use [pytest](https://docs.pytest.org/en/7.2.x/) as our testing framework. This project uses [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) to define package information, requirements and tooling configuration.\n\n## Releases and Publishing on Pypi\n\nReleases are done via github release\n\n- a release will trigger a github workflow to publish the package on Pypi\n- Make sure to update to a new version in `pyproject.toml` before making the release\n- It is possible to test the publishing on Pypi.test by running a manual workflow: go to github actions and run the Workflow: \'Publish on Pypi Test\'\n',
    'author': 'Swiss Data Science Center',
    'author_email': 'contact@datascience.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SDSC-ORD/gimie',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
