# python-tuxechange

# Developed By Sneurlax
# https://github.com/sneurlax

![python](https://img.shields.io/badge/python-2.7-blue.svg)

Inspired by [this](https://github.com/Olliecad1/Tux_Exchange_Python) wrapper written by [Olliecad1](https://github.com/Olliecad1) and following the example of [this](https://github.com/ericsomdahl/python-bittrex) wrapper written by [Eric Somdahl](https://github.com/ericsomdahl)

> I ([sneurlax](https://github.com/sneurlax)) am not affiliated with, nor paid by [Tux Exchange](https://tuxexchange.com).  Use at your own risk

## Step 1

### Git clone the github page

```
sudo git clone https://github.com/Olliecad1/python-tuxexchange
```

## Step 2

### Change Directory into python-tuxexchange

```
cd python-tuxexchange
```

## Step 3

### Building and Installing the setup file

```
sudo python setup.py build
sudo python setup.py install
```

## Step 4 

### If you are on a Linux Machine or Raspberry pi

```
sudo mv tuxexchange.py /usr/lib/python2.7/dist-packages/
```

## Usage

See available methods in the [Tux exchange API docs](https://tuxexchange.com/docs)

[test_manual.py](https://github.com/olliecad1/python-tuxexchange/blob/master/test_manual.py):
```python
from tuxexchange import Tuxexchange

tuxexchange = Tuxexchange()

print tuxexchange.api_query('getcoins')
{'PPC': {'website': 'www.peercoin.org', ...
print tuxexchange.api_query('getticker')
{'BTC_ICN': {'last': '0.00040418', ...
```

## Testing

Run unit tests in [test.py](https://github.com/olliecad1/python-tuxexchange/blob/master/test.py)

