from splitstrategy import SplitStrategy

class PercentSplit(SplitStrategy):

    def __init__ (self,splits:dict):
        if sum(splits.values())!=100:
            raise ValueError("Sum not equal to 100")

        self._splits = splits

    def split(self,amount,users):
        result = {}
        for user,percent in self._splits.items():
            result[user] = round(amount*percent*0.01,2)
        return result

