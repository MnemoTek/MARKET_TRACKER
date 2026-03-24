import requests
import plotly.graph_objs as go

def crypto_chart(coin):

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": "1"
    }

    r = requests.get(url, params=params, timeout=10)

    if r.status_code != 200:
        return "<h3>Chart temporarily unavailable (API limit)</h3>"

    data = r.json()

    if "prices" not in data:
        return "<h3>Chart temporarily unavailable</h3>"

    prices = [p[1] for p in data["prices"]]
    times = list(range(len(prices)))

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=times,
            y=prices,
            mode="lines",
            name=coin
        )
    )

    fig.update_layout(title=f"{coin} 24h Price Chart")

    return fig.to_html(full_html=False)