num = int(input())
value = range(1,num+1)
print("----")


def mu_function():
	res = 1	
	if num == 0:
		print("something")
	else:
		for i in value:
			res = res * i
			print(res)

mu_function()			
