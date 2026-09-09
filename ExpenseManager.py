from Expense import Expense
from User import User

class ExpenseManager:
    def __init__(self):
        self._expenses = []

    def add_expense(self, expense: Expense):
        self._expenses.append(expense)

    def get_user_expense(self):
        total_owed = {}
        for expense in self._expenses:
            result = expense.split()
            for user,amount in result.items():
                total_owed[user] = total_owed.get(user,0)+amount
        return total_owed

        



