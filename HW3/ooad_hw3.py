import numpy as np 
from random import randint
from abc import ABCMeta, abstractmethod

class Customer(metaclass = ABCMeta): #Abstract customer class 
	def __init__(self, name, typeOf):
		self.name = name #unique customer name
		self.typeOf = typeOf #one of three customer types
		tool = 0 #number of tools available to rent for customer type
		time = 0 #number of nights the customer type may rent their tools for
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
			if (tools == []): # If the tools catalog is empty report that there is nothing to rent
				print("Nothing to rent right now")
			else:
				toolstaken.append(tools.pop(0)) # Append it to the tracking list
			return (toolstaken, tools) #Return tuple of tools rented by customer and new catalog of tools
	def returns(self, toolsRented, tools):
		for i in range (len(toolsRented)):
			tools.append(toolsRented[i]) # Return the tool back to the catalog
		return toolsRented

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
			if (tools == []): # If the tools catalog is empty report that there is nothing to rent
				print("Nothing to rent right now")
			else:
				toolstaken.append(tools.pop(0)) # Append it to the tracking list
		return (toolstaken, tools) #Return tuple of tools rented by customer and new catalog of tools
	def returns(self, toolsRented, tools):
		for i in range (len(toolsRented)):
			tools.append(toolsRented[i]) # Return the tool back to the catalog
		return toolsRented

class Business(Customer): #Derived Business customer class
	def __init__(self, name):
		self.name = name
		self.typeOf = "Business"
		self.time = 7 #number of time rented
		self.tool = 3 #number of tools rented

	def rentals(self, tools):
		tool = 3
		toolstaken = [] # List to track tools
		for i in range(tool):
			if (tools == []): # If the tools catalog is empty report that there is nothing to rent
				print("Nothing to rent right now")
			else:
				toolstaken.append(tools.pop(0)) # Append it to the tracking list
		return (toolstaken, tools) #Return tuple of tools rented by customer and new catalog of tools
	def returns(self, toolsRented, tools):
		for i in range (len(toolsRented)):
			tools.append(toolsRented[i]) # Return the tool back to the catalog
		return toolsRented

class customerFactory: #Factory for encapsulating creation of customer objects
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
			randint = np.random.choice(3, 1) #Create customer type based on random number
			if randint == 0:
				customers.append(Casual("Customer " +str(num))) #Give the customer a unique name
			elif randint == 1:
				customers.append(Regular("Customer " +str(num))) #Give the customer a unique name
			else:
				customers.append(Business("Customer " +str(num))) #Give the customer a unique name
			num += 1
		return customers

class Tool(metaclass = ABCMeta):
	def __init__(self, name, typeOf):
		self.name = name # Unique tool name
		self.typeOf = typeOf # One of 5 tool types
		self.returnDay = 0 #How long until the tool should be returned
	
	def cost(self): # Cost of renting tool
		pass

class Painting(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf) # Override variable values from abstract super class
		self.returnDay
	def cost(self):
		return 5 # Specific cost of tool category

class Concrete(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf) # Override variable values from abstract super class
		self.returnDay
	def cost(self):
		return 10 # Specific cost of tool category

class Plumbing(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf) # Override variable values from abstract super class
		self.returnDay
	def cost(self):
		return 7 # Specific cost of tool category

class Woodwork(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf) # Override variable values from abstract super class
		self.returnDay
	def cost(self):
		return 15 # Specific cost of tool category

class Yardwork(Tool):
	def __init__(self, name, typeOf):
		Tool.__init__(self, name, typeOf) # Override variable values from abstract super class
		self.returnDay
	def cost(self):
		return 12 # Specific cost of tool category

class toolFactory(): # Factory for encapsulating creation of tool objects
	def creation(self):
		tools = [] # Catalog 20 tools in store

		for i in range(20):
			choice = np.random.choice(5)
			tools.append(choice)

		counter = 0
		for tool, item in enumerate(tools): # For each item in the tools array 
			counter += 1
			if item == 0:
				tools[tool] = Painting("Tool-" +str(counter), "Painting") # Give the object a unique name
			elif item == 1:
				tools[tool] = Concrete("Tool-" +str(counter), "Concrete") # Give the object a unique name
			elif item == 2:
				tools[tool] = Plumbing("Tool-" +str(counter), "Plumbing") # Give the object a unique name
			elif item == 3:
				tools[tool] = Woodwork("Tool-" +str(counter), "Woodwork") # Give the object a unique name
			else:
				tools[tool] = Yardwork("Tool-" +str(counter), "Yardwork") # Give the object a unique name

		return tools

class Store:
	def checkoutCustomer(self, customers, toolArray): # Method to allow customers to rent tools
		rentaldata = [] # Store rental receipts for customers
		revenue = 0 # Amount of money gained from renting tools
		for i, j in enumerate(customers): # Check if each customer may rent tools based on what is available. 

			if (len(toolArray) > customers[i].tool): # If the catalog array has enough tools for the type of customer to rent then allow them to rent tools
				rental = Rental() # Create a rental for each purchase
				createrent = (rental.createRental(customers[i].rentals(toolArray)[0], customers[i].time)) # Fill the rental with the tool objects and when to return them by
				print("Renting - " + str(createrent)) 
				rentaldata.append(createrent) # Add to store of rental receipts

			else:
				print("The requested amount of tools is not available.") # If there aren't enough tools for that customer print this statement

		for item, j in enumerate(rentaldata): # For each rental receipt
			revenue += (rentaldata[item][1]) # Sum the revenue gained from each customer

		return (rentaldata, revenue)

class Rental:
	def createRental(self, toolsRented, nights): # Create a rental that contains tools rented and how many nights rented for
		revenue = 0
		rental = [] # Rental receipts are displayed as lists
		for item, j in enumerate(toolsRented): # For each tool that a customer rents
			rental.append(toolsRented[item].name) # Add the name of the tool to the rental receipt
			rental.append(toolsRented[item].typeOf) # Add the type of the tool to the rental receipt
			revenue += toolsRented[item].cost() # Add the total cost of the tools to the rental receipt

		rental.append(nights) # Add the number of nights before the customer must return the tools
		return (rental, revenue)

def simulate(): # Simulation function creates objects and factories
	days = [1, 2, 3, 4, 5, 6, 7] # Create days list to simulate days of the week
	tools = toolFactory() # Create instance of factory
	customers = customerFactory() # Create instance of factory
	tools.creation() # Call method to create objects
	customers.creation() # Call method to create objects
	store = Store() # Create instance of store class
	
	for i in range(35): # Run simulation for 35 nights
		print("Day - " + str(i)) # Print out what day the simulation is on
		print("Total revenue: " + str(store.checkoutCustomer(customers.creation(), tools.creation())[1])) # Sum the total daily revenue 

		if (days[i % len(days)] == customers.creation()[i % len(customers.creation())].time): # Checks if the customer's rental is out of time
			customers.creation()[i % len(customers.creation())].returns(store.checkoutCustomer(customers.creation(), tools.creation()), tools.creation()) # Readd tools to the store's catalog 
			print("Returning - " + str(customers.creation()[i % len(customers.creation())].returns(store.checkoutCustomer(customers.creation(), tools.creation()), tools.creation())))

def main():
	simulate() # Call simulation method
		
if __name__ == '__main__':
	main()