# Chapter 5 - Electrodynamics with Moving Charges

## Section 5.1 - Currents in Steady-State Regime

We want to work in a steady-state system. Thus, we restrict ourselves to currents that do not change in time.

With math, we see that $\nabla \cdot \mathbf{J}(\mathbf{r}) = -\frac{\partial \rho(\mathbf{r})}{\partial t}$. Since we are only considering a steady-state system, $\nabla \cdot \mathbf{J}_e = \nabla \cdot \mathbf{J}_m = 0$.

**Definition**. The *conductance* of a material is $G = \frac{1}{R}$, where $R$ is the resistance of a material.

For a wire of uniform cross-sectional area, we see that $G = \sigma \frac{A}{L}$, where $A$ is the cross-sectional area, $L$ is the length of the wire, and $\sigma$ is the conductivity of a wire. Inverted, we see that $R$ = $\rho \frac{L}{A}$, where $\rho = \frac{1}{\sigma}$ is the resistivity of the wire.

**Definition**. *Ohm's Law* can be written as $I = G V$, or inverted, $V = IR$. In a wire, we see that current density $\mathbf{} = \frac{I}{A} = \sigma \frac{V}{L} = \sigma \mathbf{E}$

## Section 5.2 - Currents and Curling Fields

We know that $\mathbf{J}_e = \nabla \times{\mathbf{H}}$ and $\mathbf{J}_m = -\nabla \times{\mathbf{E}}$. That is, current densities cause the opposing field to curl.

For a wire with current $I_e$, we see that applying Stoke's theorem to the first equation,

$ \int_S \nabla \times{\mathbf{H}} \cdot \hat{\mathbf{n}} d{S} = \int_{\partial S} = \mathbf{H} \cdot d{\mathbf{l}}$. Apply the identity $\nabla \times{\mathbf{H}} = \mathbf{J}_e$ to the left side to see that $\int_S \nabla \times{\mathbf{H}} \cdot \hat{\mathbf{n}} d{S} = \int_S \mathbf{J}_e \cdot \hat{\mathbf{n}} d{S} = (I_e)_S$, or the current passing through the cross-sectional area. By the original equation, we see that $(I_e)_S = \mathbf{H} \cdot d{\mathbf{l}}$.

If we assume cylindrical coordinates and that $\mathbf{H}(vb{r}) = H_\varphi(s) \hat{\mathbf{\varphi}}$, then $\mathbf{H} \cdot d{\mathbf{l}} = \int_0^{2\pi} H_\varphi(S) s d{\varphi}$, so then $(I_e)_S = \int_0^{2\pi} H_\varphi(S) s d{\varphi}$. Thus, for $s > a$ (where $a$ is the radius of the wire), $2\pi s H_\varphi = I_e$, and for $s < a$, $2\pi s H_\varphi = I_e \frac{s^2}{a^2}$.

---

By Helmholtz Theorem, we know that $\mathbf{H}(\mathbf{r}) = \nabla \times{\mathbf{A}(\mathbf{r})}$. For a current-carrying wire, $\mathbf{A}(\mathbf{r}) = \frac{I_e}{4\pi} \int_{\text{wire}} \frac{d{\mathbf{l'}}}{|\mathbf{r}-\mathbf{r'}|}$. Applying identities, we see the *Law of Biot and Savart$, where

$$
\mathbf{H}(\mathbf{r}) = \int{I_e}{4\pi}\int_{\text{wire}} \frac{-(\mathbf{r}-\mathbf{r'}) \times d{\mathbf{l'}}}{|\mathbf{r}-\mathbf{r'}|^3}
$$

---

Consider a current loop instead, on the $x-y$ plane and current $I$. Then, $r = z \hat{\mathbf{z}}$ and $d{\mathbf{l'}} = R \hat{\mathbf{\varphi'}} d\phi'$, and the magnetic field collapses to $\mathbf{H}(s = 0, z) = \frac{I_e R^2}{2(R^2 + z^2)^{\frac{3}{2}}} \hat{\mathbf{z}}$

---

Consider some infinite bar magnet with height $h$ and width $w$. Then, the top and bottom surfaces will have a magnetic charge with density $\mathbf{J}_m^+ = M_0 \mathbf{b} \delta(z - h)$ and $\mathbf{J}_m^- = -M_0 \mathbf{v} \delta(z)$ respectively. By definition, $I_m = M_0 w v$.

Now, consider a loop around only the top of the conductor. Then,

$$
\int_S \mathbf{J}_m \cdot \hat{\mathbf{n}} d{S} = I_m = M_o w v
$$

By definition,

$$
\int_S \mathbf{J}_m \cdot \hat{\mathbf{n}} d{S} = -\int_S (\nabla \times{\mathbf{E}}) \cdot \hat{\mathbf{n}} d{S}
$$

Applying Stokes theorem,

$$
\int_S (\nabla \times{\mathbf{E}}) \cdot \hat{\mathbf{n}} d{S} = M_0 w v
$$

## Section 5.3 - Forces on Moving Charges and Current

Consider an electric charge moving with velocity $\mathbf{v}$ in a magnetic parallel plate capacitor with charge densities $\pm \sigma_m$. That is, $\mu_0 \mathbf{H} = \sigma_m \hat{\mathbf{z}}$. Then, we can apply theorems to see the resulting force.

**Theorem**. *Lorentz Force Law* states that $\mathbf{F} = q_e \mathbf{v} \times \mu_0 \mathbf{H}$ in the presence of a magnetic field. In the presence of both an electric and magnetic field, $\mathbf{F} = q_e (\mathbf{E} + \mathbf{v} \times \mu_0 \mathbf{H})$.

**Theorem**. *Ampere's Force Law* states that generalizing the previous theorem, we can see that

$$d\mathbf{F} = I_e d{\mathbf{L}} \times \mu_0 \mathbf{H}(\mathbf{r})$$

## Section 5.4 - Multipole Expansion of a Vector Potential

This is messy. Skipped.
