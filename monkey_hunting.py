"""
モンキーハンティングの可視化
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.8 # 重力加速度[m/s^2]
L = 10 # 弾丸と猿との直線距離
theta = np.pi/4 # 弾丸の発射角度[rad]
v0 = 10 # 弾丸の初速[m/s]
interval = 10 # 計算上の時間間隔[ms]

t = np.arange(0.0, L/v0, interval/1000)
bullet0 = [0, v0*np.sin(theta)] # 弾丸の初期条件(y, v)
monkey0 = [L*np.sin(theta), 0]  # 猿の初期条件(y, v)

def equation(var, t, g):
    dydt = var[1]
    dvdt = -g
    
    return [dydt, dvdt]

bullet = odeint(equation, bullet0, t, args = (g, )) # [弾丸の位置 弾丸の鉛直方向速度]が返る
monkey = odeint(equation, monkey0, t, args = (g, )) # [猿の位置　猿の鉛直方向速度]が返る

fig, ax = plt.subplots()
obj_bullet, = ax.plot([], [], 'o')
obj_monkey, = ax.plot([], [], '^')
ax.set_xlim(0, L*np.cos(theta)*1.2)
ax.set_ylim(0, L*np.sin(theta)*1.2)
ax.set_aspect('equal')
ax.set_title('v0 = {}, theta = {}°'.format(v0, theta*180/np.pi))

def update_anim(frame_num):
    
    obj_bullet.set_data(v0*np.cos(theta)*t[frame_num], bullet[:, 0][frame_num])
    obj_monkey.set_data(L*np.cos(theta), monkey[:, 0][frame_num])
    return obj_bullet, obj_monkey
    
    """
    obj_bullet.set_data(v0*np.cos(theta)*t[frame_num], bullet.T[0][frame_num]) # (水平方向速度*経過時間, 鉛直方向位置)
    obj_monkey.set_data(L*np.cos(theta), monkey.T[0][frame_num])
    return obj_bullet, obj_monkey
    """
    
anim = FuncAnimation(fig, update_anim, frames = np.arange(0, len(t)), interval = interval, blit = True, repeat = True)

# anim.save("monkey_hunting.gif")
plt.show()