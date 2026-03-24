import requests

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"


def get_crypto_data(coins):

    try:

        params = {
            "vs_currency": "usd",
            "ids": ",".join(coins),
            "order": "market_cap_desc",
            "sparkline": "false",
            "price_change_percentage": "24h"
        }

        r = requests.get(COINGECKO_URL, params=params, timeout=10)

        data = r.json()

        if not isinstance(data, list):
            return []

        results = []

        for c in data:

            results.append({
                "name": c.get("name", ""),
                "symbol": c.get("symbol", "").upper(),
                "price": c.get("current_price", 0),
                "change": c.get("price_change_percentage_24h", 0),
                "market_cap": c.get("market_cap", 0),
                "volume": c.get("total_volume", 0)
            })

        return results

    except Exception:
        return []


def get_forex(pair):

    try:

        base, target = pair.split("/")

        url = f"https://open.er-api.com/v6/latest/{base}"

        r = requests.get(url, timeout=10)

        data = r.json()

        if "rates" not in data:
            return None

        rate = data["rates"].get(target)

        if not rate:
            return None

        return {
            "pair": pair,
            "rate": rate,
            "bid": rate * 0.999,
            "ask": rate * 1.001
        }

    except Exception:
        return None