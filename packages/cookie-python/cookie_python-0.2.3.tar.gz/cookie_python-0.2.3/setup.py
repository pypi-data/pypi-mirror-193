# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['{{cookiecutter.project_name}}',
 '{{cookiecutter.project_name}}.tests',
 '{{cookiecutter.project_name}}.{{cookiecutter.project_slug}}']

package_data = \
{'': ['*'],
 '{{cookiecutter.project_name}}': ['.github/workflows/*',
                                   '.github/workflows/actions/python-poetry/*',
                                   'cookiecutter_template_data/*',
                                   'cookiecutter_template_data/licenses/*',
                                   'docker/*']}

install_requires = \
['loguru', 'poetry-dynamic-versioning', 'pygithub', 'pyyaml', 'semver']

entry_points = \
{'console_scripts': ['manage-cookie = cookie_python.manage.main:main',
                     'new-cookie = cookie_python.new:main']}

setup_kwargs = {
    'name': 'cookie-python',
    'version': '0.2.3',
    'description': '',
    'long_description': '# [Cookiecutter][cookiecutter] template for new Python projects\n\n[![PyPI](https://img.shields.io/pypi/v/cookie-python)][pypi]\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cookie-python)][pypi]\n[![Build](https://img.shields.io/github/checks-status/smkent/cookie-python/main?label=build)][gh-actions]\n[![codecov](https://codecov.io/gh/smkent/cookie-python/branch/main/graph/badge.svg)][codecov]\n[![GitHub stars](https://img.shields.io/github/stars/smkent/cookie-python?style=social)][repo]\n\n[![cookie-python][logo]](#)\n\nA template for new Python projects, with:\n\n* [poetry][poetry] (with [poetry-dynamic-versioning][poetry-dynamic-versioning])\n* [pytest][pytest]\n* [pre-commit][pre-commit]\n* [mypy][mypy]\n* [black][black]\n* [flake8][flake8] (with [bugbear][flake8-bugbear], [simplify][flake8-simplify],\n  and [pep8-naming][pep8-naming])\n* [autoflake][autoflake]\n* [pyupgrade][pyupgrade]\n* [bandit][bandit]\n* [cruft][cruft]\n* GitHub Actions support\n* Coverage reports with [codecov.io][codecovio]\n\n## Poetry installation\n\nVia [`pipx`][pipx]:\n\n```console\npip install pipx\npipx install poetry\npipx inject poetry poetry-dynamic-versioning poetry-pre-commit-plugin\n```\n\nVia `pip`:\n\n```console\npip install poetry\npoetry self add poetry-dynamic-versioning poetry-pre-commit-plugin\n```\n\n## New project creation\n\n### With [cruft][cruft] via script\n\n```console\npoetry install\npoetry run new-cookie <path>  # or poetry run cruft create\n```\n\n### With [cookiecutter][cookiecutter] directly\n\n```console\npip install cookiecutter\ncookiecutter https://github.com/smkent/cookie-python\n```\n\n## Development tasks\n\n* Setup: `poetry install`\n* Run static checks: `poetry run poe lint` or\n  `poetry run pre-commit run --all-files`\n* Run static checks and tests: `poetry run poe test`\n* Update test expected output files from test results:\n  `poetry run poe updatetests`\n\n[autoflake]: https://github.com/PyCQA/autoflake\n[bandit]: https://github.com/PyCQA/bandit\n[black]: https://github.com/psf/black\n[codecov]: https://codecov.io/gh/smkent/cookie-python\n[codecovio]: https://codecov.io\n[cookiecutter]: https://github.com/cookiecutter/cookiecutter\n[cruft]: https://github.com/cruft/cruft\n[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear\n[flake8-simplify]: https://github.com/MartinThoma/flake8-simplify\n[flake8]: https://github.com/pycqa/flake8\n[gh-actions]: https://github.com/smkent/cookie-python/actions?query=branch%3Amain\n[logo]: https://raw.github.com/smkent/cookie-python/main/img/cookie-python.png\n[mypy]: https://github.com/python/mypy\n[pep8-naming]: https://github.com/PyCQA/pep8-naming\n[pipx]: https://pypa.github.io/pipx/\n[poetry-dynamic-versioning]: https://github.com/mtkennerly/poetry-dynamic-versioning\n[poetry-installation]: https://python-poetry.org/docs/#installation\n[poetry]: https://python-poetry.org/\n[pre-commit]: https://pre-commit.com/\n[pypi]: https://pypi.org/project/cookie-python/\n[pytest]: https://docs.pytest.org\n[pyupgrade]: https://github.com/asottile/pyupgrade\n[repo]: https://github.com/smkent/cookie-python\n',
    'author': 'Stephen Kent',
    'author_email': 'smkent@smkent.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/smkent/cookie-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
