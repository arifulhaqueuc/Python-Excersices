
## Print the items form the following list
## if the items ONLY start with "ba"

list_all_1 = [


 'bb1'
,'bb2'
,'bb3'
,'ba4'


]


bb_remove = [x for x in list_all_1 if x[:2]=='ba']

for i in ba_remove:
	print i



	
list_all_2 = [


 'b000b1'
,'b000b2'
,'b000b3'
,'b000a4'


]
	
## let's print the items if 
## "ba" is in a item

ba_remove = [s for s in list_all if 'ba' in s]
for i in ba_remove:

	print i



