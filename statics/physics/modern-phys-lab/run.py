import numpy as np
from numpy.polynomial import polynomial
import matplotlib.pyplot as plt
import scipy

colors = ['blue', 'green', 'orange', 'purple', 'red']
wavelengths = {
  'blue': 465,
  'green': 520,
  'orange': 589,
  'purple': 390,
  'red': 622
}

u_0 = np.empty((len(colors)))
wavelength_inv = np.empty((len(colors)))

fig, axs = plt.subplots(len(colors), sharex='all', sharey='all')
fig.tight_layout()

for color_index, color in enumerate(colors):
  with open(f'{color}.dat', 'r') as file:
    lines = file.readlines()
    lines.pop(0)

    voltage = np.empty((len(lines)))
    current = np.empty((len(lines)))
    for index, line in enumerate(lines):
      parts = line.split('\t')
      voltage[index] = float(parts[0])
      current[index] = float(parts[1])

    ## Line 1
    line_1_bound = len(lines) // 3
    line_2_bound = len(lines) - 12
    line_1 = polynomial.Polynomial.fit(voltage[1:line_1_bound], current[1:line_1_bound], 1)
    line_2 = polynomial.Polynomial.fit(voltage[line_2_bound:], current[line_2_bound:], 1)
    line_1 = line_1.convert(domain=(voltage[0], voltage[-1]))
    line_2 = line_2.convert(domain=line_1.domain)

    intersect_x = scipy.optimize.fsolve(line_1 - line_2, 0)
    intersect_y = line_1(intersect_x)

    ax = axs[color_index]
    ax.scatter(voltage, current, label="Raw Data", color=color)
    ax.set_ylim(ax.get_ylim())

    space = np.linspace(voltage[0], voltage[-1])
    ax.plot(space, line_1(space), color='red', label='Trendline 1')
    ax.plot(space, line_2(space), color='orange', label='Trendline 2')
    ax.scatter(intersect_x, intersect_y, color='pink', label=f'Intersect: {intersect_x[0]:0.3f}V')

    ax.legend()
    ax.set_title(f"Voltage v Current ({color})")
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Current (mA)")

    u_0[color_index] = intersect_y[0]
    wavelength_inv[color_index] = 1 / wavelengths[color]

plt.show()

line = polynomial.Polynomial.fit(u_0, wavelength_inv, 1)
space = np.linspace(min(u_0), max(u_0))
plt.plot(space, line(space), color='orange', label='Trendline 2')

plt.scatter(u_0, wavelength_inv)
plt.xlabel("U_0")
plt.ylabel("1/Wavelength")
plt.show()
