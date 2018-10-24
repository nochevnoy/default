# list comprehension
# конструктор списков

a = [ i**2 for i in range(1,10)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

a = [i**2 for i in range(1,10) if i % 2 == 0]
# [4, 16, 36, 64]

