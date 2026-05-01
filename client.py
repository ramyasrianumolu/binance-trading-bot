from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import API_KEY, API_SECRET, BASE_URL
from logger import setup_logger

logger = setup_logger()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(f"Placing order: {symbol}, {side}, {order_type}, {quantity}, {price}")

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price required for LIMIT order")
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(**params)

            logger.info(f"Order response: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e}")
            raise
        except Exception as e:
            logger.error(f"General error: {e}")
            raise