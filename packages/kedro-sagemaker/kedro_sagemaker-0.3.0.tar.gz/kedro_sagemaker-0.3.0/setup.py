# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kedro_sagemaker']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=2.2.1,<3.0.0',
 'cloudpickle>=2.2.0,<3.0.0',
 'kedro>=0.18.3,<0.19',
 'pydantic>=1.10.2,<2.0.0',
 's3fs>=2022.11.0,<2023.0.0',
 'sagemaker>=2.117.0,<3.0.0',
 'tarsafe==0.0.4',
 'zstandard>=0.19.0,<0.20.0']

entry_points = \
{'kedro.project_commands': ['sagemaker = kedro_sagemaker.cli:commands']}

setup_kwargs = {
    'name': 'kedro-sagemaker',
    'version': '0.3.0',
    'description': 'Kedro plugin with AWS SageMaker Pipelines support',
    'long_description': '# Kedro SageMaker Pipelines plugin\n\n[![Python Version](https://img.shields.io/pypi/pyversions/kedro-sagemaker)](https://github.com/getindata/kedro-sagemaker)\n[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n[![SemVer](https://img.shields.io/badge/semver-2.0.0-green)](https://semver.org/)\n[![PyPI version](https://badge.fury.io/py/kedro-sagemaker.svg)](https://pypi.org/project/kedro-sagemaker/)\n[![Downloads](https://pepy.tech/badge/kedro-sagemaker)](https://pepy.tech/project/kedro-sagemaker)\n\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=getindata_kedro-sagemaker&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=getindata_kedro-sagemaker)\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=getindata_kedro-sagemaker&metric=coverage)](https://sonarcloud.io/summary/new_code?id=getindata_kedro-sagemaker)\n[![Documentation Status](https://readthedocs.org/projects/kedro-sagemaker/badge/?version=latest)](https://kedro-sagemaker.readthedocs.io/en/latest/?badge=latest)\n\n<p align="center">\n  <a href="https://getindata.com/solutions/ml-platform-machine-learning-reliable-explainable-feature-engineering"><img height="150" src="https://getindata.com/img/logo.svg"></a>\n  <h3 align="center">We help companies turn their data into assets</h3>\n</p>\n\n## About\nThis plugin enables you to run Kedro projects on Amazon SageMaker. Simply install the package and use the provided `kedro sagemaker` commands to build, push, and run your project on SageMaker.\n\n<img src="./docs/images/sagemaker_running_pipeline.gif" alt="Kedro SageMaker plugin" title="Kedro SageMaker plugin" />\n\n\n## Documentation \n\nFor detailed documentation refer to https://kedro-sagemaker.readthedocs.io/\n\n## Usage guide\n\n```\nUsage: kedro sagemaker [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -e, --env TEXT  Environment to use.\n  -h, --help      Show this message and exit.\n\nCommands:\n  compile  Compiles the pipeline to a JSON file\n  init     Creates basic configuration for Kedro SageMaker plugin\n  run      Runs the pipeline on SageMaker Pipelines\n```\n\n## Quickstart\nFollow **quickstart** section on [kedro-sagemaker.readthedocs.io](https://kedro-sagemaker.readthedocs.io/) to see how to run your Kedro project on AWS SageMaker or watch the video below:\n\n<a href="https://www.youtube.com/watch?v=yXIdz4kNMc8">\n    <img src="./docs/images/kedro-sagemaker-video-tutorial.jpg" alt="Kedro SageMaker video tutorial" title="Kedro SageMaker video tutorial" />\n</a>\n',
    'author': 'Marcin Zabłocki',
    'author_email': 'marcin.zablocki@getindata.com',
    'maintainer': 'GetInData MLOPS',
    'maintainer_email': 'mlops@getindata.com',
    'url': 'https://github.com/getindata/kedro-sagemaker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
