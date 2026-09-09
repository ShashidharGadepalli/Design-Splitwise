from SplitStrategy import SplitStrategy

class Expense:

    def __init__(self, amount:float, users:list, splitStrategy: SplitStrategy):
        self._amount = amount
        self._users = users
        self._splitStrategy = splitStrategy

    def split(self):
        return self._splitStrategy.split(self._amount,self._users)




