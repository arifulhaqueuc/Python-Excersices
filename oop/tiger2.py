
class Tiger:

	def __init__(self, name):
		self.name = name

	def can_run(self):
		#print(self.name)
		print("Tiger " + self.name + " can run")

	def can_eat(self):
		#print(self.name)
		print("Tiger "+ self.name +" can eat")


def main():
	x= Tiger("Leo")
	x.can_run()
	x.can_eat()   



if __name__ == "__main__":
	main()

