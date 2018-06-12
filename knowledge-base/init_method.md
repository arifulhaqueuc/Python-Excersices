
```__init__``` method
===
  - This is a special method in Python.
  - This is the constructor method for a class. 
  - this method is called when an object is created from a class. 

Example
```
class Student(object):
    """
    Returns a ```Student``` object with the given name, branch and year.
    """
    def __init__(self, name, branch, year):
            self.name = name
            self.branch = branch
            self.year = year
            print("A student object is created.")

    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)


In terminal
>>> std1 = Student()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 4 arguments (1 given)

>>> std1 = Student('Kushal','CSE','2005')
A student object is created

>>> std1.print_details()
Name: Kushal
Branch: CSE
Year: 2005
```
