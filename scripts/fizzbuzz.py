



def abc():
	values = range(1,20)
	for i in values:
		if i%3 == 0 and i%5 == 0:
			print("fizzbuzz")
		elif i%3 == 0:
			print("fizz")
		elif i%5 == 0:
			print("buzz")


		else:
			print("\n")





if __name__ == "__main__":
	abc()
