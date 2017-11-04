import hmac
import hashlib
import time
import json

try:
    from urllib import urlencode
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urlencode
    from urllib.parse import urljoin

import requests

PublKey = ('')

PrivKey = ('')

BASE_URL = 'https://tuxexchange.com/api?method={method}'

# Possible methods
PUBLIC_METHODS = [
    'getticker',
    'get24hvolume',
    'getorders',
    'gettradehistory',
    'getcoins']

AUTHENTICATED_METHODS = [
    'getmybalances',
    'withdraw',
    'getmyaddresses',
    'getmytradehistory',
    'buy',
    'sell',
    'getmyopenorders',
    'cancelorder']


def using_requests(request_url):
    return requests.get(
        request_url
    ).json()


class Tuxexchange(object):
    def __init__(self, calls_per_second=6, dispatch=using_requests):
        self.dispatch = dispatch
        self.call_rate = 1.0 / calls_per_second
        self.last_call = None

    def wait(self):
        if self.last_call is None:
            self.last_call = time.time()
        else:
            now = time.time()
            passed = now - self.last_call
            if passed < self.call_rate:
                # print('sleep')
                time.sleep(1.0 - passed)

            self.last_call = time.time()

    def api_query(self, method, options=None):
        '''
        Queries Tux Exchange with given method and options.
        :param method: Method to query
        :return      : JSON response from Tux Exchange
        :rtype       : dict
        '''
        if not options:
            options = {}
        nonce = str(int(time.time() * 1000))

        request_url = BASE_URL.format(method=method)

        request_url += urlencode(options)

        self.wait()

        return self.dispatch(request_url)

    def getBalances(self):
        query = {"method": "getmybalances"}

        encoded = urlencode(query)

        signature = hmac.new(PrivKey, encoded, hashlib.sha512).hexdigest()

        Tuxexchangeheader = {'Sign': signature, 'Key': PublKey}

        tuxgetbalance = requests.post(BASE_URL, data=query, headers=Tuxexchangeheader, timeout=15).json()

        return tuxgetbalance

    def getMyWithdrawHistory(self):
        query = {"method": "getmywithdrawhistory"}

        encoded = urlencode(query)

        signature = hmac.new(PrivKey, encoded, hashlib.sha512).hexdigest()

        TuxexchangeHeader = {'Sign': signature, 'Key': PublKey}

        tuxGetWithdrawHistory = requests.post(BASE_URL, data=query, headers=TuxexchangeHeader, timeout=15).json()

        return tuxGetWithdrawHistory
    
     def getMyDepositHistory(self):
        query = {"method": "getmydeposithistory"}
        
        encoded = urlencode(query)
        
        signature = hmac.new(PrivKey, encoded, hashlib.sha512).hexdigest()
        
        Tuxexchangeheader = {'Sign': signature, 'Key': PublKey}
        
        tuxgetDepositHistory = requests.post(BASE_URL, data=query, headers=Tuxexchangeheader, timeout=15).json()

        return tuxgetDepositHistory
    
     
