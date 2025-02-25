import random

def r():
 random_set = set(random.randint(15, 45) for _ in range(10))
 print("Original Set:", random_set)

 count_less_than_30 = sum(1 for num in random_set if num < 30)
 print("\n Numbers less than 30:", count_less_than_30)

 random_set = {num for num in random_set if num <= 35}
 print("\n Set after deletion:", random_set)

r()