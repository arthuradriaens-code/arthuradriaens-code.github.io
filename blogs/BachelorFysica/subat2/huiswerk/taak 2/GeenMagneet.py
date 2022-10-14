#Duffing oscillator
#m\ddot{x} = -\gamma\dot{x} + 2ax - 4bx^3 + F_0cos(\omega t)
# These are 2 first order 
import numpy as np
import matplotlib.pyplot as plt
import math

def Verlet(x0,v0,steps,time):
    t = np.linspace(0.,time,steps)
    dt = t[1] - t[0]
    x = np.zeros(steps)
    v = np.zeros(steps)
    x[0] = x0
    v[0] = v0
    for step in range(steps-1):
        #update x_1/2
        x_12 = x[step] + 1/2*dt*v[step]
        #update v
        v[step+1] = v[step] + dt*function1(x_12)
        #update x
        x[step + 1] = x_12 + 1/2*dt*v[step+1]
    return x,v,t

def function1(x):
    return 3.97*10**9/(x**2)
fig, (ax1, ax2) = plt.subplots(2)
x,v,t = Verlet(0.0000075,0,1000000,0.000000001)
ax1.plot(t,x,color="blue")
ax2.plot(t,v,color='red')
ax2.set_ylim(0,1000)
ax2.set_xlabel("time(s)")
ax1.set_ylabel("distance(m)")
ax2.set_ylabel("speed(m/s)")
plt.show()

