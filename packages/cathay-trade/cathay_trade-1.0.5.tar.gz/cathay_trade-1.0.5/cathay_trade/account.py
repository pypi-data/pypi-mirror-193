from dataclasses import dataclass,field

@dataclass
class account_info:   
    _trade: any = field(repr=False)
    no : int = field(default=0)
    branch_code: str = field(init=False)
    account_id: str = field(init=False)
    account_type: str = field(init=False)
    day_trade: str = field(init=False)
    is_foreign: str = field(init=False)
    def __post_init__(self):
        acc = self._trade.AccountDetail(self.no)
        self.branch_code = acc.branch_code
        self.account_id = acc.account_id
        self.account_type = acc.account_type
        self.day_trade = acc.day_trade
        self.is_foreign = acc.is_foreign

