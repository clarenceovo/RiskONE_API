from exchange_api.binance_api_handler import binance_api_handler
from exchange_api.okx_api_handler import okx_api_handler
from .BaseHandler import BaseHandler
from model.order import order
class risk_api_handler(BaseHandler):

    def __init__(self,credential_config:dict):
        super().__init__("Risk_API")
        self.api_client ={}
        self.api_client['binance'] = binance_api_handler(credential_config)
        self.api_client['okx'] = okx_api_handler(credential_config)

    def get_future_position(self):
        """        okx_position = self.okx_client.get_future_position()
        binance_position = self.binance_client.get_future_position()
        data = {
            "okx":okx_position,
            "binance":binance_position
        }"""
        data = {}
        for exchange in self.api_client.keys():
            data[exchange]= self.api_client[exchange].get_future_position()
        return self.to_api_response(data)

    def get_future_position_by_exchange(self,exchange:str):
        data = {}
        if exchange in self.api_client.keys():
            data[exchange] = self.api_client[exchange].get_future_position()
        return self.to_api_response(data)

    def get_account_balance(self):
        data = {}
        for exchange in self.api_client.keys():
            data[exchange]= self.api_client[exchange].get_balance_usd()

        return self.to_api_response(data)

    def get_okx_live_orders(self):
        ret = []
        data = self.api_client['okx'].get_live_order()
        for item in data:
            obj = order("okx",item['instType'],item['instId'],item['side'],
                          item['ordType'],float(item['px']),float(item['sz']),item['ordType'],item['ordId']
                          ,item['category'],float(item['fillSz']))
            ret.append(obj.to_json())
        return self.to_api_response(ret)