import numpy as np
import matplotlib.pyplot as plt

# Units: V
voltages = np.array(np.arange(2500, 5000 + 1, +500)) #+1 to include 5000
voltages_inv_sqrt = 1 / np.sqrt(voltages)

# New units: m
diameter_measured_error = 0.001

# Average inner and outer
# New format: d[0 = small, 1 = large][voltage]
diameter_measured = np.array([
    [0.026, 0.0235, 0.024, 0.022, 0.019, 0.02],
    [0.049, 0.0435, 0.04, 0.0385, 0.036, 0.035]
])

diameter_error = 100
print(diameter_measured[0][4])


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
    ax.plot(voltages_inv_sqrt, line(voltages_inv_sqrt), label=f'Trendline', linestyle='--', color='purple')
    ax.legend()

    # D_E
    d = (0.123 if size == 1 else 0.213) * 10**(-9)

    # error
    delta = sum(1 / diameter_actual_error[size]**2) * sum((voltages_inv_sqrt ** 2) / (diameter_actual_error[size] ** 2)) - sum(voltages_inv_sqrt / (diameter_actual_error[size] ** 2))**2
    slope_error = np.sqrt((1 / delta) * sum(1 / diameter_actual_error[size]**2))

    alpha = np.sqrt(2) * L * (6.63 * 10**(-34)) / (d * np.sqrt((9.1093837 * 10**(-31)) * (1.60217663 * 10**(-19))))

    ax=axs[size][1]
    ax.set_xlabel(r'$1/\sqrt{U_0}$')
    ax.set_ylabel(f'$D_E$ ({size_name}) (meters)')
    ax.set_title(r'$1/\sqrt{U_0}$ ' + f'vs $D_E$ ($\\alpha = {alpha:0.6f}$), ({size_name})')
    #ax.scatter(voltages_inv_sqrt, diameter_measured[size], label='Data')
    ax.errorbar(voltages_inv_sqrt, diameter_actual[size], fmt='o', yerr=diameter_actual_error[size], capsize=5)

    # Trendlines
    line = np.polynomial.Polynomial.fit(voltages_inv_sqrt, diameter_actual[size], deg=1)
    ax.plot(voltages_inv_sqrt, line(voltages_inv_sqrt), label=f'Trendline {line.convert()} (err {slope_error:0.4f})', linestyle='--', color='purple')
    ax.legend()

plt.show()