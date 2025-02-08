# Chapter 9 - Conservation Laws

## Section 9.1 - Continuity Equation as a Model Conservation Law

The laws of physics exhibit temporal, spatial, and angular symmetry. That is, the laws of physics do not change dependent on the time, position, and rotation of the observer. These symmetries lead to conservation of energy, momentum, and angular momentum respectively.

The conservation of chargee is another symmetry-based conservation law, derived from "gauge invariance". In this section, this is conservation law is assumed to be valid.

Recall the *continuity equation*, that is, $\frac{\partial \rho(\mathbf{r})}{\partial t} = - \nabla \cdot \mathbf{J}(\mathbf{r})$. That is, the charge density at any point in space is equal to to the divergence of the current. From this, we can integrate to find $Q(t) = \int_V \rho(\mathbf{r}, t) dV$, and $\frac{dQ}{dt} = -\int_{\partial V} \mathbf{J}(\mathbf{r}, t) \cdot \hat{\mathbf{n}} dS$. This is a *local conservation law*, because it does not address situations in which charge decreases in one region and increases in another without the flow of current.

## Section 9.2 - Conservation of Electomagnetic Energy

Consider a volume $V$ with surface $\partial V$, that encloses some magnetic and electric point charges. Then, for any electric charge $q_{ei}$ or magnetic charge $q_{mj}$, the force on each charge is

$$\begin{align}
    \mathbf{F}_i &= q_{ei} (\mathbf{E}_i + \mathbf{v}_i \times \mathbf{B}_i) \\
    \mathbf{F}_j &= q_{mi} (\mathbf{H}_j - \mathbf{v}_j \times \mathbf{D}_j)
\end{align}$$

We also know that the rate at which energy changes due to changing fields is $\frac{dw_i}{dt} = \mathbf{F}_i \cdot \mathbf{v}_i$ and $\frac{dw_m}{dt} = \mathbf{F}_j \cdot \mathbf{v}_j$. This allows us to conclude that at any point $\mathbf{r}$ inside the volume, the rate at which the mechanical energy density changes is

$$\frac{du_{mech}}{dt} = \sum_i \delta(\mathbf{r} - \mathbf{r}_i) \mathbf{F}_i \cdot \mathbf{v}_i + \delta(\mathbf{r} - \mathbf{r}_j) \mathbf{F}_j \cdot \mathbf{v}_j$$

Since $(\mathbf{v}_i \times \mathbf{B}_i) \cdot \mathbf{v}_i = 0$ and $(\mathbf{v}_j \times \mathbf{D}_j) \cdot \mathbf{v}_j = 0$, and the current densities are given as $\mathbf{J}_e(\mathbf{r}) = \sum_i \mathbf{v}_i q_{ei}\delta(\mathbf{r} - \mathbf{r}_i)$ and $\mathbf{J}_m(\mathbf{r}) = \sum_j \mathbf{v}_j q_{mj}\delta(\mathbf{r} - \mathbf{r}_j)$, we can rewrite this as

$$\frac{du_{mech}}{dt} = \mathbf{J}_e(\mathbf{r}) \cdot \mathbf{E}(\mathbf{r}) + \mathbf{J}_m(\mathbf{r}) \cdot \mathbf{H}(\mathbf{r})$$

Combine this with the Maxwell equations to remove current densities, we see that

$$\frac{du_{mech}}{dt} = (\nabla \times \mathbf{H} - \frac{\partial \mathbf{H}}{\partial t}) \cdot \mathbf{E} + (-\nabla \times \mathbf{E} - \frac{\partial \mathbf{B}}{\partial t}) \cdot \mathbf{H}$$

With a vector identity, this simplifies to

$$\frac{du_{mech}}{dt} = -\nabla \times (\mathbf{E} \times \mathbf{H})$$

**Definition**. We call $\mathbf{S} = \mathbf{E} \times \mathbf{H}$ the *Poynting vector*.

With this vector, we can define

$$\frac{du_{mech}}{dt} = -\nabla \times \mathbf{S}$$

### Section 9.2.2 - Energy Density for Linear Materials

For a simple material, that is, one in which $\mathbf{D} = \varepsilon \mathbf{E}$ and $\mathbf{B} = \mu \mathbf{H}$, we can express the rate of change of electomagnetic energy $\frac{\partial u_{em}}{\partial t}$ as $\frac{\partial u_{em}}{\partial t} = \frac{1}{2} \frac{\partial}{\partial t} (\mathbf{E} \cdot \mathbf{D} + \mathbf{H} \cdot \mathbf{B})$. After integration, we can see that $u_{em} = \frac{1}{2}(\varepsilon E^2 + \mu H^2)$.

**Definition**. A material is said to be an *anisotropic linear material* if $\mathbf{D} = \overleftrightarrow{\mathbf{\varepsilon}} \cdot \mathbf{E}$ and $\mathbf{B} = \overleftrightarrow{\mathbf{\mu}} \cdot \mathbf{H}$. Then, the internal electromagnetic energy becomes

$$u_{em} = \frac{1}{2}(\mathbf{E} \cdot \overleftrightarrow{\mathbf{\varepsilon}} \cdot \mathbf{E}+ \mathbf{H} + \overleftrightarrow{\mathbf{\mu}} \cdot \mathbf{H}) = \frac{1}{2}\sum_{i,j}(\varepsilon_{ij}E_iE_j + \mu_{ij}H_iH_j)$$

If the dyadics are symmetric, the energy functions uniquely specify the energy in terms of fields. In general, the polarization or magnetization of a material may depend on its past history and on time, and as such, the energy density for such materials cannot be expressed entirely in terms of the fields.

### Section 9.2.3 - Poynting Vector Examples

Consider a long coaxial cable, bridged by a constant voltage $V$ on one side and a resistor $R$ on the other. Then, we know that between the conductors, $\mathbf{H} = \frac{R}{2\pi s R}\mathbf{\varphi}$. Additionally, we know that

$$V=\int_a^b \mathbf{E} \cdot d\mathbf{l} = \frac{Q}{2\pi \ell \varepsilon_0} \ln(\frac{b}{a}) \Rightarrow \frac{Q}{\ell} = \frac{2\pi\varepsilon_0}{\ln(\frac{b}{a})} V$$

This then implies that $\mathbf{E} = \frac{V}{\ln(\frac{b}{a})s} \hat{\mathbf{s}}$. We can then solve for both the energy density and Poynting vector, as well as $\mathbf{v} = \mathbf{S} / u$, the speed at which energy moves through the cable. With the impedance for a coaxial cable $Z_{C0} = \sqrt{\frac{\mu_0}{\varepsilon_0}} \frac{\ln(\frac{b}{a})}{2\pi}$, we see that

$$\mathbf{v} = \frac{2c \hat{\mathbf{z}}}{\frac{R}{Z_{C0}} + \frac{Z_{C0}}{R}}$$

---

Consider a long cylindrical ohmic wire of radius $a$, length $L$, and resistivity $\rho$ along the $z$-axis. If this wire is carrying a constant current $I$, we know that inside the wire, $E_z = \rho J = \rho \frac{I}{\pi a^2}$. From Ampere's Law, $H_\phi = \frac{s}{2\pi a^2} I$. Then, inside the wire,

$$\mathbf{S} = -s \frac{\rho I^2}{2 \pi^2 a^4} \hat{\mathbf{s}}$$

Outside the wire, we know that $\mathbf{E} = \frac{\rho I}{\pi a^2} \hat{\mathbf{z}}$ and $\mathbf{H} = \frac{I}{2\pi s}\hat{\mathbf{\varphi}}$, so

$$\mathbf{S} = -\frac{\rho I}{\pi a^2} \frac{I}{2\pi s} \hat{\mathbf{s}}$$

Notably, inside the wire, $\nabla \cdot \mathbf{S} = \frac{\rho I^2}{\pi^2 a^4}$, but is equal to $0$ outside of the wire.

---

Further examples are present but omitted.

## Section 9.3 - Conservation of Momentum and Maxwell Stress Tensor

We know that the rate of change of momentum for any given particle is simply the force acting on it. To calculate this, recall the force density:

$$\mathbf{f} = \sum_i \mathbf{F}_i\delta(\mathbf{r}-\mathbf{r}_i) + \sum_j \mathbf{F}_j\delta(\mathbf{r}-\mathbf{r}_j) = \sum_i q_{ei}\delta(\mathbf{r}-\mathbf{r}_i)(\mathbf{E} + \mathbf{v}_i \times \mathbf{B}) + \sum_j q_{ej} \delta(\mathbf{r}-\mathbf{r}_i) (\mathbf{H} - \mathbf{v}_j \times \mathbf{D})$$

Converting to currents, we see that

$$\mathbf{f}(\mathbf{r}) = \rho_e(\mathbf{r})\mathbf{E}(\mathbf{r}) + \mathbf{J}_e(\mathbf{r}) \times \mathbf{B}(\mathbf{r}) + \rho_m(\mathbf{r}) + \mathbf{H}(\mathbf{r}) - \mathbf{J}_m(\mathbf{r}) \times \mathbf{D}(\mathbf{r})$$

Substituting in Maxwell's Equations, we see that

$$\mathbf{f}(\mathbf{r}) + \frac{\partial}{\partial t}(\mathbf{D} \times \mathbf{B}) = \varepsilon_0 (\nabla \cdot \mathbf{E})\mathbf{E} + (\nabla \times \mathbf{E})\times\mathbf{D} + \mu_0(\nabla \cdot \mathbf{H})\mathbf{H} + (\nabla \times \mathbf{H})\times\mathbf{B}$$

Now, we claim that the right-hand side is the divergence of some tensor $\overleftrightarrow{\mathbf{T}}$, so that

$$\mathbf{f}(\mathbf{r}) + \frac{\partial}{\partial t}(\mathbf{D} \times \mathbf{B}) = \nabla \cdot \overleftrightarrow{\mathbf{T}}$$

This tensor is the Maxwell Stress Tensor. We claim that the divergence of this tensor is composed of both an electric and magnetic part, so that $\nabla \cdot \overleftrightarrow{\mathbf{T}} = \nabla \cdot \overleftrightarrow{\mathbf{T}}_e + \nabla \cdot \overleftrightarrow{\mathbf{T}}_m$. Then, we  can state

$$\begin{align}
\nabla \cdot \overleftrightarrow{\mathbf{T}}_e &= \varepsilon_0 [(\nabla \cdot \mathbf{E})\mathbf{E} + (\nabla \times \mathbf{E})\times \mathbf{E}] \\
\nabla \cdot \overleftrightarrow{\mathbf{T}}_m &= \varepsilon_0 [(\nabla \cdot \mathbf{H})\mathbf{H} + (\nabla \times \mathbf{H})\times \mathbf{H}]
\end{align}$$

We know that $\nabla \cdot(\mathbf{EE}) = (\nabla \cdot \mathbf{E})\mathbf{E} + (\mathbf{E} \cdot \nabla)\mathbf{E}$ and $\nabla \cdot(\overleftrightarrow{\mathbf{I}}f) = \nabla f$. If we let $f = \frac{1}{2}\mathbf{E} \cdot \mathbf{E}$, we see that $\nabla(\frac{1}{2}\mathbf{E} \cdot \mathbf{E}) = (\mathbf{E} \cdot \nabla)\mathbf{E} + (\nabla \times \mathbf{E})\mathbf{E}$. Then, we see that

$$\begin{align}
\overleftrightarrow{\mathbf{T}}_e &= \varepsilon_0 \mathbf{EE} - \frac{\varepsilon_0}{2} \overleftrightarrow{\mathbf{I}}(\mathbf{E} \cdot \mathbf{E}) \\
\overleftrightarrow{\mathbf{T}}_m &= \mu_0 \mathbf{HH} - \frac{\mu_0}{2} \overleftrightarrow{\mathbf{I}}(\mathbf{H} \cdot \mathbf{H})
\end{align}$$

Knowing that $\overleftrightarrow{\mathbf{T}} = \overleftrightarrow{\mathbf{T}}_e + \overleftrightarrow{\mathbf{T}}_m$, and that $u = \frac{1}{2}(\varepsilon_0 E^2 + \mu_0 H^2)$ is the energy density of the electromagnetic fields in a vacuum,

$$\overleftrightarrow{\mathbf{T}} = \varepsilon_0 \mathbf{EE} + \mu_0 \mathbf{HH} - \overleftrightarrow{\mathbf{I}}u$$

Additionally, we denote the time rate of change of the momentum density of the electromagnetic fields as $\mathbf{g}(\mathbf{r}) = \mathbf{D}(\mathbf{r}) \times \mathbf{B}(\mathbf{r})$. Thus,

$$\mathbf{f}(\mathbf{r}) = \frac{\partial}{\partial t}\mathbf{g} = \nabla \cdot \overleftrightarrow{\mathbf{T}}$$

---

The Divergence Theorem states that $\int_V(\nabla \cdot \overleftrightarrow{\mathbf{T}}) dV = \int_{SofV} dS \hat{\mathbf{n}} \cdot \overleftrightarrow{\mathbf{T}}$. We can prove this by expanding the left-hand side over a cube. Note that as $\overleftrightarrow{\mathbf{T}}$ is symmetric, $\hat{\mathbf{n}} \cdot \overleftrightarrow{\mathbf{T}} = \overleftrightarrow{\mathbf{T}} \cdot \hat{\mathbf{n}}$.

Given a static field, the momentum does not change in time. That is,

$$\frac{\partial}{\partial t} \mathbf{g} = \frac{\partial}{\partial t}(\mathbf{D} \times \mathbf{B}) = 0$$

Then, we can see that $\mathbf{f}(\mathbf{r}) = \nabla \cdot \overleftrightarrow{\mathbf{T}}$. We can thus integrate over the volume to find force on an object.

$$\mathbf{F} = \int_V \mathbf{f}(\mathbf{r}) dV = \int_V \nabla \cdot \overleftrightarrow{\mathbf{T}} dV = \int_{\partial V} dS \hat{\mathbf{n}} \cdot \overleftrightarrow{\mathbf{T}} = \int_{\partial V} \overleftrightarrow{\mathbf{T}} \cdot \hat{\mathbf{n}} dS$$
