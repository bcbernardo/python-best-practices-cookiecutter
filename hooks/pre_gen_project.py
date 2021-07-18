import re
import sys

PROJECT_REGEX = r"^[a-zA-Z][a-zA-Z0-9 ]+$"
project_name = "{{ cookiecutter.project_name }}"

if not re.match(PROJECT_REGEX, project_name):
    print(
        "ERROR: '{}' is not a valid Python project name!".format(project_name)
    )
    sys.exit(1)
