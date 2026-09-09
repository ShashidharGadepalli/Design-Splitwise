from PercentSplit import PercentSplit
from User import User
from Expense import Expense
from EqualSplit import EqualSplit
from ExactSplit import Exactsplit
from ExpenseManager import ExpenseManager

user1 = User("Shashi",235)
user2 = User("Chris",324)
user3 = User("Morris",908)

expense1 = Expense(900,[user1,user2,user3],EqualSplit())
result1 = expense1.split()

for user,amount in result1.items():
    print(f"{user.get_username()} owes {amount}")

user4= User("Usher",766)
expense2 = Expense(600,[user1,user2,user3,user4],EqualSplit())
result2 = expense2.split()

for user,amount in result2.items():
    print(f"{user.get_username()} owes: {amount}")

expense3 = Expense(1000,[user4,user3],Exactsplit({user4:600,user3:400},1000))
result3 = expense3.split()
for user,amount in result3.items():
    print(f"{user.get_username()} owes: {amount}")

user5 = User("Eeshan",890)
user6 = User("Messi",108)

expense4 = Expense(1000,[user5,user6,user3],PercentSplit({user5:50,user6:25,user3:25}))
result4 = expense4.split()

for user,amount in result4.items():
    print(f"{user.get_username()} owes: {amount}")


expenses = ExpenseManager()
expenses.add_expense(expense1)
expenses.add_expense(expense2)
expenses.add_expense(expense3)
expenses.add_expense(expense4)
total = expenses.get_user_expense()
for user,money in total.items():
    print(f"{user.get_username()} total owes: {money}")

