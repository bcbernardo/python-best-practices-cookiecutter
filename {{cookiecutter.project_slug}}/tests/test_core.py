# SPDX-FileCopyrightText: {{cookiecutter.year}} {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>
#
# SPDX-License-Identifier: {{cookiecutter.license}}


import pytest

from {{cookiecutter.package_name}}.core import main


def test_main() -> None:
    with pytest.raises(NotImplementedError):
        main()
