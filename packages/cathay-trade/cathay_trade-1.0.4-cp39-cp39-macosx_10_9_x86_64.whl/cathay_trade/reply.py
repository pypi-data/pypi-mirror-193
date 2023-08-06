import clr ,os , time ,threading
dir = os.path.dirname(__file__)
csharp = os.path.join(dir, 'dll','CSTrader.dll')
clr.AddReference(csharp)
csharp = os.path.join(dir, 'dll','CSAPIComm.dll')
clr.AddReference(csharp)
from CSAPIComm import MESSAGE_TYPE


receiver = ''
receiver_rcv = ''
def OnTAPIStatus(sender, status, msg):
    global receiver
    match status:
        case MESSAGE_TYPE.MT_CONNECT_READY:
            print(f'CONNECT_READY-\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_CONNECT_FAIL:
            print(f'CONNECT_FAIL\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_DISCONNECTED:
            print(f'DISCONNECTED\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_SUBSCRIBE:
            print(f'訂閱:\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_UNSUBSCRIBE:
            print(f'解除訂閱!:\n{msg}\n')
            receiver = True 
        case MESSAGE_TYPE.MT_HEART_BEAT:
            print(f'HEART_BEAT:\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_LOGIN_OK:
            print(f'LOGIN_OK\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_EXTRA_LOGIN_TWOWAY_FAIL:
            print(f'EXTRA_LOGIN_TWOWAY_FAIL\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_LOGIN_TWOWAY_FAIL:
            print(f'LOGIN_TWOWAY_FAIL\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_LOGIN_FAIL:
            print(f'LOGIN_FAIL\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_ERROR:
            print(f'其他錯誤:\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_RETRIEVE_FUT_DONE:
            print(f'RETRIEVE_FUT_DONE\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_RETRIEVE_OPT_DONE:
            print(f'RETRIEVE_OPT_DONE\n{msg}\n')
            receiver = True
        case MESSAGE_TYPE.MT_RETRIEVE_STK_DONE:
            print(f'RETRIEVE_STK_DONE\n{msg}\n')
            receiver = True
        case _:
            print(f'other reply\n{msg}\n')
            receiver = True

def OnTAPIRcvData(sender, mb):
    global receiver_rcv,order_rcv
    match mb.dataType:
        case 103:
            print (f'公告查詢成功，數量 {mb.notices.Count}\n')
            for item in mb.notices:
                print(item.kind, item.notice_type, item.post_time, item.content)
            receiver_rcv = True
        case 114:
            print(f"收到主機公告, {mb.content}\n")
            receiver_rcv = True
        case 201:
            match int(mb.err_code):
                case 0:
                    print(f'{mb.user_def} 委託成功 {mb.toLog()}\n')
                    receiver_rcv = True
                case _:
                    print(f'{mb.user_def} 委託失敗, ErrCode={mb.err_code} ErrMsg= {mb.err_msg}\n')
                    receiver_rcv = True
        case 241:
            match int(mb.err_code):
                case 0:
                    print(f'{mb.user_def} 委託成功 {mb.toLog()}\n')
                    receiver_rcv = True
                case _:
                    print(f'{mb.user_def} 委託失敗, ErrCode={mb.err_code} ErrMsg= {mb.err_msg}\n')
                    receiver_rcv = True
        case 285:
            match int(mb.err_code):
                case 0:
                    print(f'{mb.user_def} 委託成功回補 {mb.toLog()}\n')
                    receiver_rcv = True
                case _:
                    print(f'{mb.user_def} 中菲委託回補失敗, ErrCode={mb.err_code} ErrMsg= {mb.err_msg}\n')
                    receiver_rcv = True
        case 202:
            print(f'{mb.user_def} 成交{mb.qty_cum}口 {mb.toLog()}\n')   
            receiver_rcv = True     
        case 208:
            print(f"Speedy複式 : {mb.User_def} 成交{mb.CumQty}口, Leg1Price={mb.DealPrice1}, Leg2Price={mb.DealPrice2}, {mb.toLog()}\n")
            receiver_rcv = True
        case 242:
            print(f"內期成交 : {mb.User_def} 成交{mb.CumQty}口, Leg1Price={mb.DealPrice1}, Leg2Price={mb.DealPrice2}, {mb.toLog()}\n")
            receiver_rcv = True
        case 212:
            print(f"內期成交回補 : {mb.User_def} 成交{mb.CumQty}口, Leg1Price={mb.DealPrice1}, Leg2Price={mb.DealPrice2}, {mb.toLog()}\n")
            receiver_rcv = True
        case 401:
            match int(mb.ErrorCode):
                case 0:
                    print(f"證券委託成功 {mb.toLog()}\n")
                    order_rcv = mb.OrderNo
                    receiver_rcv = True
                case _:
                    print(f"證券委託失敗, ErrCode={mb.ErrorCode} ErrMsg={mb.ErrorMsg}\n")
                    order_rcv = mb.toLog()
                    receiver_rcv = True
        case 402:
            print(f"{mb.UserDef} 成交{mb.DealQty} 股 {mb.toLog()}\n")
            receiver_rcv = True
        case 404:#確認何時回傳
            match int(mb.ErrorCode):
                case 0:
                    print(f"{mb.UserDef} [404]證券委託成功 {mb.toLog()}\n")
                    receiver_rcv = True
                case _:
                    print(f"{mb.UserDef} [404]證券委託失敗, ErrCode={mb.ErrorCode} ErrMsg={mb.ErrorMsg}\n")
                    receiver_rcv = True
        case 405:
            match int(mb.ErrorCode):
                case 0:
                    print(f"{mb.UserDef} [record]證券委託成功 {mb.toLog()}\n")
                    receiver_rcv = True
                case _:
                    print(f"{mb.UserDef} [record]證券委託失敗, ErrCode={mb.ErrorCode} ErrMsg={mb.ErrorMsg}\n")
                    receiver_rcv = True
        case 406:
            print(f"[record]證券成交回報回補:{mb.toLog()}\n")
            receiver_rcv = True
        case 413:
            print(f"對帳單查詢:{mb.toLog()}\n")
            receiver_rcv = True           
        case 415:
            print(f"整戶維持率查詢:{mb.toLog()}\n")
            receiver_rcv = True           
        case 417:
            print(f"證券庫存回報:{mb.toLog()}\n")
            receiver_rcv = True           
        case 419:
            print(f"證券全額交割股回覆:{mb.toLog()}\n")
            receiver_rcv = True           
        case 421:
            print(f"證券歷史淨收付回報:{mb.toLog()}\n")
            receiver_rcv = True           
        case 423:
            print(f"證券對帳單回報:{mb.toLog()}\n")
            receiver_rcv = True           
        case 425:
            print(f"證券已實現損益查詢:{mb.toLog()}\n")
            receiver_rcv = True           
        case 427:
            print(f"證券即時庫存明細損益試算回報:{mb.toLog()}\n")
            receiver_rcv = True           
        case 429:
            print(f"證券即時庫存彙總損益試算回報:{mb.toLog()}\n")
            receiver_rcv = True           
        case 431:
            print(f"證券自訂成本回覆:{mb.toLog()}\n")
            receiver_rcv = True           
        case 433:
            print(f"證券資券配額回覆:{mb.toLog()}\n")
            receiver_rcv = True           
        case 205:
            if len(mb.sub_acno.strip()) > 0:
                print(f"{mb.branch_id}-{mb.sub_acno} 委託回報回補 {mb.toLog()}\n")
                receiver_rcv = True
            else:
                print(f"{mb.branch_id}-{mb.acno} 委託回報回補 {mb.toLog()}\n")
                receiver_rcv = True           
        case 206:
            if len(mb.sub_acno.strip()) > 0:
                print(f"{mb.branch_id}-{mb.sub_acno} 成交回報回補 {mb.toLog()}\n")
                receiver_rcv = True
            else:
                print(f"{mb.branch_id}-{mb.acno} 成交回報回補 {mb.toLog()}\n")
                receiver_rcv = True           
        case 328:
            print(f"權益數查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 303:
            print(f"客戶部位明細查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 305:
            print(f"客戶平倉明細查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 308:
            print(f"客戶平倉彙總查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 310:
            print(f"客戶部位彙總查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 336:
            print(f"客戶拆解組合查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 312:#與303相同
            print(f"客戶部位明細查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 229:
            print(f"客戶平倉明細MB229查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 314:
            print(f"客戶平倉明細彙總查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 326:
            print(f"客戶歷史平倉明細查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 316:
            print(f"客戶部位彙總查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 320:
            print(f"VIP權益數查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 323:
            print(f"VIP權益數查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 322:
            print(f"VIP部位彙總查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 324:
            print(f"VIP部位彙總查詢成功:{mb.toLog()}\n")
            receiver_rcv = True           
        case 501:
            match int(mb.ErrorCode):
                case 0:
                    print(f"{mb.UserDef} 委託成功 {mb.toLog()}\n")
                    receiver_rcv = True
                case _:
                    print(f"{mb.UserDef} 委託失敗, ErrCode={mb.ErrCode} ErrMsg={mb.Msg}\n")
                    receiver_rcv = True     
        case 505:
            match int(mb.ErrorCode):
                case 0:
                    print(f"{mb.UserDef} 委託成功 {mb.toLog()}\n")
                    receiver_rcv = True
                case _:
                    print(f"{mb.UserDef} 委託失敗, ErrCode={mb.ErrCode} ErrMsg={mb.Msg}\n")
                    receiver_rcv = True     

        case 502:
            print(f"成交{mb.DealQty}口 {mb.toLog()}\n")
            receiver_rcv = True
        case 506:
            print(f"成交{mb.DealQty}口 {mb.toLog()}\n")
            receiver_rcv = True
        case 504:
            print(f"外期回補回報狀態通知:{mb.toLog()}\n")
            receiver_rcv = True
        case 511:
            print(f"外期權益數查詢成功(大量):{mb.toLog()}\n")
            receiver_rcv = True
        case 513:
            print(f"外期部位彙總查詢成功(大量):{mb.toLog()}\n")
            receiver_rcv = True
            
        case 515:
            print(f"外期部位明細查詢成功(大量):{mb.toLog()}\n")
            receiver_rcv = True
        case 517:
            print(f"外期平倉明細查詢成功(大量):{mb.toLog()}\n")
            receiver_rcv = True
        case 9000:
            print(f"Note for market status:{mb.toLog()}\n")
            receiver_rcv = True
        case 262:
            print(f"出入金帳戶查詢成功:{mb.toLog()}\n")
            receiver_rcv = True
        case 264:
            print(f"出金查詢成功:{mb.toLog()}\n")
            receiver_rcv = True
        case 266:
            print(f"歷史出入金查詢成功:{mb.toLog()}\n")
            receiver_rcv = True
        case 268:
            print(f"出金申請:{mb.toLog()}\n")
            receiver_rcv = True
        case 270:
            print(f"互轉申請:{mb.toLog()}\n")
            receiver_rcv = True
        case 272:
            print(f"國外出金查詢成功:{mb.toLog()}\n")
            receiver_rcv = True
        case 701:
            print(f"reply 701:{mb.toLog()}\n")
            receiver_rcv = True
        case 703:
            print(f"reply 703:{mb.toLog()}\n")
            receiver_rcv = True
        case 9000:
            print(f"Note for market status:{mb.toLog()}\n")
            receiver_rcv = True
        case _:
            print(f'other reply\n{mb.toLog()}\n')
            receiver_rcv = True

def return_order_rcv():
    global order_rcv
    return(order_rcv)

def receive_Status():
    global receiver
    start = time.time()
    receiver = False
    while True:
        end = time.time()
        if (end-start) > 15:
            receiver = True
            print('response Status failed')
            break
        if receiver == True:
            #time.sleep(0.5)
            break
    
def receive_RcvData():
    global receiver_rcv
    start = time.time()
    receiver_rcv = False
    while True:
        end = time.time()
        if (end-start) > 15:
            receiver_rcv = True
            print('response Rcv failed')
            break
        if receiver_rcv == True:
            #time.sleep(0.5)
            break
    

class thread:
    def __init__(self,func1,func2):
        self.func1 = func1
        self.func2 = func2
        self.thread_job()
    def thread_job(self):
        self.threads = []
        t = threading.Thread(target=self.func1)
        self.threads.append(t)
        t = threading.Thread(target=self.func2)
        self.threads.append(t)
    def thread_start(self): #開始線程
        global threads
        for th in self.threads:
            th.start()
        for th in self.threads:
            th.join() #等待結束