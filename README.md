# Installation and configuration requirements

## Installation

Create virtual environment:

```
# Install Python virtualenv software
pip3 install virtualenv

# Change to directory and create a virtual environment
cd CandleHoarder
virtualenv venv
source venv/bin/activate

# in windows:  source venv/Scripts/activate

# Install packages for CandleHoarder
pip install -r requirements.txt
```

## Configuration

## secret file

File 'secret.py' should be made to contain confidential information. The format should be:

```
API_KEY = ""
API_SECRET = ""

```

This file is not here by default but should be made manually.


## Misc

Read: 

* https://python-binance.readthedocs.io/en/latest/overview.html
* https://python-binance.readthedocs.io/en/latest/constants.html

For information about the python-binance library.


