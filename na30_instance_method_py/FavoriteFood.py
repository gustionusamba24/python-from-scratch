class FavoriteFood:
    def __init__(self):
        self.name = ""

    def print_name(self):
        print(self.name)

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name


food1 = FavoriteFood()
food1.set_name("seblak")
food1.print_name()
print(food1.get_name())
