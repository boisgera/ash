#!/usr/bin/env python

# Python Standard Library
pass

# Third-Party Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb


# Local Library
import mivp


# ------------------------------------------------------------------------------
grey_4 = to_rgb("#ced4da")

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

df = 60.0
dt = 1.0 / df
t = np.arange(t_span[0], t_span[1], dt)
t = np.r_[t, t_span[1]]

# Initial set boundary
y0 = [0.0, 0.0]
radius = 0.5
n = 10
xc, yc = y0


def vectorize(fun):
    return np.vectorize(fun, signature="()->(n)")


@vectorize
def boundary(s):
    if 0 <= s < 0.25:
        return np.array([-0.5 + 4 * s, 0.5])
    elif 0.25 <= s < 0.5:
        return np.array([0.5, 0.5 - 4 * (s - 0.25)])
    elif 0.5 <= s < 0.75:
        return np.array([0.5 - 4 * (s - 0.5), -0.5])
    else:
        return np.array([-0.5, -0.5 + 4 * (s - 0.75)])


# Precision
rtol = 1e-9  # default: 1e-3
atol = 1e-12  # default: 1e-6

# ------------------------------------------------------------------------------

fig = plt.figure()
x = y = np.linspace(-1.0, 1.0, 1000)
plt.streamplot(*Q(lambda xy: fun(0, xy), x, y), color=grey_4, zorder=-100)
#plt.plot([0], [0], lw=3.0, marker="o", ms=10.0, markevery=[-1],
#        markeredgecolor="white", color=grey_4)
plt.axis("square")
plt.axis("off")

data = mivp.solve_alt(
    fun=fun,
    t_eval=t,
    boundary=boundary,
    boundary_rtol=0.0,
    boundary_atol=0.05,
    rtol=rtol,
    atol=atol,
    method="LSODA",
)

mivp.generate_movie(data, filename="vinograd.mp4", axes=fig.axes[0], fps=df)
