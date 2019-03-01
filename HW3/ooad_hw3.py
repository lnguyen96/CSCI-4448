import numpy as np 
from random import randint
from abc import ABCMeta, abstractmethod

class Customer(metaclass = ABCMeta): #Abstract customer class 
	def __init__(self, name, typeOf):
		self.name = name #unique customer name
		self.typeOf = typeOf #one of three customer types
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
		self.time = randint(1, 2) #number of time rented
		self.tools = randint(1, 2) #number of tools rented

	def rentals(self, tools):
		toolstaken = [] # List to track tools
		for i, j in enumerate(tools):
			toolstaken.append(tools.pop(0)) # Append it to the tracking list
			tools.pop(0) # To rent pop the first tool from the catalog
	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i]) # Return the tool back to the catalog
		del toolsRented[:] # Delete tracking list

class Regular(Customer): #Derived Regular customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Regular"
		self.time = randint(3, 5) #number of time rented
		self.tools = randint(1, 3) #number of tools rented

	def rentals(self, tools): # Keep track of tools rented
		toolstaken = [] # List to track tools
		for i, j in enumerate(tools):
			toolstaken.append(tools.pop(0)) # Append it to the tracking list
			tools.pop(0) # To rent pop the first tool from the catalog

	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i]) # Return the tool back to the catalog
		del toolsRented[:] # Delete tracking list

class Business(Customer): #Derived Business customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Business"
		self.time = 7
		self.tools = 3

	def rentals(self, tools):
		toolstaken = []
		for i, j in enumerate(tools):
			toolstaken.append(tools.pop(0)) # Append it to the tracking list
			tools.pop(0) # To rent pop the first tool from the catalog
	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i]) # Return the tool back to the catalog
		del toolsRented[:] # Delete tracking list

class customerFactory:
	def Casual(name): # Create casual customer
		return(Casual(name))
	def Regular(name): # Create regular customer
		return(Regular(name))
	def Business(name): # Create business customer
		return(Business(name))
	def creation(self): # Randomly create 10 customers and place into a customer array
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
		self.name = name # Unique tool name
		self.typeOf = typeOf # One of 5 tool types
	
	def cost(self): # Cost of renting tool
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
		tools = [] # Catalog 20 tools in store

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
	revenue = 0 # Amount of money gained from renting tools
	def checkoutCustomer(self, customers, toolArray): # Method to allow customers to rent tools
		for i, j in enumerate(customers): 
			if (len(toolArray) >= customers[i].tools): # If the catalog array has enough tools for the type of customer to rent then allow them to rent tools
				customers[i].rentals(toolArray) # Call rental method from customer class
				rental = Rental() # Crete a rental for each purchase
				print(customers[i].rentals(toolArray))
				print(rental.createRental(customers[i].rentals(toolArray), customers[i].time))
			else:
				pass

class Rental:
	def createRental(self, toolsRented, nights): # Create a rental that contains tools rented and how many nights rented for
		rental = []
		for item in toolsRented:
			rental[item] = toolsRented[item]
		rental.append(nights)
		return rental

def simulate(): # Simulation function creates objects and factories
	tools = toolFactory()
	customers = customerFactory()
	tools.creation()
	customers.creation()
	store = Store()
	print(store.checkoutCustomer(customers.creation(), tools.creation()))

def main():
	simulate()
	#for i in range(35):
	#	simulate()
		
if __name__ == '__main__':
	main()