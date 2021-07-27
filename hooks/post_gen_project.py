# SPDX-FileCopyrightText: 2019 Sourcery
# SPDX-FileCopyrightText: 2021 Bernardo C Baron <bc.bernardo@hotmail.com>
#
# SPDX-License-Identifier: MIT


import shutil
import sys
import urllib3
from pathlib import Path
from typing import Union


def set_python_version():
    python_version = "{}.{}".format(
        sys.version_info.major,
        sys.version_info.minor,
    )

    file_names = ["Dockerfile", "pyproject.toml", ".github/workflows/test.yml"]
    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read()
            contents = contents.replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"

LICENSE = "{{cookiecutter.license}}"
LICENSES_DIR = Path("LICENSES")


def get_license(license: str, out_dir: Union[str, Path]) -> None:
    """Downloads a license text file from SPDX repository."""
    spdx_license_url = (
        "https://raw.githubusercontent.com/spdx/license-list-data/master/text"
        "/{}.txt".format(license)
    )
    http = urllib3.PoolManager()
    out_path = Path(out_dir, license)
    if not out_path.is_file():
        with \
                http.request("GET", spdx_license_url) as r, \
                open(out_path, "w") as out_file:
            shutil.copyfileobj(r.data, out_file)


def main() -> None:
    set_python_version()
    get_license(LICENSE, LICENSES_DIR)
    print(SUCCESS + "Project successfully initialized" + TERMINATOR)


if __name__ == "__main__":
    main()
