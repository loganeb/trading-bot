import requests

PRODUCT_URL = 'https://api.exchange.coinbase.com/products'

def get_all_coinbase_products(url):
    res = requests.get(url)
    return res.json()

def get_coinbase_product(base_url, product_id):
    url = base_url + f'/{product_id}'
    res = requests.get(url)
    return res.json()

def get_coinbase_product_price(base_url, product_id):
    url = base_url + f'/{product_id}/ticker'
    res = requests.get(url)
    return res.json()['price']

def get_coinbase_product_candles(base_url, product_id):
    url = base_url + f'/{product_id}/candles'
    res = requests.get(url)
    return res.json()

def coinbase_convert_to_dicts(candle_data):
    dicts = []
    for dp in candle_data:
        dict_dp = {
            'date': dp[0], 
            'low': dp[1], 
            'high': dp[2],
            'open': dp[3],
            'close': dp[4],
            'volume': dp[5]
            }
        dicts.append(dict_dp)
    return dicts