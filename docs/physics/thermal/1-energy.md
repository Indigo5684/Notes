# Chapter 1 - Energy in Thermal Physics

## Section 1.1 - Thermal Equilibrium

**Definition**. The *theoretical definition* for *temperature* is the quantity that is the same for two objects when in thermal equilibrium.

**Definition**. The time for a system to reach thermal equilibrium is the *relaxation time*.

**Definition**. A substance is in *diffusive equilibrium* when the composition molecules of each substance is in equilibrium.

**Definition**. A substance is in *mechanical equilibrium* if there is no net torque and no net force.

**Definition**. *Temperature* is the measure of the tendency of an object to spontaneously give up energy to its surroundings.

**Definition**. *Absolute zero* is the temperature at which the volume of an expanding gas should go to zero given constant pressure, or if volume is constant, pressure goes to zero.

**Definition**. An *absolute temperature scale* is any temperature scale at which $0$ is absolute zero.

**Definition**. The **SI absolute temperature unit** is the *kelvin*.

## Section 1.2 - The Ideal Gas

**Theorem**. Recall the *Ideal Gas Law* from chemistry, in which given $P = \text{pressure}$, $V = \text{volume}$, $n = \text{number of moles of a gas}$, $T = \text{temperature in an absolute scale}$, and $R = \text{the ideal gas constant}$,

$$PV = nRT$$

In SI units, $R = 8.31 \frac{\text{J}}{\text{mol} \cdot \text{K}}$.

**Definition**. Recall that one *mole* of a substance is $6.022 \times 10^{23}$ units of said substance. This constant, $N_A$, is *Avogadro's Number*.

Using Avogadro's Number, we can rewrite the Ideal Gas law in terms of molecules, with $N = \text{number of molecules of a gas}$ and $n \cdot N_A = N$. Thus,

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

**Definition**. A useful unit to measure energy on this scale is the **electron-volt** (eV), which is the kinetic energy gained by an electron that has been accelerated through a voltage difference of one volt. Note that $1 \text{eV} = 1.6 \times 10^{-19} \text{J}$.

Note that the average speed in this model can be obtained as follows:

$$\overline{v^2} = \frac{3kT}{m}$$

Then, taking the square root results in

$$v_\text{rms} \equiv \sqrt{\overline{v^2}} = \sqrt{\frac{3kT}{m}}$$

## Section 1.3 - Equipartition of Energy

We are familiar with energy in the form of $\frac{1}{2}ab_{x, y, z}^2$, where $a$ is some fixed property of an object.

**Theorem**. *Equipartition Theorem*. The average energy of any quadratic degree of freedom is $\frac{1}{2}kT$.

If an object contains $N$ molecules, each with $f$ degrees of freedom, the total (average) thermal energy is

$$U_\text{thermal} = N \cdot f \cdot \frac{1}{2}{k}{T} $$

In monoatomic molecules, each molecule has $3$ degrees of freedom, corresponding to the translational position. In diatomic gasses, there are $2$ additional rotational degrees of freedom.

Additionally, there exist modes of vibration, which each contribute two degrees of freedom (positional energy and vibrational kinetic energy). At room temperature, these are negligible in gasses. In solids, each atom may vibrate in three directions (as there are 3 translational axis), but atoms may not rotate, leading to $6$ total degrees of freedom.

In liquids, we are sad.

## Section 1.4 - Heat and Work

We are familiar with energy, temperature, and work.

**Theorem**. The Law of Conservation of Energy. Energy cannot be created or destroyed, only moved.

**Theorem**. In thermodynamics, energy may only enter or leave a closed system via *heat* and *work*.

**Definition**. *Heat* is any spontaneous flow of energy between two objects due to a difference in temperature.

**Definition**. *Work* is any other flow of energy in or out of a system.

With $U$ being the total energy of a system, we can write

$$\Delta U = Q + W$$

That is, the change in total energy of a system is equal to the heat being added to the system and work done on the system.

Note that with heat engines, we often see $Q - W$, where $W$ instead represents the work done by the system.

**Theorem**. The First Law of Thermodynamics. $\Delta U = Q + W$, along with the Law of Conservation of Energy. In  other words, you can't win the game.

**Definition**. The SI unit of energy is the *Joule*, where $1J = 1 \text{kg} \cdot \text{m}^2 / \text{s}^2$.

**Definition**. The imperial unit of energy is the *calorie*, or the amount of energy to heat one gram of water by $1 \degree \text{C}$. The exact conversion factor is defined as $1 \text{J} = 4.184 \text{cal}$

**Definition**. *Conduction* is the transfer of heat by molecular contact, in which fast moving molecules bump into slow moving molecules and transfer energy.

**Definition**. *Convection* is the transfer of heat by the bulk motion of a liquid or gas.

**Definition**. *Radiation* is the transfer of heat via electromagnetic waves.

## Section 1.5 - Compression Work

From classical mechanics, we know that $W = \vec{F} \cdot d\vec{r}$.

Consider a piston with a compressible gas. In this case, with $\Delta x$ positive as the piston moves inwards, we can state that $W = F \Delta x$. Now, we want the gas to always maintain internal equilibrium. For this to be true, the piston must be moving relatively slowly. Note that any volume change that happens in this way is said to be *quasistatic*.

We know that the force exerted by the piston is equal to the pressure times the area. Thus, $W = P A \Delta  x$. But $A\Delta x$ is just volume (in this case, negative, as volume is decreasing). So, $W = -P \Delta V$.

However, this assumes constant pressure. For a non-constant pressure, $P(V)$, we know that $W = \int F dx = - \int P(V) dV$.

**Definition**. In *isothermal compression*, we see that $\delta T = 0$. Then, $T$ is a constant, so $nRT$ is constant meaning $PV$ is constant. Then, as $P(V) = (P_0V_0)/(V)$, we can see that $W = \int_{V_1}^{V_2} P(V) dV = nRT \ln(V_i/V_f) = PV \ln(P_f/P_i)$

**Definition**. The line formed by isothermal compression on a $PV$-diagram is called an *isotherm*.

**Definition**. In *adiabatic compression*, we assume that $Q = 0$. Then, we see that $PV^\gamma$ is constant, with $\gamma$ being the adiabatic constant. Note that as $U = \frac{f}{2}NkT = W$, we can see that $V_2 T_2^{f/2} = V_1 T_1^{f/2}$, and \$gamma = (f+2)(f)$. Additionally, we see that $W$ = $\frac{P_2 V_2 - P_1 V_1}{1-\gamma}$

## Section 1.6 - Heat Capacity

**Definition**. The *heat capacity* $C = Q / \Delta T$ of an object is the energy required to raise its temperature by one degree.

**Definition**. The *specific heat capacity* $c = C / m = C / (m \Delta T)$ is the energy needed to raise a substance by one degree per unit mass.

In a system, we can note that

$$C = \frac{Q}{\Delta T} = \frac{\Delta U - W}{\Delta T}$$

Consider the case in which volume is constant. Under these circumstances, we can calculate the *heat capacity at constant volume*, and as volume does not change, $W = 0$, so

$$C_V = (\frac{\Delta U}{\Delta T})_V = (\frac{\partial U}{\partial T})_V$$

In the case where pressure is constant instead, we see that the *heat capacity at constant pressure* is defined as

$$C_P = (\frac{\Delta U}{\Delta T})_V = (\frac{\Delta  U - (- P \Delta V)}{\Delta T})_P = (\frac{\partial U}{\partial T})_P + P (\frac{\partial V}{\partial T})_P$$

Knowing that $U = \frac{1}{2}NfkT$, we can see that $C_V = \frac{NfK}{2}$.

**Theorem**. The *Rule of Dulong and Pitt* states that in solids, $f = 6$, so the heat capacity per mole is $3R$. In reality, all degrees of freedom freeze out as $T$ approaches $0$, so $C$ approaches $0$.

For an ideal gas, at constant pressure,

$$(\frac{\partial V}{\partial T})_P = \frac{\partial}{\partial T} (\frac{NkT}{P}) = \frac{Nk}{P}$$

So, $C_P = C_V + Nk = C_V + nR$.

---

There are times when heat can be added without increasing the temperature at all, such as during a *phase transformation*. Then,

**Definition**. The *latent heat* $L$ of an object is the energy required to melt or boil a substance completely. We can also define *specific latent heat* $l$ as

$$l = \frac{L}{m} = \frac{Q}{m}$$

Note that during this, we assume the pressure is constant and no other work is done aside from constant-pressure volume change. Additionally, the latent heat for freezing and boiling does not have to be (and almost never is) equal.

 **Definition**. We define *enthalpy*, $H$, as the total energy needed to create any given system out of nothing in a set environment, and is defined as

$$H = U + PV$$

This can also be interpreted as the maximum possible energy extracted from annihilating the system, consisting of the system's internal energy $U$ and the work $PV$ done by the atmosphere to fill its absence.

In a system, if the pressure is held constant, we see that $\Delta H = \Delta U + P \Delta V$. Thus, enthalpy can only increase due to expansion or internal energy changes. From the First Law of Thermodynamics, $\Delta H = Q + W_{other}$ if pressure is constant. Notably, the change in enthalpy per degree of temperature at a constant pressure is the same as the heat capacity at constant pressure $C_P$.

**Definition**. The *Enthalpy of Formation* is the energy needed to create a compound or undergo a phase transition from base constituents in their most stable states.

## Section 1.7 - Rates of Processes

Skipped.
