# python-tuxexchange

# Developed By Sneurlax
# https://github.com/sneurlax
# [Original PyPi](https://pypi.python.org/pypi/python-tuxexchange/0.0.1)

![python](https://img.shields.io/badge/python-2.7-blue.svg)

# [Guides For Installation](https://github.com/Olliecad1/python-tuxexchange-Wrapper/tree/master/Guides)



## [PyPi Link](https://pypi.python.org/pypi/python-tuxexchange-Wrapper)

```
$ sudo apt-get install python-requests
```

## Use  
```$ sudo pip install requests ``` 
## If you have pip installed


##  On OSX you can also use 
```sudo easy_install -U requests ```
## if you have easy_install installed.

## Windows
This might help: http://stackoverflow.com/questions/17309288/importerror-no-module-named-requests
## Dependencies
- https://pypi.python.org/pypi/requests



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
print tuxexchange.getMyWithdrawHistory()
print tuxexchange.getMyAddresses()
```


## Testing

Run unit tests in [test.py](https://github.com/olliecad1/python-tuxexchange/blob/master/test.py)

