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
		self.tool = randint(1, 2) #number of tools rented

	def rentals(self, tools):
		tool = randint(1, 2)
		toolstaken = [] # List to track tools
		for i in range(tool):
			toolstaken.append(tools.pop(0)) # Append it to the tracking list
			return (toolstaken, tools)
	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i]) # Return the tool back to the catalog

class Regular(Customer): #Derived Regular customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Regular"
		self.time = randint(3, 5) #number of time rented
		self.tool = randint(1, 3) #number of tools rented

	def rentals(self, tools): # Keep track of tools rented
		tool = randint(1, 3)
		toolstaken = [] # List to track tools
		for i in range(tool):
			toolstaken.append(tools.pop(0)) # Append it to the tracking list
		return (toolstaken, tools)
	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i])

class Business(Customer): #Derived Business customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Business"
		self.time = 7
		self.tool = 3

	def rentals(self, tools):
		tool = 3
		toolstaken = []
		for i in range(tool):
			toolstaken.append(tools.pop(0)) # Append it to the tracking list
		return (toolstaken, tools)
	def returns(self, toolsRented, tools):
		for i in range (time):
			tools.append(toolsRented[i]) # Return the tool back to the catalog

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
		self.returnDay = 0
	
	def cost(self): # Cost of renting tool
		pass

class Painting(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
		self.returnDay
	def cost(self):
		return 5

class Concrete(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
		self.returnDay
	def cost(self):
		return 10

class Plumbing(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
		self.returnDay
	def cost(self):
		return 7

class Woodwork(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
		self.returnDay
	def cost(self):
		return 15

class Yardwork(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf)
		self.returnDay
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
	def checkoutCustomer(self, customers, toolArray): # Method to allow customers to rent tools
		rentaldata = []
		revenue = 0 # Amount of money gained from renting tools
		for i, j in enumerate(customers): 

			if (len(toolArray) > customers[i].tool): # If the catalog array has enough tools for the type of customer to rent then allow them to rent tools
				rental = Rental() # Crete a rental for each purchase
				rentaldata.append((rental.createRental(customers[i].rentals(toolArray)[0], customers[i].time)))

			else:
				pass
				#print("The requested amount of tools is not available.")
		
		for item, j in enumerate(rentaldata):
			revenue += (rentaldata[item][1])
		return (rentaldata, revenue)

	def returnCustomer(self, customers, rentalArray):
		pass


class Rental:
	def createRental(self, toolsRented, nights): # Create a rental that contains tools rented and how many nights rented for
		revenue = 0
		rental = []
		for item, j in enumerate(toolsRented):
			rental.append(toolsRented[item].name)
			rental.append(toolsRented[item].typeOf)
			revenue += toolsRented[item].cost()

		rental.append(nights)
		return (rental, revenue)

def simulate(): # Simulation function creates objects and factories
	tools = toolFactory()
	customers = customerFactory()
	tools.creation()
	customers.creation()
	store = Store()
	#store.checkoutCustomer(customers.creation(), tools.creation())
	print("Daily revenue: " + str(store.checkoutCustomer(customers.creation(), tools.creation())[1]))
	#print(store.checkoutCustomer(customers.creation(), tools.creation()))

def main():
	#simulate()
	for i in range(35):
		simulate()
		
if __name__ == '__main__':
	main()