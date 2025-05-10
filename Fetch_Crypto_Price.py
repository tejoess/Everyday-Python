import requests
import time
url ='https://api.coingecko.com/api/v3/simple/price'
def get_crypto_price(crypto_id):
    params = {
        'ids': crypto_id,
        'vs_currencies':'usd'
    }
    try:
        response = requests.get(url,params=params)
        response.raise_for_status()
        data =response.json()
        price = data[crypto_id]['usd']
        return price
    except Exception as e:
        print('Error',e)
        return None
    
cryptoname=input('Enter name of Crypto: ').lower()

while True:
    price = get_crypto_price(cryptoname)
    if price:
        print(f'{cryptoname.capitalize()} price: ${price}')
        
    else:
        print('Failed to fetch price.')
        
    time.sleep(7)

