from abc import ABC, abstractmethod
import datetime

class Bank:
    def __init__(self, name, bank_swift_code):
      self.name = name
      self.swift_code = bank_swift_code
      customers = []
        
class Customer:
 def __init__(self, name, address, phone_number, email):
   self.name = name
   self.address = address
   self.phone_number = phone_number
   self.email = email
   self.accounts = []

class Account:
  def __init__(self, account_number):
    self.accont_number = account_number
    self.balance = 0
    self.linked_card = None
    self.transacions_history []

  def add_transacions(self, transaction):
    self.transaction_history.append(transaction)

class Card:
  def __init__(self, number, pin):
    self.number = number
    self.pin = pin
    
  
class Atm: 
 def __init__(self, bank, atm_location):
    self.bank = bank
    self.location = atm_location


class Transaction(ABC):
    transaction_counter = 0

    def __init__(self, transaction_type, amount=None):
      self.transaction_id = Transaction.transaction_counter
      self.timestamp = datetime.datetime.now()
      Transaction.transaction_counter += 1
      self.transaction_type = transaction_type
      self.amount = amount

    @abstractmethod
    def execute(self):
       pass

class WithdrawTransaction(Transaction):
    def __init__(self, amount):
        super().__init__("withdrawal", amount)
        self.amount = amount

    def execute(self, account):
        if account.balance >= self.amount:
            account.balance -= self.amount
            print(f"Withdrawal Successful. New Balance: {account.balance}")
            account.add_transactions(self)
        else:
            print("Insufficient balance")

class DepositTransaction(Transaction):
    def __init__(self, amount):
        super().__init__("deposit", amount)
        self.amount = amount
        
    def execute(self, account):
        account.balance += self.amount
        print(f"Deposit Successful. New Balance: {account.balance}")
        account.add_transactions(self)

class BalanceInpuiry(Transaction):
    def __init__(self, transaction_type, amount=None):
      super().__init__("balance inpuiry")
      

    def execute(self):
       print("Your balaince is: {account.balance}")
       account.add_transiction(self)
       
       for transaction in self.transaction_hestory.items():
          print(f"Transaction : {transaction} in {self.timestamp})
                
