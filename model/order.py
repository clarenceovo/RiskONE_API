class order:
    def __init__(self,exchange,instType,instId,side,ordType,px,sz,clOrdId,ordId,category,fill_size,execType=None):
        self.exchange = exchange
        self.instType = instType
        self.instId = instId
        self.side = side
        self.ordType = ordType
        self.px = px
        self.sz = sz
        self.clOrdId = clOrdId
        self.ordId = ordId
        self.category = category
        self.fill_size = fill_size
        self.execType = execType

    def to_json(self):
        return {"exchange":self.exchange,"instType":self.instType,"instId":self.instId,"side":self.side,"ordType":self.ordType,"px":self.px,"sz":self.sz,"clOrdId":self.clOrdId,"ordId":self.ordId,"category":self.category,"fill_size":self.fill_size,"execType":self.execType}

class historical_order:
    def __init__(self,trade_id ,instrument_id , side , size, fill_time_utc,fill_price , fill_size ,fill_notional_usd , fee):
        self.trade_id = trade_id
        self.instrument_id = instrument_id
        self.side = side
        self.size = size
        self.fill_time_utc = fill_time_utc
        self.fill_price = fill_price
        self.fill_size = fill_size
        self.fill_notional_usd = fill_notional_usd
        self.fee = fee

    def to_json(self):
        return {"trade_id":self.trade_id,"instrument_id":self.instrument_id,"side":self.side,"size":self.size,"fill_time_utc":self.fill_time_utc,"fill_price":self.fill_price,"fill_size":self.fill_size,"fill_notional_usd":self.fill_notional_usd,"fee":self.fee}
http://16.162.240.195/