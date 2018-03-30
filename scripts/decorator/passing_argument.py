

from functools import wraps

def mydecorator_not_actually(count):
    def true_decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            for i in range(count):
                print "Before decorated function"
            r = f(*args, **kwargs)
            for i in range(count):
                print "After decorated function"
            return r
        return wrapped
    return true_decorator

@mydecorator_not_actually(count=5)
def myfunc(myarg):
    print "my function", myarg
    return "return value"

r = myfunc('asdf')
print r
