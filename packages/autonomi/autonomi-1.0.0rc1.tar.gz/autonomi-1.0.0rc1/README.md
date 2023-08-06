# Autonomi AI Python Client

<p align="center">
    <a href="https://pypi.org/project/autonomi/">
        <img alt="PyPi Version" src="https://badge.fury.io/py/autonomi.svg">
    </a>
    <a href="https://pypi.org/project/autonomi/">
        <img alt="PyPi Version" src="https://img.shields.io/pypi/pyversions/autonomi">
    </a>
    <a href="https://pypi.org/project/autonomi/">
        <img alt="PyPi Package Version" src="https://img.shields.io/pypi/v/autonomi">
    </a>
    <a href="https://pypi.org/project/autonomi/">
        <img alt="PyPi Downloads" src="https://img.shields.io/pypi/dm/autonomi">
    </a>
    <a href="https://betteruptime.com/?utm_source=status_badge">
        <img alt="Better Uptime" src="https://betteruptime.com/status-badges/v1/monitor/m27f.svg" height="20px">
    </a>
</p>


The Autonomi Cloud Python Client provides a convenient way to interact with the Autonomi Cloud API. We provide a unified client interface for various API services offered on the [Autonomi Cloud Platform](https://console.autonomi.ai/).

You can find more usage examples and tutorials in the [Autonomi Cloud Documentation](https://app.gitbook.com/o/jHSHyuhyMWNKfTelYovd/home).

## Installation

The Autonomi AI Python Client is available on PyPI. You can install it using pip:

```sh
pip install autonomi
```

Install from source:

```sh
git clone https://github.com/autonomi-ai/autonomi-client
cd autonomi-client
pip install -e .
```

## Authentication

The Autonomi AI Python Client uses API keys to authenticate requests. You can create your own API keys, after you've signed up, in the [Autonomi Cloud console](https://console.autonomi.ai/).

```bash
export AUTONOMI_API_KEY='...'
```

## Usage

The python client needs to be configured with your personal API key before you can use it. You can set the API key in the environment variable `AUTONOMI_API_KEY` as described above or pass it to the client constructor.

```python
from autonomi.client import AutonomiClient

# Usage with variable `AUTONOMI_API_KEY` read from your environment.
>>> cli = AutonomiClient()
AutonomiClient [version=X.Y.Z] :: [endpoint=https://api.autonomi.ai/v1, health=OK, auth=OK]

# Usage with API key passed to constructor
cli = AutonomiClient(api_key='...')
AutonomiClient [version=X.Y.Z] :: [endpoint=https://api.autonomi.ai/v1, health=OK, auth=OK]
```

## Requirements

 - Python 3.7+

 We currently support Python 3.7+ on Linux and macOS. If you have any questions or issues, please [open an issue](https://github.com/autonomi-ai/autonomi-client/issues).
