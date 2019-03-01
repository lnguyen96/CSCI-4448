import numpy as np 
from random import randint
from abc import ABCMeta, abstractmethod

class Customer(metaclass = ABCMeta): #Abstract customer class 
	def __init__(self, name, typeOf):
		self.name = name
		self.typeOf = typeOf
		mintools = 0
		maxtools = 3
		maxrent = 3
		rents = 0
		mintime = 0
		maxtime = 7
		pass
	@property
	@abstractmethod
	def rentals(self): #method for when a customer rents a tool
		pass
	def returns(self): #method to return tools to the tools array
		pass

class Casual(Customer): #Derived Casual customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Casual"
		self.time = randint(1, 2)
		self.tools = randint(1, 2)

	def rentals(self, tools):
		toolstaken = []
		for i in range (tools):
			toolstaken[i] = tools.pop(0)
	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i])
		del toolsRented[:]

class Regular(Customer): #Derived Regular customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Regular"
		self.time = randint(3, 5)
		self.tools = randint(1, 3)

	def rentals(self, tools): # Keep track of tools rented
		toolstaken = [] # List to track tools
		for i in range (tools):
			toolstaken[i] = tools.pop(0)
	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i])
		del toolsRented[:]

class Business(Customer): #Derived Business customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Business"
		self.time = 7
		self.tools = 3

	def rentals(self, tools):
		toolstaken = []
		for i in range (tools):
			toolstaken[i] = tools.pop(0)
	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i])
		del toolsRented[:]

class customerFactory:
	def Casual(name):
		return(Casual(name))
	def Regular(name):
		return(Regular(name))
	def Business(name):
		return(Business(name))
	def creation(self):
		customers = []
		num = 0
		for i in range(10):
			randint = np.random.choice(3, 1)
			if randint == 0:
				customers.append(Casual("Customer " +str(num)))
			elif randint == 1:
				customers.append(Regular("Customer " +str(num)))
			else:
				customers.append(Business("Customer " +str(num)))
			num += 1
		return customers

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

		return tools

class Store:
	revenue = 0
	def checkoutCustomer(self, customers, toolArray):
		for i, j in enumerate(customers):
			if (len(toolArray) <= customers[i].tools):
				customers[i].rentals(toolArray)
				rental = Rental()
				print(customers[i].rentals(toolArray))
				print(rental.createRental(customers[i].rentals(toolArray), customers[i].time))
			else:
				pass

class Rental:
	def createRental(self, toolsRented, nights):
		rental = []
		for item in toolsRented:
			rental[item] = toolsRented[item]
		rental.append(nights)

def simulate():
	tools = toolFactory()
	customers = customerFactory()
	tools.creation()
	customers.creation()
	store = Store()
	print(store.checkoutCustomer(customers.creation(), tools.creation()))

def main():
	for i in range(35):
		simulate()
		
if __name__ == '__main__':
	main()