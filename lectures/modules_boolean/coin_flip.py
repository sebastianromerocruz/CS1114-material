import random

random_decimal = random.random()  # generates a random decimal from 0.0 to 1.0, non-inclusive
result = round(random_decimal)  # rounds random_decimal to the closest integer value

print("The result of this coin flip is: " + str(result))
