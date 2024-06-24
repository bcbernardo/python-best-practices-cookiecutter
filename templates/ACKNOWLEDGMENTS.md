<!--
{%- for author_info in authors -%}
SPDX-FileCopyrightText: {{copyright_years}} {{author_info}}
{%- endfor %}

SPDX-License-Identifier: {{project_license}}
-->

# Acknowledgements

## Template

This package was created with [Cookiecutter][] and the [bcbernardo/python-best-practices-cookiecutter][] project template, which in turn
extends the [Sourcery.AI's cookiecutter][] with the same name.

By default, this template features [Contributor Covenant][] as the repository's Code of Conduct, as well as an auto-generated `.gitignore` file by [gitignore.io][]. The code used by this template to automate documentation generation is adapted from [mkdocstrings][].

[Cookiecutter]: https://cookiecutter.readthedocs.io/en/1.7.2/advanced/index.html
[bcbernardo/python-best-practices-cookiecutter]: https://github.com/bcbernardo/python-best-practices-cookiecutter
[Sourcery.AI's cookiecutter]: https://github.com/sourcery-ai/python-best-practices-cookiecutter
[Contributor Covenant]: https://www.contributor-covenant.org/
[gitignore.io]: https://gitignore.io/
[mkdocstrings]: https://github.com/mkdocstrings/mkdocstrings

## Dependencies

### General dependencies

This package relies on [Python 3][] and its ecosystem and community.

Special thanks to the authors and contributors of Python's Standard Library and those responsible for the projects used in **{{project_name}}**, namely:

| Package name | Version | Summary |
| :----------: | :-----: | :------ |
{%- for pkg in direct_dependencies -%}
| [`{{ pkg["name"] }}`]({{ pkg["homepage"] }}) | `{{ pkg["version"] }}` | {{ pkg["summary"] }} |
{%- endfor %}

[Python 3]: https://www.python.org/

### Development dependencies

This project uses [`Poetry`][] to manage its dependencies.

Other utilities used for development purposes are:

| Package name | Version | Summary |
| :----------: | :-----: | :------ |
{%- for pkg in dev_dependencies -%}
| [`{{ pkg["name"] }}`]({{ pkg["homepage"] }}) | `{{ pkg["version"] }}` | {{ pkg["summary"] }} |
{%- endfor %}

[`Poetry`]: https://python-poetry.org/

### Indirect dependencies

The following libraries are required by the direct dependencies listed above, and therefore indirectly used by **{{project_name}}**:

| Package name | Version |
| :----------: | :-----: |
{%- for pkg in indirect_dependencies -%}
| [`{{ pkg["name"] }}`]({{ pkg["homepage"] }}) | `{{ pkg["version"] }}` |
{%- endfor %}

## Pre-commit hooks

The following packages have been implemented as external [pre-commit][] hooks to ensure code consistency, quality and safety:

{%- for hook in pre_commit_hooks -%}
[`{{ hook["id"] }}`]({{ hook["repo"] }}){% if not loop.last %} |{% endif %}
{%- endfor %}

[pre-commit]: https://pre-commit.com/
