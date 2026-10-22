class User:
    
    def __init__(self,userName:str,userId:int):
        self._userName = userName
        self._userId = userId

    def get_username(self):
        return self._userName

    def get_userId(self):
        return self._userId
