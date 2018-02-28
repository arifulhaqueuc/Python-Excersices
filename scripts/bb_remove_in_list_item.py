
## Print the items form the following list
## if the items ONLY start with "ba"

list_all = [


 'bb1'
,'bb2'
,'bb3'
,'ba4'


]


bb_remove = [x for x in list_all if x[:2]=='ba']

for i in ba_remove:
	print i

