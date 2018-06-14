
def me(**kwargs):
    for key, value in kwargs.items():
        print("{0}=={1}". format(key, value))

me(name="Rahim", ID=18)
me(name="Ariful", age=109)
me(age=10)
