import numpy as np
import matplotlib.pyplot as plt

# Current units: pixels
# Format: d[0 = small, 1 = large][voltage][0 = inner, 1 = outer]
diameter_measured = np.array([
    [[570, 646], [567, 725], [623, 750], [730, 866], [800, 962], [861, 1051]],
    [[968, 1090], [1034, 1147], [1036, 1183], [1311, 1461], [1405, 1624], [1476, 1600]]
])
diameter_error = 100

voltages = np.array(np.arange(5000, 2500 - 1, -500)) #-1 to include 2500
voltages_inv_sqrt = 1 / np.sqrt(voltages)

# New units: m
diameter_measured = diameter_measured / 19440
diameter_measured_error = 100 / 19440

# Average inner and outer
# New format: d[0 = small, 1 = large][voltage]
diameter_measured = np.average(diameter_measured, axis=2)

# Find actual diameter
L = 138 / 1000
r = 63 / 1000
diameter_actual = L * diameter_measured / (r + np.sqrt(r**2 - diameter_measured**2 / 4))
diameter_actual_error = (((L * (r + np.sqrt(r**2 - diameter_measured**2 / 4)) + diameter_measured**2 / (2 * np.sqrt(r**2 - diameter_measured**2 / 4)) / 2 * L)/ (r + np.sqrt(r**2 - diameter_measured**2 / 4))**2) * diameter_measured_error)

fig, axs = plt.subplots(len(diameter_measured), 2, sharex='all')
fig.tight_layout()
for size in range(len(diameter_measured)):
    ax = axs[size][0]
    size_name = 'small' if size == 0 else 'large'

    ax.set_xlabel(r'$1/\sqrt{U_0}$')
    ax.set_ylabel(f'$D_M$ ({size_name}) (meters)')
    ax.set_title(r'$1/\sqrt{U_0}$ ' + f'vs $D_M$ ({size_name})')
    #ax.scatter(voltages_inv_sqrt, diameter_measured[size], label='Data')
    ax.errorbar(voltages_inv_sqrt, diameter_measured[size], fmt='o', yerr=diameter_measured_error, capsize=5)

    # Trendlines
    line = np.polynomial.Polynomial.fit(voltages_inv_sqrt, diameter_measured[size], deg=1)
    ax.plot(voltages_inv_sqrt, line(voltages_inv_sqrt), label='Trendline', linestyle='--', color='purple')
    ax.legend()

    ax=axs[size][1]
    ax.set_xlabel(r'$1/\sqrt{U_0}$')
    ax.set_ylabel(f'$D_E$ ({size_name}) (meters)')
    ax.set_title(r'$1/\sqrt{U_0}$ ' + f'vs $D_E$ ({size_name})')
    #ax.scatter(voltages_inv_sqrt, diameter_measured[size], label='Data')
    ax.errorbar(voltages_inv_sqrt, diameter_actual[size], fmt='o', yerr=diameter_actual_error, capsize=5)

    # Trendlines
    line = np.polynomial.Polynomial.fit(voltages_inv_sqrt, diameter_actual[size], deg=1)
    ax.plot(voltages_inv_sqrt, line(voltages_inv_sqrt), label='Trendline', linestyle='--', color='purple')
    ax.legend()

plt.show()