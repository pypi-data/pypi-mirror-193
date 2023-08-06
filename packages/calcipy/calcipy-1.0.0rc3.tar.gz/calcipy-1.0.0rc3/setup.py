# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['calcipy',
 'calcipy.check_for_stale_packages',
 'calcipy.code_tag_collector',
 'calcipy.dot_dict',
 'calcipy.md_writer',
 'calcipy.noxfile',
 'calcipy.tasks']

package_data = \
{'': ['*']}

install_requires = \
['beartype>=0.12.0', 'corallium>=0.1.0rc0', 'invoke>=2.0.0', 'pydantic>=1.10.5']

extras_require = \
{'ddict': ['python-box>=6.0.2'],
 'doc': ['commitizen>=2.42.0',
         'mdx_truly_sane_lists>=1.2',
         'mkdocs>=1.4.1',
         'mkdocs-build-plantuml-plugin>=1.7.4',
         'mkdocs-gen-files>=0.4.0',
         'mkdocs-git-revision-date-localized-plugin>=1.0.1',
         'mkdocs-literate-nav>=0.5.0',
         'mkdocs-material>=8.2.16',
         'mkdocs-section-index>=0.3.4',
         'mkdocstrings[python]>=0.18.1',
         'pandas>=1.5.3',
         'pylint>=2.16.2',
         'pyyaml>=5.2',
         'transitions>=0.9.0'],
 'doc:python_version < "3.12"': ['mkdocs-include-markdown-plugin>=4.0.3'],
 'flake8': ['dlint>=0.14.0',
            'flake8>=6.0.0',
            'flake8-adjustable-complexity>=0.0.6',
            'flake8-annotations-complexity>=0.0.7',
            'flake8-class-attributes-order>=0.1.3',
            'flake8-executable>=2.1.3',
            'flake8-expression-complexity>=0.0.11',
            'flake8-functions>=0.0.7',
            'flake8-pep3101>=2.0.0',
            'flake8-pie>=0.16.0',
            'flake8-printf-formatting>=1.1.2',
            'flake8-raise>=0.0.5',
            'flake8-require-beartype>=0.1.1',
            'flake8-sql>=0.4.1',
            'flake8-string-format>=0.3.0',
            'flake8-super>=0.1.3',
            'flake8-tuple>=0.4.1',
            'flake8-typing-imports>=1.14.0',
            'flake8-use-pathlib>=0.3.0',
            'flake8-variables-names>=0.0.5'],
 'lint': ['autopep8>=2.0.1',
          'bandit>=1.7.4',
          'pip-check>=2.8.1',
          'ruff>=0.0.248',
          'semgrep>=1.12.1'],
 'nox': ['nox-poetry>=1.0.2'],
 'pylint': ['pylint>=2.16.2'],
 'stale': ['arrow>=1.2.3',
           'bidict>=0.22.1',
           'pyrate_limiter>=2.4',
           'requests>=2.28.1'],
 'tags': ['arrow>=1.2.3', 'pandas>=1.5.3', 'tabulate>=0.9.0'],
 'test': ['pytest>=7.2.1',
          'pytest-cov>=4.0.0',
          'pytest-randomly>=3.12.0',
          'pytest-watcher>=0.2.6'],
 'types': ['mypy>=1.0.0']}

entry_points = \
{'console_scripts': ['calcipy = calcipy.scripts:start']}

setup_kwargs = {
    'name': 'calcipy',
    'version': '1.0.0rc3',
    'description': 'Python package to simplify development. Includes functionality for task running, testing, linting, documenting, and more',
    'long_description': '# calcipy\n\n![./calcipy-banner-wide.svg](https://raw.githubusercontent.com/KyleKing/calcipy/main/docs/calcipy-banner-wide.svg)\n\n`calcipy` is a Python package that implements best practices such as code style (linting, auto-fixes), documentation, CI/CD, and logging. Like the calcium carbonate in hard coral, packages can be built on the `calcipy` foundation.\n\n`calcipy` has some configurability, but is tailored for my particular use cases. If you want the same sort of functionality, there are a number of alternatives to consider:\n\n- [pyscaffold](https://github.com/pyscaffold/pyscaffold) is a much more mature project that aims for the same goals, but with a slightly different approach and tech stack (tox vs. nox, cookiecutter vs. copier, etc.)\n- [tidypy](https://github.com/jayclassless/tidypy#features), [pylama](https://github.com/klen/pylama), and [codecheck](https://pypi.org/project/codecheck/) offer similar functionality of bundling and running static checkers, but makes far fewer assumptions\n- [pytoil](https://github.com/FollowTheProcess/pytoil) is a general CLI tool for developer automation\n- And many more such as [pyta](https://github.com/pyta-uoft/pyta), [prospector](https://github.com/PyCQA/prospector), [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide) / [cjolowicz/cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python), [formate](https://github.com/python-formate/formate), [johnthagen/python-blueprint](https://github.com/johnthagen/python-blueprint), [oxsecurity/megalinter](https://github.com/oxsecurity/megalinter)etc.\n\n## Installation\n\nCalcipy needs a few static files managed using copier and a template project: [kyleking/calcipy_template](https://github.com/KyleKing/calcipy_template/)\n\nYou can quickly use the template to create a new project or add calcipy to an existing one:\n\n```sh\n# Install copier. Pipx is recommended\npipx install copier\n\n# To create a new project\ncopier copy gh:KyleKing/calcipy_template new_project\ncd new_project\n\n# Or update an existing one\ncd my_project\ncopier copy gh:KyleKing/calcipy_template .\n```\n\nSee [./Advanced_Configuration.md](./Advanced_Configuration.md) for documentation on the configurable aspects of `calcipy`\n\n### Calcipy CLI\n\nAdditionally, `calcipy` can be run as a CLI application without adding the package as a dependency.\n\nQuick Start:\n\n```sh\npipx install calcipy\n\n# Use the Collect Code Tags command to write all code tags to a single file\ncalcipy collect-code-tags -h\ncalcipy collect-code-tags -b=~/Some/Project\n\n# See additional documentation from the CLI help\ncalcipy -h\n```\n\n### Calcipy Pre-Commit\n\n`calcipy` can also be used as a `pre-commit` task by adding the below snippet to your `pre-commit` file:\n\n```yaml\nrepos:\n  - repo: https://github.com/KyleKing/calcipy\n    rev: main\n    hooks:\n      - id: calcipy-code-tags\n```\n\n## Calcipy Module Features\n\nThe core functionality of calcipy is the rich set of tasks run with `doit`\n\n- `poetry run doit --continue`: runs all default tasks. On CI (AppVeyor), this is a shorter list that should PASS, while locally the list is longer that are much more strict for linting and quality analysis\n\n    - The local default tasks include:\n        - **collect_code_tags**: Create a summary file with all of the found code tags. (i.e. TODO/FIXME, default output is [./docs/CODE_TAG_SUMMARY.md](./docs/CODE_TAG_SUMMARY.md))\n        - **cl_write**: Auto-generate the changelog based on commit history and tags.\n        - **lock**: Ensure poetry.lock and requirements.txt are up-to-date.\n        - **nox_coverage**: Run the coverage session in nox.\n        - **auto_format**: Format code with isort, autopep8, and others.\n        - **document**: Build the HTML documentation. (along with creating code diagrams!)\n        - **check_for_stale_packages**: Check for stale packages.\n        - **pre_commit_hooks**: Run the pre-commit hooks on all files.\n        - **lint_project**: Lint all project files that can be checked. (py, yaml, json, etc.)\n        - **static_checks**: General static checkers (Inspection Tiger, etc.).\n        - **security_checks**: Use linting tools to identify possible security vulnerabilities.\n        - **check_types**: Run type annotation checks.\n\n- Additional tasks include:\n\n    - **nox**/**test**/**coverage**: Tasks for running nox sessions, pytest in the local environment, and pytest coverage\n    - **ptw\\_\\***: Variations of tasks to run pytest watch\n    - **cl_bump** (**cl_bump_pre**):Bumps project version based on commits & settings in pyproject.toml.\n    - **doc.deploy**: Deploy docs to the Github `gh-pages` branch.\n    - **publish**: Build the distributable format(s) and publish.\n    - **check_license**: Check licenses for compatibility.\n    - **lint_critical_only**: Suppress non-critical linting errors. Great for gating PRs/commits.\n    - **lint_python**: Lint all Python files and create summary of errors.\n    - **open_docs**: Open the documentation files in the default browser.\n    - **open_test_docs**: Open the test and coverage files in default browser.\n    - **zip_release**: Zip up important information in the releases directory.\n\n- **calcipy** also provides a few additional nice features\n\n    - **dev.conftest**: some additional pytest configuration logic that outputs better HTML reports. Automatically implemented (imported to `tests/conftest.py`) when using `calcipy_template`\n    - **dev.noxfile**: nox functions that can be imported and run with or without the associated doit tasks. Also automatically configured when using `calcipy_template`\n    - **file_helpers**: some nice utilities for working with files, such as `sanitize_filename`, `tail_lines`, `delete_old_files`, etc. See documentation for most up-to-date documentation\n    - **log_heleprs**: where the most common use will be for `activate_debug_logging` or the more customizable `build_logger_config`\n    - **dot_dict**: has one function `ddict`, which is a light-weight wrapper around whatever is the most [maintained dotted-dictionary package in Python](https://pypi.org/search/?q=dot+accessible+dictionary&o=). Dotted dictionaries can sometimes improve code readability, but they aren\'t a one-size fits all solution. Sometimes `attr.s` or `dataclass` are more appropriate.\n        - The benefit of this wrapper is that there is a stable interface and you don\'t need to rewrite code as packages are born and die (i.e. [Bunch](https://pypi.org/project/bunch/) > [Chunk](https://pypi.org/project/chunk/) > [Munch](https://pypi.org/project/munch/) > [flexible-dotdict](https://pypi.org/project/flexible-dotdict/) > [Python-Box](https://pypi.org/project/python-box/) > ...)\n        - Note: if you need nested dotted dictionaries, check out [classy-json](https://pypi.org/project/classy-json/)\n\n> NOTE\n>\n> For the full list of available tasks, run `poetry run doit list`\n\n## Project Status\n\nSee the `Open Issues` and/or the [CODE_TAG_SUMMARY]. For release history, see the [CHANGELOG].\n\n## Contributing\n\nWe welcome pull requests! For your pull request to be accepted smoothly, we suggest that you first open a GitHub issue to discuss your idea. For resources on getting started with the code base, see the below documentation:\n\n- [DEVELOPER_GUIDE]\n- [STYLE_GUIDE]\n\n## Code of Conduct\n\nWe follow the [Contributor Covenant Code of Conduct][contributor-covenant].\n\n### Open Source Status\n\nWe try to reasonably meet most aspects of the "OpenSSF scorecard" from [Open Source Insights](https://deps.dev/pypi/calcipy)\n\n## Responsible Disclosure\n\nIf you have any security issue to report, please contact the project maintainers privately. You can reach us at [dev.act.kyle@gmail.com](mailto:dev.act.kyle@gmail.com).\n\n## License\n\n[LICENSE]\n\n[changelog]: ./docs/CHANGELOG.md\n[code_tag_summary]: ./docs/CODE_TAG_SUMMARY.md\n[contributor-covenant]: https://www.contributor-covenant.org\n[developer_guide]: ./docs/DEVELOPER_GUIDE.md\n[license]: https://github.com/kyleking/calcipy/LICENSE\n[style_guide]: ./docs/STYLE_GUIDE.md\n',
    'author': 'Kyle King',
    'author_email': 'dev.act.kyle@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyleking/calcipy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8.12,<4.0.0',
}


setup(**setup_kwargs)
