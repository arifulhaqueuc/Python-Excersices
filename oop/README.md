

<pre>


class Car:                                      |   This is class body.
	make = "Nissan"                               |   And, make, model, year = Attributes of class
	model = "Sentra"                              |   
	year = "2010"                                 |



x = Car()                                       | x, y are just simple variables. And, when we invoke a
y = Car()                                       | class, and assign it to a variable,
                                                | we call it "creating objects of the class". 
                                                | And after that, x,y become the instances of class Car


print("This is the value of instance 1")        | After creating an instance of the class,
print(x.make)                                   | the new instance will have access to the 
                                                | value of the attributes of the class.
                                                | So, ```x.make```this is how we can access to the values of the class attributes.

print("This is the value of instance 2")
print(y.make)



</pre>
