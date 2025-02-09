import numpy as np
from numpy.polynomial import polynomial
import matplotlib.pyplot as plt
import scipy

colors = ['blue', 'green', 'orange', 'purple', 'red']
wavelengths = {
  'blue': 465 * 10**(-9),
  'green': 520 * 10**(-9),
  'orange': 589 * 10**(-9),
  'purple': 390 * 10**(-9),
  'red': 622 * 10**(-9)
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
      current[index] = float(parts[1]) / 1000

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
    ax.set_ylabel("Current (A)")

    u_0[color_index] = intersect_x[0]
    wavelength_inv[color_index] = 1 / wavelengths[color]

plt.show()

line = polynomial.Polynomial.fit(wavelength_inv, u_0, 1).convert()
line = line.convert(domain = [min(wavelength_inv), max(wavelength_inv)]).convert()

s_2 = (1 / (len(wavelength_inv) - 2)) * sum((u_0 - line.coef[1] * wavelength_inv - line.coef[0]) ** 2)
delta_p = len(wavelength_inv) * sum(wavelength_inv ** 2) - (sum(wavelength_inv) ** 2)
slope_error = np.sqrt(len(wavelength_inv) / delta_p) * np.sqrt(s_2)
print(delta_p)
print(slope_error)
print(s_2)

space = np.linspace(min(wavelength_inv), max(wavelength_inv))
plt.plot(space, line(space), color='orange', label=f'{line.convert()}')

plt.scatter(wavelength_inv,u_0)
plt.ylabel("U_0")
plt.xlabel("1/Wavelength")
plt.legend()
plt.show()
