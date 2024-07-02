from exchange_api.BaseApiHandler import BaseApiHander
from binance import Client
from model.position import position
class binance_api_handler(BaseApiHander):
    def __init__(self,credential_config:dict):
        super().__init__("binance",credential_config)
        self.client = Client(self.api_key, self.api_secret)

    def get_future_position(self, symbol=None)->list[position]:
        total_pos = []
        pos = self.client.futures_account()['positions']
        for future in pos:
            if float(future['positionAmt']) !=0:
                total_pos.append(position("binance",future['symbol'],float(future['positionAmt']),
                                          float(future['entryPrice']),0
                                          ,float(future['unrealizedProfit']),0).json())
        return total_pos


    def get_balance_usd(self):
        balance = self.client.futures_account_balance()
        ret = self.client.futures_account()
        return ret['totalWalletBalance']