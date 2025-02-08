# Chapter 3 - Electric and Magnetic Scalar Potentials

## Section 3.1 - Work and Energy in Electrostatics and Magnetostatics

The force on charge $q$ is given by $\mathbf{F}(\mathbf{r}) = q_e \mathbf{E}(\mathbf{r})$ or $\mathbf{F}(\mathbf{r}) = q_m \mathbf{H}(\mathbf{r})$. If this charge is moved $d{\mathbf{l}} = d x \hat{\mathbf{x}} + d y \hat{\mathbf{y}} + d z \hat{\mathbf{z}}$, the change in internal energy (work) this produces can be written as

$$
d{U}= - \mathbf{F} \cdot d{\mathbf{l}}
$$

Rewriting this, $\mathbf{F} = -\nabla{U}$, with $U$ as potential energy. Now, we can denote this change in internal energy in terms of $q$ as follows:

$$
\mathbf{E}(\mathbf{r}) = \frac{1}{q_e} \mathbf{F_e}(\mathbf{r}) = - \frac{1}{q_e} \nabla{U_e(\mathbf{r})} = -\nabla{V_e(\mathbf{r})}
$$

The units of electrostatic potential is Joule/Coulomb, also known as a Volt. Thus, the units of the electric field should be expressed in Volts/meter. Similarly,

$$
\mathbf{H}(\mathbf{r}) = \frac{1}{q_m} \mathbf{F_m}(\mathbf{r}) = - \frac{1}{q_m} \nabla{U_m(\mathbf{r})} = -\nabla{V_m(\mathbf{r})}
$$

The units of magnetostatic potential is Joule/Weber, also known as an Ampere. Thus, the units of the magnetic field can be written as Amperes/meter.

With this, we can calculate work. Moving a charge $q$ from $A$ to $B$, we see that

$$
\delta W = \int_A^B \mathbf{F} \cdot d{\mathbf{l}} = q_e \int_A^B \mathbf{E} \cdot d{\mathbf{l}} = -q_e \int_A^B \nabla{\mathbf{V}} \cdot d{\mathbf{l}} = -q_e \delta V_e
$$

Strictly speaking, this is a potential difference. To find the absolute potential, assume a point charge $Q$ at the origin, and a charge $q$. We take the work as $q$ moves from $\mathbf{r'} = \mathbf{\infty}$ to $\mathbf{r'} = \mathbf{r}$. Thus,

$$
W = -q_e \frac{Q_e}{4 \pi \varepsilon_0} \int_{\infty}^0 \frac{\hat{\mathbf{r'}}}{r'^2} \cdot (\hat{\mathbf{r'}}) d{r'} = -q_e \frac{Q_e}{4 \pi \varepsilon_0} [\frac{-1}{r'}]_{\infty}^{r'} = q_e \frac{Q_e}{4 \pi \varepsilon_0} \frac{1}{r}
$$

$$
W = -q_m \frac{Q_m}{4 \pi \mu_0} \int_{\infty}^0 \frac{\hat{\mathbf{r'}}}{r'^2} \cdot (\hat{\mathbf{r'}}) d{r'} = -q_m \frac{Q_m}{4 \pi \mu_0} [\frac{-1}{r'}]_{\infty}^{r'} = q_m \frac{Q_m}{4 \pi \mu_0} \frac{1}{r}
$$

Letting the potential as $\mathbf{r} \rightarrow \infty$ equal $0$ be our reference and dividing out $q$, we find that the voltage for arrangement is the following:

$$
V_e(\mathbf{r}) = \frac{Q_e}{4 \pi \varepsilon_0 r} \text{ and } V_m(\mathbf{r}) = \frac{Q_m}{4 \pi \mu_0 r}
$$

Now, if we let the stationary charge $Q$ be located at $\mathbf{r'}$, we see that

$$
V_e(\mathbf{r}) = \frac{Q_e}{4 \pi \varepsilon_0}{|\mathbf{r}-\mathbf{r'}|} \text{ and } V_m(\mathbf{r}) = \frac{Q_m}{4 \pi \mu_0}{|\mathbf{r}-\mathbf{r'}|}
$$

If we allow multiple charges, this becomes

$$
V_e(\mathbf{r}) = \frac{1}{4\pi \varepsilon_0} \sum_{i=1}^N \frac{Q_{ei}}{|\mathbf{r}-\mathbf{r_i}|}
$$

Taking this to its natural limit,

$$
V_e(\mathbf{r}) = \frac{1}{4 \pi \varepsilon_0} \int_{V'} \frac{\rho_e(\mathbf{r'})}{|\mathbf{r}-\mathbf{r'}}| d{V'}
$$

$$
V_m(\mathbf{r}) = \frac{1}{4 \pi \mu_0} \int_{V'} \frac{\rho_m(\mathbf{r'})}{|\mathbf{r}-\mathbf{r'}}| d{V'}
$$

## Section 3.2 - Energy of a Charge Distribution

Given two point charges $Q_{e1}, Q_{e2}$ we know the work to bring them together is

$$
W_2 = W_{21} = \frac{1}{4 \pi \varepsilon_0} \frac{Q_{e1} Q_{e2}}{|\mathbf{r_2} - \mathbf{r_1}|}
$$

Superposition applies here. The energy to create $N$ charges is

$$
W_n = \frac{1}{2} \frac{4 \pi \varepsilon_0} \sum_{i = 1}^{N} \sum_{j > i}^{N} \frac{Q_{ei}Q_{ej}}{|\mathbf{r_i}-\mathbf{r_j}|}
$$

For the sake of symmetry, sum overall charges and divide by 2.

$$
W_n = \frac{1}{2} \frac{1}{4 \pi \varepsilon_0} \sum_{i = 1}^{N} \sum_{j \neq i}^{N} \frac{Q_{ei}Q_{ej}}{|\mathbf{r_i}-\mathbf{r_j}|}
$$

Rearranging, we see the following:

$$
W_n = \frac{1}{2} \sum_{i = 1}^{N}Q_{ei} \sum_{i \neq j}^{N} \frac{1}{4 \pi \varepsilon_0} \frac{Q_{ej}}{|\mathbf{r_i}-\mathbf{r_j}|}
= \frac{1}{2}\sum_{i = 1}^{N} Q_{ei} V(\mathbf{r_i})
$$

We can rewrite this as a Riemann sum and convert to an integral.

$$
W_e = \frac{1}{2} \int_V p_e(\mathbf{r}) V_e(\mathbf{r}) d V ; \quad
W_m = \frac{1}{2} \int_V p_m(\mathbf{r}) V_m(\mathbf{r}) d V
$$

We can also express this as

$$
W_e = \frac{1}{2} \frac{1}{4 \pi \varepsilon_0} \int_V \int_{V'} \frac{\rho_e(\mathbf{r})\rho_e(\mathbf{r'})}{|\mathbf{r}-\mathbf{r'}|} d{V'} d{V}
$$

$$
W_m = \frac{1}{2} \frac{1}{4 \pi \mu_0} \int_V \int_{V'} \frac{\rho_m(\mathbf{r})\rho_m(\mathbf{r'})}{|\mathbf{r}-\mathbf{r'}|} d{V'} d{V}
$$

Note the $\frac{1}{2}$ is the same anti-double-counting factor introduced previously. If we were to determine the potential based on a different set of charges, the factor would be absent.

We can now write an expression for energy of a charge density in terms of the field that it produces.

$$
W = \frac{\varepsilon_0}{2} \int_V (\nabla \cdot \mathbf{E}(\mathbf{r})) V(\mathbf{r}) d V
$$

Simplifying, we see that

$$
W_e = \frac{\varepsilon_0}{2} \int_{V} E^2(\mathbf{r}) d V ; \quad
W_m = \frac{\mu_0}{2} \int_{V} H^2(\mathbf{r}) d V
$$

## Section 3.3 - The Poisson and Laplace Equations

We know that $\mathbf{E}(\mathbf{r}) = -\nabla \cdot V_e(\mathbf{r})$ and $\mathbf{H}(\mathbf{r}) = -\nabla \cdot V_m(\mathbf{r})$

Combined this, as well as the first of the Maxwell equations, we see that

$$
\nabla \cdot \mathbf{E} = -\nabla \cdot \nabla V_e = - \nabla^2{V_e} = \frac{\rho_e}{\varepsilon_0}
$$

$$
\nabla \cdot \mathbf{H} = -\nabla \cdot \nabla V_m = - \nabla^2{V_m} = \frac{\rho_m}{\mu_0}
$$

The last inequality is called the Poisson Equation, or the inhomogeneous Laplace equation.

To solve this equation, we define a Green function as follows:

$$
\nabla^2 G(\mathbf{r}, \mathbf{r'}) = \delta(\mathbf{r} - \mathbf{r'})
$$

Now, we can construct a potential function in terms of said green function that satisfies the Laplace equation.

$$
V_e(\mathbf{r}) = - \int_V G(\mathbf{r}, \mathbf{r'}) \frac{\rho_e(\mathbf{r'})}{\varepsilon_0} d{V'}
$$

This is the specific solution. Let $\psi(\mathbf{r})$ be a solution to the homogenous equation. We can state the following:

$$
V_e(\mathbf{r}) = \psi(\mathbf{r}) - \int_V G(\mathbf{r}, \mathbf{r'}) \frac{\rho_e(\mathbf{r'})}{\varepsilon_0} d{V'}
$$

We will consider the potential of a point charge. THat is, the limit of potential is zero as distance approaches infinity.

Recall the potential of a point charge:

$$
V_e(\mathbf{r}) = \frac{Q_e}{\varepsilon_0} \frac{1}{4 \pi |\mathbf{r} - \mathbf{r}|}
$$

We know that $- \nabla^2{V(\mathbf{r})} = \nabla \cdot \mathbf{E}(\mathbf{r})$. Thus, recall the electric field of a point charge.

$$
\mathbf{E}(\mathbf{r}) = -\nabla{V(\mathbf{r})} = \frac{Q_e}{\varepsilon_0} \nabla({\frac{-1}{4\pi|\mathbf{r}-\mathbf{r'}|}}) = \frac{Q_e}{\varepsilon_0} \frac{\mathbf{r} - \mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3}
$$

Taking the divergence, we find that

$$
- \nabla^2{V(\mathbf{r})} = G(\mathbf{r}, \mathbf{r'}) \frac{Q_e}{\varepsilon_0} = \frac{Q_e}{\varepsilon_0} \nabla^2({\frac{-1}{4\pi|\mathbf{r}-\mathbf{r'}|}})
=  \frac{Q_e}{\varepsilon_0} \nabla \cdot \frac{\mathbf{r} - \mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3} = \frac{Q_e}{\varepsilon_0} \delta(\mathbf{r} - \mathbf{r'})
$$

Thus, we see that

$$
\nabla^2 {\frac{-1}{4\pi}}{|\mathbf{r}-\mathbf{r'}|} = \delta(\mathbf{r} - \mathbf{r'}) \quad \Rightarrow \quad G(\mathbf{r}, \mathbf{r'}) = {\frac{-1}{4\pi}}{|\mathbf{r}-\mathbf{r'}|}
$$

Finally,

$$
V_e(\mathbf{r}) = \int_{V'} \frac{1}{4 \pi |\mathbf{r} - \mathbf{r}|} \frac{\rho_e}{\varepsilon_0} d{V'}
$$

$$
V_m(\mathbf{r}) = \int_{V'} \frac{1}{4 \pi |\mathbf{r} - \mathbf{r}|} \frac{\rho_m}{\mu_0} d{V'}
$$

## Section 3.4 - The Laplace and Poisson Equations with Boundary Conditions

**Theorem**. The *Mean Value Theorem* states that if a function satisfies the laplace equation for every point within a region, then the value of the function at the center of the applicable region is equal to the average of the function along the boundary of said region.

This can be extended to the *Method of Relaxations*, in which each point in a mesh is defined by the average of its neighboring points. This is only useful in computer graphics.

An interesting consequence of this states that there are no local minima or maxima within said region. The global maximum and minimum must be located at the boundary.

**Theorem**. This leads to *Earnshaw's Theorem*. To make an electric trap to hold charges, more than zero forces must be applied to the charge, so that if the charge leaves its dedicated position it is forced back. Depending on the sign, at said point, potential must increase or decrease in all directions. However, this would force a local extrema. This cannot be possible.

**Theorem**. The solution to a Laplace or Poisson equation is unique.

## Section 3.5 - Multipole Expansion of the Electrostatic or Magnetostatic Field

We want a simple way to write the Green function.

Let us assume all charge is contained in a sphere with radius $R$ centered at the origin. Then, for points $r$ far from the origin, the Green function can be written as

$$
\frac{1}{4 \pi|\mathbf{r}-\mathbf{r'}|} = \frac{1}{4\pi \sqrt{r^2 - 2\mathbf{r} \cdot \mathbf{r'} + r'^2}}
= \frac{1}{4\pi r}(1 - 2 \hat{\mathbf{r}} \cdot \hat{\mathbf{r'}} + \frac{r'}{r} + \frac{r'^2}{r^2})^{-\frac{1}{2}}
$$

This inverse square root term $(1 - 2 \hat{\mathbf{r}} \cdot \hat{\mathbf{r'}} + \frac{r'}{r} + \frac{r'^2}{r^2})^{-\frac{1}{2}}$ can be expanded as a power series in $\frac{r'}{r}$.

The first two terms of this power series are simple enough.

$$
G(\mathbf{r}, \mathbf{r'}) = \frac{1}{4 \pi |\mathbf{r}-\mathbf{r'}|} \approx \frac{1}{4 \pi r} ( 1 + \frac{\hat{\mathbf{r}} \cdot \mathbf{r'}}{r}); \quad \text{ for}  r > r'
$$

Applying this to the equation for voltage, we see that

$$
V_e(r) = \frac{1}{\varepsilon_0} \int_{V'} G(\mathbf{r}, \mathbf{r'}) p_e(\mathbf{r'}) d{V'} \approx
\frac{1}{4 \pi \varepsilon_0 r} \int_{V'}  (1 + \frac{\hat{\mathbf{r}} \cdot \mathbf{r'}}{r}) p_e(\mathbf{r'}) d{V'}
= \frac{Q_e}{4 \pi \varepsilon_0 r} + \frac{\hat{\mathbf{r}} \cdot \mathbf{p}}{4 \pi \varepsilon_0 r^2}
$$

**Definition**. The first and second terms of this equation are the *monopole* and *dipole* terms respectively.

**Definition**. We define $\mathbf{p}$ as the *electric dipole moment*, and in the magnetic version, $\mathbf{m}$ as the *magnetic dipole moment* as follows:

$$
\mathbf{p} = \int_{V'} \mathbf{r'} \rho_e(\mathbf{r'}) d{V'}
$$

Notably, the moments only depend on the charge density, not the point at which the field is being examined. That is, this integral only needs to be computed once.

To compute higher-order terms, let $\varepsilon = 2\frac{r'}{r}\hat{\mathbf{r}}\cdot\hat{\mathbf{r'}}-(\frac{r'}{r})^2$. Now we can expand $(1-\varepsilon)^{-\frac{1}{2}}$.

$$
(1-\varepsilon)^{-\frac{1}{2}} = 1 + \frac{1}{2}\varepsilon + \frac{3}{8}\varepsilon^2 + \frac{5}{16}\varepsilon^3 + \ldots
$$

However, we want an expansion in terms of $t = \frac{r'}{r}$. To do this, we write the expansion as

$$
\frac{1}{4 \pi |\mathbf{r}-\mathbf{r'}|} = \frac{1}{4 \pi r} \sum_{n=0}^{\infty} (\frac{r'}{r}) P_n(\hat{\mathbf{r}} \cdot \hat{\mathbf{r'}})
$$

Here, $P_n(\hat{\mathbf{r}} \cdot \hat{\mathbf{r'}})$ is a polynomial. Because $|\mathbf{r}-\mathbf{r'}|$ is symmetric, we can say that if $r' > r$ instead, simply switch the two. Thus the equation becomes

$$
\frac{1}{4 \pi |\mathbf{r}-\mathbf{r'}|} = \frac{1}{4 \pi} \sum_{n=0}^{\infty} (\frac{r'^n_{<}}{r^{n+1}_{>}}) P_n(\hat{\mathbf{r}} \cdot \hat{\mathbf{r'}})
$$

Where $r_>$ is the greater of $r, r'$, and $r_<$ the lesser.

**Definition**. The polynomials $P_n(x)$ are Legendre Polynomials. We define them as follows:

$$
(1 - 2tx + t^2)^{-\frac{1}{2}} = \sum_{n=0}^\infty t^n P_n(x)
$$

Note that as a quirk of the function, $P_n(1) = 1$ for all $n$.

We can apply these quadrupole and beyond terms to the violate or other equations, however, this becomes very messy.
