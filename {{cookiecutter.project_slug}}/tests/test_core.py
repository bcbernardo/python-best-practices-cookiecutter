import pytest

from {{cookiecutter.package_name}}.core import main


def test_main() -> None:
    with pytest.raises(NotImplementedError):
        main()
