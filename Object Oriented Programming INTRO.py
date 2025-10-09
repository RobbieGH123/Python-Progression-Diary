## Object Oriented Programming

## Establishing a Class:

class Dog:                                                           # Class Creation

    def __init__ (self, name, age):                                  # Constructor

     self.name = name                                                # Assigns the name argument to the object
     self.age = age                                                  # Assigns the age argument to the object

    def bark(self):                                                  # 1st Method
        print(f"{self.name} says woof!")                             # Print 'Object Name' says woof!

    def birthday(self):                                              # 2nd Method
       self.age += 1                                                 # Adds 1 to the stored age
       print(f"{self.name} is now {self.age} years old!")            # Print 'Object Name' is now 'Object Age' years old!

my_dog = Dog("Nora", 3)                                              # 1st Instance of Dog
my_dog.bark()                                                        # Calls Bark Method
my_dog.birthday()                                                    # Calls Birthday Method

my_second_dog = Dog("Louis", 3)                                      # 2nd Instance of Dog
my_second_dog.bark()                                                 # Calls Bark Method
my_second_dog.birthday()                                             # Calls Birthday Method


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
# Task list:
# Create a class with at least: 3 attributes, 2 methods (1 that updates an attribute) Create multiple objects. 

class Book:
   
   def __init__ (self, title, author, status="not updated the completion status for"):
      
      self.title = title
      self.author = author
      self.status = status

   def describe(self):
      
      print(f"This book is called {self.title} and it was written by {self.author}, you have {self.status} it.")

   def update_status(self):
      
      new_status = input("Have you: Not read, Began reading or Read: ")
      self.status = new_status
      print(f"This book is called {self.title} and it was written by {self.author}, you have {self.status.lower()} it.\n")
      
first_book = Book("A tale of Two Cities", "Charles Dickens")
first_book.describe()
first_book.update_status()

second_book = Book("The Lord of The Rings", "J.R.R. Tolkein")
second_book.describe()
second_book.update_status()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Create a Rectangle Class
# Create a Method that returns the Area of the triangle.

class Rectangle:
   
   def __init__(self, width, length):
      
      self.width = width
      self.length = length
      
   def area(self):
      area = (self.width * self.length)
      print(f"The rectangle has an area of {area}cm")

rectangle_example = Rectangle(6, 8)
rectangle_example.area()

# Create a Bank Account
# Create 1 Method for Deposits, Create another Method for Withdrawals.

class BankAccount:                                                                    # Class Creation
   
    def __init__(self, balance):                                                      # Constructor, 1 paramater
       
        self.balance = balance                                                        # Assign a Balance

    def deposit(self):                                                                # Deposit Method
        deposit_amount = int(input("How much would you like to deposit: "))           # Deposit amount
        self.balance += deposit_amount                                                # Update the balance
        print(f"Your new balance is {self.balance}")                                  # Print the new balance
        self.menu()                                                                   # Call the Menu method

    def withdraw(self):                                                               # Withdrawal Method
        withdrawal_amount = int(input("How much would you like to withdraw: "))       # Withdraw amount
        if withdrawal_amount > self.balance:                                          # If the user tries to withdraw more than the full balance
            print("Insufficient funds.")                                              # Print Insufficient funds
        else:                                                                         # If withdrawal amount < balance
            self.balance -= withdrawal_amount                                         # Update the balance
            print(f"Your new balance is {self.balance}")                              # Print the new balance
        self.menu()                                                                   # Call the Menu Method

    def menu(self):                                                                   # Menu Method
        user_choice = input("\nWhat would you like to do now:\nCheck Balance\nMake a Deposit\nMake a Withdrawal\nExit\n\n").lower() 
    
        if "balance" in user_choice:                                                  # If the User wants to check their balance
            print(f"Your current balance is {self.balance}")                          # Print their balance
            self.menu()                                                               # Return to the Menu Method.
        elif "deposit" in user_choice:                                                # If the user wants to make a Deposit
            self.deposit()                                                            # Run the Deposit Method
        elif "withdraw" in user_choice:                                               # If the user wants to Withdraw
            self.withdraw()                                                           # Run the Withdrawal Method
        elif user_choice == "exit":                                                   # If the user wants to exit
            print("Thank you for banking with us.")
        else:                                                                         # All other bases
            print("Invalid choice. Try again.")
            self.menu()

my_bank = BankAccount(500)

my_bank.menu()

#=======================================================================================================================================================================#

class Example:
    def __init__(self):
        self._secret = 42

e = Example()
print(e._secret)      # ❌ AttributeError




   


