
budget_type = ["clothing", "entertainment", "food"]

# Budget App
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

# Push your code to GitHub, and submit the repo link.
ledger = []

class Budget:
  def __init__(self, category):
    self.category = category
   
    self.amount = 0

  def deposit_funds(self,amount,  category, description= 'credit'):
    ledger.append({"category": category, "amount": amount, "description": description })
    self.amount += amount 
    print(ledger)
    return 'transaction completed'

  def check_funds(self, amount):
     return True if amount <= self.amount else False
  
  def withdraw_funds(self, amount, description='debit'):

    if self.check_funds(amount, category):
      self.amount -= amount
      ledger.append({"category": category, "amount": -amount, "description": description })
      return 'transaction completed'
    else:
        return('insufficient fund')

  
  def transfer_balance(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False


def menu():
    try:

        user = int(input('\n=== ****What would you like to do?**** ===\nPress (1) To create a new budget\nPress (2) To deposit into a budget\nPress (3) To withdraw from a budget\nPress (4) To check your budget balance\nPress (5) To transfer money between budgets\nPress (6) To quit\n'))
    except:
        print('Invalid input')
        menu()

    if (user == 1):
        deposit()
    elif (user == 2):
        withdraw()
        pass
    elif (user == 3):
        # debit()
        pass
    elif (user == 4):
        # balance()
        pass
    elif (user == 5):
        # transfer()
        pass
    elif (user == 6):
        # out()
        pass
    else:
        print('Invalid input\n')
        menu()


#  Depositing funds to each of the categories
def deposit():
    try:
        print('********ADD BUDGET CATEGORY********')

        budget_name = str(input('Input your budget category \n'))
        if budget_name not in budget_type:
            print(f'budget but be either {budget_type}')
            menu()

        amount = int(input("Enter your budget amount \n$ "))
        print(type(amount))

        budget = Budget(budget_name)
        data = budget.deposit_funds(amount, budget_name, description='credit')
        print('ppp', data)
        print(f'{budget_name} budget is setup with {amount}')
        menu()
    except:
        print('Invalid input')
        menu()


def withdraw():
    try:
        print('*****Withdraw amount from wallet')
        print('Available budgets:')

        for budget in range(len(ledger)):
            print(f'{budget + 1}. {ledger[budget]["category"]}')
            num =+ 1

        selected_input =  int(input('Input (1) to continue your debit transaction, input 0 to stop transaction'))
        if selected_input == 1:
            user = input("Select a budget \n")
            if user in ledger:
                amount = int(input("Enter amount \n$"))
                Budget(category)
        
        amount = int(input("Enter your budget amount \n$"))
        data = Budget.withdraw_funds(amount)
        print(data)
        print(f'{amount}')
        menu()
    except:
        print('Invalid input')
        menu()


menu()
