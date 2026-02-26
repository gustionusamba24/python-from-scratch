print("from my_program.py:", __name__)

import calculate

import random

num = random.randint(0, 1000)
calculate.is_prime(num)
