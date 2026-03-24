from rich.console import Console
from rich.table import Table
import time
from api import get_crypto_data, get_forex

console = Console()

cryptos = ["bitcoin","ethereum","solana"]
forex_pairs = ["USD/EUR","GBP/USD"]

def run_terminal():

    while True:

        crypto = get_crypto_data(cryptos)

        forex = []
        for p in forex_pairs:
            result = get_forex(p)
            if result:
                forex.append(result)

        console.clear()

        table = Table(title="Crypto Market")

        table.add_column("Asset")
        table.add_column("Price")
        table.add_column("24h %")
        table.add_column("Market Cap")
        table.add_column("Volume")

        for c in crypto:
            table.add_row(
                c["name"],
                f"${c['price']}",
                f"{c['change']:.2f}%",
                str(c["market_cap"]),
                str(c["volume"])
            )

        console.print(table)

        table2 = Table(title="Forex Market")

        table2.add_column("Pair")
        table2.add_column("Rate")
        table2.add_column("Bid")
        table2.add_column("Ask")

        for f in forex:
            table2.add_row(
                f["pair"],
                str(f["rate"]),
                str(f["bid"]),
                str(f["ask"])
            )

        console.print(table2)

        time.sleep(5)