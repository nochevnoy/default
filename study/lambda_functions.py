def f(x):
    return str(x)[-1]

s.sort(key = f)

#Можно заменить на:

s.sort(key = lambda x: str(x)[-1])

######################################
def g(x):
    return x[::-1]
s = list(map(g, s))

#Можно заменить на:

s = list(map(lambda x: x[::-1], s))
