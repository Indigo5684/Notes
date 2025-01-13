# Chapter 8 - Quasi-static Electrodynamics and Alternating Current Circuits

## Section 8.1 - The Quasi-static Regime of Electrodynamics

### Section 8.1.1 - RC Circuit - Time-dependent Circuits with Resistor and Capacitor in Series Transient Currents

Here, we have a DC voltage source followed by a switch, capacitor with capacitance $C$, and a resistor with resistance $R$.

By Kirchoff's Voltage Law, we know that $V_{cell} = V_capacitor + V_resistor$, so $V_{cell} = IR + \frac{Q}{C}$. As current is simply charge over time,

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

## Section 8.1.2 - Quasi-Static Error for a Parallel Plate Capacitor

Consider a parallel-plate capacitor. We know that within the capacitor, the electric flux is $\vb{D}(t) = \epsilon_0 \vb{E}(t)$. With the charge on a plate given by $Q(t)$, we can say that $\vb{D}(t) = \frac{Q(t)}{\pi R^2}$.

We also know by Ampere's law that $\curl \vb{H} = \frac{\partial}{\partial t} \vb{D}$. From this, given circular platFrom this, applying Stokes to Ampere's Law, we see that

$$\vb{H} = \frac{\partial Q}{\partial t} \frac{s}{2 \pi R^2} \vu    {\varphi}$$

This continues on in this manner, however the rest is omitted.

## Section 8.1.3 - Inductance

For an inductor, the voltage drop across an inductor is directly proportional to the change in current. That is,

$$\Delta V_L = L \frac{d^2Q}{dt^2} = L\frac{dI}{dt}$$

Consider a circular current loop with a voltage source in the $x-y$ plane. Then, applying Faraday's law, $\int_{circle} = (\curl \vb{E}) \cdot \vu{z} dS = -\frac{\partial}{\partial t} \int_{circle} \vb{B} \cdot \vu{z} dS$.

Apply Stokes' law to the left hand side to see that $\int_{circumference} \vb{E} \cdot d\vb{l} = -\frac{\partial \Phi_B}{\partial t}$.

With $\Phi_B = LI$, we see the "back EMF" opposing the increasing current will be $\vb{\varepsilon} = -L \frac{\partial I}{\partial t}$.

Consider a circuit with a voltage source, a switch, an inductor, and a resistor in series. Then, by KVL, $V_{cell} = L \frac{dI}{dt} + IR$.

This is a differential equation. Assuming $I(0) = 0$, we can see that

$$I(t) = \frac{V_{cell}}{R}(1 - e^{-\frac{R}{L}t})$$

Now, consider an alternating current voltage source. Then, by KVL, $V_0 \cos \omega t = R I(t) + L \frac{dI(t)}{dt}$. If we assume that current is also sinusoidal, we can say that $I(t) = I_0 \cos(\omega t + \phi)$. Substituting into the voltage expression,

$$V_0 \cos \omega t = R I_0 \cos(\omega t + \phi) + L \omega I_0 \sin(\omega t + \phi)$$

After expanding using trigonometric identities and setting coefficients to zero, we see that

$$\sin \phi = -\frac{X_L}{Z}; \cos \phi = \frac{R}{Z}; I_0 = \frac{V_0}{Z}$$

**Definition**. Here, $X_Z = \omega L$ is the *impedence* of the circuit.
