
#### Purpose(s)
This repository helps us understand how to use solve basic Python programming tasks.

#### Multi-Threading programs in Python
In general, running several programs at the same time is referred to as multi-threaded programs. 
It is a very common idea in a multi-threaded program that two separate threads can access/read a same data such as a shared variable at the same time. And, such operation (accessing a same data at the same is absolutely fine), however the problem is that if the threads try to change/manipulate the data at that same data, the program might output a wrong result, or the program may even crash. 

There are two threading modules in Python
  - thread
  - threading 
  
| thread | threading |
| --- | --- |
| this is the basic thread module in Python, this was developed in earlier version of Python | threading is based on thread, and this is a newer version with many new features. As a result, this is obviously a better option in todays multi-threaded Python program |


#### Global Interpreter Lock (GIL)
  - One of the fundamental concepts in a multi-threaded program in Python.
  - GIL is basically a kind of lock held by an interpreter thread to avoid sharing code which is not thread-safe with other threads. 
  - The underlying idea of GIL is that it is a mechanism used by an interpreter to synchronize the execution of threads in a multi-threaded program, so that only one thread is being executed at a given point of time. 
  - An interpreter that uses GIL always allows only one thread to be executed at a time, even if it's being run on a multi-core processor.   
  - The main challenge is that CPython is not fully thread safe. So, in order to support multi-threaded Python program, CPython provides a global lock, and this global lock must be held by the current thread before it can safely access any Python object in a program. As a result, no matter how many threads are present, only one thread is being executed at a given point of time. 
  - In Python, the popular interpreter that offers GIL is CPython.

Benefits of GIL
  - easy integration of C libraries with a Python program, because usually C libraries are not thread-safe. 
  - GIL helps to increase speed of a single-threaded program.

Drawbacks
  - In a multi-threaded program, use of GIL may limit the amount of parallelism reachable though concurrency of a single interpreter process.

Solution of GIL / How can we fix or avoid the drawbacks of GIL
  - We can use multi-processing instead of multi-threading, meaning that, we can use multiple processing instead of threads. In this process, each Python process will get its own Python intepreter and memory space, so that the GIL will not cause any issue anymore. 
  - Python has multi-processing module, and that allows us to create multiple process easily. 
  - PyPy implementation provides a stackless mode that can support micro-thread for massive concurrency. 

#### Multi-processing in Python 
  - Multi-processing is a package that supports spawning processes using an API similar to the threading module. 
  - The multi-processing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. 
  - Due to this, the multi-processing module allows a programmer to fully leverage multiple processors on a given machine. And, it runs on both Unix and Windows.

*(directly from source mentioned below)*

#### Range vs Xrange
| range() | xrange() |
| --- | --- |
| range() produces a Python List | xrange() produces an xrange object |
| range generates a static list at run-time | xrange doesnot generate a static list at run-time |
| it consumes more memory | it is very memory efficient because it generates an object which is available for display by looping |
| present in Python 3 | removed in Python 3, was only available in Python 2 |
| range() is faster | --- |


#### List Comprehension
  - List Comprehension is a very popular way in Python to produce a list in a very concise way. 
  - The idea is that sometimes we need to apply either some conditions and expressions within a for loop to produce a list object. 
  - In such case, instead of writing several lines of code, we can write only one line of code to produce the same output. Such process is called List comprehension.
  
We have the following formula to produce a list with list comprehension approach.   
```
list = [expression + for loop + condition]
```
Let's see a side by side comparison between Regular Function and List Comprehension. 
<br /> The task is to produce a list of square numbers between 1 to 10 when the input numbers are greater than 4.
<pre>
Regular Function                |         List Comprehension
x = []                          |         x = [i*i for i in range(1,10) if i>4]
for i in range(1,10):           |
  if i > 4:                     | 
    list.append(i*i)            |
print(list)
</pre>


#### Python's Basic Data Structure 

| Properties | List | String | Tuple | Sets | Dict |
| ---        | --- | --- | --- | --- | --- | 
| Def        | Ordered Sequence of values | Sequence of Unicode Char | Ordered sequence of values | Unordered clooection of values | Unordered collection of key-value paris | 
| Ordered    | Yes | No | Yes | No | No | 
| Mutable    | Yes | No | No | --- | Yes | 


#### Lists vs Tuples  

| List | Tuple | 
| ---- | ----- |
| There are some helpful functions in list. Such as append(),insert() | We donot have such functions in tuple |
| ---- | Tuples use less space |
| ---- | We can use tuples as dict keys |
| ---- | We can use **Named Tuples** as an alternative to objects |
| ---- | We can pass functions arguments as Tuples |
| Lists are homogeneous sequences, and have an order | Tuples are heterogeneous sequences, and have a structure |
| Lists are not hashable | Tuples are hashable (To be hashable, an object needs to be immutable, and have a hash function) |


#### Django vs Flask

| Django | Flask | 
| ---- | ----- |
| This is useful for large application | This is a micro-framework, suitable for medium-level application with simple requirements |
| Django has very powerful tool to connect Django application with several Database. This is called Django ORM. Example Sql Alchemy | In Flask, we have several libraries to connect Flask application with Database |
| Many features are built-in in Django. Such as templating, forms, routing, authentication, admin panel | In Flask, we need to create such features from scratch |
| Django has built-in bootstrap template | Flask doesnot have such feature |



#### Python OOP

| Terms | Definition | 
| ---- | ----- |
| attribute | This is a  property of a class that can further define the class in details |
| method | It is a function within a class that performs a specific task. And, a method can access all the attributes of a class. In Python, a method has a by-default initial paramter which is called "self" |
| class attribute | attributes that are shared across all instances of a class. They are created in tow ways (i) as part of the class, (ii) by using className.attributeName |
| instance attribute | attributes that are specific to each instance of a class. They are created by using objectName.attributeName. They are only available to a spefic object |
| instance attribute | attributes that are specific to each instance of a class. They are created by using objectName.attributeName. They are only available to a spefic object |
| instance method | methods that accept self as default parameter. And they are used to modify an instance attribute |
| static method | methods that donot accept the default self paramter. But they are used to modify a class attribute |
| init method | this is a special method in Python, and they are called when we instantiate and object. They are used to initialized the attrbutes of a class. All the attributes of a class should be initiazed in this method to make them available within the class |
| encapsulation | Hiding the implementation details from the end user is called as encapsulation |
| abstraction | Abstraction is the process of steps followed to achieve encapsulation |


#### Series VS Dataframe

| Series | Dataframe | 
| ---- | ----- |
| Series is one-dimensional | Dataframe is two-dimentional |
| Series holds any types of data such as int, str, floating point | Dataframe is a labeled data structure with column of potential different types |


#### How to import libraries
General Syntax
<br />Option 1
```
import math as m
```
Option 2
```
from *Library Name* import *Features*
```
Example
```
from math import *
x = sinh(5)
print(x)
```



:computer: Support & Disclaimer
===
### Support
Found a bug??
<br />Here are the options
  - Please file an issue with detailed description.
  - If you know a possible solution, please create a new brnach, update the code and then submit pull request.
  - If you would  like to reach out to me directly with any question, email me at ariful.haque.uc@gmail.com

Interester in Collaboration and Contribution??
<br /> I am open to except any relevant collaboration suggestion from developers. Feel free to reach out to me in email.

### General Disclaimer
This is my personal repo and not an official product of any company. If you would like to use this code, please keep it in your mind that, although I have tried to make it as error-free as possible, there's no warranty of a 100% bug free application. 



#### References
GIL
  - https://en.wikipedia.org/wiki/Global_interpreter_lock
  - https://en.wikipedia.org/wiki/Mutual_exclusion
  - https://www.quora.com/What-is-Global-Interpreter-Lock-How-it-is-related-to-Python
  - https://opensource.com/article/17/4/grok-gil
  - https://realpython.com/python-gil/#what-problem-did-the-gil-solve-for-python
  - https://wiki.python.org/moin/GlobalInterpreterLock
  
Multi-processing
  - https://pymotw.com/2/multiprocessing/basics.html
  - https://docs.python.org/3.4/library/multiprocessing.html?highlight=process
  - https://docs.python.org/2/library/multiprocessing.html
  
Deep Copy vs Shallow Copy
  - https://docs.python.org/3/library/copy.html
  - https://www.python-course.eu/deep_copy.php
  - https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
  - https://stackoverflow.com/questions/17246693/what-exactly-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignm
  
  
  
