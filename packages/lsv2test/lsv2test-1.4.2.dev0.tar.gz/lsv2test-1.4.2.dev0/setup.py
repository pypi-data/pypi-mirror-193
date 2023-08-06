#!/usr/bin/env python

import urllib.request

from setuptools import setup

from localstack_cli import __version__

# download the README.md from the community repo
url = "https://raw.githubusercontent.com/localstack/localstack/master/README.md"
response = urllib.request.urlopen(url)
charset = response.info().get_content_charset()
readme_content = response.read().decode(charset)

setup(
    name="lsv2test",
    version=__version__,
    long_description=readme_content,
    long_description_content_type="text/markdown",
    description="LocalStack - A fully functional local Cloud stack",
    author="LocalStack Contributors",
    author_email="info@localstack.cloud",
    url="https://github.com/localstack/localstack",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Emulators",
    ],
    install_requires=[f"lsv2test-ext=={__version__}"],
    extras_require={
        "runtime": [f"lsv2test-ext[runtime]=={__version__}"],
        # TODO remove with 2.0 - full is deprecated, but might still be used
        "full": [f"lsv2test-ext[runtime]=={__version__}"],
    },
)
