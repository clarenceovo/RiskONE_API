from exchange_api.BaseApiHandler import BaseApiHander
import okx.Account as Account
import okx.Trade as TradeAPI
from model.position import position
class okx_api_handler(BaseApiHander):
    def __init__(self,credential_config:dict):
        super().__init__("okx",credential_config)
        self.client = Account.AccountAPI(debug=False, flag="0", api_key=self.api_key,
                                         api_secret_key=self.api_secret, passphrase=self.api_passphrase)
        self.trade_client = TradeAPI.TradeAPI(debug=False, flag="0", api_key=self.api_key,
                                         api_secret_key=self.api_secret, passphrase=self.api_passphrase)
    def get_future_position(self, symbol=None)->list[position]:
        try:
            total_pos = []
            pos = self.client.get_positions()['data']
            for future in pos:
                if len(future['liqPx'])>0:
                    liquidation_price = float(future['liqPx'])
                else:
                    liquidation_price = None
                total_pos.append(position("okx",future['instId'],float(future['pos']),
                                          float(future['avgPx']),float(future['markPx'])
                                          ,float(future['upl']),float(future['realizedPnl']),liquidation_price=liquidation_price).json())

            return total_pos
        except Exception as e:
            print(e)
            return []
    def get_balance_usd(self):
        data = {}
        try:
            balance = self.client.get_account_balance()['data'][0]['adjEq']
            balance = float(balance)
            return balance
        except Exception as e:
            print(e)
            return data

    def get_live_order(self):
        try:
            orders = self.trade_client.get_order_list()['data']
            return orders
        except Exception as e:
            print(e)
            return []