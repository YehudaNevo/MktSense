import os
from dotenv import load_dotenv
from utils.db_storage import fetch_historical_prices_from_db
from scripts.visualData.base_visualizer import BaseVisualizer


def main():
    load_dotenv()
    visualizer = BaseVisualizer()

    symbols = ["TSLA", "PLTR", "MSFT", "LMND"]

    for symbol in symbols:
        data = fetch_historical_prices_from_db(symbol)
        if data:
            print(f"Visualizing data for {symbol}")
            visualizer.plot_all(data, symbol)
        else:
            print(f"No data available for {symbol}")


if __name__ == "__main__":
    main()
