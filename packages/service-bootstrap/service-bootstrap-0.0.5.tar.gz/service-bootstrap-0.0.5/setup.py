import setuptools
import os
import time

with open("README.md", "r") as fh:
    long_description = fh.read()

version = open("version.txt", "r").read()
postfix = "" if os.getenv("RELEASE", "0") == "1" else ".dev%s" % round(time.time())


setuptools.setup(
    name="service-bootstrap",
    version=f"{version}{postfix}",
    description="Framework for setting up service",
    author="Rafał Zarajczyk",
    author_email="rzarajczyk@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rzarajczyk/service-bootstrap",
    keywords=[],
    packages=['bootstrap'],
    package_dir={'bootstrap': './src/bootstrap'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyyaml~=6.0", "tzlocal", "pytz"],
)
