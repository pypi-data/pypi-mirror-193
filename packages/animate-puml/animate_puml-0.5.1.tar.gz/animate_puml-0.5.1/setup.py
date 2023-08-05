# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['animate_puml']

package_data = \
{'': ['*']}

install_requires = \
['pillow>=9.4.0,<10.0.0',
 'py-executable-checklist==1.4.0',
 'pygifsicle>=1.0.7,<2.0.0',
 'pytest>=7.2.0,<8.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'rich>=13.0.0,<14.0.0']

entry_points = \
{'console_scripts': ['animate-puml = animate_puml.app:main']}

setup_kwargs = {
    'name': 'animate-puml',
    'version': '0.5.1',
    'description': 'Simple animation of PlantUML diagrams',
    'long_description': '# PlantUML Animation\n\n[![PyPI](https://img.shields.io/pypi/v/animate-puml?style=flat-square)](https://pypi.python.org/pypi/animate-puml/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/animate-puml?style=flat-square)](https://pypi.python.org/pypi/animate-puml/)\n[![PyPI - License](https://img.shields.io/pypi/l/animate-puml?style=flat-square)](https://pypi.python.org/pypi/animate-puml/)\n\nSimple animation for PlantUML diagrams.\n\n![](assets/security-puml.gif)\n\n---\n\n**Documentation**: [https://namuan.github.io/animate-puml](https://namuan.github.io/animate-puml)\n\n**Source Code**: [https://github.com/namuan/animate-puml](https://github.com/namuan/animate-puml)\n\n**PyPI**: [https://pypi.org/project/animate-puml/](https://pypi.org/project/animate-puml/)\n\n---\n\n## Pre-requisites\n\n- [PlantUML](https://plantuml.com/)\n  ```shell\n  brew install plantuml\n  ```\n\n## Installation\n\n```sh\npip install animate-puml\n```\n\n## Usage\n\nGiven an example PlantUML document in `assets/security.puml`:\n\n```shell\nanimate-puml -i assets/security.puml -o assets/security-puml.gif\n```\n\nBy default, the script will delete any temporary files generated during the animation process.\nTo keep the files, use the `--debug` flag.\n\n```shell\nanimate-puml -i assets/security.puml -o assets/security-puml.gif --debug\n```\n\nEach frame of the animation will wait for 1 second by default.\nTo change the wait time, use the `--frame-duration` flag to specify the time in milliseconds.\n\n```shell\nanimate-puml -i assets/security.puml -o assets/security-puml.gif --frame-duration 4000\n```\n\nUse the `-h` flag to see all available options.\n\n```shell\nanimate-puml -h\n```\n\n## Acknowledgements\n\n- [PlantUML](https://plantuml.com/)\n\n## Development\n\n* Clone this repository\n* Requirements:\n  * Python 3.7+\n  * [Poetry](https://python-poetry.org/)\n\n* Create a virtual environment and install the dependencies\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n```sh\npoetry shell\n```\n\n### Validating build\n```sh\nmake build\n```\n\n### Release process\nA release is automatically published when a new version is bumped using `make bump`.\nSee `.github/workflows/build.yml` for more details.\nOnce the release is published, `.github/workflows/publish.yml` will automatically publish it to PyPI.\n\n### Disclaimer\n\nThis project is not affiliated with PlantUML.\n',
    'author': 'namuan',
    'author_email': 'github@deskriders.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://namuan.github.io/animate-puml',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0',
}


setup(**setup_kwargs)
