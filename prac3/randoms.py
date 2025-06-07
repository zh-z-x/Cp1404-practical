import random

# Line 1: Random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # line 1
# What did you see on line 1? → 15
# Smallest: 5
# Largest: 20

# Line 2: Random odd number between 3 and 9 (step = 2)
print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2? → 5
# Smallest: 3
# Largest: 9
# Could line 2 have produced a 4? No

# Line 3: Random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3? → 3.1210989973174224
# Smallest: 2.5
# Largest: 5.5

# Random number between 1 and 100 (inclusive)
print(random.randint(1, 100))
#16