class Shape:
	def display(self): pass

class Circle(Shape):
	def display(self):
		print("Circle")

class Square(Shape):
	def display(self):
		print("Square")

class Triangle(Shape):
	def display(self):
		print("Triangle")

def main():
	database = []
	
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


	print("There are " + str(len(database)) + " shapes in the database.")
	for shape in database:
		shape.display()


if __name__ == "__main__":
	main()