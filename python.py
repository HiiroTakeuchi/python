def sin(x):
    import math
    return math.sin(math.radians(x))

def cos(x):
    import math
    return math.cos(math.radians(x))

def tan(x):
    import math
    return math.tan(math.radians(x))

x = 0


while x <= 360:
    a = sin(x)
    b = cos(x)
    c = tan(x)
    print("sin{}°= {}".format(x,a))
    print("cos{}°= {}".format(x,b))
    print("tan{}°= {}".format(x,c))
    x += 15
