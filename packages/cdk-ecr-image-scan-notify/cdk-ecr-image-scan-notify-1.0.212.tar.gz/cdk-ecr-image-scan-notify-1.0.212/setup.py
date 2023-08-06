import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-ecr-image-scan-notify",
    "version": "1.0.212",
    "description": "cdk-ecr-image-scan-notify is an AWS CDK construct library that notify the slack channel of Amazon ECR image scan results",
    "license": "Apache-2.0",
    "url": "https://github.com/hayao-k/cdk-ecr-image-scan-notify.git",
    "long_description_content_type": "text/markdown",
    "author": "hayao-k<30886141+hayao-k@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/hayao-k/cdk-ecr-image-scan-notify.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_ecr_image_scan_notify",
        "cdk_ecr_image_scan_notify._jsii"
    ],
    "package_data": {
        "cdk_ecr_image_scan_notify._jsii": [
            "cdk-ecr-image-scan-notify@1.0.212.jsii.tgz"
        ],
        "cdk_ecr_image_scan_notify": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.31.1, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.75.0, <2.0.0",
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
