from cmds.function import *
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.animation as animation



def get2d(list):
    Size, N, cut = 6, 500, 5 
    fps, fr = 24, 50
    x = numpy.linspace(-Size, Size, N)
    y = numpy.linspace(-Size, Size, N)
    X, Y = numpy.meshgrid(x, y)
    Z = numpy.zeros((N, N, fr))
    time = numpy.linspace(0, 2*numpy.pi, fr)
#計算
    for i in range(fr):
        Z[:, :, i] = func(X, Y, time[i],list).clip(-cut, cut)
#繪圖
    Fu = plt.figure(figsize=(7, 6), dpi=100)
    A = Fu.gca()
    A.set_aspect(1.0)
    mappable = plt.cm.ScalarMappable(cmap='plasma')
    mappable.set_array(numpy.arange(-cut, cut, 0.1))

    div = make_axes_locatable(A)
    c = div.append_axes("left", size="5%", pad=0.05)
    plt.colorbar(mappable, cax=c)

    def update(num):
        img[0] = A.contourf(X, Y, Z[:, :, num], cmap=mappable.cmap, norm=mappable.norm)
        print(f"正在繪製 2D-{num+1} 圖")
    img = [A.contourf(X, Y, Z[:, :, 0], cmap=mappable.cmap, norm=mappable.norm)]
    Fu.colorbar(mappable, shrink=0.8, aspect=3)
    ai = animation.FuncAnimation(Fu, update, fr, interval=1000/fps)
    print("====================\n\n**開始繪製2D圖片**\n\n====================")
    ai.save('water2D.gif', writer='imagemagick', fps=fps)
    print("====================\n\n**2D圖片製作完成**\n請查看\n\n====================")