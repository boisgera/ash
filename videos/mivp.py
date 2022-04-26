# Third-Party Libraries
import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import tqdm

# TODO: measure the error from last to first too (boundary is a closed path)

# DEPRECATED
# def solve(**kwargs):
#     kwargs = kwargs.copy()
#     kwargs["dense_output"] = True
#     y0s = kwargs["y0s"]
#     del kwargs["y0s"]
#     results = []
#     for y0 in y0s:
#         kwargs["y0"] = y0
#         result = sci.solve_ivp(**kwargs)
#         results.append(result)
#     return results


def solve_alt(**kwargs):
    kwargs = kwargs.copy()

    boundary = kwargs["boundary"]
    boundaries = None
    single = None
    if callable(boundary):
        single = True
        boundaries = [boundary]
    else:
        single = False
        boundaries = boundary
    del kwargs["boundary"]

    boundary_atol = kwargs.get("boundary_atol", 0.01)
    del kwargs["boundary_atol"]
    boundary_rtol = kwargs.get("boundary_rtol", 0.1)
    del kwargs["boundary_rtol"]
    t_eval = kwargs["t_eval"]
    kwargs["t_span"] = (t_eval[0], t_eval[-1])

    data_list = []

    for i, boundary in enumerate(boundaries):
        data = [np.zeros((2, len(t_eval)), dtype=np.float64) for _ in range(4)]

        s = list(np.linspace(0.0, 1.0, 4))
        y0s = boundary(np.array(s))
        for i, y0 in enumerate(y0s):
            kwargs["y0"] = y0
            result = sci.solve_ivp(**kwargs)
            data[i] = result.y

        while True:
            data_array = np.array(data)
            x, y = data_array[:, 0], data_array[:, 1]
            d = np.sqrt(x * x + y * y)[:, :-1]
            error = boundary_atol + boundary_rtol * d
            # compute max and index that corresponds ?
            dxdy = np.diff(data, axis=0)
            dx, dy = dxdy[:, 0], dxdy[:, 1]
            dd = np.sqrt(dx * dx + dy * dy)
            if np.all(np.amax(dd) <= error):
                break
            index_flat = np.argmax(dd)
            i, j = divmod(index_flat, np.shape(dd)[1])
            assert np.amax(dd) == dd[i, j]  # may fail when nan/infs?
            # with vinograd, np.amax(dd) may be nan if we include the origin.
            # Investigate !
            print(f"{len(data)=} {(i, j)=}", f"{np.amax(dd)=}")

            s.insert(i + 1, 0.5 * (s[i] + s[i + 1]))
            y0 = boundary(np.array([s[i + 1]]))[0]
            kwargs["y0"] = y0
            result = sci.solve_ivp(**kwargs)
            data.insert(i + 1, result.y)

        # print(np.shape(data))
        reshaped_data = np.einsum("kji", data)
        # reshaped_data is a (time_index, dim_state_space, num_points)-shaped array
        data_list.append(reshaped_data)
    if single:
        return data_list[0]
    else:
        return data_list

solve = solve_alt


# def get_data(results, t):
#     n = len(results)
#     data = np.zeros((len(t), 2, n))
#     for i, r in enumerate(results):
#         sol_t = r.sol(t)
#         data[:, :, i] = sol_t.T
#     return data


def generate_movie(data, filename, fps, dpi=300, axes=None, hook=None):
    if isinstance(data, np.ndarray):
        data = [data]
    fig = None
    if axes:
        fig = axes.get_figure()
    if not fig:
        fig = plt.figure(figsize=(16, 9))
        axes = fig.subplots()
        axes.axis("equal")
        ratio = 16 / 9
        x_max = np.amax(data[:, 0, :])
        x_min = np.amin(data[:, 0, :])
        y_max = np.amax(data[:, 1, :])
        y_min = np.amin(data[:, 1, :])

        # Create a margin
        x_c, y_c = 0.5 * (x_max + x_min), 0.5 * (y_max + y_min)
        width, height = x_max - x_min, y_max - y_min
        x_min = x_min - 0.1 * width
        x_max = x_max + 0.1 * width
        y_min = y_min - 0.1 * width
        y_max = y_max + 0.1 * width
        width, height = x_max - x_min, y_max - y_min

        if width / height <= ratio:  # adjust width
            width = height * ratio
            x_min, x_max = x_c - 0.5 * width, x_c + 0.5 * width
        else:  # adjust height
            height = width / ratio
            y_min, y_max = y_c - 0.5 * height, y_c + 0.5 * height
        axes.axis([x_min, x_max, y_min, y_max])
        fig.subplots_adjust(0, 0, 1, 1)
        axes.axis("off")

    polygons = [None] * len(data)

    def update(i):
        nonlocal polygons
        for p in polygons:
            try:
                p.remove()
            except:
                pass

        #x, y = [], []
        for j, d in enumerate(data):
            # print(f"{d = }", f"{np.shape(d)  = }")
            # print(f"{i = }")
            x = d[i][0]
            y = d[i][1]
            polygons[j] = axes.fill(x, y, color="k", zorder=1000)[0]

        if hook:
            hook(i, axes)

    writer = ani.FFMpegWriter(fps=fps)
    animation = ani.FuncAnimation(fig, func=update, frames=len(data[0]))
    bar = tqdm.tqdm(total=len(data[0]))
    animation.save(filename, writer=writer, dpi=dpi, progress_callback=lambda i, n: bar.update(1))
    bar.close()