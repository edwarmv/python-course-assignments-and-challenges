import math

def transform(value):
    i, x = value
    return x.upper() if i % 2 == 0 else x.lower()

def myfunc(value):
    return list(map(transform, enumerate(value)))

print(myfunc('edwar'))
