# Chapter 5 - Electrodynamics with Moving Charges

## Section 5.1 - Currents in Steady-State Regine

We want to work in a steady-state system. Thus, we restrict ourselves to currents that do not change in time.

With math, we see that $\div \vb{J}(\vb{r}) = -\frac{\partial \rho(\vb{r})}{\partial t}$. Since we are only considering a steady-state system, $\div \vb{J}_e = \div \vb{J}_m = 0$.

**Definition**. The *conductance* of a material is $G = \frac{1}{R}$, where $R$ is the resistance of a material.

For a wire of uniform cross-sectional area, we see that $G = \sigma \frac{A}{L}$, where $A$ is the cross-sectional area, $L$ is the length of the wire, and $\sigma$ is the conductivity of a wire. Inverted, we see that $R$ = $\rho \frac{L}{A}$, where $\rho = \frac{1}{\sigma}$ is the resistivity of the wire.

**Definition**. *Ohm's Law* can be written as $I = G V$, or inverted, $V = IR$. In a wire, we see that current density $\vb{} = \frac{I}{A} = \sigma \frac{V}{L} = \sigma \vb{E}$

## Section 5.2 - Currents and Curling Fields

We know that $\vb{J}_e = \curl{\vb{H}}$ and $\vb{J}_m = -\curl{\vb{E}}$. That is, current densities cause the opposing field to curl.

For a wire with current $I_e$, we see that applying Stoke's theorem to the first equation,

$ \int_S \curl{\vb{H}} \vdot \vu{n} \dd{S} = \int_{\partial S} = \vb{H} \vdot \dd{\vb{l}}$. Apply the identity $\curl{\vb{H}} = \vb{J}_e$ to the left side to see that $\int_S \curl{\vb{H}} \vdot \vu{n} \dd{S} = \int_S \vb{J}_e \vdot \vu{n} \dd{S} = (I_e)_S$, or the current passing through the cross-sectional area. By the original equation, we see that $(I_e)_S = \vb{H} \vdot \dd{\vb{l}}$.

If we assume cylindrical coordinates and that $\vb{H}(vb{r}) = H_\varphi(s) \vu{\varphi}$, then $\vb{H} \vdot \dd{\vb{l}} = \int_0^{2\pi} H_\varphi(S) s \dd{\varphi}$, so then $(I_e)_S = \int_0^{2\pi} H_\varphi(S) s \dd{\varphi}$. Thus, for $s > a$ (where $a$ is the radius of the wire), $2\pi s H_\varphi = I_e$, and for $s < a$, $2\pi s H_\varphi = I_e \frac{s^2}{a^2}$.

---

By Helmholtz Theorem, we know that $\vb{H}(\vb{r}) = \curl{\vb{A}(\vb{r})}$. For a current-carying wire, $\vb{A}(\vb{r}) = \frac{I_e}{4\pi} \int_{\text{wire}} \frac{\dd{\vb{l'}}}{|\vb{r}-\vb{r'}|}$. Applying identities, we see the *Law of Biot and Savart$, where

$$
\vb{H}(\vb{r}) = \int{I_e}{4\pi}\int_{\text{wire}} \frac{-(\vb{r}-\vb{r'}) \cross \dd{\vb{l'}}}{|\vb{r}-\vb{r'}|^3}
$$

---

Consider a current loop instead, on the $x-y$ plane and current $I$. Then, $r = z \vu{z}$ and $\dd{\vb{l'}} = R \vu{\varphi'} \dd{\phi'}$, and the magnetic field collapses to $\vb{H}(s = 0, z) = \frac{I_e R^2}{2(R^2 + z^2)^{\frac{3}{2}}} \vu{z}$

---

Consider some infinite bar magnet with height $h$ and width $w$. Then, the top and bottom surfaces will have a magnetic charge with density $\vb{J}_m^+ = M_0 \vb{b} \delta(z - h)$ and $\vb{J}_m^- = -M_0 \vb{v} \delta(z)$ respectively. By definition, $I_m = M_0 w v$.

Now, consider a loop around only the top of the conductor. Then,

$$
\int_S \vb{J}_m \vdot \vu{n} \dd{S} = I_m = M_o w v
$$

By definition,

$$
\int_S \vb{J}_m \vdot \vu{n} \dd{S} = -\int_S (\curl{\vb{E}}) \vdot \vu{n} \dd{S}
$$

Applying Stokes theorem,

$$
\int_S (\curl{\vb{E}}) \vdot \vu{n} \dd{S} = M_0 w v
$$

## Section 5.3 - Forces on Moving Charges and Current

Consider an electric charge moving with velocity $\vb{v}$ in a magnetic parallel plate capacitor with charge densities $\plusminus \sigma_m$. That is, $\mu_0 \vb{H} = \sigma_m \vu{z}$. Then, we can apply theorems to see the resulting force.

**Theorem**. *Lorentz Force Law* states that $\vb{F} = q_e \vb{v} \cross \u_0 \vb{H}$ in the presence of a magnetic field. In the presence of both an electic andmagnetic field, $\vb{F} = q_e (\vb{E} + \vb{v} \cross \u_0 \vb{H})$.

**Theorem**. *Ampere's Force Law* states that generalizing the previous theorem, we can see that

$$
\dd{\vb{F}} = I_e \dd{\vb{L}} \cross \u_0 \vb{H}(\vb{r})
$$

## Section 5.4 - Multipole Expansion of a Vector Potential

This is messy. Skipped.