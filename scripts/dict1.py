# input = 4
# output = {1:1, 2:4, 3:9, 4:16}


def abc():
	user=int(input())
	print("-----")
#	print(user)

	d = dict()
	for i in range(1,user+1):
		d[i] = i*i
	print(d)





abc()
