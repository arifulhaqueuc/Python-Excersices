	
class Employee:

	def __init__(self, name, age, city):
		self.name = name
		self.age = age
		self.city = city


	def emp_details(self):
		print(self.name)
		print(self.age)
		print(self.city)




def main():
	x = Employee("Mak", 12, "Bristol")
	y = Employee("Robin", 83, "Cumberland")

	print("Details of employee 1")
	x.emp_details()
	print("Details of employee 2")
	y.emp_details()


if __name__ == "__main__":
	main()