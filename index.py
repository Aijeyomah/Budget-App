# Budget App
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

# Push your code to GitHub, and submit the repo link.

class Budget:
  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.amount = 0

  def deposit_funds(self,amount, description= 'credit'):
    self.ledger.append({"amount": amount, "description": description })
    self.amount += amount 
    print(self.ledger)
    return 'transaction completed'

  def check_funds(self, amount):
     return True if amount <= self.amount else False
  
  def withdraw_funds(self, amount, description='debit'):
    print('*****Withdraw amount from wallet')
    print('Available budgets:')

    for budget in self.ledger:
      print(budget.category)

    if self.check_funds(amount):
      self.amount -= amount
      self.ledger.append({"amount": -amount, "description": description })

  
  def transfer_balance(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False




