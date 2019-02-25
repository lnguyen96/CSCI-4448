import numpy as np 
from abc import ABCMeta, abstractmethod

class Customer(metaclass = ABCMeta):
	def __init__(self, name, typeOf):
		self.name = name
		self.typeOf = typeOf
		pass
	@property
	@abstractmethod
	def rentals(self):
		pass

class Casual(Customer):
	def __init__(self, name):
		self.name = name
		self.typeOf = "Casual"

	def rentals(self):
		pass
class Regular(Customer):
	def __init__(self, name):
		self.name = name
		self.typeOf = "Regular"

	def rentals(self):
		pass

class Business(Customer):
	def __init__(self, name):
		self.name = name
		self.typeOf = "Business"

	def rentals(self):
		pass

class Store:
	def __init__(self, category, name):
		self.category = category
		self.name = name
		self.available = 1


def main():
	tools = []
	customer = []

	for i in range(20):
		choice = np.random.choice(5)
		tools.append(choice)

	counter = 0
	for tool, item in enumerate(tools):
		counter += 1
		if item == 0:
			tools[tool] = "Painting " + "Tool-" +str(counter)
		elif item == 1:
			tools[tool] = "Concrete " + "Tool-" +str(counter)
		elif item == 2:
			tools[tool] = "Plumbing " + "Tool-" +str(counter)
		elif item == 3:
			tools[tool] = "Woodwork " + "Tool-" +str(counter)
		else:
			tools[tool] = "Yardwork " + "Tool-" +str(counter)

	for i in range(len(tools)):

		tools[i] = Store((tools[i]).split(' ')[0], (tools[i]).split(' ')[1])

	for i in range(10):
		customer[i].append()

		

if __name__ == '__main__':

	main()