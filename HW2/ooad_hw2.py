class Shape: #Abstract Shape Class
	def display(self): pass

class Circle(Shape): #Circle is a subclass of Shape and prints out what it is in its overridden display method.
	def display(self):
		print("Circle")

class Square(Shape): #Square is a subclass of Shape and prints out what it is in its overridden display method.
	def display(self):
		print("Square")

class Triangle(Shape): #Triangle is a subclass of Shape and prints out what it is in its overridden display method.
	def display(self):
		print("Triangle")

def main():
	database = [] #database list will act as a database that stores shape objects
	
	database.append(Square())
	database.append(Triangle())
	database.append(Triangle())
	database.append(Circle())
	database.append(Triangle())
	database.append(Square())
	database.append(Circle())
	database.append(Triangle())
	database.append(Square())
	database.append(Square())
	database.append(Triangle())
	database.append(Circle())


	print("There are " + str(len(database)) + " shapes in the database.") #print out number of shapes in database
	for shape in database: #each shape has the ability to display itself
		shape.display()


if __name__ == "__main__":
	main()