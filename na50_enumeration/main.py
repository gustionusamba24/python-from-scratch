"""
    Enumeration adalah nilai konstan yang umumnya disiapkan untuk merepresentasikan sekumpulan data konstan yang konteksnya masih sama.
"""
from enum import Enum
class City(Enum):
    MALANG = 1
    YOGYAKARTA = 2
    SURABAYA = 3
    BANDUNG = 4

print(list(City))

city1 = City.YOGYAKARTA
print(city1)

print(f"name {city1.name}")
print(f"value {city1.value}")
