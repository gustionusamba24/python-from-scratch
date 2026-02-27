class Car:
    def __init__(self):
        self.name = ""
        self.manufacturer = ""
        self.year = 0
        self.description = ""

    def info(self):
        print(f"Car name: {self.get_name()}")
        print(f"Description: {self.description}")
        print(f"Released year: {self.year}")

    def set_details(self, **param):
        for key in param:
            if key == "name":
                self.name = param[key]
            if key == "manufacturer":
                self.manufacturer = param[key]
            if key == "year":
                self.year = param[key]
            if key == "description":
                self.description = param[key]

    def get_name(self):
        return f"{self.manufacturer} {self.name}"


all_cars = []

car1 = Car()
car1.set_details(name="Avanza", manufacturer="Toyota", year=2022, description="Mobil sejuta umat")
all_cars.append(car1)

car2 = Car()
car2.name = "Fortuner"
car2.manufacturer = "Toyota"
car2.set_details(description="Mobil SUV paling laris", year=2024)
all_cars.append(car2)

car3 = Car()
car3.name = "Agya"
car3.manufacturer = "Toyota"
car3.set_details(description="Mobil teririt di muka bumi ini", year=2020)
all_cars.append(car3)

for c in all_cars:
    c.info()
    print()
