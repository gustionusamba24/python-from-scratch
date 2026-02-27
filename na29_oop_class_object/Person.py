class Person:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""


person1 = Person()
print(f"instance object: {person1}")
print(f"type: {type(person1).__name__}")
