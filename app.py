from flask import Flask, render_template
from api import get_crypto_data, get_forex
from charts import crypto_chart

app = Flask(__name__)

cryptos = ["bitcoin","ethereum","solana"]
forex_pairs = ["USD/EUR","GBP/USD"]

@app.route("/")
def dashboard():

    crypto = get_crypto_data(cryptos)

    forex = []
    for p in forex_pairs:
        f = get_forex(p)
        if f:
            forex.append(f)

    chart = crypto_chart("bitcoin")

    return render_template(
        "dashboard.html",
        crypto=crypto,
        forex=forex,
        chart=chart
    )


if __name__ == "__main__":
    app.run(debug=True)