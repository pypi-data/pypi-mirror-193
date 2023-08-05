# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hyperfastpy']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['hyperfastpy = hyperfastpy.__cli__:main']}

setup_kwargs = {
    'name': 'hyperfast-python-template',
    'version': '0.0.1rc10',
    'description': 'A python template that helps you jump start your project',
    'long_description': '# Hyperfast Python Template\n\n![][version-image]\n[![Release date][release-date-image]][release-url]\n[![License][license-image]][license-url]\n[![semantic-release][semantic-image]][semantic-url]\n[![Jupyter Book][jupyter-book-image]][jupyter-book-url]\n[![Conventional Commits][conventional-commits-image]][conventional-commits-url]\n\nA python template that helps you jump start your project\n\n- Documentation: https://entelecheia.github.io/hyperfast-python-template\n- GitHub: https://gihub.com/entelecheia/hyperfast-python-template\n- PyPI: https://pypi.org/project/hyperfast-python-template\n\nHyperfast Python Template is a self-contained template that helps you initialize your Python project inside the template.\n\n## Usage\n\nThere are three ways to use this project:\n\n1. Use [the template][template-url] to create a new repository\n2. Use [Copier][copier-url] to create a project to your local machine directly\n3. Inject [the template][template-url] into an existing project\n\n### 1. Use the template\n\n1. Click the `Use this template` button\n2. Enter a name for your repository\n3. Click `Create repository from template`\n4. Clone your new repository to your local machine\n5. Initialize your project with `make init-project`\n6. Do your work\n\n### 2. Use Copier\n\n1. Install Copier with `pipx install copier`\n2. Run `copier gh:entelecheia/hyperfast-python-template path/to/destination`\n3. Initialize your project with `make init-git`\n4. Do your work\n\n### 3. Inject the template\n\n1. From the root of your project, run `copier gh:entelecheia/hyperfast-python-template .`\n2. If your project is not a git repository, initialize it with `make init-git`\n3. Do your work\n\n## License\n\nThis project is released under the [MIT License][license-url].\n\n<!-- Links: -->\n\n[repo-url]: https://gihub.com/entelecheia/hyperfast-python-template\n[pypi-url]: https://pypi.org/project/hyperfast-python-template\n[docs-url]: https://entelecheia.github.io/hyperfast-python-template\n[version-image]: https://img.shields.io/github/v/release/entelecheia/hyperfast-python-template?sort=semver\n[release-date-image]: https://img.shields.io/github/release-date/entelecheia/hyperfast-python-template\n[release-url]: https://github.com/entelecheia/hyperfast-python-template/releases\n[license-image]: https://img.shields.io/github/license/entelecheia/hyperfast-python-template\n[license-url]: https://github.com/entelecheia/hyperfast-python-template/blob/main/LICENSE\n[changelog-url]: https://github.com/entelecheia/hyperfast-python-template/blob/main/CHANGELOG.md\n\n[template-url]: https://github.com/entelecheia/hyperfast-python-template\n[semantic-image]: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg\n[semantic-url]: https://github.com/semantic-release/semantic-release\n[conventional-commits-image]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white\n[conventional-commits-url]: https://conventionalcommits.org\n[copier-url]: https://copier.readthedocs.io\n[jupyter-book-image]: https://jupyterbook.org/en/stable/_images/badge.svg\n[jupyter-book-url]: https://jupyterbook.org\n',
    'author': 'Young Joon Lee',
    'author_email': 'entelecheia@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
