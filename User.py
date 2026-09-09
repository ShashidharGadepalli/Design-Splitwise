class User:
    
    def __init__(self, username:str, userId: int):
        self._username = username
        self._userId = userId

    def get_username(self):
        return self._username

    def get_userId(self):
        return self._userId


