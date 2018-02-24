'''
Write a function that takes a list of numbers and
returns the largest value.
'''

def max_in_list(l):
	largest = reduce(lambda x,y:max(x,y), l)
	return largest


l = [1,2,3,4,12,817,189,17]
print "We can do this in two ways."
print "\nFirst approach is define a function and then calling it"
print max_in_list(l)

print "\nSecond approach is using reduce function provided by lambda"
print reduce(max, l)

