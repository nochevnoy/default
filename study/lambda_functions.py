def f(x):
    return str(x)[-1]

s.sort(key = f)

#Можно заменить на:
s.sort(key = lambda x: str(x)[-1])
