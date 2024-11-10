import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class BaseVisualizer:
    def __init__(self):
        plt.style.use('dark_background')  # Set a style for consistent plots

    def plot_price_per_day(self, data, symbol):
        dates = list(data.keys())
        prices = list(data.values())

        plt.figure(figsize=(12, 6))
        plt.plot(dates, prices, marker='o', linestyle='-', color='b', label='Price')
        plt.title(f"{symbol} - Price per Day")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_price_derivative(self, data, symbol):
        dates = list(data.keys())
        prices = list(data.values())
        prices = np.array(prices, dtype=float)
        derivatives = np.gradient(prices)

        plt.figure(figsize=(12, 6))
        plt.plot(dates, derivatives, marker='x', linestyle='-', color='r', label='Derivative')
        plt.title(f"{symbol} - Price Derivative per Day")
        plt.xlabel("Date")
        plt.ylabel("Price Change Rate")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_price_with_moving_average(self, data, symbol, window=30):
        dates = list(data.keys())
        prices = pd.Series(list(data.values()), index=dates, dtype=float)
        moving_avg = prices.rolling(window=window).mean()

        plt.figure(figsize=(12, 6))
        plt.plot(dates, prices, marker='o', linestyle='-', color='b', label='Price')
        plt.plot(dates, moving_avg, color='orange', label=f'{window}-Day Moving Average')
        plt.title(f"{symbol} - Price with {window}-Day Moving Average")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_all(self, data, symbol):
        self.plot_price_per_day(data, symbol)
        self.plot_price_derivative(data, symbol)
        self.plot_price_with_moving_average(data, symbol)
