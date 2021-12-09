import numpy
Size, N, k= 6, 500, 5
x = numpy.linspace(-Size, Size, N)
y = numpy.linspace(-Size, Size, N)
X, Y = numpy.meshgrid(x, y)
j = numpy.complex(0, 1)
def func(x, y, t, list):
    first=0
    for i in list:
        r=numpy.sqrt((x-int(i['x']))**2 + (y-int(i['y']))**2)
        tmp = (numpy.exp(j*k*r)/r)*float(i['lambda'])
        if(first==0):
            z = tmp
            first+=1
        else:
            z+=tmp
    return numpy.real(z*numpy.exp(-j*t))/2