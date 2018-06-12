
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
