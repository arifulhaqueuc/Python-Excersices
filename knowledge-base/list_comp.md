
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
  if i > 4:                     |         Example, values = [1,2,3,4]
    list.append(i*i)            |         d = [i*i for i in values if i>2]
print(list)                     |         print(d) ## output: [9,16]


</pre>

