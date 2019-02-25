import numpy as np 
from abc import ABCMeta, abstractmethod

class Customer(metaclass = ABCMeta):
	def __init__(self, name, typeOf):
		self.name = name
		self.typeOf = typeOf
		mintools = 0
		maxtools = 0
		maxrent = 3
		rents = 0
		mintime = 0
		maxtime = 0
		pass
	@property
	@abstractmethod
	def rentals(self):
		pass
	def returns(self):
		pass
	def rent(self):
		pass

class Casual(Customer):
	def __init__(self, name):
		self.name = name
		self.typeOf = "Casual"
		mintime = 1
		maxtime = 2
		mintools = 1
		maxtools = 2

	def rentals(self):
		pass
	def returns(self):
		pass
	def rent(self):
		pass
class Regular(Customer):
	def __init__(self, name):
		self.name = name
		self.typeOf = "Regular"
		mintime = 3
		maxtime = 5
		mintools = 1
		maxtools = 3

	def rentals(self):
		pass
	def returns(self):
		pass
	def rent(self):
		pass

class Business(Customer):
	def __init__(self, name):
		self.name = name
		self.typeOf = "Business"
		mintime = 7
		maxtime = 7
		mintools = 3
		maxtools = 3

	def rentals(self):
		pass
	def returns(self):
		pass
	def rent(self):
		pass

class customerFactory:
	def Casual(name):
		return(Casual(name))
	def Regular(name):
		return(Regular(name))
	def Business(name):
		return(Business(name))
	def creation(name):
		randint = np.random.choice(3, 1)
		if randint == 0:
			return Casual("Customer " +str(np.random.choice(11)))
		elif randint == 1:
			return Regular("Customer " +str(np.random.choice(11)))
		else:
			return Business("Customer " +str(np.random.choice(11)))

class Tool(metaclass = ABCMeta):
	def __init__(self, name, typeOf):
		self.name = name
		self.typeOf = typeOf
	
	def cost(self):
		pass

class Painting(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
	def cost(self):
		return 5

class Concrete(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
	def cost(self):
		return 10

class Plumbing(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
	def cost(self):
		return 7

class Woodwork(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
	def cost(self):
		return 15

class Yardwork(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
	def cost(self):
		return 12

class toolFactory():
	def creation(self):
		tools = []

		for i in range(20):
			choice = np.random.choice(5)
			tools.append(choice)

		counter = 0
		for tool, item in enumerate(tools):
			counter += 1
			if item == 0:
				tools[tool] = Painting("Tool-" +str(counter), "Painting")
			elif item == 1:
				tools[tool] = Concrete("Tool-" +str(counter), "Concrete")
			elif item == 2:
				tools[tool] = Plumbing("Tool-" +str(counter), "Plumbing")
			elif item == 3:
				tools[tool] = Woodwork("Tool-" +str(counter), "Woodwork")
			else:
				tools[tool] = Yardwork("Tool-" +str(counter), "Yardwork")

		for i, item in enumerate(tools):
			print(tools[i].typeOf)
		return tools

class Store:
	def __init__(self, category, name):
		self.category = category
		self.name = name
		self.available = 1

class Rental:
	def __init__(self, rented, day):
		self.rented = rented
		self.day = day
		returnby = 0

def main():
	
	tools = toolFactory()
	print(tools.creation())
	customers = customerFactory()
	print(customers.creation().name)
		
if __name__ == '__main__':

	main()