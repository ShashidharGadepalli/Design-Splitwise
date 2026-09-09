from SplitStrategy import SplitStrategy

class EqualSplit(SplitStrategy):

    def split(self, amount:float, users:list):
        
        num_users = len(users)
        amount_split = round(amount/num_users,2)
        result = { user: amount_split for user in users}

        total_amount = amount_split*num_users
        remainder = round(amount - total_amount,2)

        last_user = users[-1]
        result[last_user] = round(result[last_user]+remainder,2)

        return result
