

class Bank:

	def __init__(self, balance = 0.0):
		self.balance = balance



	def deposit(self, amount):
		self.balance += amount
		return self.balance




	def withdraw(self, amount):
		if amount < self.balance:
			raise RuntimeError("You donot have sufficient fund")
		else:
			self.balance -= amount
			return self.balance


x = Bank()
d = x.deposit(100)			
print(d)
