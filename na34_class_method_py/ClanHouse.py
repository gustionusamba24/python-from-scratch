class ClanHouse:

    def __init__(self, name="", house=""):
        self.name = name
        self.house = house

    @classmethod
    def create(cls, name="", house=""):
        obj = cls()
        obj.name = name
        obj.house = house
        return obj

    def info(self):
        print(f"{self.name} of {self.house}")


p1 = ClanHouse()
p1.name = "Paul Atriedes"
p1.house = "House of Atriedes"
p1.info()
# output ➜ Paul Atriedes of House of Atriedes

p2 = ClanHouse("Lady Jessica", "Bene Gesserit")
p2.info()
# output ➜ Lady Jessica of Bene Gesserit

p3 = ClanHouse.create()
p3.name = "Baron Vladimir Harkonnen"
p3.house = "House of Harkonnen"
p3.info()
# output ➜ Baron Vladimir Harkonnen of House of Harkonnen

p4 = ClanHouse.create("Glossu Rabban", "House of Harkonnen")
p4.info()
# output ➜ Glossu Rabban of House of Harkonnen
