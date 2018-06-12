class Car(object):

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car("Nissan", "silver", 88)

print (my_car.model)
print (my_car.color)
print (my_car.mpg)
