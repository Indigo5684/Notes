# Chapter 9 - Conservation Laws

## Section 9.1 - Continuity Equation as a Model Conservation Law

The laws of physics exhibit temporal, spatial, and angular symmetry. That is, the laws of physics do not change dependent on the time, position, and rotation of the observer. These symmetries lead to conservation of energy, momentum, and angular momentum respectively.

The conservation of chargee is another symmetry-based conservation law, derived from "gauge invariance". In this section, this is conservation law is assumed to be valid.

Recall the *continuity equation*, that is, $\frac{\partial \rho(\vb{r})}{\partial t} = - \div \vb{J}(\vb{r})$. That is, the charge density at any point in space is equal to to the divergence of the current. From this, we can integrate to find $Q(t) = \int_V \rho(\vb{r}, t) dV$, and $\frac{dQ}{dt} = -\int_{\partial V} \vb{J}(\vb{r}, t) \vdot \vu{n} dS$. This is a *local conservation law*, because it does not address situations in which charge decreases in one region and increases in another without the flow of current.

## Section 9.2 - Conservation of Electomagnetic Energy

Consider a volume $V$ with surface $\partial V$, that encloses some magnetic and electric point charges. Then, for any electric charge $q_{ei}$ or magnetic charge $q_{mj}$, the force on each charge is

$$\begin{align}
    \vb{F}_i &= q_{ei} (\vb{E}_i + \vb{v}_i \times \vb{B}_i) \\
    \vb{F}_j &= q_{mi} (\vb{H}_j - \vb{v}_j \times \vb{D}_j)
\end{align}$$

We also know that the rate at which energy changes due to changing fields is $\frac{dw_i}{dt} = \vb{F}_i \vdot \vb{v}_i$ and $\frac{dw_m}{dt} = \vb{F}_j \vdot \vb{v}_j$. This allows us to conclude that at any point $\vb{r}$ inside the volume, the rate at which the mechanical energy density changes is

$$\frac{du_{mech}}{dt} = \sum_i \delta(\vb{r} - \vb{r}_i) \vb{F}_i \vdot \vb{v}_i + \delta(\vb{r} - \vb{r}_j) \vb{F}_j \vdot \vb{v}_j$$

Since $(\vb{v}_i \times \vb{B}_i) \vdot \vb{v}_i = 0$ and $(\vb{v}_j \times \vb{D}_j) \vdot \vb{v}_j = 0$, and the current densities are given as $\vb{J}_e(\vb{r}) = \sum_i \vb{v}_i q_{ei}\delta(\vb{r} - \vb{r}_i)$ and $\vb{J}_m(\vb{r}) = \sum_j \vb{v}_j q_{mj}\delta(\vb{r} - \vb{r}_j)$, we can rewrite this as

$$\frac{du_{mech}}{dt} = \vb{J}_e(\vb{r}) \vdot \vb{E}(\vb{r}) + \vb{J}_m(\vb{r}) \vdot \vb{H}(\vb{r})$$

Combine this with the Maxwell equations to remove current densities, we see that

$$\frac{du_{mech}}{dt} = (\curl \vb{H} - \frac{\partial \vb{H}}{\partial t}) \vdot \vb{E} + (-\curl \vb{E} - \frac{\partial \vb{B}}{\partial t}) \vdot \vb{H}$$

With a vector identity, this simplifies to

$$\frac{du_{mech}}{dt} = -\curl (\vb{E} \times \vb{H})$$

**Definition**. We call $\vb{S} = \vb{E} \times \vb{H}$ the *Poynting vector*.

With this vector, we can define

$$\frac{du_{mech}}{dt} = -\curl \vb{S}$$

### Section 9.2.2 - Energy Density for Linear Materials

For a simple material, that is, one in which $\vb{D} = \epsilon \vb{E}$ and $\vb{B} = \mu \vb{H}$, we can express the rate of change of electomagnetic energy $\frac{\partial u_{em}}{\partial t}$ as $\frac{\partial u_{em}}{\partial t} = \frac{1}{2} \frac{\partial}{\partial t} (\vb{E} \vdot \vb{D} + \vb{H} \vdot \vb{B})$. After integration, we can see that $u_{em} = \frac{1}{2}(\epsilon E^2 + \mu H^2)$.

**Definition**. A material is said to be an *anisotropic linear material* if $\vb{D} = \overleftrightarrow{\vb{\epsilon}} \vdot \vb{E}$ and $\vb{B} = \overleftrightarrow{\vb{\mu}} \vdot \vb{H}$. Then, the internal electromagnetic energy becones

$$u_{em} = \frac{1}{2}(\vb{E} \vdot \overleftrightarrow{\vb{\epsilon}} \vdot \vb{E}$ and $\vb{B} + \vb{H} + \overleftrightarrow{\vb{\mu}} \vdot \vb{H}) = \frac{1}{2}\sum_{i,j}(\epsilon_{ij}E_iE_j + \mu_{ij}H_iH_j)$$

If the dyadics are symmetric, the energy functions uniquely specify the energy in terms of fields. In general, the polarization or magnetization of a material may depend on its past history and on time, and as such, the energy density for such materials cannot be expressed entirely in terms of the fields.

### Section 9.2.3 - Poynting Vector Examples

Consider a long coaxial cable, bridged by a constant voltage $V$ on one side and a resistor $R$ on the other. Then, we know that between the conductors, $\vb{H} = \frac{R}{2\pi s R}\vb{\varphi}$. Additionally, we know that

$$V=\int_a^b \vb{E} \vdot d\vb{l} = \frac{Q}{2\pi \ell \epsilon_0} \ln(\frac{b}{a}) \Rightarrow \frac{Q}{\ell} = \frac{2\pi\epsilon_0}{\ln(\frac{b}{a})} V$$

This then implies that $\vb{E} = \frac{V}{\ln(\frac{b}{a})s} \vu(s)$. We can then solve for both the energy density and Poynting vector, as well as $\vb{v} = \vb{S} / u$, the speed at which energy moves through the cable. With the impedance for a coaxial cable $Z_{C0} = \sqrt{\frac{\mu_0}{\epsilon_0}} \frac{\ln(\frac{b}{a})}{2\pi}$, we see that

$$\vb{v} = \frac{2c \vu{z}}{\frac{R}{Z_{C0}} + \frac{Z_{C0}}{R}}$$

---

Consider a long cylindrical ohmic wire of radius $a$, length $L$, and resistivity $\rho$ along the $z$-axis. If this wire is carrying a constant current $I$, we know that inside the wire, $E_z = \rho J = \rho \frac{I}{\pi a^2}$. From Ampere's Law, $H_\phi = \frac{s}{2\pi a^2} I$. Then, inside the wire,

$$\vb{S} = -s \frac{\rho I^2}{2 \pi^2 a^4} \vu{s}$$

Outside the wire, we know that $\vb{E} = \frac{\rho I}{\pi a^2} \vu{z}$ and $\vb{H} = \frac{I}{2\pi s}\vu{\varphi}$, so

$$\vb{S} = -\frac{\rho I}{\pi a^2} \frac{I}{2\pi s} \vu{s}$$

Notably, inside the wire, $\div \vb{S} = \frac{\rho I^2}{\pi^2 a^4}$, but is equal to $0$ outside of the wire.

---

Further examples are present but omitted.

## Section 9.3 - Conservation of Momentum and Maxwell Stress Tensor

We know that the rate of change of momentum for any given particle is simply the force acting on it. To calculate this, recall the force density:

$$\vb{f} = \sum_i \vb{F}_i\delta(\vb{r}-\vb{r}_i) + \sum_j \vb{F}_j\delta(\vb{r}-\vb{r}_j) = \sum_i q_{ei}\delta(\vb{r}-\vb{r}_i)(\vb{E} + \vb{v}_i \cross \vb{B}) + \sum_j q_{ej} \delta(\vb{r}-\vb{r}_i) (\vb{H} - \vb{v}_j \times \vb{D})$$

Converting to currents, we see that

$$\vb{f}(\vb{r}) = \rho_e(\vb{r})\vb{E}(\vb{r}) + \vb{J}_e(\vb{r}) \times \vb{B}(\vb{r}) + \rho_m(\vb{r}) + \vb{H}(\vb{r}) - \vb{J}_m(\vb{r}) \times \vb{D}(\vb{r})$$

Substituting in Maxwell's Equations, we see that

$$\vb{f}(\vb{r}) + \frac{\partial}{\partial t}(\vb{D} \times \vb{B}) = \epsilon_0 (\div \vb{E})\vb{E} + (\curl \vb{E})\times\vb{D} + \mu_0(\div \vb{H})\vb{H} + (\curl \vb{H})\times\vb{B}$$

Now, we claim that the right-hand side is the divergence of some tensor $\overleftrightarrow{\vb{T}}$, so that

$$\vb{f}(\vb{r}) + \frac{\partial}{\partial t}(\vb{D} \times \vb{B}) = \div \overleftrightarrow{\vb{T}}$$

This tensor is the Maxwell Stress Tensor. We claim that the divergence of this tensor is composed of both an electric and magnetic part, so that $\div \overleftrightarrow{\vb{T}} = \div \overleftrightarrow{\vb{T}}_e + \div \overleftrightarrow{\vb{T}}_m$. Then, we  can state

$$\begin{align}
\div \overleftrightarrow{\vb{T}}_e &= \epsilon_0 [(\div \vb{E})\vb{E} + (\curl \vb{E})\times \vb{E}] \\
\div \overleftrightarrow{\vb{T}}_m &= \epsilon_0 [(\div \vb{H})\vb{H} + (\curl \vb{H})\times \vb{H}]
\end{align}$$

We know that $\div(\vb{EE}) = (\div \vb{E})\vb{E} + (\vb{E} \vdot \nabla)\vb{E}$ and $\div(\overleftrightarrow{\vb{I}}f) = \grad f$. If we let $f = \frac{1}{2}\vb{E} \vdot \vb{E}$, we see that $\grad(\frac{1}{2}\vb{E} \vdot \vb{E}) = (\vb{E} \vdot \nabla)\vb{E} + (\curl \vb{E})\vb{E}$. Then, we see that

$$\begin{align}
\overleftrightarrow{\vb{T}}_e &= \epsilon_0 \vb{EE} - \frac{\epsilon_0}{2} \overleftrightarrow{\vb{I}}(\vb{E} \vdot \vb{E}) \\
\overleftrightarrow{\vb{T}}_m &= \mu_0 \vb{HH} - \frac{\mu_0}{2} \overleftrightarrow{\vb{I}}(\vb{H} \vdot \vb{H})
\end{align}$$

Knowing that $\overleftrightarrow{\vb{T}} = \overleftrightarrow{\vb{T}}_e + \overleftrightarrow{\vb{T}}_m$, and that $u = \frac{1}{2}(\epsilon_0 E^2 + \mu_0 H^2)$ is the energy density of the electromagnetic fields in a vacuum,

$$\overleftrightarrow{\vb{T}} = \epsilon_0 \vb{EE} + \mu_0 \vb{HH} - \overleftrightarrow{\vb{I}}u$$

Additionally, we denote the time rate of change of the momentum density of the electromagnetic fields as $\vb{g}(\vb{r}) = \vb{D}(\vb{r}) \times \vb{B}(\vb{r})$. Thus,

$$\vb{f}(\vb{r}) = \frac{\partial}{\partial t}\vb{g} = \div \overleftrightarrow{\vb{T}}$$

---

The Divergence Theorem states that $\int_V(\div \overleftrightarrow{\vb{T}}) dV = \int_{SofV} dS \vu{n} \vdot \overleftrightarrow{\vb{T}}$. We can prove this by expanding the left-hand side over a cube. Note that as $\overleftrightarrow{\vb{T}}$ is symmetric, $\vu{n} \vdot \overleftrightarrow{\vb{T}} = \overleftrightarrow{\vb{T}} \vdot \vu{n}$.

Given a static field, the momentum does not change in time. That is,

$$\frac{\partial}{\partial t} \vb{g} = \frac{\partial}{\partial t}(\vb{D} \times \vb{B}) = 0$$

Then, we can see that $\vb{f}(\vb{r}) = \div \overleftrightarrow{\vb{T}}$. We can thus integrate over the volume to find force on an object.

$$\vb{F} = \int_V \vb{f}(\vb{r}) dV = \int_V \div \overleftrightarrow{\vb{T}} dV = \int_{\partial V} dS \vu{n} \vdot \overleftrightarrow{\vb{T}} = \int_{\partial V} \overleftrightarrow{\vb{T}} \vdot \vu{n} dS$$
