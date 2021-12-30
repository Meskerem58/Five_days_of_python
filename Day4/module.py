""" import math
# print(dir(math))
print(math.sqrt(3))
print(math.pi)
print(math.floor(9.81))  """
def get_lucky_nums(n):
    import random
    lottory= []
    for i in range(n):
        n = random.randint( 0, 10)
        lottory.append(n)
        return lottory
print(get_lucky_nums(3))

