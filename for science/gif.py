import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

"""
設定
"""
def getgif(list):
    L, sep, N, k, cut = 6, 3, 500, 5, 5 
    fps, frn = 24, 50
    x = np.linspace(-L, L, N)
    y = np.linspace(-L, L, N)
    X, Y = np.meshgrid(x, y)
    j = np.complex(0, 1)

    """
    計算
    """
    def func(x, y, t):
        first=0
        for i in list:
            r=np.sqrt((x-int(i['x']))**2 + (y-int(i['y']))**2)
            tmp = np.exp(j*k*r)/r
            if(first==0):
                z = tmp
                first+=1
            else:
                z+=tmp
        return np.real(z*np.exp(-j*t))/2

    Z = np.zeros((N, N, frn))
    T = np.linspace(0, 2*np.pi, frn)

    for i in range(frn):
        Z[:, :, i] = func(X, Y, T[i]).clip(-cut, cut)

    """
    繪圖
    """
    fig = plt.figure(figsize=(8, 6), dpi=100)
    ax = fig.gca(projection='3d')
    ax.set_zlim(-cut, cut)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    mappable = plt.cm.ScalarMappable(cmap='plasma')
    mappable.set_array(np.arange(-cut, cut, 0.1))
    def update(frame_number):
        plot[0].remove()
        plot[0] = ax.plot_surface(X, Y, Z[:, :, frame_number], cmap=mappable.cmap,
                                norm=mappable.norm, linewidth=0.5, antialiased=False, alpha=0.7)
    plot = [ax.plot_surface(X, Y, Z[:, :, 0], cmap=mappable.cmap, norm=mappable.norm,
                            linewidth=0.5, antialiased=False, alpha=0.7)]

    fig.colorbar(mappable, shrink=0.8, aspect=3)
    ani = animation.FuncAnimation(fig, update, frn, interval=1000/fps)
    print("====================\n\n**正在製作圖片**\n\n====================")
    ani.save('Two3D.gif', writer='imagemagick', fps=fps)
    print("====================\n\n**圖片製作完成**\n請查看\n\n====================")
    #plt.show()