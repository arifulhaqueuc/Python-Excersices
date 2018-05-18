## Lambda expressions
## Definition: They are anonnymus functions, meaning that they donot have any function name.
## We cannot use lambda experessions for multi-line functions
## real-life example: sorting and filtering data i.e. sorting people based on their last name

## simple example 
## lambda function with one input
x = lambda x:3*x +1
print(x(2))


## real-life example 
## lambda function with more than one input
name = lambda first, last: first.strip() + " " + last.strip()
print(name("ariful", "haque"))
