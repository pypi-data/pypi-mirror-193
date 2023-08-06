# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_docker_service']

package_data = \
{'': ['*']}

install_requires = \
['docker>=6.0.0', 'pytest>=7.1.3', 'tenacity>=8.1.0']

entry_points = \
{'pytest11': ['docker-service = pytest_docker_service.plugin']}

setup_kwargs = {
    'name': 'pytest-docker-service',
    'version': '0.2.4',
    'description': 'pytest plugin to start docker container',
    'long_description': '[![Python package](https://github.com/ClementDelgrange/pytest-docker-service/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/ClementDelgrange/pytest-docker-service/actions/workflows/ci.yaml)\n\n# pytest-docker-service\n\n`pytest-docker-service` is a pytest plugin for writing integration tests based on docker containers.\n\nThe plugin provides a *fixtures factory*: a configurable function to register fixtures.\n\nThe package has been developed and tested with Python 3.10, and pytest version 6.2.\n\n## Installation\nInstall `pytest-docker-service` with `pip`.\n\n```\npython -m pip install pytest-docker-service\n```\n\n## Usage\nYou just have to create a fixture in your `conftest.py` or in individual test modules, using the `docker_container` helper.\nFixture is created with the scope provided through the `scope` parameter.\nOther parameters are wrappers around the `docker-py` API (https://docker-py.readthedocs.io/en/stable/).\n\n```python\nimport requests\nfrom pytest_docker_service import docker_container\n\ncontainer = docker_container(\n    scope="session",\n    image_name="kennethreitz/httpbin",\n    ports={"80/tcp": None},\n)\n\n\ndef test_status_code(container):\n    port = container.port_map["80/tcp"]\n\n    status = 200\n    response = requests.get(f"http://127.0.0.1:{port}/status/{status}")\n\n    assert response.status_code == status\n```\n\nOf course, if you want to build your own docker image, it is possible.\nJust set the `build_path` parameter pointing to the directory containing the Dockerfile.\n```python\ncontainer = docker_container(\n    scope="session",\n    image_name="my-image",\n    build_path="path/to/dockerfile/directory",\n    ports={"80/tcp": None},\n)\n\n\ndef test_status_code(container):\n    port = container.port_map.["5432/tcp"]\n\n    ...\n\n```\n',
    'author': 'Clément Delgrange',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ClementDelgrange/pytest-docker-service',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0',
}


setup(**setup_kwargs)
