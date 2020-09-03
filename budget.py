class Category:
  ledger= list()
  category=""
  amount = 0
  def __init__(self, category): 
        self.category = category 


  def check_funds(self,amount):
    if self.amount> amount:
      return True
    else:
      return False


  def deposit(self,amount, description=""):
    self.ledger.append({"amount":amount,"description":description})
    self.amount += amount


  def withdraw(self,amount,description=""):
    if self.check_funds(amount) ==True:
      self.amount -=amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False

  # return balanace of budget 
  def get_balance(self):
    print("*************Food*************")
    for transaction in self.ledger:
      amount=0
      description=""
      for key,value in transaction.items():
          if key=="amount":
            amount = value
          elif key=="description":
            description=value
      if amount 
      line = description[:23] + str(amount)[:7].rjust(30-len(description))
      print(line)





  def transfer(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False


def create_spend_chart(categories):
    return "------karu akaur ----"