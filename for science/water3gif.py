from cmds.function import *
import numpy
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation




def get3d(list):
#設定
    Size, N, cut = 6, 500, 5 
    fps, frn = 24, 50
    x = numpy.linspace(-Size, Size, N)
    y = numpy.linspace(-Size, Size, N)
    X, Y = numpy.meshgrid(x, y)
    Z = numpy.zeros((N, N, frn))
    time = numpy.linspace(0, 2*numpy.pi, frn)


#計算
    for i in range(frn):
        Z[:, :, i] = func(X, Y, time[i],list).clip(-cut, cut)
#繪圖
    fig = plt.figure(figsize=(8, 6), dpi=100)
    ax = fig.gca(projection='3d')
    ax.set_zlim(-cut, cut)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    mappable = plt.cm.ScalarMappable(cmap='plasma')
    mappable.set_array(numpy.arange(-cut, cut, 0.1))

    def update(num):
        img[0].remove()
        img[0] = ax.plot_surface(X, Y, Z[:, :, num], cmap=mappable.cmap,
                                norm=mappable.norm, linewidth=0.5, antialiased=False, alpha=0.7)
        print(f"正在繪製 3D-{num+1} 圖")
    img = [ax.plot_surface(X, Y, Z[:, :, 0], cmap=mappable.cmap, norm=mappable.norm,
                            linewidth=0.5, antialiased=False, alpha=0.7)]
    fig.colorbar(mappable, shrink=0.8, aspect=3)
    ani = animation.FuncAnimation(fig, update, frn, interval=1000/fps)
    print("====================\n\n**開始繪製3D圖片**\n\n====================")
    ani.save('water3D.gif', writer='imagemagick', fps=fps)
    print("====================\n\n**3D圖片製作完成**\n請查看\n\n====================")