class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0


car1 = Car()
car1.name = "M3-GTR"
car1.manufacturer = "BMW"
car1.year = 2001
print(f"Car name: {car1.manufacturer} {car1.name}\nReleased year: {car1.year}\n")

car2 = Car()
car2.name = "RX-8"
car2.manufacturer = "MAZDA"
car2.year = 2002
print(f"Car name: {car2.manufacturer} {car2.name}\nReleased year: {car2.year}\n")

car3 = Car()
car3.name = "Le Mans Quattro"
car3.manufacturer = "Audi"
car3.year = 2003
print(f"Car name: {car3.manufacturer} {car3.name}\nReleased year: {car3.year}\n")

data1 = Car()
if isinstance(data1, Car):
    print(f"data1 class inherit from Car")
if isinstance(data1, object):
    print(f"data1 class inherit from object")

data2 = "Noval Agung"
if isinstance(data2, str):
    print(f"data2 class inherit from str")
if isinstance(data2, object):
    print(f"data2 class inherit from object")
