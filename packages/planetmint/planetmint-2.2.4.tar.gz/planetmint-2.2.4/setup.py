# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['planetmint',
 'planetmint.backend',
 'planetmint.backend.localmongodb',
 'planetmint.backend.models',
 'planetmint.backend.tarantool',
 'planetmint.commands',
 'planetmint.web',
 'planetmint.web.views']

package_data = \
{'': ['*']}

install_requires = \
['abci==0.8.3',
 'aiohttp==3.8.1',
 'base58==2.1.1',
 'chardet==3.0.4',
 'flask-cors==3.0.10',
 'flask-restful==0.3.9',
 'flask==2.1.2',
 'gunicorn==20.1.0',
 'jsonschema==4.16.0',
 'logstats==0.3.0',
 'nest-asyncio==1.5.5',
 'packaging>=22.0',
 'planetmint-ipld>=0.0.3',
 'planetmint-transactions>=0.7.0',
 'protobuf==3.20.2',
 'pyasn1>=0.4.8',
 'pymongo==3.11.4',
 'python-decouple>=3.7,<4.0',
 'python-rapidjson>=1.0',
 'pyyaml==6.0.0',
 'requests==2.25.1',
 'setproctitle==1.2.2',
 'tarantool==0.7.1',
 'werkzeug==2.0.3']

entry_points = \
{'console_scripts': ['planetmint = planetmint.commands.planetmint:main']}

setup_kwargs = {
    'name': 'planetmint',
    'version': '2.2.4',
    'description': 'Planetmint: The Blockchain Database',
    'long_description': '<!---\nCopyright © 2020 Interplanetary Database Association e.V.,\nPlanetmint and IPDB software contributors.\nSPDX-License-Identifier: (Apache-2.0 AND CC-BY-4.0)\nCode is Apache-2.0 and docs are CC-BY-4.0\n--->\n\n<!--- There is no shield to get the latest version\n(including pre-release versions) from PyPI,\nso show the latest GitHub release instead.\n--->\n\n[![Codecov branch](https://img.shields.io/codecov/c/github/planetmint/planetmint/master.svg)](https://codecov.io/github/planetmint/planetmint?branch=master)\n[![Latest release](https://img.shields.io/github/release/planetmint/planetmint/all.svg)](https://github.com/planetmint/planetmint/releases)\n[![Status on PyPI](https://img.shields.io/pypi/status/planetmint.svg)](https://pypi.org/project/Planetmint)\n[![Build Status](https://app.travis-ci.com/planetmint/planetmint.svg?branch=main)](https://app.travis-ci.com/planetmint/planetmint)\n[![Join the chat at https://gitter.im/planetmint/planetmint](https://badges.gitter.im/planetmint/planetmint.svg)](https://gitter.im/planetmint/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n\n# Planetmint Server\n\nPlanetmint is the blockchain database. This repository is for _Planetmint Server_.\n\n## The Basics\n\n* [Try the Quickstart](https://docs.planetmint.io/en/latest/introduction/index.html#quickstart)\n\n## Run and Test Planetmint Server from the `master` Branch\n\nRunning and testing the latest version of Planetmint Server is easy. Make sure you have a recent version of [Docker Compose](https://docs.docker.com/compose/install/) installed. When you are ready, fire up a terminal and run:\n\n```text\ngit clone https://github.com/planetmint/planetmint.git\ncd planetmint\nmake run\n```\n\nPlanetmint should be reachable now on `http://localhost:9984/`.\n\nThere are also other commands you can execute:\n\n* `make start`: Run Planetmint from source and daemonize it (stop it with `make stop`).\n* `make stop`: Stop Planetmint.\n* `make logs`: Attach to the logs.\n* `make lint`: Lint the project\n* `make test`: Run all unit and acceptance tests.\n* `make test-unit-watch`: Run all tests and wait. Every time you change code, tests will be run again.\n* `make cov`: Check code coverage and open the result in the browser.\n* `make docs`: Generate HTML documentation and open it in the browser.\n* `make clean`: Remove all build, test, coverage and Python artifacts.\n* `make reset`: Stop and REMOVE all containers. WARNING: you will LOSE all data stored in Planetmint.\n\nTo view all commands available, run `make`.\n\n## Links for Everyone\n\n* [Planetmint.io](https://www.planetmint.io/) - the main Planetmint website, including newsletter signup\n\n## Links for Developers\n\n* [All Planetmint Documentation](https://docs.planetmint.io/en/latest/)\n* [CONTRIBUTING.md](.github/CONTRIBUTING.md) - how to contribute\n* [Community guidelines](CODE_OF_CONDUCT.md)\n* [Open issues](https://github.com/planetmint/planetmint/issues)\n* [Open pull requests](https://github.com/planetmint/planetmint/pulls)\n* [Gitter chatroom](https://gitter.im/planetmint/planetmint)\n\n## Legal\n\n* [Licenses](LICENSES.md) - open source & open content\n',
    'author': 'Planetmint contributors',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
