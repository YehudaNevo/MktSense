import os
from dotenv import load_dotenv
from data_fetcher.alpha_vantage_fetcher import AlphaVantageFetcher
from utils.db_storage import save_historical_prices



def main():
    load_dotenv()
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

    if not api_key:
        raise ValueError("API key not found. Please set it in the .env file.")

    fetcher = AlphaVantageFetcher(api_key=api_key)
    symbol = "TSLA"
    days = 360
    data = fetcher.fetch_historical_prices(symbol, days)
    save_historical_prices(data, symbol)


if __name__ == "__main__":
    main()
