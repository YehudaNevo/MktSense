import os
from dotenv import load_dotenv
from data_fetcher.alpha_vantage_fetcher import AlphaVantageFetcher


def main():
    load_dotenv()
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

    if not api_key:
        raise ValueError("API key not found. Please set it in the .env file.")

    fetcher = AlphaVantageFetcher(api_key=api_key)
    symbols = ['TSLA', 'PLTR', 'MSFT', 'LMND']
    for symbol in symbols:
        price = fetcher.fetch_last_price(symbol)
        print(f"Latest available price for {symbol}: ${price}")


if __name__ == "__main__":
    main()
