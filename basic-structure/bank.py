class Bank:

  def __init__(self,initial_bal):
    self.amount=initial_bal

  def credit(self,amt:int)->int:
    if amt <0:
      raise Exception("Amount should be -ve")
    self.amount+=amt
    return self.amount

  def debit(self,amt:int)->int:
    if amt>self.amount:
      raise Exception("Cannot withdraw")
    self.amount-=amt
    return  self.amount
    
  def calculation(self):
    x=self.credit(100)
    y=self.debit(100)
    return  self.amount

