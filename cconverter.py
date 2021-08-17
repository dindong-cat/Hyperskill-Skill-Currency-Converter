import requests
import json
cache = []
owned_currency = input().lower()
target_currency = input().lower()
money_amount = int(input())
url = f"http://www.floatrates.com/daily/{owned_currency}.json".lower()
r = requests.get(url)


def initial_cache():
    if owned_currency == 'usd':
        cache.append(json.loads(r.text)['eur'])
    elif owned_currency == 'eur':
        cache.append(json.loads(r.text)['usd'])
    else:
        cache.append(json.loads(r.text)['usd'])
        cache.append(json.loads(r.text)['eur'])


def check_cache(x):
    print("Checking the cache...")
    for i in range(len(cache)):
        if cache[i]['code'] == x:
            print('Oh! It is in the cache!')
            return cache[i]['rate']
    else:
        print("Sorry, but it is not in the cache!")
        cache.append(json.loads(r.text)[f"{target_currency}"])
        for i in range(len(cache)):
            if cache[i]['code'] == x:
                return cache[i]['rate']


initial_cache()


while True:
    if target_currency != "":
        print(f"You received {round(money_amount * check_cache(target_currency.upper()), 2)} {target_currency.upper()}.")
        owned_currency = target_currency
        target_currency = input().lower()
        if target_currency == "":
            break
        else:
            money_amount = int(input())
    else:
        break
