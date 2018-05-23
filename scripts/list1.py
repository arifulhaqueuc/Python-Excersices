## input = 1,2,3,4
## output = ['1','2','3','4'], ('1','2','3','4')



def abc():
	values = input()
	print("----")
	print(values)
	print("----")
	
	x = values.split(",")
	print(x)
	y = tuple(x)
	print("===")
	print(y)
	

if __name__ == "__main__":
	abc()
