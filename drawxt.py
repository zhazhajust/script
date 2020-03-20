import numpy as np
import matplotlib.pyplot as plt
import sdf
plt.switch_backend('agg')
c       =  3e8
micron  =  1e-6
gridnumber = 2400
stop    =  17000
dt_snapshot= 1e-15
x_end   =  60 * micron
x_max   =  60 * micron
x_min   =  0 * micron
window_start_time =  (x_max - x_min) / c
delta_x =  x_end/gridnumber
t_end   =  stop * dt_snapshot
if t_end-window_start_time<0:
      xgrid   =  int(gridnumber)
else:
      xgrid   =  int(gridnumber + c*(t_end-window_start_time)/delta_x)
t=np.loadtxt('t.txt')
xt=np.loadtxt('xt.txt')
x=np.arange(xgrid+1)

Xt=xt.T
fig,ax=plt.subplots()
im=ax.pcolormesh(Xt,cmap=plt.get_cmap('rainbow'))
fig.colorbar(im,ax=ax)

fig.savefig('Xt.png',dpi=200)
