## Lambda expressions
## We cannot use lambda experessions for multi-line functions
## common application: sorting and filtering data


## They are anonnymus functions, meaning that they donot have any function name.


## General approach

def func(x):
	return 3*x + 1


func(2) ## >> 7



## Labmda approach

## example 1
lambda x: 3*x + 1

## example 2
g = lambda x: 3*x + 1
g(2)


## with more than two inputs
## example: combine first and last name

full_name = lambda x, y: x.strip().title() + " " + y.strip().title()
full_name(" ariful", "HAQUE" )

