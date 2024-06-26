from abc import abstractclassmethod
from abc import ABC
# Base class for all exchange api handlers
class BaseApiHander(ABC):
    def __init__(self, exchange_name,credential_config:dict):
        self.exchange = exchange_name
        if self.exchange not in credential_config.keys():
            raise ValueError("exchange name not found in credential_config")
        self.api_key = credential_config[self.exchange]['api_key']
        self.api_secret = credential_config[self.exchange]['api_secret']
        if 'api_passphrase' in credential_config[self.exchange].keys():
            self.api_passphrase = credential_config[self.exchange]['api_passphrase']

    def get_balance(self):
        raise NotImplementedError("get_balance not implemented")

    def get_trades(self, symbol=None):
        raise NotImplementedError("get_trades not implemented")

    def get_future_position(self, symbol=None):
        raise NotImplementedError("get_position not implemented")

    def get_open_orders(self, symbol):
        raise NotImplementedError("get_open_orders not implemented")

    def get_closed_orders(self, symbol):
        raise NotImplementedError("get_closed_orders not implemented")

    def get_order_status(self, order_id, symbol):
        raise NotImplementedError("get_order_status not implemented")
