import clr , os , time
from dataclasses import dataclass,field
from cathay_trade.reply import *
dir = os.path.dirname(__file__)
csharp = os.path.join(dir, 'dll','CSTrader.dll')
clr.AddReference(csharp)
csharp = os.path.join(dir, 'dll','CSAPIComm.dll')
clr.AddReference(csharp)
from System import Int32,Decimal
from CSAPIComm import ORDER_RETURN_CODE,SIDE,STOCK_TRADE_SEGMENT
from CSAPIComm import STOCK_ORDER_TYPE,PRICEFLAG_STOCK,STOCK_ORDER_GROUP,ORDER_RETURN_CODE,TIME_IN_FORCE
from CSAPIComm import ORDER_RETURN_CODE
from cathay_trade.reply import return_order_rcv
from enum import Enum

class BS(Enum):
    Buy = SIDE.BUY
    """買"""
    Sell = SIDE.SELL
    """賣"""
    
class MarketFlag(Enum):#market
    TSE = STOCK_ORDER_GROUP.TSE
    """集中"""    
    OTC = STOCK_ORDER_GROUP.OTC
    """櫃買"""
    EMER = STOCK_ORDER_GROUP.EMER
    """興櫃"""
    
class PriceType(Enum):#pf
    Limit = PRICEFLAG_STOCK.LIMIT_PRICE
    """限價"""
    LimitUp = PRICEFLAG_STOCK.UP_LIMIT_PRICE
    """漲停"""
    LimitDown = PRICEFLAG_STOCK.DOWN_LIMIT_PRICE
    """跌停"""
    Market = PRICEFLAG_STOCK.MARKET_PRICE
    """市價"""
    Flag = PRICEFLAG_STOCK.REFERENCE_PRICE#待確認
    """平盤"""
    
class OrderType(Enum):#ts
    Common = STOCK_TRADE_SEGMENT.NORMAL
    """整股"""
    AfterMarket = STOCK_TRADE_SEGMENT.AFTER_MARKET
    """盤後"""
    IntradayOdd = STOCK_TRADE_SEGMENT.ODD_LOT#待確認
    """盤後零股"""
    Odd = STOCK_TRADE_SEGMENT.NormalOdd#待確認
    """盤中零股"""
    
class OrderMethod(Enum):#ot
    Cash = STOCK_ORDER_TYPE.NORMAL
    """普通"""
    Margin = STOCK_ORDER_TYPE.MARGIN_PURCHASE
    """融資"""
    Short = STOCK_ORDER_TYPE.SHORT_SALE#待確認
    """融券"""
    DayTradingSell = STOCK_ORDER_TYPE.OFFSET_SALE#待確認
    """現股當沖先賣"""
    
class OrderPeriod(Enum):#timeinfoce
    ROD = TIME_IN_FORCE.ROD
    IOC = TIME_IN_FORCE.IOC
    FOK = TIME_IN_FORCE.FOK


@dataclass
class Trade:   
    _trade:any = field(repr=False)
    func:any = field(repr=False)
    symbol:str   
    price:Decimal
    qty:Int32
    order_no:str 
    sequence_no:str  
    order_date:str 
    BS:any
    broker_id:str
    account_id:str
    price_type:any
    order_type:any
    order_method:any  
    order_period:any
    market_flag:any
    sub_acc:str
    sales_id:str  
    user_define:str
        
    def order_stock(self):    
        rc = self._trade.Order_Stock(self.func,self.market_flag.value,self.user_define,self.broker_id,
                                self.account_id,
                                self.sub_acc,self.symbol,self.sales_id,self.BS.value,self.price_type.value,Decimal(self.price),
                                self.order_type.value,Int32(self.qty),self.order_method.value,self.order_no,self.sequence_no,
                                self.order_date,self.order_period.value)
        #self.order_status(rc) 回傳時間過久約2秒
    def run(self):
        t = thread(receive_RcvData,self.order_stock)
        t.thread_start()
        try:
            order_no = return_order_rcv()
        except:
            order_no = None
        return self._trade,order_no
    def order_status(self,rc):
        match rc:
            case ORDER_RETURN_CODE.SUCCESS:
                print("委託傳送成功")
            case ORDER_RETURN_CODE.CERT_NOT_FOUND:
                print("憑證錯誤")
            case ORDER_RETURN_CODE.SIGN_OBJECT_ERROR:
                print("簽章元件錯誤")
            case ORDER_RETURN_CODE.ACCOUNT_NOT_FOUND_ERROR:
                print("無可下單帳號")
            case ORDER_RETURN_CODE.PRICE_ZERO_ERROR:
                print("限價單價格不得為0")
            case ORDER_RETURN_CODE.SYMBOL_LENGTH_ERROR:
                print("商品代碼長度錯誤")
            case ORDER_RETURN_CODE.ORDERNO_EMPTY_ERROR:
                print("刪改單，請輸入委託書號")
            case _:
                print("其他錯誤")


