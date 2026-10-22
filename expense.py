from splitstrategy import SplitStrategy
from user import User

class Expense:
    def __init__(self,amount:float, paid_by:User, users:list, splitStrategy:SplitStrategy):
        self._amount = amount
        self._users = users
        self._paidby = paid_by
        self._splitStrategy = splitStrategy

    def get_paidby(self):
        return self._paidby
    
    def split(self):
        return self._splitStrategy.split(self._amount,self._users)
    