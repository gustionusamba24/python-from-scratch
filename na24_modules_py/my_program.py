a = 10
b = 15

from calculate import note
from calculate import calc_hypotenuse
from calculate import sqrt
from calculate import pow

print(note)

res = calc_hypotenuse(a, b)
print("hypotenuse:", res)

res = sqrt(a ** 2 + b ** 2)
print("hypotenuse:", res)

res = sqrt(pow(a) + pow(b))
print("hypotenuse:", res)
