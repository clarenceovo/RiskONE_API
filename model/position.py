from util.util import timestamp_now

class position:
    def __init__(self,exchange,instrument , quantity, avg_price, mark_price, unrealized_pnl, realized_pnl,liquidation_price=None,funding_fee=None):
        self.last_update_time = timestamp_now()
        self.exchange = exchange
        self.instrument = instrument
        self.quantity = quantity
        self.mark_price= mark_price
        self.avg_price = avg_price
        self.unrealized_pnl = unrealized_pnl
        self.realized_pnl = realized_pnl
        self.liquidation_price = liquidation_price
        self.funding_fee = funding_fee

    def update_position(self,quantity,avg_price,mark_price,unrealized_pnl,realized_pnl):
        self.quantity = quantity
        self.avg_price = avg_price
        self.mark_price = mark_price
        self.unrealized_pnl = unrealized_pnl
        self.realized_pnl = realized_pnl


    def json(self):
        return {
            "exchange":self.exchange,
            "instrument":self.instrument,
            "quantity":self.quantity,
            "avg_price":self.avg_price,
            "mark_price":self.mark_price,
            "unrealized_pnl":self.unrealized_pnl,
            "realized_pnl":self.realized_pnl,
            "total_pnl":self.unrealized_pnl+self.realized_pnl,
            "liquidation_price":self.liquidation_price
        }
