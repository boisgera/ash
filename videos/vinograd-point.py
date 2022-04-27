#!/usr/bin/env python

# Python Standard Library
pass

# Third-Party Libraries
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.colors import to_rgb
from tqdm import tqdm

# Local Library
import mivp


# ------------------------------------------------------------------------------
neutral = grey_4 = to_rgb("#ced4da")
#grey_5 = to_rgb("#adb5bd")
#grey_8 = to_rgb("#343a40")
good = to_rgb("#51cf66")
bad = to_rgb("#ff6b6b")

# ------------------------------------------------------------------------------

def Q(f, xs, ys):
    X, Y = np.meshgrid(xs, ys)
    v = np.vectorize
    fx = v(lambda x, y: f([x, y])[0])
    fy = v(lambda x, y: f([x, y])[1])
    return X, Y, fx(X, Y), fy(X, Y)

# ------------------------------------------------------------------------------

# Vector field
def fun(t, xy):
    x, y = xy
    q = x**2 + y**2 * (1 + (x**2 + y**2) ** 2)
    dx = (x**2 * (y - x) + y**5) / q
    dy = y**2 * (y - 2 * x) / q
    return [dx, dy]


# Time span & frame rate
t_span = (0.0, 20.0)

fps = df = 60.0
dt = 1.0 / df
t_span = t_i, t_f = (0.0, 20.0)
t = np.arange(t_i, t_f + dt, dt)


fig = plt.figure()
x = y = np.linspace(-1.0, 1.0, 1000)
plt.streamplot(*Q(lambda xy: fun(0, xy), x, y), color=grey_4, zorder=-100)
plt.plot([0], [0], lw=3.0, marker="o", ms=10.0, markevery=[-1],
        markeredgecolor="white", color=neutral)
#plt.plot([0], [0], lw=3.0, marker="o", ms=10.0, markevery=[-1],
#        markeredgecolor="white", color=grey_4)
plt.axis("square")
plt.axis("off")



y0s = [[-0.75, 0.05], [-0.75, -0.05]]
colors = [good]*len(y0s)
xys = []
for y0 in tqdm(y0s):
    r = solve_ivp(fun=fun, y0=y0, t_span=t_span, t_eval=t)
    xys.append(r.y)

lines = []
for x, y in xys:
    line = plt.plot(
        [x[0]], [y[0]],
        lw=3.0, 
        ms=10.0,
        color=neutral,
        marker="o", markevery=[-1],
        markeredgecolor="white")[0]
    lines.append(line)
plt.tight_layout()



# Precision
rtol = 1e-9  # default: 1e-3
atol = 1e-12  # default: 1e-6

# ------------------------------------------------------------------------------

def gamma(x):
    return pow(x, 0.5)

num_frames = len(t)

def update(i):
    for j, line in enumerate(lines):
        x, y = xys[j]
        line = lines[j]
        line.set_data(x[i:i+1], y[i:i+1])
        alpha = gamma(i / (len(t)-1))
        color = "black"
        line.set_color(color)

writer = ani.FFMpegWriter(fps=fps)
animation = ani.FuncAnimation(fig, func=update, frames=num_frames)
bar = tqdm(total=num_frames)
animation.save("vinograd-point.mp4", writer=writer, dpi=300, progress_callback = lambda i, n: bar.update(1))
bar.close()



