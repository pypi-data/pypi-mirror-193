# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['combadge',
 'combadge.core',
 'combadge.core.markers',
 'combadge.support',
 'combadge.support.http',
 'combadge.support.httpx',
 'combadge.support.httpx.backends',
 'combadge.support.rest',
 'combadge.support.soap',
 'combadge.support.zeep',
 'combadge.support.zeep.backends']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.4,<2.0.0', 'typing-extensions>=4.4.0,<5.0.0']

extras_require = \
{':python_version < "3.10"': ['get-annotations>=0.1.2,<0.2.0'],
 'httpx': ['httpx>=0.23.3,<0.24.0'],
 'pkgsettings': ['pkgsettings>=1.0.0,<2.0.0'],
 'zeep': ['zeep>=4.2.1,<5.0.0']}

setup_kwargs = {
    'name': 'combadge',
    'version': '0.1.0.dev5',
    'description': 'Generic API client based on Pydantic',
    'long_description': '# Combadge\n\n[![Checks](https://img.shields.io/github/checks-status/kpn/combadge/main?logo=github)](https://github.com/kpn/combadge/actions/workflows/check.yaml)\n[![Coverage](https://codecov.io/gh/kpn/combadge/branch/main/graph/badge.svg?token=ZAqYAaTXwE)](https://codecov.io/gh/kpn/combadge)\n![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)\n[![Python Version](https://img.shields.io/pypi/pyversions/combadge?logo=python&logoColor=yellow)](https://pypi.org/project/combadge/)\n[![License](https://img.shields.io/github/license/kpn/combadge)](LICENSE)\n\n**📻 Application to the service, please respond!**\n\n## Features\n\n- [**Pydantic**](https://docs.pydantic.dev/)-based request and response models\n- Automatically derived exception classes\n- Using [**Protocol**](https://peps.python.org/pep-0544/)s to define service classes\n- Built-in backends:\n  - [HTTPX](https://www.python-httpx.org/), sync and async\n  - [Zeep](https://docs.python-zeep.org/en/master/), sync and async\n- Pluggable backends\n\n## Documentation\n\n<a href="https://kpn.github.io/combadge/">\n    <img alt="Documentation" height="30em" src="https://img.shields.io/github/actions/workflow/status/kpn/combadge/docs.yml?label=documentation&logo=github">\n</a>\n\n## 🚀 Quick example\n\n```python title="quickstart_httpx.py"\nfrom http import HTTPStatus\nfrom typing import List\n\nfrom httpx import Client\nfrom pydantic import BaseModel, Field\nfrom typing_extensions import Annotated, Protocol\n\nfrom combadge.core.binder import bind\nfrom combadge.support.http.markers import QueryParam, StatusCode, http_method, path\nfrom combadge.support.httpx.backends.sync import HttpxBackend\n\n\n# 1️⃣ Declare the response models:\nclass CurrentCondition(BaseModel):\n    humidity: int\n    temperature: Annotated[float, Field(alias="temp_C")]\n\n\nclass Weather(BaseModel):\n    status: StatusCode\n    current: Annotated[List[CurrentCondition], Field(alias="current_condition")]\n\n\n# 2️⃣ Declare the protocol:\nclass SupportsWttrIn(Protocol):\n    @http_method("GET")\n    @path("/{in_}")\n    def get_weather(\n        self,\n        *,\n        in_: str,\n        format_: Annotated[str, QueryParam("format")] = "j1",\n    ) -> Weather:\n        raise NotImplementedError\n\n\n# 3️⃣ Bind the service:\nbackend = HttpxBackend(Client(base_url="https://wttr.in"))\nservice = bind(SupportsWttrIn, backend)\n\n# 🚀 Call the service:\nresponse = service.get_weather(in_="amsterdam")\nassert response.status == HTTPStatus.OK\nassert response.current[0].humidity == 71\nassert response.current[0].temperature == 8.0\n```\n',
    'author': 'Pavel Perestoronin',
    'author_email': 'pavel.perestoronin@kpn.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kpn/combadge',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
