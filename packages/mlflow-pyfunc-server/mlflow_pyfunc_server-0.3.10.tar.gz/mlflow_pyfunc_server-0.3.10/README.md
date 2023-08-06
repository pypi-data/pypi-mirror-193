# MLflow PyFunc Server

[![Python Package](https://github.com/VK/mlflow-pyfunc-server/actions/workflows/python-publish.yml/badge.svg)](https://github.com/VK/mlflow-pyfunc-server/actions/workflows/python-publish.yml)
[![PyPI](https://img.shields.io/pypi/v/mlflow-pyfunc-server?logo=pypi)](https://pypi.org/project/mlflow-pyfunc-server)

A simple server to publish several mlflow pyfunc models quickly in the private network.

Settings can be defined in a config file (./mlflow-pyfunc-server.cfg, ~/.mlflow-pyfunc-server.cfg) or at startup:
```
mlflow-pyfunc-server --host 0.0.0.0 -w 2 --mlflow https://mlflow:1234
```
![Screenshot](https://raw.githubusercontent.com/VK/mlflow-pyfunc-server/master/media/screenshot.png "Screenshot")

## Develop
```
$ py -m venv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```
