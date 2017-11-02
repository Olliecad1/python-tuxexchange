# python-tuxexchange

# Developed By Sneurlax
# https://github.com/sneurlax
# https://pypi.python.org/pypi/python-tuxexchange/0.0.1

![python](https://img.shields.io/badge/python-2.7-blue.svg)

# [Guides For Installation](https://github.com/Olliecad1/python-tuxexchange-Wrapper/tree/master/Guides)



## [PyPi Link](https://pypi.python.org/pypi/python-tuxexchange-Wrapper)


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

## Get Balance api, NEEDS PRIVATE AND PUBLIC KEY ACCESS

```python
from tuxexchange import Tuxexchange

tuxexchange = Tuxexchange()

print tuxexchange.getBalances()
```


## Testing

Run unit tests in [test.py](https://github.com/olliecad1/python-tuxexchange/blob/master/test.py)

