# SPDX-FileCopyrightText: 2019 Sourcery
# SPDX-FileCopyrightText: 2021 Bernardo C Baron <bc.bernardo@hotmail.com>
#
# SPDX-License-Identifier: MIT


import re
import sys

PROJECT_REGEX = r"^[a-zA-Z][a-zA-Z0-9 ]+$"
project_name = "{{ cookiecutter.project_name }}"

if not re.match(PROJECT_REGEX, project_name):
    print(
        "ERROR: '{}' is not a valid Python project name!".format(project_name)
    )
    sys.exit(1)
