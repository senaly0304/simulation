"""
ばねの振動シミュレーション
f = 0, a = 0 ➡ 外力なしの普通の振動
f = 500, a = 0 ➡ 強制振動
f = 0, a = 0.3 ➡ 減衰振動
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

interval = 10 # 計算上の時間間隔[ms]
t = np.arange(0, 20, interval/1000)

k = 50 # ばね定数[N/m]
m = 0.1 # おもりの質量[kg]
w = np.sqrt(k/m)
w0 = np.sqrt(k/m) # 今回は共振を再現するためにw=w0
x0 = [0, -1*w**2*0.2] # 初期条件(v, x). おもりを釣り合いの位置から20cm離した位置からスタート
f = 0 # 外力
a = 0.3 # 減衰定数

def equation(var, t, w, f, m, w0, a):
    dxdt = var[1]
    dvdt = -w**2*var[0] + (f/m)*np.cos(w0*t) - (a/m)*var[1]
    
    return [dxdt, dvdt]

x = odeint(equation, x0, t, args = (w, f, m, w0, a))

fig,ax = plt.subplots()
image, = ax.plot([],[], 'o-', linewidth=2)
ax.set_xlim(min(x.T[1]*(-1)*m/k)*1.2,max(x.T[1]*(-1)*m/k)*1.2)
ax.set_ylim(-0.1,0.1)
ax.set_title('f={},a={}'.format(f,a))

def update_anim(frame_num):
    image.set_data([x[:, 1][frame_num]*(-1)*m/k,0],[0,0])
    
    return image,

anim = FuncAnimation(fig, update_anim,frames=np.arange(0, len(t)),interval=interval ,blit=True)
#anim.save("spring_vibration.gif")
plt.show()