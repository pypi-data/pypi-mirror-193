import clr ,os , time
dir = os.path.dirname(__file__)
csharp = os.path.join(dir, 'dll','CSTrader.dll')
clr.AddReference(csharp)
csharp = os.path.join(dir, 'dll','CSAPIComm.dll')
clr.AddReference(csharp)
from CSTrader import TradeAPI
from cathay_trade.reply import *

class connect:
    def __init__(self,domain,port):
        self.domain = domain
        self.port = port
        
    def set_connect(self):
        self._trade = TradeAPI(self.domain, self.port, "API")
        self._trade.OnTradeAPIStatus += OnTAPIStatus 
        self._trade.OnTradeAPIRcvData += OnTAPIRcvData
        self._trade.Connect()
        self._trade.AutoRetrieveProductInfo = False
        self._trade.AutoSubReport = True
        self._trade.AutoRecoverReport = True
        
        
    def run(self):
        t = thread(receive_Status,self.set_connect)
        t.thread_start()
        return self._trade

class login_trade:
    def __init__(self,_trade,userid,password,sub_acc):
        self._trade = _trade
        self.userid = userid
        self.password = password
        
    def set_login(self):
        time.sleep(7)
        self._trade.LoginTrade(self.userid, self.password,"")
        
    def run(self):
        t = thread(receive_RcvData,self.set_login)
        t.thread_start()