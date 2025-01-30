# Chapter 4 - Conductors and Static Electric Fields

## Section 4.1 - Introduction

We will focus primarily on electric fields and charges. For the purposes for this section, we will assume insulators are perfect.

## Section 4.2 - Electrostatic Properties of a Conductor

In a metal or conductor, there are plentiful charges not bound to a particular atom and are thus free to move throughout the material.

We note that there is no electric fiend inside a conductor, as charges internal to the material would move under the force it generates until they find a configuration that eliminates the field. This may happen, but not in electrostatics.

Additionally, as the field is zero, it follows from Maxwell's equations that there is no charge inside a conductor. However, charge may be present at the surface. For sufficiently symmetric charges, this charge may be calculated.

Consider any two points internal to the conductor. The voltage between said points is defined as $\int_A^B \vb{E} \vdot \dd{\vb{l}}$. Since $\vb{E} = 0$ inside the conductor, the voltage difference must be zero. Thus, any two points in or on the surface (TODO: Why on the surface?) of a conductor must be at the same potential.

The electric field at the surface of a conductor is perpendicular to its surface. Consider some displacement $\dd{\vb{l}}$. Now, $\vb{E} \vdot \dd{\vb{l}} = \vb{E}_s \vdot \dd{\vb{l}}_s + \vb{E}_p \vdot \dd{\vb{l}}_p = \dd{V_s} + \dd{V_p}$, in terms of parallel and perpendicular components. The parallel voltage difference is zero, so the electric field must be zero.

Consider the surface of a conductor with surface charge density $\sigma_e$. A cylinder with one end inside and one end outside said surface, with its axis normal to said surface, will be a Gaussian "pillbox", which will show that with V being the volume of the pillbox, $\int_V \div{\vb{E}} \dd{V} = \frac{Q_e}{\varepsilon_0} = \frac{A\sigma_e}{\varepsilon_0}$. Thus, $\sigma_e = \varepsilon_0 E$.

## Section 4.3 - Exercises involving conductors at fixed potentials

Consider a square with left and right potentials $V(0, y) = V(l, y) = V_1$ and $V(x, 0) = V(x, l) = V_2$. Since we are uniform in $z$, we can say that $V(x, y) = X(x)Y(y)$ and apply separation of variables.

In spherical polar coordinates, we see that with azimuthal symmetry, $V(r, \theta) = \sum_{l=0}^\infty a_l r^l P_l(cos\theta)$ where $P_l(x)$ are Legendre polynomials.

**Theorem**. 4.3.3: A Laplace equation's solution must be unique inside a volume $\Omega$ if $\int_{\dd{\Omega}}[\Phi(\vb{r})\grad{\Phi{\vb{r}}} \vdot \vu{n} \dd{S} = 0]$. With this, consider a surface $\dd{\Omega}$ that surrounds conductors. The integral vanishes if a) the potential is specified on each conductor or b) the total charge on each conductor is specified.

Now, define $\Phi(\vb{r})$ as the difference between any two potential solutions to the Laplace equation at point $\vb{r}$. Since potential must be a constant,

$$
\int_{\dd{\Omega}}[\Phi(\vb{r})\grad{\Phi{\vb{r}}}] \vdot \vu{n} \dd{S}
= \sum_{i=1}^N \Phi_i \int_{\dd{\Omega_i}} \grad{\Phi{\vb{r}}} \vdot \vu{n} \dd{S}
$$

Thus, if potential is specified, $\Phi_i$ vanishes for that conductor. If the total charge is instead specified, the gradient vanishes because there is no difference in charge between any two points.

## Section 4.4 - Electric Field, Polarization Field, and Flux Density in the Presence of Conductors

**Definition**. A *bound charge* is any charge in a conductor that is bound to an atom and not free to be redistributed at the surface. We say that bound charges are the source of the polarization field $\vb{P}$. Additionally, we note the charge density of bound charges is $\rho_{eb}$. Thus,

$$
\div \vb{P} = - \rho_{eb}
$$

This field is zero outside of a material, and if non-zero inside a material, will drop to zero at the surface discontinuously. If there is a component perpendicular to the surface, the discontinuity will generate curl. If there is a component parallel to the surface, it will generate divergence.

**Definition**. Charges not bound are called *free*, with density denoted as $\rho_{ef}$. Combined with $\rho_{eb}$, they form the basis of the electric field. THat is,

$$
\varepsilon_0 \div \vb{E} = \rho_{ef} + \rho_{eb}
$$

**Definition**. The electric flux density field $\vb{D}$ is defined as

$$
\vb{D} = \varepsilon_0 \vb{E} + \vb{P}
$$

Both $\vb{D}$ and $\vb{P}$ have units of Coulombs/m^2. Additionally, we see that

$$
\div \vb{D} = \div (\varepsilon_0 \vb{E} + \vb{P}) = \div \varepsilon_0 \vb{E} + \div \vb{P} = (\rho_{ef} + \rho_{eb}) - \rho_{eb} = \rho_{ef}
$$

## Section 4.5 - Induced Electric Charges, their Potentials and Fields

This is an application chapter.

## Section 4.6 - Capacitance

**Definition**. The *capacitance* of an object $C$ is the charge per volt, such that

$$
C := \frac{Q}{V}
$$

This unit, $\frac{C}{V}$, is known as a Farad. For a sphere, $C = 4 \pi \varepsilon_0 R$. For a parallel plate capacitor, this reduces to $C = \frac{epsilon_0 A}{d}$.

## Section 4.7 - Forces on Charged Conductors in Electric Fields

We know that $\vb{F} = \int \vb{E}_{ext}(\vb{r}) \rho_e(\vb{r}) dV$, where $\vb{E}_{ext}(\vb{r})$ is the external electric field and $\rho_e(\vb{r})$ is the charge density of the object.
