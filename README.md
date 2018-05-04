:zap: Project Update Information
====
Last major update: May 02'2018



:couple: Audience Insights 
====
#### Target Audience
Python Developers who are interested to upgrade their knowledge by practicing common Python problems.


#### Purpose(s)
This repository helps us understand how to use solve basic Python pprogramming tasks.


#### What to expect
After practicing all given queries at least couple of times would help the beginners of Python propgramming on how to write basic Python scripts. 


#### Pre-requisites / Know Before You Go
  - Basic knowledge of Python 2.x
  - Basic knoledge of OOP


:green_book: Project Insights
===
#### Repository Type
This repo is a collection of individual Python scripts. 

#### Knowledge Base
To be added later


#### Birds Eye View 
|  |  |
| --- | --- |
| Repo Type | Tutorial |
| Current Status | Phase 1 |
| Development Timeline | Start Feb 2018 :: Finish Feb 2018 |
| Application Type | Backend |
| License Type | MIT |


#### List Comprehension
List Comprehension is a very popular way in Python to produce a list in a very concise way. The idea is that sometimes we need to apply either some conditions and expressions within a for loop to produce a list object. In such case, if we donot apply list comprehension approach, we may need to write several lines of code. 


```
formula = [expression + for loop + condition]
```
Without list comprehension
```
list = []
for i in range(1,10):
  list.append(i*i)
```
With list comprehension
```
square = [x*x for i in range(1,10) if k>4]
```


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


#### Global Interpreter Lock(GIL)
The main idea behind GIL<br />
The main challenge is that CPython is not fully thread safe. So, in order to support multi-threaded Python program, CPython provides a global lock, and this global lock must be held by the current thread before it can safely access any Python object in a program. As a result, no matter how many threads are present, only one thread is being executed at a given point of time. 

Solution: PyPy implementation provides a stackless mode that can support micro-thread for massive concurrency. 



#### Series VS Dataframe

| Series | Dataframe | 
| ---- | ----- |
| Series is one-dimensional | Dataframe is two-dimentional |
| Series holds any types of data such as int, str, floating point | Dataframe is a labeled data structure with column of potential different types |


### Technical Description
Following primary Technologies/concepts were used
  - Python 2.x

### How to run
  - clone the repo
  - activate the virtual environment
  - install the required libraries from requiriement.txt
  - run individual file from scripts directory



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
