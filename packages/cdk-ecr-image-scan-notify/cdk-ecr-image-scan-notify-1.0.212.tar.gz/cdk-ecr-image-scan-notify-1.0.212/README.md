[![NPM version](https://badge.fury.io/js/cdk-ecr-image-scan-notify.svg)](https://badge.fury.io/js/cdk-ecr-image-scan-notify)
[![PyPI version](https://badge.fury.io/py/cdk-ecr-image-scan-notify.svg)](https://badge.fury.io/py/cdk-ecr-image-scan-notify)
![Release](https://github.com/hayao-k/cdk-ecr-image-scan-notify/workflows/release/badge.svg)

# cdk-ecr-image-scan-notify

cdk-ecr-image-scan-notify is an AWS CDK construct library that notify the slack channel of Amazon ECR image scan results.

## Overview

Amazon EventBridge (CloudWatch Events) detects the image scan execution and starts the Lambda function.
The Lambda function summarizes the scan results, formatting them and notifying Slack.

Basic scanning

![](https://raw.githubusercontent.com/hayao-k/cdk-ecr-image-scan-notify/main/images/basic-scanning.png)

Enhanced scanning (Support for initial scan only)

![](https://raw.githubusercontent.com/hayao-k/cdk-ecr-image-scan-notify/main/images/enhanced-scanning.png)

Click on an image name to go to the scan results page.

![](https://github.com/hayao-k/ecr-image-scan-findings-to-slack/raw/master/docs/images/scan-result.png)

## Getting Started

### TypeScript

Installation

```
$ yarn add cdk-ecr-image-scan-notify
```

Usage

```python
import * as cdk from 'aws-cdk-lib';
import { EcrImageScanNotify } from 'cdk-ecr-image-scan-notify';

const mockApp = new cdk.App();
const stack = new cdk.Stack(mockApp, '<your-stack-name>');

new EcrImageScanNotify(stack, 'ecr-image-scan-notify', {
  webhookUrl: '<your-incoming-webhook-url>',
});
```

Deploy!

```
$ cdk deploy
```

### Python

Installation

```
$ pip install cdk-ecr-image-scan-notify
```

Usage

```py
import aws_cdk as cdk
from cdk_ecr_image_scan_notify import EcrImageScanNotify

app = cdk.App()
stack = cdk.Stack(app, "<your-stack-name>", env={'region': 'ap-northeast-1'})

EcrImageScanNotify(stack, "EcrImageScanNotify",
    webhook_url = '<your-incoming-webhook-url>',
)
```

Deploy!

```
$ cdk deploy
```
