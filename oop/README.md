Structure of an OOP app
===

<pre>


class Car:                                            |   This is class body.
	make = "Nissan"                               |   And, make, model, year = Attributes of class
	model = "Sentra"                              |   
	year = "2010"                                 |



x = Car()                                       | x, y are just simple variables. And, when we invoke a
y = Car()                                       | class, and assign it to a variable,
                                                | we call it "creating objects of the class". 
                                                | And after that, x,y become the instances of class Car


print("This is the value of instance 1")        | After creating an instance of the class,
print(x.make)  ## output>>> Nissan              | the new instance will have access to the 
print(x.year) ## output>>> 2010                 | value of the attributes of the class.
                                                | So, ```x.make```this is how we can get access 
						| to the values of the class attributes.

print("This is the value of instance 2")	| this is just another instance of the class ```Car```.
print(y.make) ## output>>> Nissan       	| We can make as many instances as we want. 
print(y.year) ## output >>> 2010 

## But this is a way we can change the value of a class attribute
Car.year = "2011"
print(x.year) ## output>>> 2011
print(y.year) ## output>>> 2011

</pre>
