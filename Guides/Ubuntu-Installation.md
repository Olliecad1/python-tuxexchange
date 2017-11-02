# Ubuntu Installation Guide

## Step 1

### Git clone the github page


![python](https://img.shields.io/badge/python-2.7-blue.svg)

```
sudo git clone https://github.com/Olliecad1/python-tuxexchange-Wrapper
```

## Step 2

### Change Directory into python-tuxexchange-Wrapper

```
cd python-tuxexchange-Wrapper
```

### Step 3

### Adding Tux Exchange Public and Private Key to tuxexchange.py file
```
sudo nano tuxexchange.py
```

### go down until you see PublKey = ('') PrivKey = ('') just to add your public and private keys in between the ''

## Step 4

### Building and Installing the setup file

```
sudo python setup.py build
sudo python setup.py install
```

## Step 5

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

## Get Balance api, Get Withdraw History and Addresses api, NEEDS PRIVATE AND PUBLIC KEY ACCESS

```python
from tuxexchange import Tuxexchange

tuxexchange = Tuxexchange()

print tuxexchange.getBalances()
print tuxexchange.getMyWithdrawHistory()
print tuxexchange.getMyAddresses()
```


## Testing

Run unit tests in [test.py](https://github.com/olliecad1/python-tuxexchange/blob/master/test.py)

