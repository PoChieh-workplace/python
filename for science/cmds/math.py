import math

def sin(a,model):
    if(model=="R"):
        tmp = math.sin(math.degrees(a))
    else:
        tmp = math.sin(a)
    return tmp

def cos(a,model):
    if(model=="R"):
        tmp = math.cos(math.degrees(a))
    else:
        tmp = math.cos(a)
    return tmp

def tan(a,model):
    if(model=="R"):
        tmp = math.tan(math.degrees(a))
    else:
        tmp = math.tan(a)
    return tmp


def index(a,b):
    tmp = a**b
    return tmp


def abs(a):
    tmp = math.ads(a)
    return tmp

def average(i):
    tmp = 0
    for j in i:
        tmp += float(j)
    return tmp