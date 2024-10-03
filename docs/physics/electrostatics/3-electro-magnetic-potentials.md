# Chapter 3 - Electric and Magnetic Scalar Potentials

## Section 3.1 - Work and Energy in Electrostatics and Magnetostatics

The force on charge $q$ is given by $\vb{F}(\vb{r}) = q_e \vb{E}(\vb{r})$ or $\vb{F}(\vb{r}) = q_m \vb{H}(\vb{r})$. If this charge is moved $\dd{\vb{l}} = \dd x \vu{x} + \dd y \vu{y} + \dd z \vu{z}$, the change in internal energy (work) this produces can be written as

$$
\dd{U}= - \vb{F} \vdot \dd{\vb{l}}
$$

Rewriting this, $\vb{F} = -\grad{U}$, with $U$ as potential energy. Now, we can denote this change in internal energy in terms of $q$ as follows:

$$
\vb{E}(\vb{r}) = \frac{1}{q_e} \vb{F_e}(\vb{r}) = - \frac{1}{q_e} \grad{U_e(\vb{r})} = -\grad{V_e(\vb{r})}
$$

The units of electrostatic potential is Joule/Coublomb, also known as a Volt. Thus, the units of the electric field should be expressed in Volts/meter. Similarly,

$$
\vb{H}(\vb{r}) = \frac{1}{q_m} \vb{F_m}(\vb{r}) = - \frac{1}{q_m} \grad{U_m(\vb{r})} = -\grad{V_m(\vb{r})}
$$

The units of magnetostatic potential is Joule/Weber, also known as an Ampere. Thus, the units of the magnetic field can be written as Amperes/meter.

With this, we can calculate work. Moving a charge $q$ from $A$ to $B$, we see that

$$
\delta W = \int_A^B \vb{F} \vdot \dd{\vb{l}} = q_e \int_A^B \vb{E} \vdot \dd{\vb{l}} = -q_e \int_A^B \grad{\vb{V}} \vdot \dd{\vb{l}} = -q_e \delta V_e 
$$

Strictly speaking, this is a potential difference. To find the absolute potential, assume a point charge $Q$ at the origin, and a charge $q$. We take the work as $q$ moves from $\vb{r'} = \vb{\infty}$ to $\vb{r'} = \vb{r}$. Thus,

$$
W = -q_e \frac{Q_e}{4 \pi \epsilon_0} \int_{\infty}^0 \frac{\vu{r'}}{r'^2} \vdot (\vu{r'}) \dd{r'} = -q_e \frac{Q_e}{4 \pi \epsilon_0} [\frac{-1}{r'}]_{\infty}^{r'} = q_e \frac{Q_e}{4 \pi \epsilon_0} \frac{1}{r}
$$

$$
W = -q_m \frac{Q_m}{4 \pi \mu_0} \int_{\infty}^0 \frac{\vu{r'}}{r'^2} \vdot (\vu{r'}) \dd{r'} = -q_m \frac{Q_m}{4 \pi \mu_0} [\frac{-1}{r'}]_{\infty}^{r'} = q_m \frac{Q_m}{4 \pi \mu_0} \frac{1}{r}
$$

Letting the potential as $\vb{r} \leftarrow \infty$ equal $0$ be our reference and dividing out $q$, we find that the voltage for arrangement is the following:

$$
V_e(\vb{r}) = \frac{Q_e}{4 \pi \epsilon_0 r} \text{ and } V_m(\vb{r}) = \frac{Q_m}{4 \pi \mu_0 r}
$$

Now, if we let the stationary charge $Q$ be located at $\vb{r'}$, we see that

$$
V_e(\vb{r}) = \frac{Q_e}{4 \pi \epsilon_0 \abs{\vb{r} - \vb{r'}}} \text{ and } V_m(\vb{r}) = \frac{Q_m}{4 \pi \mu_0 \abs{\vb{r} - \vb{r'}}}
$$

If we allow multiple charges, this becomes

$$
V_e(\vb{r}) = \frac{1}{4\pi \epsilon_0} \sum_{i=1}^N \frac{Q_ei}{\abs{\vb{r}-\vb{r_i}}}
$$

Taking this to its natural limit,

$$
V_e(\vb{r}) = \frac{1}{4 \pi \epsilon_0} \int_{V'} \frac{\rho_e(\vb{r'})}{\abs{\vb{r}-\vb{r'}}} \dd{V'}
$$


$$
V_m(\vb{r}) = \frac{1}{4 \pi \mu_0} \int_{V'} \frac{\rho_m(\vb{r'})}{\abs{\vb{r}-\vb{r'}}} \dd{V'}
$$

## Section 3.2 - Energy of a Charge Distribution

Given two point charges $Q_{e1}, Q_{e2}$ we know the work to bring them together is

$$
W_2 = W_{21} = \frac{1}{4 \pi \epsilon_0} \frac{Q_{e1} Q_{e2}}{\abs{\vb{r_2} - \vb{r_1}}}
$$

Superposition applies here. The energy to create $N$ charges is 

$$
W_n = \frac{1}{2} \frac{4 \pi \epsilon_0} \sum_{i = 1}^{N} \sum_{j > i}^{N} \frac{Q_{ei}Q_{ej}}{\abs{\vb{r_i}-\vb{r_j}}}
$$

For the sake of symnetry, sum overall charges and divide by 2.

$$
W_n = \frac{1}{2} \frac{1}{4 \pi \epsilon_0} \sum_{i = 1}^{N} \sum_{j \neq i}^{N} \frac{Q_{ei}Q_{ej}}{\abs{\vb{r_i}-\vb{r_j}}}
$$

Rearranging, we see the following:

$$
W_n = \frac{1}{2} \sum_{i = 1}^{N}Q_{ei} \sum_{i \neq j}^{N} \frac{1}{4 \pi \epsilon_0} \frac{Q_{ej}}{\abs{\vb{r_i}-\vb{r_j}}}
= \frac{1}{2}\sum_{i = 1}^{N} Q_{ei} V(\vb{r_i})
$$

We can rewrite this as a Reimann sum and convert to an integral.

$$
W_e = \frac{1}{2} \int_V p_e(\vb{r}) V_e(\vb{r}) \dd V ; \quad
W_m = \frac{1}{2} \int_V p_m(\vb{r}) V_m(\vb{r}) \dd V
$$

We can also express this as

$$
W_e = \frac{1}{2} \frac{1}{4 \pi \epsilon_0} \int_V \int_{V'} \frac{\rho_e(\vb{r})\rho_e(\vb{r'})}{\abs{\vb{r} - \vb{r'}}} \dd{V'} \dd{V}
$$

$$
W_m = \frac{1}{2} \frac{1}{4 \pi \mu_0} \int_V \int_{V'} \frac{\rho_m(\vb{r})\rho_m(\vb{r'})}{\abs{\vb{r} - \vb{r'}}} \dd{V'} \dd{V}
$$

Note the $\frac{1}{2}$ is the same anti-double-counting factor introduced previously. If we were to determine the potential based on a different set of charges, the factor would be absent.

We can now write an expression for energy of a charge density in terms of the field that it produces.

$$
W = \frac{\epsilon_0}{2} \int_V (\div{\vb{E}(\vb{r})}) V(\vb{r}) \dd V
$$

Simplifying, we see that

$$
W_e = \frac{\epsilon_0}{2} \int_{V} E^2(\vb{r}) \dd V ; \quad
W_m = \frac{\mu_0}{2} \int_{V} H^2(\vb{r}) \dd V
$$

## Section 3.3 - The Poisson and Laplace Equations

We know that $\vb{E}(\vb{r}) = -\div{V_e(\vb{r})}$ and $\vb{H}(\vb{r}) = -\div{V_m(\vb{r})}$

Combinind this, as well as the first of the Maxwell equations, we see that

$$
\div{\vb{E}} = -\div{\grad{V_e}} = - \laplacian{V_e} = \frac{\rho_e}{\epsilon_0}
$$

$$
\div{\vb{H}} = -\div{\grad{V_m}} = - \laplacian{V_m} = \frac{\rho_m}{\mu_0}
$$

The last inequatlity is called the Poisson Equation, or the inhomogenous Laplace equation.

To solve this equation, we define a Green function as follows:

$$
\laplacian G(\vb{r}, \vb{r'}) = \delta(\vb{r} - \vb{r'})
$$

Now, we can construct a potential function in terms of said green function that satisfies the lapalce equation.

$$
V_e(\vb{r}) = - \int_V G(\vb{r}, \vb{r'}) \frac{\rho_e(\vb{r'})}{\epsilon_0} \dd{V'}
$$

This is the specific solution. Let $\psi(\vb{r})$ be a solution to the homogenous equation. We can state the following:

$$
V_e(\vb{r}) = \psi(\vb{r}) - \int_V G(\vb{r}, \vb{r'}) \frac{\rho_e(\vb{r'})}{\epsilon_0} \dd{V'}
$$

We will consider the potential of a point charge. THat is, the limit of potential is zero as distance approaches infinity.

Recall the potential of a point charge:

$$
V_e(\vb{r}) = \frac{Q_e}{\epsilon_0} \frac{1}{4 \pi \abs{\vb{r} - \vb{r}}}
$$

We know that $- \laplacian{V(\vb{r})} = \div{\vb{E}(\vb{r})}$. Thus, recall the electric field of a point charge.

$$
\vb{E}(\vb{r}) = -\grad{V(\vb{r})} = \frac{Q_e}{\epsilon_0} \grad({\frac{-1}{4\pi \abs{\vb{r} - \vb{r'}}}}) = \frac{Q_e}{\epsilon_0} \frac{\vb{r} - \vb{r'}}{\abs{\vb{r} - \vb{r'}}^3}
$$

Taking the divergence, we find that

$$
- \laplacian{V(\vb{r})} = G(\vb{r}, \vb{r'}) \frac{Q_e}{\epsilon_0} = \frac{Q_e}{\epsilon_0} \laplacian({\frac{-1}{4\pi \abs{\vb{r} - \vb{r'}}}}) 
=  \frac{Q_e}{\epsilon_0} \div \frac{\vb{r} - \vb{r'}}{\abs{\vb{r} - \vb{r'}}^3} = \frac{Q_e}{\epsilon_0} \delta(\vb{r} - \vb{r'})
$$

Thus, we see that

$$
\laplacian {\frac{-1}{4\pi \abs{\vb{r} - \vb{r'}}}} = \delta(\vb{r} - \vb{r'}) \quad \Rightarrow \quad G(\vb{r}, \vb{r'}) = {\frac{-1}{4\pi \abs{\vb{r} - \vb{r'}}}}
$$

Finally,

$$
V_e(\vb{r}) = \int_{V'} \frac{1}{4 \pi \abs{\vb{r} - \vb{r}}} \frac{\rho_e}{\epsilon_0} \dd{V'}
$$

$$
V_m(\vb{r}) = \int_{V'} \frac{1}{4 \pi \abs{\vb{r} - \vb{r}}} \frac{\rho_m}{\mu_0} \dd{V'}
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
\frac{1}{4 \pi \abs{\vb{r} - \vb{r'}}} = \frac{1}{4\pi \sqrt{r^2 - 2\vb{r} \vdot \vb{r'} + r'^2}}
= \frac{1}{4\pi r}(1 - 2 \vu{r} \vdot \vu{r'} + \frac{r'}{r} + \frac{r'^2}{r^2})^{-\frac{1}{2}}
$$

This inverse square root term $(1 - 2 \vu{r} \vdot \vu{r'} + \frac{r'}{r} + \frac{r'^2}{r^2})^{-\frac{1}{2}}$ can be expanded as a power series in $\frac{r'}{r}$.

The first two terms of this power series are simple enough.

$$
G(\vb{r}, \vb{r'}) = \frac{1}{4 \pi \abs{\vb{r} - \vb{r'}}} \approx \frac{1}{4 \pi r} ( 1 + \frac{\vu{r} \vdot \vb{r'}}{r}); \quad \text{ for}  r > r'
$$

Applying this to the equation for voltage, we see that

$$
V_e(r) = \frac{1}{\epsilon_0} \int_{V'} G(\vb{r}, \vb{r'}) p_e(\vb{r'}) \dd{V'} \approx
\frac{1}{4 \pi \epsilon_0 r} \int_{V'}  (1 + \frac{\vu{r} \vdot \vb{r'}}{r}) p_e(\vb{r'}) \dd{V'}
= \frac{Q_e}{4 \pi \epsilon_0 r} + \frac{\vu{r} \vdot \vb{p}}{4 \pi \epsilon_0 r^2}
$$

**Definition**. The first and second terms of this equation are the *monopole* and *dipole* terms respectively.

**Definition**. We define $\vb{p}$ as the *electric dipole moment*, and in the magnetic version, $\vb{m}$ as the *magnetic dipole moment* as follows:

$$
\vb{p} = \int_{V'} \vb{r'} \rho_e(\vb{r'}) \dd{V'}
$$

Notably, the moments only depend on the charge density, not the point at which the field is being examined. That is, this integral only needs to be computed once.

To compute higher-order terms, let $\epsilon = 2\frac{r'}{r}\vu{r}\vdot\vu{r'}-(\frac{r'}{r})^2$. Now we can expand $(1-\epsilon)^{-\frac{1}{2}}$.

$$
(1-\epsilon)^{-\frac{1}{2}} = 1 + \frac{1}{2}\epsilon + \frac{3}{8}\epsilon^2 + \frac{5}{16}\epsilon^3 + \ldots
$$

However, we want an expansion in terms of $t = \frac{r'}{r}$. To do this, we write the expansion as

$$
\frac{1}{4 \pi \abs{\vb{r} - \vb{r'}}} = \frac{1}{4 \pi r} \sum_{n=0}^{\infty} (\frac{r'}{r}) P_n(\vu{r} \vdot \vu{r'})
$$

Here, $P_n(\vu{r} \vdot \vu{r'})$ is a polynomial. Because $\abs{\vb{r} - \vb{r'}}$ is symmetric, we can say that if $r' > r$ instead, simply switch the two. Thus the equation becomes

$$
\frac{1}{4 \pi \abs{\vb{r} - \vb{r'}}} = \frac{1}{4 \pi} \sum_{n=0}^{\infty} (\frac{r'^n_{<}}{r^{n+1}_{>}}) P_n(\vu{r} \vdot \vu{r'})
$$

Where $r_>$ is the greater of $r, r'$, and $r_<$ the lesser.

**Definition**. The polynomials $P_n(x)$ are Legendre Polynomials. We define them as follows:

$$
(1 - 2tx + t^2)^{-\frac{1}{2}} = \sum_{n=0}^\infty t^n P_n(x)
$$

Note that as a quirk of the function, $P_n(1) = 1$ for all $n$.

We can apply these quadrupole and beyond terms to the volate or other equations, however, this becomes very messy.