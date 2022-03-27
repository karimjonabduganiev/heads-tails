test_seed = int(input("Create a seed number: "))

import random

test = random.randint(0,10)

if test == 1:
    print("Heads")
else:
    print("Tails")