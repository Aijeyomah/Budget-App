class Budget:
    def __init__(self, category):
        self.category = category
        self.amount = 1000

    def deposit(self, amount):
        self.amount += amount
        return self.amount

    def __check_balance(self, amount):
       return True if self.amount > amount else False

    def withdraw(self, amount):
        if self.__check_balance(amount) == True:
            self.amount -= amount
            return self.amount
        else:
            return 'You do not have sufficient funds'

    def transfer(self, amount, category):
        print(self.amount, amount)
        if self.__check_balance(amount) == True:
            self.amount -= amount
            category.amount += amount
            return f"You have transferred {amount} to {category.category} category"
        else:
            return 'You do not have sufficient funds'



category_1 = Budget("clothing")
print("This is deposit for clothing", category_1.deposit(1000))
print("This is withdrawal for clothing", category_1.withdraw(300))

category_2 = Budget("food")
print(category_1.transfer(500, category_2))

category_3 = Budget("entertainment")