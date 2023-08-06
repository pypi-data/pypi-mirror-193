from cathay_trade.login import connect
from cathay_trade.login import login_trade
import datetime,clr
from System import Int32,Decimal
from CSAPIComm import ORDER_RETURN_CODE,FUNCTION_STOCK,MARKET,SIDE,STOCK_TRADE_SEGMENT
from CSAPIComm import STOCK_ORDER_TYPE,PRICEFLAG_STOCK,STOCK_ORDER_GROUP,ORDER_RETURN_CODE,TIME_IN_FORCE
from cathay_trade.order import Trade
from cathay_trade.account import account_info
from cathay_trade.order import *

class SDK:
    def __init__(self, domain, port):
        self.domain = domain
        self.port = port
        self.connect()
    def connect(self):
        self._trade = connect(self.domain,self.port).run()
    def log_in(self, userid, password):
        login_trade(self._trade,userid, password,"").run()
        self.accs = self.list_accounts()
    def account(self,n=0):
        try:
            return self.accs[n]
        except:
            print("ErrMsg: account not found")
    def list_accounts(self):
        accounts = []
        for no in range(self._trade.AccountCount()):  
            acc = account_info(self._trade,no)
            if acc.account_type == 'S':
                    accounts.append(acc)
        return accounts
    
    def getindustGroups(self):
        all_industGroups = self._trade.GetIndustryGroups()
        print(all_industGroups)
        
    def place_order(self,BS,price_type,symbol,price,qty,
                    account,user_define='',
                    order_date='',
                    order_type = OrderType.Common,
                    order_method=OrderMethod.Cash,
                    order_period=OrderPeriod.ROD,
                    func = FUNCTION_STOCK.NEW,
                    market_flag = MarketFlag.TSE,
                    sub_acc='',sales_id='',
                    order_no='',sequence_no=''):
        order_date=datetime.datetime.today().strftime('%Y%m%d')
        broker_id = account.branch_code
        account_id = account.account_id
        trade = Trade(_trade=self._trade,func=func,market_flag=market_flag,user_define=user_define,
                      broker_id=broker_id,account_id=account_id,sub_acc=sub_acc,symbol=symbol,
                      sales_id=sales_id,BS=BS,price_type=price_type,price=price,
                      order_type=order_type,qty=qty,order_method=order_method,order_no=order_no,
                      sequence_no=sequence_no,order_date=order_date,order_period=order_period)
        self._trade,order_no = trade.run() 
        trade.order_no = order_no
        trade.sequence_no = order_no
        if order_no != '':
            return trade
        else:
            return ''
    def update_price(self,account,trade,price):
        func = FUNCTION_STOCK.CH_Price
        broker_id = account.branch_code
        account_id = account.account_id
        market_flag = trade.market_flag
        user_define = trade.user_define
        sub_acc = trade.sub_acc
        symbol = trade.symbol
        sales_id = trade.sales_id
        BS = trade.BS
        price_type = trade.price_type
        order_type = trade.order_type
        qty = trade.qty
        order_method = trade.order_method
        order_no = trade.order_no
        sequence_no = trade.order_no
        order_date = trade.order_date
        order_period = trade.order_period

        trade = Trade(_trade=self._trade,func=func,market_flag=market_flag,user_define=user_define,
                      broker_id=broker_id,account_id=account_id,sub_acc=sub_acc,symbol=symbol,
                      sales_id=sales_id,BS=BS,price_type=price_type,price=price,
                      order_type=order_type,qty=qty,order_method=order_method,order_no=order_no,
                      sequence_no=sequence_no,order_date=order_date,order_period=order_period)
        trade.run() 
        return trade    
    
    def update_qty(self,account,trade,qty):
        func = FUNCTION_STOCK.CH_QTY
        broker_id = account.branch_code
        account_id = account.account_id
        market_flag = trade.market_flag
        user_define = trade.user_define
        sub_acc = trade.sub_acc
        symbol = trade.symbol
        sales_id = trade.sales_id
        BS = trade.BS
        price_type = trade.price_type
        order_type = trade.order_type
        price = trade.price
        order_method = trade.order_method
        order_no = trade.order_no
        sequence_no = trade.order_no
        order_date = trade.order_date
        order_period = trade.order_period

        trade = Trade(_trade=self._trade,func=func,market_flag=market_flag,user_define=user_define,
                      broker_id=broker_id,account_id=account_id,sub_acc=sub_acc,symbol=symbol,
                      sales_id=sales_id,BS=BS,price_type=price_type,price=price,
                      order_type=order_type,qty=qty,order_method=order_method,order_no=order_no,
                      sequence_no=sequence_no,order_date=order_date,order_period=order_period)
        trade.run() 
        return trade    
    def cancel_order(self,account,trade):
        func = FUNCTION_STOCK.CANCEL
        broker_id = account.branch_code
        account_id = account.account_id
        market_flag = trade.market_flag
        user_define = trade.user_define
        sub_acc = trade.sub_acc
        symbol = trade.symbol
        sales_id = trade.sales_id
        BS = trade.BS
        price_type = trade.price_type
        order_type = trade.order_type
        price = trade.price
        qty = trade.qty
        order_method = trade.order_method
        order_no = trade.order_no
        sequence_no = trade.order_no
        order_date = trade.order_date
        order_period = trade.order_period

        trade = Trade(_trade=self._trade,func=func,market_flag=market_flag,user_define=user_define,
                      broker_id=broker_id,account_id=account_id,sub_acc=sub_acc,symbol=symbol,
                      sales_id=sales_id,BS=BS,price_type=price_type,price=price,
                      order_type=order_type,qty=qty,order_method=order_method,order_no=order_no,
                      sequence_no=sequence_no,order_date=order_date,order_period=order_period)
        trade.run() 
        return trade    
            
    def disconnect(self):
        self._trade.Disconnect()