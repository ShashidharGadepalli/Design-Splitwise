from SplitStrategy import SplitStrategy

class PercentSplit(SplitStrategy):

    def __init__(self,percents:dict):

        if sum(percents.values())!=100:
            raise ValueError("Percents dont add upto 100")
        self._percents = percents

    def split(self,amount:float,users:list):
        result = {}
        for user,percent in self._percents.items():
            result[user] = round(amount*percent*0.01,2)
        return result




