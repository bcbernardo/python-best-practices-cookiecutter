<!--
SPDX-FileCopyrightText: {{cookiecutter.year}} {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

SPDX-License-Identifier: {{cookiecutter.license}}
-->

# {{cookiecutter.project_name}}

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md)

{{cookiecutter.project_description}}

## Install

```sh
# Install dependencies
poetry install

# Setup pre-commit and pre-push hooks
poetry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [bcbernardo/python-best-practices-cookiecutter](https://github.com/bcbernardo/python-best-practices-cookiecutter) project template.
