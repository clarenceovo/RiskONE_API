
class balance:
    def __init__(self, asset:str, balance:float):
        self.asset = asset
        self.balance = balance
        self.usd_notional = 0

class asset_balance:
    def __init__(self, instrument, balance):
        self.instrument = instrument
        self.balance = balance


class account_balance:
    def __init__(self, exchange:str):
        self.exchange = exchange
        self.balances = {}

    def update_balance(self,asset:str,balance:float,usd_notional:float=0):
        if asset in self.balances:
            self.balances[asset].balance = balance
        else:
            self.balances[asset] = balance(asset,balance,usd_notional)