
def myFunc():
    for i in range(10):
        yield (i)


for i in myFunc():
    print(i)
