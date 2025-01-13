# Chapter 1 - Energy in Thermal Physics

## Section 1.1 - Thermal Equilibruim

**Definition**. The *theoretical definition* for *temperature* is the quantity that is the same for two objects when in thermal equilibrium.

**Definition**. The time for a system to reach thermal equilibrium is the *relaxation time*.

**Definition**. A substance is in *diffusive equilibrium* when the composition molecules of each substance is in equilibrium.

**Definition**. A substance is in *mechanical equilibrium* if there is no net torque and no net force.

**Definition**. *Temperature* is the measure of the tendency of an object to spontaneously give up energy to its surroundings.

**Definition**. *Absolute zero* is the temperature at which the volume of an expanding gas should go to zero given constant pressure, or if volume is constant, pressure goes to zero.

**Definition**. An *absolute temperature scale* is any temperature scale at which $0$ is absolute zero.

**Definition**. The **SI absolute temperature unit** is the *kelvin*.

## Section 1.2 - The Ideal Gas

**Theorem**. Recall the *Ideal Gas Law* from chemistry, in which given $P = \text{pressure}$, $V = \text{volume}$, $n = \text{number of moles of a gas}$, $T = \text{tempreature in an absoltue scale}$, and $R = \text{the ideal gas constant}$,

$$PV = nRT$$

In SI units, $R = 8.31 \frac{\text{J}}{\text{mol} \vdot \text{K}}$.

**Definition**. Recall that one *mole* of a substance is $6.022 \cross 10^{23}$ units of said substance. This constant, $N_A$, is *Avogadro's Number*.

Using Avogadro's Number, we can rewrite the Ideal Gas law in terms of molecules, with $N = \text{number of molecules of a gas}$ and $n \vdot N_A = N$. Thus,

$$PV = NkT$$

for some constant $k = R / N_A$.

**Definition**. This constant $k = R / N_A$ is *Boltzmann's constant*.

Note that if the number of moles is constant, we can rewrite this as

$$\frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2}$$

### Microscopic Model of an Ideal Gas

Consider a piston with length $L$ with a piston area of $A$. Then, the average pressure $\overline{P}$ can be defined as

$$\overline{P} = \frac{\overline{F_{x, \text{piston}}}}{A} = - \frac{\overline{F_{x, \text{on molecule}}}}{A}$$

Now, consider some arbitrary molecule of gas with velocity $v$. Then, we can apply $F = ma$ to see

$$\overline{P} = -\frac{m\overline{a}}{A} = \frac{m\frac{\overline{\Delta v_x}}{\Delta t}}{A}$$

Now, let $\delta t = 2L / v_x$, or the time it takes for half an oscillate between the piston boundary in regards to the $x$-direction. Then, $\delta v_x = -2v_x$, as we are only considering acceleration due to the piston and not the chamber wall. Then,

$$\overline{P} = \frac{mv_x^2}{AL} = \frac{mv_x^2}{V}$$

As velocity is a distribution in an ideal gas, with $N$ as the sum of all molecules, we can rewrite this equation as

$$PV = Nm\overline{v_x^2}$$,

where $N$ is the number of molecules and $\overline{v_x^2}$ is the expected value of the square of the velocity. Now, apply the ideal gas law to see that

$$kT = m\overline{v_x^2}$$

Divide by $2$ to see that

$$\frac{1}{2} kT = \frac{1}{2} m\overline{v_x^2}$$

Summing over all directions, we see that

$$\frac{1}{2} m \overline{v^2} = \frac{1}{2} m (\overline{v_x^2} + \overline{v_y^2} + \overline{v_z^2}) = \frac{3}{2} k T$$

This is the average translational kinetic energy for an ideal gas.

**Definition**. A useful unit to measure energy on this scale is the **electron-volt** (eV), which is the kinetic energy gained by an electron that has been accelerated through a voltage difference of one volt. Note that $1 \text{eV} = 1.6 \cross 10^{-19} \text{J}$.

Note that the average speed in this model can be obtained as follows:

$$\overline{v^2} = \frac{3kT}{m}$$

Then, taking the square root results in

$$v_\text{rms} \equiv \sqrt{\overline{v^2}} = \sqrt{\frac{3kT}{m}}$$

## Section 1.3 - Equipartition of Energy

We are familar with energy in the form of $\frac{1}{2}ab_{x, y, z}^2$, where $a$ is some fixed property of an object.

**Theorem**. *Equipartition Theorem*. The average energy of any quadratic degree of freedom is $\frac{1}{2}kT$.

If an object contains $N$ molecules, each with $f$ degrees of freedom, the total (average) thermal energy is 

$$U_\text{thermal} = N \vdot f \vdot \frac{1}{2}{k}{T} $$

In monoatomic molecules, each molecule has $3$ degrees of freedom, corresponding to the translational position. In diatomics, there are $2$ additional rotational degrees of freedom.

Additionally, there exist modes of vibration, which each contribute two degrees of freedom (positional energy and vibrational kinetic energy). At room temperature, these are negligible in gasses. In solids, each atom may vibrate in three directions (as there are 3 translational axis), but atoms may not rotate, leading to $6$ total degrees of freedom.

In liquids, we are sad.
