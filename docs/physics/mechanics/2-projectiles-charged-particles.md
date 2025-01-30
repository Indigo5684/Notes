# Chapter 2 - Projectiles and Charged Particles

## Section 2.1 - Air Resistance

**Definition**. The *drag*, or resistive force on an object due to the atmosphere, is denoted as $\vb{f}$. Note that this is **not** the force density, but the overall force. In most cases, this force directly opposes the direction of motion. If not, the other component is known as *lift*, however this is mostly negligible.

We define air resistance as $\vb{f} = -f(v) \vu{v}$. We consider two types in this text: linear, where $f(v) = f_{lin} = bv$, and quadratic, where $f(v) = f_{quad} = cv^2$. Note that often times we consider both, and state that $f(v) = f_{lin} + f_{quad} = bv + cv^2$.

The linear term comes from viscous drag and is generally proportional to the viscosity of the medium, while quadratic drag tends to arise from the particle needing to accelerate the mass of air which it is constantly colliding against.

In some cases, we can calculate these coefficients. With $D$ as the diameter of a spherical object, and $\beta$ and $\gamma$ as properties of the medium, we can state that $b = \beta D$ and $c = \gamma D^2$. In air at STP, $\beta = 1.6 \times 10^{-4} \text{N} \vdot \text{s}/\text{m}^2$, and $\gamma = 0.25 \text{N} \vdot \text{s}^2/\text{m}^4$.

Oftentimes, one factor is far more impactful than the other, meaning that the smaller of the two may be neglected. To do so, compute the following ratio:

$$\frac{f_{quad}}{f_{lin}} = \frac{cv^2}{bv} = \frac{\gamma D}{\beta}v$$

Note that the result is expected to be of the same order of magnitude as the *Reynolds number* $R = Dv \mathcal{Q}/\eta$, where $\mathcal{Q}$ is the density of the medium and $\eta$ the viscosity.

## Section 2.2 - Linear Air Resistance

