# {{cookiecutter.project_name}}

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