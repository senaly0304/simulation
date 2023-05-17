"""
1階常微分方程式（放射性崩壊）
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#1階常微分方程式（放射性崩壊）
def func_dydt(y, t):
    
    dydt = -y
    return dydt

#2D可視化
def plot2d(t_list, y_list, t_label, y_label):
    plt.xlabel(t_label) #x軸の名前
    plt.ylabel(y_label) #y軸の名前
    plt.grid() #点線の目盛りを表示
    plt.plot(t_list, y_list)
    
    plt.show()

#メイン実行部
if (__name__ == '__main__'):
    #常微分方程式（放射性崩壊）
    t_list = np.linspace(0.0, 10.0, 1000) #0~10の区間を1000等分
    y_init = 1.0 #初期値
    y_list = odeint(func_dydt, y_init, t_list)
    print(y_list)
    
    #可視化
    plot2d(t_list, y_list[:, 0], "$t$", "$y(t)$")