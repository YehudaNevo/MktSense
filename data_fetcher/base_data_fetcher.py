from abc import ABC, abstractmethod


class BaseDataFetcher(ABC):

    @abstractmethod
    def fetch_stock_data(self, symbol: str, interval: str):
        pass

    @abstractmethod
    def fetch_last_price(self, symbol: str):
        pass
