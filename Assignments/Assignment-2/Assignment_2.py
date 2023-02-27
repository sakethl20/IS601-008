#Saketh Lakshmanan
#sl778
#Sunday Feb 26

# Task 1 (50 points)
# Question 1
arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 1
arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 2
arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9] # 3
# only output the odd values from the above lists (print the output for all lists)
def odd_values(num,arr): # pass the num as list number and arr as list name
    print(f'output for arr {num}: \n')
    
    for i in arr:
        if(i%2 == 1):
            print(f'{i} \n')
    
    print('\n End of odd values\n')
    
odd_values(1, arr1)
odd_values(2, arr2)
odd_values(3, arr3)


# Question 2
arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # 1
arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20] #2
arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44] #3
# Only output the sum/total of the lists values (print the output for all lists)
def sum_values(num, arr): # pass the num as list number and arr as list name
    print(f'Output for arr {num} : \n')
    
    total = 0
    for i in arr:
        total+= i
    print(total)
    
    print('\n End of sum values\n')

sum_values(1, arr1)  
sum_values(2, arr2) 
sum_values(3, arr3) 


# Question 3
arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100] #1
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233] #2 
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33] #3
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99] #4
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30] #5
# Convert the negative values in the following lists to positive and ouput the sum of all values (print the output for all lists).
def converted_sum_values(num, arr): # pass the num as list number and arr as list name
    print(f'Output for arr {num} : \n')
    
    oddSum = 0
    total =  0
    for i in arr:
        if (i < 0):
           oddSum+= (i*-1) 
        else:
            i+=total
    total+=oddSum
    print(total)
    print('\n End of converted sum values\n')

converted_sum_values(1, arr1)
converted_sum_values(2, arr2)
converted_sum_values(3, arr3)


# Question 4
arr1 = ['apple', '', 'banana', '', 'cherry'] #1
arr2 = ['', 'dog', '', 'cat', ''] #2
arr3 = ['hello', '', 'world', '', ''] #3
arr4 = ['', '', '', '', ''] #4
arr5 = ['one', '', 'two', '', 'three'] #5
# Remove empty strings from the above lists and output the lists (print the output for all lists)
def empty_str(num, arr): # pass the num as list number and arr as list name
    print(f'Output for arr {num} : \n')
    
    updated_empty_string = [i for i in arr if i != '']
    print(updated_empty_string)
    
    print('\n End of empty str values\n')

empty_str(1, arr1)
empty_str(2, arr2)
empty_str(3, arr3)


# Question 5
# Write a function that takes in a list and prints the smallest value from that list.
# Task 2 (50 Points)
# This task is divided into sub parts.
# Part 1: Bank Account Class
# 1. Create BankAccount class with following attributes and methods:
    # Attributes:
        # account_number: An integer.
        # balance: A float. 
        # account_holder: A string.
    # Methods:
        # deposit(self, amount): Adds the amount to current balance.
        # withdraw(self, amount): Subtracts the amount from current balance.
        # get_balance(self): Returns the current balance.

class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
      
# call the BankAccount class by creating an instance of it and pass in the values.
# pass the balance as 1000, give a account number and account holder name  
# call deposit() method, withdraw() method by passing deposit amount as 200, withdraw amount as 700
# then print the total balance of the account (call the get_balance() method)

bank_act = BankAccount(314929, 1000, 'Saketh Lakshmanan')
bank_act.deposit(200)
bank_act.withdraw(700)
print("Bank Account ballance: ", bank_act.get_balance())

# Part 2: Checking Account Class
# 1. Create CheckingAccount class that inherits from BankAccount
# 2. Add the following attributes and methods to the CheckingAccount class:
    # Attributes:
        # transaction_fees: A float, transaction fees charged for each transaction.
    # Methods:
        # apply_transaction_fees(self): Subtracts the transaction fees from current balance.
        
class Checking_Account(BankAccount):
    def __init__(self, transaction_fees):
        self.transaction_fees = transaction_fees
    
    def apply_transaction_fees(self):
        self.balance-= self.transaction_fees

# call CheckingAccount class by creating an instance of it
# pass the transaction fees as 34.50 and call the apply_transaction_fees() method
# then print the total balance of the account (call the get_balance() method)

checking_act = Checking_Account(34.50)
Checking_Account.apply_transaction_fees()
print(Checking_Account.get_balance())

# Part 3: Savings Account Class
# 1. Create SavingsAccount class that inherits from BankAccount.
# 2. Add the following attributes and methods to the SavingsAccount class:
    # Attributes:
        # interest_rate: A float
    # Methods:
        # calculate_interest(self): Calculates and adds the interest to the currentbalance.

class SavingsAccount(BankAccount):
    def __init__(self, interest_rate):
        self.interest_rate = interest_rate
    def calculate_interest(self):
        self.balance += (self.interest_rate * self.balance)

# call SavingsAccount class by creating an instance of it
# pass the interest rate as 0.12 and call the calculate_interest() method
# then print the total balance of the account (call the get_balance() method)

savings_acct = SavingsAccount(0.12)
savings_acct.calculate_interest()
savings_acct.get_balance()