#!/usr/bin/env python

from numpy import *
from numpy.linalg import *
from scipy.integrate import solve_ivp
from matplotlib.pyplot import *
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.animation as ani
from matplotlib.colors import to_rgb
from tqdm import tqdm


neutral = grey_4 = to_rgb("#ced4da")
#grey_5 = to_rgb("#adb5bd")
#grey_8 = to_rgb("#343a40")
good = to_rgb("#51cf66")
bad = to_rgb("#ff6b6b")

def Q(f, xs, ys):
    X, Y = meshgrid(xs, ys)
    v = vectorize
    fx = v(lambda x, y: f([x, y])[0])
    fy = v(lambda x, y: f([x, y])[1])
    return X, Y, fx(X, Y), fy(X, Y)

def f(xy):
    x, y = xy
    dx = -2*x + y
    dy = -2*y + x
    return array([dx, dy])

ft = lambda t, y: f(y)
fps = df = 60.0
dt = 1.0 / df
t_span = t_i, t_f = (0.0, 5.0)
t = np.arange(t_i, t_f + dt, dt)

y0s = [[-4.0, 1.0], [4.0, -1.0], [1.0, 4.0], [-1.0, -4.0]]
colors = [good, good, good, good]
xys = []
for y0 in tqdm(y0s):
    r = solve_ivp(fun=ft, y0=y0, t_span=t_span, t_eval=t)
    xys.append(r.y)


fig = figure()
x = y = linspace(-5.0, 5.0, 1000)
streamplot(*Q(f, x, y), color=grey_4, zorder=-100)
plot([0], [0], lw=3.0, marker="o", ms=10.0, markevery=[-1],
        markeredgecolor="white", color=neutral)
axis("square")
axis("off")

lines = []
for x, y in xys:
    line = plot(
        [x[0]], [y[0]],
        lw=3.0, 
        ms=10.0,
        color=neutral,
        marker="o", markevery=[-1],
        markeredgecolor="white")[0]
    lines.append(line)
tight_layout()

def gamma(x):
    return pow(x, 0.5)

num_frames = len(t) * len(lines)

def update_(i):
    j, k = divmod(i, len(t)) 
    x, y = xys[j]
    line = lines[j]
    line.set_data(x[:k+1], y[:k+1])
    alpha = gamma(k / (len(t)-1))
    final_color = colors[j]
    line.set_color(
      tuple((1-alpha)*array(neutral) + alpha*array(final_color))
    )

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
animation.save("attractivity.mp4", writer=writer, dpi=300, progress_callback = lambda i, n: bar.update(1))
bar.close()

