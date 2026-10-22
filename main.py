from splitstrategy import SplitStrategy
from user import User
from equalsplit import EqualSplit
from exactsplit import ExactSplit
from expense import Expense
from percentsplit import PercentSplit
from expensemanager import ExpenseManager

user1 = User("Shashi",1234)
user2 = User("Ramesh",1235)
user3 = User("Suresh",1236)

expense1 = Expense(1800,user1, [user1,user2,user3],EqualSplit())
for user,amount in expense1.split().items():
    print(f"{user.get_username()} : {amount}")


expensemanager = ExpenseManager()
expensemanager.add_expense(expense1)
expensemanager.show_user_balances(user1)

expense2 = Expense(300, user2, [user2, user1], EqualSplit())
expensemanager.add_expense(expense2)
expensemanager.show_user_balances(user2)