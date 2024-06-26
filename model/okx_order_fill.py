from dataclasses import dataclass
from util.util import millisecond_to_datetime
import json
@dataclass
class okx_order_fill:
    instType: str
    instId: str
    tgtCcy: str
    ccy: str
    ordId: str
    clOrdId: str
    algoClOrdId: str
    algoId: str
    tag: str
    px: str
    sz: str
    notionalUsd: str
    ordType: str
    side: str
    posSide: str
    tdMode: str
    accFillSz: str
    fillNotionalUsd: str
    avgPx: str
    state: str
    lever: str
    pnl: str
    feeCcy: str
    fee: str
    rebateCcy: str
    rebate: str
    category: str
    uTime: str
    cTime: str
    source: str
    reduceOnly: str
    cancelSource: str
    quickMgnType: str
    stpId: str
    stpMode: str
    attachAlgoClOrdId: str
    lastPx: str
    isTpLimit: str
    slTriggerPx: str
    slTriggerPxType: str
    tpOrdPx: str
    tpTriggerPx: str
    tpTriggerPxType: str
    slOrdPx: str
    fillPx: str
    tradeId: str
    fillSz: str
    fillTime: str
    fillPnl: str
    fillFee: str
    fillFeeCcy: str
    execType: str
    fillPxVol: str
    fillPxUsd: str
    fillMarkVol: str
    fillFwdPx: str
    fillMarkPx: str
    amendSource: str
    reqId: str
    amendResult: str
    code: str
    msg: str
    pxType: str
    pxUsd: str
    pxVol: str
    algoId: str
    linkedAlgoOrd:str
    attachAlgoOrds:str
    def __post_init__(self):
        try:
            self.fillTime = millisecond_to_datetime(int(self.fillTime))
            self.is_maker = True if self.execType == "M" else False
        except:
            self.is_maker = None
            pass
    def to_dict(self):
        return self.__dict__
        pass
    def to_tuple(self):
        return (self.instId,self.clOrdId,self.side,self.instType,self.sz,self.state,self.fillPx,self.fillSz,self.fillNotionalUsd,self.fillTime,self.accFillSz,
                self.is_maker,self.fee,self.feeCcy,self.rebate,self.rebateCcy,self.tag,self.ordId,"OKX")
