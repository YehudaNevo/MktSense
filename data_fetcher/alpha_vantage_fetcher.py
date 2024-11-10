import requests
from data_fetcher.base_data_fetcher import BaseDataFetcher


class AlphaVantageFetcher(BaseDataFetcher):
    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_last_price(self, symbol: str):
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('Global Quote', {}).get('05. price', 'N/A')

    def fetch_stock_data(self, symbol: str, interval: str = "1min"):
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "apikey": self.api_key,
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
