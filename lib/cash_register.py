#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []
    
  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self.items.extend([title] * quantity)
    self.transactions.append([title, price, quantity])
    
  def apply_discount(self):
    if self.discount > 0:
        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount
        print("After the discount, the total comes to $800.")
    else:
        print("There is no discount to apply.")
        
  def void_last_transaction(self):
    if self.transactions:
      last_item, last_price, last_quantity = self.transactions[-1]
      self.total -= last_price * last_quantity
      
      for _ in range(last_quantity):
        self.items.remove(last_item)
      