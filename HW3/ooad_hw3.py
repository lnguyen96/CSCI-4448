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
		mintime = 1
		maxtime = 2
		mintools = 1
		maxtools = 2

	def rentals(self, tools):
		rand = randint(1, 2)
		toolstaken = []
		if rand == maxtools:
			for i in range (maxtools):
				toolstaken[i] = tools.pop(0)
		else:
			toolstaken[0] = tools.pop(0)
	def returns(self, toolsRented, tools):
		rand = randint(1, 2)
		if rand == maxtime:
			for i in range (maxtime):
				tools.append(toolsRented[i])
			del toolsRented[:]

class Regular(Customer): #Derived Regular customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Regular"
		mintime = 3
		maxtime = 5
		mintools = 1
		maxtools = 3

	def rentals(self, tools):
		rand = randint(1, 3)
		toolstaken = []
		if rand == maxtools:
			for i in range (maxtools):
				toolstaken[i] = tools.pop(0)
		elif rand == maxtools - 1:
			for i in range (maxtools - 1):
				toolstaken[i] = tools.pop(0)
		else:
			toolstaken[0] = tools.pop(0)
	def returns(self, toolsRented, tools):
		rand = randint(3, 5)
		if rand == maxtime:
			for i in range (maxtime):
				tools.append(toolsRented[i])
				del toolsRented[:]
		elif rand == maxtime - 1:
			for i in range (maxtime - 1):
				tools.append(toolsRented[i])
				del toolsRented[:]
		else:
			for i in range(maxtime - 2):
				tools.append(toolsRented[i])
			del toolsRented[:]

class Business(Customer): #Derived Business customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Business"
		mintime = 7
		maxtime = 7
		mintools = 3
		maxtools = 3

	def rentals(self, tools):
		toolstaken = []
		for i in range (maxtools):
			toolstaken[i] = tools.pop(0)
	def returns(self, toolsRented, tools):
		for i in range (maxtime):
			tools.append(toolsRented[i])
		del toolsRented[:]

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
	def checkoutCustomer(self, customer, toolArray):
		if not toolArray:
			customer.rent()

class Rental:
	def __init__(self, rented, day):
		self.rented = rented
		self.day = day
		returnby = 0


def simulate():
	tools = toolFactory()
	customers = customerFactory()

def main():
	
	tools = toolFactory()
	print(tools.creation())
	customers = customerFactory()
	print(customers.creation().name)

	for i in range(35):
		simulate()
		
if __name__ == '__main__':
	main()