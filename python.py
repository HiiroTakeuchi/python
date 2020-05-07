def sin(x):
    import math
    return math.sin(math.radians(x))

def cos(x):
    import math
    return math.cos(math.radians(x))

def tan(x):
    import math
    return math.tan(math.radians(x))

i = 0


while x <= 360:
    a = sin(i)
    b = cos(i)
    c = tan(i)
    print("sin{}°= {}".format(i,a))
    print("cos{}°= {}".format(i,b))
    print("tan{}°= {}".format(i,c))
    i += 15