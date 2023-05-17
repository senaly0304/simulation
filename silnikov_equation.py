"""
Silnikov方程式

・dxdt = y
・dydt = z
・dzdt = - az - y + bx(1 - cx - dx^2)   の3式が連立
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Silnikov方程式
def func_silnikov(var, t, a, b, c, d):
    dxdt = var[1]
    dydt = var[2]
    dzdt = -a*var[2] - var[1] + b*var[0]*(1.0 - c*var[0] - d*var[0]**2)
    
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
    #Slinkov方程式
    t_list = np.linspace(0.0, 100.0, 10000)
    a = 0.4
    b = 0.65
    c = 0.0
    d = 1.0
    var_init = [0.1, 0.1, 0.2]
    var_list = odeint(func_silnikov, var_init, t_list, args = (a, b, c, d))
    print(var_list)
    
    #可視化
    plot3d(t_list, var_list)