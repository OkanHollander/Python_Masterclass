class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 1000)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 2000)
print(hamilton.make)
print(hamilton.price)

print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")

"""
Class: template for creating objects. ALl objects created using the same class will have the same characteristics.
Object: an instance of a class
Instantiate: create an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
"""
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
