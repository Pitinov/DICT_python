import json
import os
from datetime import datetime
import requests

API_URL = 'http://www.floatrates.com/daily/{0}.json'
CACHE_FILE_NAME = "cache.json"


def cache_currency_value(func):
    """Cache function for currency value"""
    cache = {}

    def update_cache():
        """Update cache in file"""
        with open(CACHE_FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(cache, file)

    def expire_cache():
        """Expire cache values"""
        for currency, value in list(cache.items()):
            for target_currency in list(value.keys()):
                cur_time = cache[currency][target_currency]["time"]
                if abs(datetime.now().timestamp() - cur_time) > 600:
                    cache[currency].pop(target_currency)
        update_cache()

    if os.path.exists(CACHE_FILE_NAME):
        with open(CACHE_FILE_NAME, "r", encoding="utf-8") as file:
            cache = json.load(file)
    expire_cache()

    def wrapper(currency: str, target_currency: str):
        """Wrapper function"""
        expire_cache()
        print("Checking the cache...")
        cur_vals = cache.get(currency, {})
        if cur_vals.get(target_currency) is None:
            print("Sorry, but it is not in the cache or expired")
            value = func(currency, target_currency)
            cur_vals[target_currency] = {
                "rate": value, "time": datetime.now().timestamp()}
            cache[currency] = cur_vals
            update_cache()
        else:
            print("It`s in the cache!")
        return cache[currency][target_currency]["rate"]

    return wrapper


@cache_currency_value
def get_currency_value(currency: str, target_currency: str) -> float:
    """Function for finding currency"""
    response = requests.get(API_URL.format(currency), timeout=5)
    rate = 0
    if response.status_code == 200:
        data = response.json()
        if target_currency in data:
            rate = data[target_currency]['rate']
        else:
            return -1

    elif response.status_code in (404, 403):
        raise ValueError("Sorry, but your target currency is not found")
    else:
        raise ValueError("Sorry, but something went wrong")
    return rate


def currency_finder(currency: str):
    """Function for finding currency"""

    target_currency = input("Enter target currency: ").strip().lower()

    rate = get_currency_value(currency, target_currency)
    if rate == -1:
        print("Sorry, but your target currency is not found")
        return

    user_money = input(f"Enter amount of your money ({currency}): ")
    target_money = float(user_money) * rate
    print(f"You will get {target_money} {target_currency}")


def main():
    """Main function"""
    print("Welcome to the currency exchange! press Ctrl+C to exit")
    try:
        currency = input("Enter your currency: ").strip().lower()
        while True:
            try:
                currency_finder(currency)
            except ValueError as error:
                print(error)
                break
    except KeyboardInterrupt:
        print("\nGoodbye!")
if __name__ == "__main__":
    main()