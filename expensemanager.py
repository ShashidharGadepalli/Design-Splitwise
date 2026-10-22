from expense import Expense
from collections import defaultdict
class ExpenseManager():

    def __init__(self):
        self._expenses = []
        self._balances = defaultdict( lambda: defaultdict(float))

    def _add_debt(self,creditor,debitor,amount):
        self._balances[creditor][debitor] = round(self._balances[creditor][debitor]+amount,2)
        self._balances[debitor][creditor] = round(self._balances[debitor][creditor]-amount,2)
   
    def add_expense(self,expense:Expense):
        self._expenses.append(expense)
        shares = expense.split()
        payer = expense.get_paidby()
        for user,share in shares.items():
            if user is not payer:
                self._add_debt(payer,user,share)

    def show_user_balances(self,user):
        for other,amount in self._balances.get(user,{}).items():
                if amount > 0:
                    print(f"{other.get_username()} owes {user.get_username()}: {amount}")
                elif amount < 0:
                    print(f"{user.get_username()} owes {other.get_username()}: {abs(amount)}")

