from splitstrategy import SplitStrategy

class ExactSplit(SplitStrategy):

    def __init__(self,splits:dict,amount:float):
        if round(sum(splits.values),2)!=amount:
            raise ValueError("Split amounts dont add")
        self._splits = splits

    def split(self, amount, users):
        return self._splits