"""
Rossler方程式

・dxdt = - y - z
・dydt = x + ay
・dzdt = b + xz - cz      の3式が成立
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Rossler方程式
def func_rosser(var, t, a, b, c):
    dxdt = -var[1] -var[2]
    dydt = var[0] + a*var[1]
    dzdt = b + var[0]*var[2] - c*var[2]
    
    return [dxdt, dydt, dzdt]

#3D可視化
def plot3d(t_list, var_list):
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_zlabel("$z$")
    ax.plot(var_list[:, 0], var_list[:, 1], var_list[:, 2])
    
    plt.show()

#メイン実行部
if(__name__ == '__main__'):
    #Rossler方程式
    t_list = np.linspace(0.0, 100.0, 10000)
    a = 0.2
    b = 0.2
    c = 5.6
    var_init = [1.0, 0.0, 0.0]
    var_list = odeint(func_rosser, var_init, t_list, args = (a, b, c))
    print(var_list)
    
    #可視化
    plot3d(t_list, var_list)