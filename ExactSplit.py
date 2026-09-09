from SplitStrategy import SplitStrategy

class Exactsplit(SplitStrategy):

    def __init__(self,splits:dict,amount:float):
        if sum(splits.values())!=amount:
            raise ValueError("Split amounts do not add upto totalamount")
        self._splits = splits
    
    def split(self,amount:float,users:list):
        return self._splits


    