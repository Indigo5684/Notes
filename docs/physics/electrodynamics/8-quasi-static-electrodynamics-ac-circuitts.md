# Chapter 8 - Quasi-static Electrodynamics and Alternating Current Circuits

## Section 8.1 - The Quasi-static Regime of Electrodynamics

### Section 8.1.1 - RC Circuit - Time-dependent Circuits with Resistor and Capacitor in Series Transient Currents

Here, we have a DC voltage source followed by a switch, capacitor with capacitance $C$, and a resistor with resistance $R$.

By Kirchoff's Voltage Law, we know that $V_{cell} = V_{capacitor} + V_{resistor}$, so $V_{cell} = IR + \frac{Q}{C}$. As current is simply charge over time,

$$V_{cell} = R\frac{dQ}{dt} + \frac{Q}{C}$$

Assuming the capacitor is uncharged at $t = 0$, we obtain the initial condition $Q(0) = 0$. Solving the differential equation, we see that

$$Q(t) = C V_{cell} (1 - e^{-\frac{t}{RC}})$$

Then, taking the derivative, we see that

$$I = \frac{dQ}{dt} = \frac{V_{cell}}{R} e^{-\frac{t}{RC}}$$

If instead we assume an AC voltage source, we know that $V_{cell} = V_0 \cos \omega t$. Then, by KVL,

$${V_0 \cos \omega t = I(t)R + \frac{Q(t)}{C}}$$

Now, assume that $I(t) = I_0 \cos(\omega t + \phi)$, as the current may be out-of-phase with voltage. Additionally, we assume that charge cannot accumulate outside of the capacitor. Then, with $\frac{d}{dt} Q(t) = I(t)$, we see that

$$Q(t) = Q_0 + \frac{I_0}{\omega} \sin(\omega t + \phi)$$

Substituting into the formula for voltage, we see that

$$V_0 \cos \omega t = I_0 (R \cos (\omega t + \phi) + \frac{1}{\omega C} \sin(\omega t + \phi)) + \frac{Q_0}{C}$$

With trigonometric identities, this becomes

$$[V_0 - I_0 \cos \phi - \frac{I_0}{wC} \sin \phi]\cos(\omega t) + [I_0 R \sin \phi - \frac{I_0}{\omega C} \cos \phi]\sin(\omega t) + \frac{Q_0}{C} = 0$$

Now, assume let the $\frac{Q_0}{C}$ vanishes, as there is no constant charge on the capacitor (which would imply an additional constant voltage). Then, for this equation to hold true at all times, the coefficients of $\sin \omega t$ and $\cos \omega t$ must equal zero. This will allow us to see that

$$\cos \phi = \frac{R}{\sqrt{R^2 + X_C^2}}$$

**Definition**. Here, the term $X_C = (wC)^{-1}$ is the _capacitive reactance_ of the circuit.

**Definition**. We also can solve for current to see that $I_0 = \frac{V_0}{Z}$, where $Z = \sqrt{R^2 + X_C^2}$, where $Z$ is the _impedence_ of the circuit.

### Section 8.1.2 - Quasi-Static Error for a Parallel Plate Capacitor

Consider a parallel-plate capacitor. We know that within the capacitor, the electric flux is $\mathbf{D}(t) = \varepsilon_0 \mathbf{E}(t)$. With the charge on a plate given by $Q(t)$, we can say that $\mathbf{D}(t) = \frac{Q(t)}{\pi R^2}$.

We also know by Ampere's law that $\nabla \times \mathbf{H} = \frac{\partial}{\partial t} \mathbf{D}$. From this, given circular platFrom this, applying Stokes to Ampere's Law, we see that

$$\mathbf{H} = \frac{\partial Q}{\partial t} \frac{s}{2 \pi R^2} \hat{\mathbf{\varphi}}$$

This continues on in this manner, however, I've opted to skip most of the math.

The correction term $\delta E$ can be written as $\delta E = (\frac{\pi s}{Tc})^2 E_0$, where $T$ is the period of the sinusoidal current oscillations (that is, $\omega = 2\pi/T$, or $T = 2\pi / \omega$). If this is much smaller than the size of the device, the correction can be neglected.

### Section 8.1.3 - Inductance

For an inductor, the voltage drop across an inductor is directly proportional to the change in current. That is,

$$\Delta V_L = L \frac{d^2Q}{dt^2} = L\frac{dI}{dt}$$

Consider a circular current loop with a voltage source in the $x-y$ plane. Then, applying Faraday's law, $\int_{circle} = (\nabla \times \mathbf{E}) \cdot \hat{\mathbf{z}} dS = -\frac{\partial}{\partial t} \int_{circle} \mathbf{B} \cdot \hat{\mathbf{z}} dS$.

Apply Stokes' law to the left hand side to see that $\int_{circumference} \mathbf{E} \cdot d\mathbf{l} = -\frac{\partial \Phi_B}{\partial t}$.

With $\Phi_B = LI$, we see the "back EMF" opposing the increasing current will be $\mathbf{\mathcal{E}} = -L \frac{\partial I}{\partial t}$.

Consider a circuit with a voltage source, a switch, an inductor, and a resistor in series. Then, by KVL, $V_{cell} = L \frac{dI}{dt} + IR$.

This is a differential equation. Assuming $I(0) = 0$, we can see that

$$I(t) = \frac{V_{cell}}{R}(1 - e^{-\frac{R}{L}t})$$

Now, consider an alternating current voltage source. Then, by KVL, $V_0 \cos \omega t = R I(t) + L \frac{dI(t)}{dt}$. If we assume that current is also sinusoidal, we can say that $I(t) = I_0 \cos(\omega t + \phi)$. Substituting into the voltage expression,

$$V_0 \cos \omega t = R I_0 \cos(\omega t + \phi) + L \omega I_0 \sin(\omega t + \phi)$$

After expanding using trigonometric identities and setting coefficients to zero, we see that

$$\sin \phi = -\frac{X_L}{Z}; \cos \phi = \frac{R}{Z}; I_0 = \frac{V_0}{Z}$$

**Definition**. Here, $X_Z = \omega L$ is the _impedence_ of the circuit.

### Section 8.1.4 - Calculation of Inductance

Recall that the back EMF $\mathbf{\mathcal{E}} = -L \frac{\partial I}{\partial T}$. We can calculate the work done by this force as follows.

$$\frac{dW}{dt} = I(\mathbf{\mathcal{E}}) = IL \frac{dI}{dt} = \frac{1}{2} L \frac{d}{dt}(I^2)$$

Then, integrating both sides, we see that

$$W = \frac{1}{2}L\int_0^{I^2(t)} I^2(t') dt' = \frac{1}{2}LI^2$$

We also know from Section 3.2 that the work needed to create a magnetic field is as follows.

$$W = \frac{1}{2} \mu_0 \int_V H^2 dV$$

Now, consider a long air-filled solenoid with $n$ turns per unit length and cross-sectional area $A$. Then, we know the flux through a cross-section of the solenoid will be $\Phi = BA = \mu_0 n I A$. Then, the back-EMF for one loop of the solenoid can be given by $\mathbf{\mathcal{E}}_{1 loop} = - \frac{d\Phi}{dt} = -\mu_0 n A \frac{dI}{dt}$. Then, the total induced EMF will be $\mathbf{\mathcal{E}} = nl\mathbf{\mathcal{E}}_{1 loop}$, where $l$ is the length of the solenoid. Thus, by the definition of back-EMF,

$$\mathbf{\mathcal{E}} = -nl \mu_0 nA \frac{dI}{dt} = -L\frac{dI}{dt}$$

So, $L = \mu_0 n^2 Al$

We can also compute thsi by energy. We know that $W = \frac{1}{2} \mu_0 \int_V H^2 dV = \frac{1}{2} \mu_0 n^2 I^2 Al = \frac{1}{2}LI^2$. This simplifies immediately.

Now, consider a coaxial cable. That is, consider a solid cylinder of radius $a$ that conducts current in the $+z$ direction. The circuit is completed by a thin cylindical shell outside of the conductor yet still with radius $a$. We also assume that current density is uniform within the cylindrical conductor.

Recall that from Ampere's Law, for $s \in (0, a)$, we have $\mathbf{H}(s) = \frac{I_enc}{2\pi s}\hat{\mathbf{\varphi}}$, with $I_enc = \frac{I\pi s^2}{\pi a^2}$. Thus, $\mathbf{H} = \frac{Is}{2\pi a^2}\hat{\mathbf{\varphi}}$. Then,

$$W = \frac{1}{2} \mu_0 \int_V H^2 dV = \frac{1}{2} \mu_0 l \int_0^a 2\pi s ds (\frac{Is}{2\pi a^2})^2 = \frac{I^2}{2} \frac{\mu_0 l}{2\pi} \frac{1}{4}$$

This implies that $L = \frac{\mu_0 l}{8\pi}$.

We can also solve this via flux. We know that $\mathbf{B}(s) = \frac{u_0 Is}{2\pi a^2}\hat{\mathbf{\varphi}}$. Then,

$$\Phi = \int_0^a \mathbf{B} \cdot \hat{\mathbf{n}} dS = \int_0^a \frac{\mu_0 Is}{2\pi a^2} l ds = \frac{\mu_0 I l}{2\pi} \frac{1}{2}$$

This is off by a factor of $2$. Instead, multiply by a fator of $f(s) = \frac{s^2}{a^2}$ to see

$$\Lambda = LI = \int_0^a \frac{\mu_0 I s^3}{2\pi a^4} l ds = \frac{\mu_0 I l}{2\pi} \frac{1}{4}$$

Note that due to the Skin Effect, at high frequencies, back EMF must be considered even inside the conductor.

This becomes complicated, and is thus omitted.

### Section 8.1.5 - Quasi-static Error for a Solenoidal Inductor

In section 5.2, we learned that in a long solenoid, $\mathbf{H} = nI \mathbf{z}$, where $I$ is the current and $n$ the number of turns per uniut length. This, however, was dependent of the current being constant. Now, let current be represented as $I(t) = I_0 \cos (\omega t + \phi)$. Now, $\mathbf{H}(t) = nI(t) \hat{\mathbf{z}}$.

This implies magnetic flux with a density of $\mathbf{B} = \mu_0 n I(t) \hat{\mathbf{z}}$. Given the inductor with radius $s$, this will cause changing flux $\Phi_B(t) = \mathbf{B} * A = \mu_0 n I(t) \pi s^2$.

By Faraday's Law,

$$E_{induced} = -N \frac{\partial \Phi_B}{\partial{t}}$$

This can be rearranged to see

$$2\pi s \mathbf{E}_{induced}(t) = -\frac{\partial \Phi_b(t)}{\partial t} = -\mu_0 n \pi s^2 \frac{\partial}{\partial t} I(t)$$

This can be used to find $\mathbf{E} = -\mu_0 n \frac{s}{2} \frac{\partial}{\partial t}I(t) \hat{\mathbf{\varphi}}$, equivalent to a flux density $\mathbf{D}(t) = -\varepsilon_0 \mu_0 n \frac{s}{2} \frac{\partial}{\partial t}I(t) \hat{\mathbf{\varphi}}$. We can then apply Ampere's law to see that

$$\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}(t)}{\partial t} = -\varepsilon_0 \mu_0 n \frac{s}{2} \frac{\partial^2}{\partial t^2}I(t) \hat{\mathbf{\varphi}}$$

We can work backwards to find that $\mathbf{H}(s, t) = (1 - \frac{\mu_0 \varepsilon_0 s^2 \omega^2}{4}) H_{z0}(t)\hat{\mathbf{z}}$. Then, the same conditions should apply as in 8.1.2. That is, $\omega$ should be low enough or the d evice small enough that light can easily propagate across the device during one period of oscillation.

## Section 8.2 - Circuits with Resistance, Capacitance and Inductance and a Sinusoidal EMF

### Section 8.2.1 - RLC Circuits

Consider an AC voltage source, a resistor with resistance $R$, inductor with inductance $L$, and capacitor with capacitance $C$ all in series. Then, by KVL,

$$V(t) = RI(t) + \frac{Q(t)}{C} + L \frac{dI}{dt}$$

Then, with $I(t) = I_0 \cos(\omega t + \phi)$, we can see that with inductive reactance $X_L = \omega L$ and capactive reactance $X_C = (\omega C)^{-1}$,

$$I_0 = \frac{V_0}{Z}; \sin \phi = \frac{X_C - X_L}{Z}; \cos \phi = \frac{R}{Z}; Z = \sqrt{R^2 + (X_C - X_L)^2}$$

**Definition**. The quantity $Z$ is the *impedence* of the circuit.

**Definition**. The *resonance frequency* is the frequency at which $X_C = X_L$. This occurs only at $\omega_0 = 1 / \sqrt{LC}$. Notably, the impedence equals the resistance ($Z = R$) and the current is in-phase with voltage ($\phi = 0$).

The instantaneous power delivered by the circuit is

$$P(t) = V(t)I(t) = V_0 \cos(\omega t) \frac{V_0}{Z(\omega)}\cos(\omega t + \phi)$$

Averaged over one cycle ($T = 2\pi / \omega$),

$$\langle P(t) \rangle = \frac{V_0^2}{Z(\omega)} \frac{1}{T} \int_0^T \cos(\omega t) [ \cos(\omega t)\cos\phi - \sin(\omega t)\sin\phi] dt = \frac{V_0^2}{2Z(\omega)}\cos\phi$$

Note that $\cos\phi$ = $R/Z$, so

$$\langle P(t) \rangle = \frac{1}{2} \frac{V_0^2R}{Z^2(\omega)}$$

Recall that the charactaristic times for a capacitor and inductor to charge are $T_C = RC$ and $T_L = L/R$. Then,

$$\langle P(t) \rangle = \frac{1}{2} \frac{V_0^2}{r} \frac{1}{1 + (\omega T_l - (\omega T_c)^{-1})^2}$$

This has a clear maximum of $\frac{1}{2} \frac{V_0^2}{R}$ for the frequency $\omega T_L = \frac{1}{\omega T_C}$, when $\omega_0 = 1/\sqrt{LC}$.

The width of the resonance, or the range of angular frequencies over which $\frac{R^2}{Z^2(\omega)}$ is greater than half its peak value, is given by $\Delta \omega = \frac{1}{T_L} = \frac{L}{R} = \omega_0^2 T_C$.

Note that all power dissipation happens over the resistor, not the inductor or capacitor.

Now, consider a circuit in which the resistor, inductor, and capacitor are all in parallel. By KVL,

$$V_0 \cos(\omega t) = RI_R(t) = L \frac{dI_L(t)}{dt} = \frac{Q_C(t)}{C}$$

With currents given as $I_R(t) = I_{R0} \cos(\omega t + \phi_R)$, $I_L(t) = I_{L0} \cos(\omega t + \phi_L)$, and $I_C(t) = I_{C0} \cos(\omega t + \phi_C)$, we obtain

$$
\begin{array}{ccc}
    I_{R0} = \frac{V_0}{R} & I_{L0} = \frac{V_0}{\omega L} & I_{C0} = V_0 \omega C \\
    \phi_R = 0 & \phi_L = -\pi / 2 & \phi_C = \pi/2
\end{array}
$$

The total current them becomes $I(t) = \frac{V_0}{R} \cos(\omega t) + V_0(\frac{1}{X_L} - \frac{1}{X_C})\sin(\omega t)$. Additionally, $\langle P(t) \rangle = \frac{1}{2} \frac{V_0^2}{R}$.

### Section 8.2.2 - Applications

The voltage across the capacitor is higher than the voltage across the capacitor for frequencies less than the resonance frequency. The inverse holds for frequencies greater than the resonance frequency. This can be proved by computing $V_C / V_0 = R / Z(\omega)$ and $V_L / V_0 = \omega L / Z(\omega)$.

To eliminate high frequencies, take the voltage across the capacitor. Otherwise, take the voltage across the resistor.

These circuits can also be used in tuners by taking the voltage across the resistorr.

### Section 8.2.3 - Energy in Inductors and Capacitors

We know the energy in an electromagnetic field is

$$u = \frac{1}{2}(\varepsilon_0 e^2 + \mu_u H^2)$$

In a capacitor, we cannot directly state the energy. However, we can state its rate of change:

$$\frac{du_E}{dt} = \mathbf{E} \cdot \frac{d\mathbf{D}}{dt}$$

In the case where $\mathbf{D} = \varepsilon \mathbf{E}$, that is, in the presence of a simple dielectric,

$$u_E = \frac{1}{2} \varepsilon E^2 = \frac{1}{2}\mathbf{E} \cdot \mathbf{D}$$

This is mirrored in solenoids / inductors, where

$$\frac{du_M}{dt} = \mathbf{H} \cdot \frac{d\mathbf{B}}{dt}$$

In the case where $\mathbf{B} = \mu \mathbf{H}$, that is, in the presence of a simple magnetic material,

$$u_M = \frac{1}{2}\mathbf{H} \cdot \mathbf{B}$$

Lastly, this continues for electromagnetic fields.

$$\frac{du_{EM}}{dt} = \mathbf{E} \cdot \frac{d\mathbf{D}}{dt} + \mathbf{H} \cdot \frac{d\mathbf{B}}{dt}$$

In simple electromagnetic materials, we see that

$$u_{EM} = \frac{1}{2}(\mathbf{E} \cdot \mathbf{D} + \mathbf{H} \cdot \mathbf{B}) = \frac{1}{2}(\varepsilon E^2 + \mu H^2)$$
