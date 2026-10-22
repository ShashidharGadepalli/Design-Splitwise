from splitstrategy import SplitStrategy

class EqualSplit(SplitStrategy):

    def split(self, amount, users):
        num_users = len(users)
        amount_split = round(amount/num_users,2)

        result = {user:amount_split for user in users}

        totalSplit = amount_split * num_users

        rem = round(amount - totalSplit,2)

        lastUser = users[-1]

        result[lastUser] = round(result[lastUser]+rem,2)
        return result



