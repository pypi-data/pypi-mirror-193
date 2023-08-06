import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "blackmamba72-tgw",
    "version": "0.0.2",
    "description": "blackmamba72-tgw",
    "license": "Apache-2.0",
    "url": "https://github.com/cmorgia/tgw.git",
    "long_description_content_type": "text/markdown",
    "author": "Claudio Morgia<214524+cmorgia@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cmorgia/tgw.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "blackmamba72_tgw",
        "blackmamba72_tgw._jsii"
    ],
    "package_data": {
        "blackmamba72_tgw._jsii": [
            "blackmamba72-tgw@0.0.2.jsii.tgz"
        ],
        "blackmamba72_tgw": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.65.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.74.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
