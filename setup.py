#
# Copyright (C) 2020 RFI
#
# Author: James Parkhurst
#
# This code is distributed under the Apache license, a copy of
# which is included in the root directory of this package.
#

from setuptools import setup


def main():
    """
    Setup the package

    """
    tests_require = ["pytest"]

    setup(
        name="scivision-parakeet-datasource",
        version="0.0.1",
        packages=["scivision_parakeet_datasource"],
        install_requires=[
            "python-parakeet",
            "scivision",
            "scivision-parakeet@git+https://github.com/rosalindfranklininstitute/scivision-parakeet.git@main",
        ],
        setup_requires=["pytest-runner"],
        tests_require=["pytest"],
        test_suite="tests",
        include_package_data=True,
    )


if __name__ == "__main__":
    main()
