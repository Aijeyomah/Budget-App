from budget import Budget


# instantiate the class
budget = Budget('food')
clothing_budget = Budget('clothing')

budget.deposit_funds(110, "deposit to food category")
clothing_budget.deposit_funds(110)
clothing_budget.withdraw_funds(10)
print(budget.amount)
print(clothing_budget.amount)

