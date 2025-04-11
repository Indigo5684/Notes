# Chapter 8 - Two-Body Central Force Problems

## Section 8.1 - The Problem

Consider two objects in an inertial frame, acted upon by a central force. We know that the Lagrangian is

$$\mathcal{L} = \frac{1}{2}m_1 \dot{\mathbf{r}}_1^2 + \frac{1}{2} m_2 \dot{\mathbf{r}}_2^2$$

## Section 8.2 - CM and Relative Coordinates; Reduced Mass

We know that with $M = m_1 + m_2$, the center of mass becomes

$$\mathbf{R} = \frac{m_1\mathbf{r}_1 + m_2 \mathbf{r}_2}{m_1 + m_2} = \frac{m_1 \mathbf{r}_1 + m_2 \mathbf{r}_2}{M}$$

We know that the total momentum thus can be written as

$$\mathbf{P} = M \dot{\mathbf{R}}$$

As total momentum is conserved, $\dot{\mathbf{R}}$ is constant. Thus, we can choose a reference frame where the center of mass is at rest.

We can thus rewrite our coordinates as

$$\mathbf{r}_1 = \mathbf{R} + \frac{m_2}{M} \mathbf{r} \; \text{and} \; \mathbf{r}_2 = \mathbf{R} - \frac{m_1}{M} \mathbf{r}$$

This uses the center of mass position $\mathbf{R}$ and relative position $\mathbf{r}$

Then, via substitution, we see that kinetic energy becomes

$$T = \frac{1}{2}(M \dot{\mathbf{R}}^2 + \frac{m_1 m_2}{M} \dot{\mathbf{r}}^2)$$

We can introduce $\mu = \frac{m_1 m_2}{M} = \frac{m_1 m_2}{m_1 + m_2}$, or the *reduced mass*, to write $T$ as

$$T = \frac{1}{2}(M \dot{\mathbf{R}}^2 + \mu \dot{\mathbf{r}}^2)$$

Then, we can see that

$$\mathcal{L} = \frac{1}{2} M \dot{\mathbf{R}}^2 + (\frac{1}{2}\mu \dot{\mathbf{r}}^2 - U(R)) = \mathcal{L}_{cm} + \mathcal{L}_{rel}$$

This allows us to solve this as two separate problems.

## Section 8.3 - The Equations of Motion

$\mathcal{L}$ is independent of $\mathbf{R}$, so we know that $\dot{\mathbf{R}}$ is a constant. In other words, $\ddot{\mathbf{R}} = 0$, which means $M \ddot{\mathbf{R}} = 0$.

We can rewrite this as $\mathcal{L}_{cm} = \frac{1}{2} M \dot{\mathbf{R}}$, or the Lagrangian of a free particle.

Additionally, $\mathcal{L}_{rel}$ is indistinguishable from the Lagrangian of a single particle with mass $\mu$ and position $\mathbf{r}$. Then, the corresponding Lagrangian equation becomes

$$\mu \ddot{\mathbf{r}} = -\nabla U(\mathbf{r})$$

**Definition**. In the *CM frame*, the center of mass is at rest. We know that this is an inertial frame as it is not accelerating.

That is, $\ddot{\mathbf{R}} = 0$. Then, the Lagrangian is simply $\mathcal{L} = \mathcal{L}_{rel} = \frac{1}{2}\mu \dot{\mathbf{r}}^2 - U(r)$. It immediately follows that $\mathbf{R}$ is an ignorable coordinate.

**Note**. Know that $\mathbf{r}$ is not the position of either particle, but the position of particle 1 with respect to particle 2. That is, $\mathbf{r}_1 = \frac{m_2}{M} \mathbf{r}$. and $\mathbf{r}_2 = -\frac{m_1}{M}\mathbf{R}$

Since total momentum is zero, we see that both particles must either be still or be moving with opposing momenta.

We can now apply the conservation of angular momentum.

$$\begin{align}
\mathbf{L} &= \mathbf{r}_1 \times \mathbf{p}_1 + \mathbf{r}_2 + \mathbf{p}_2 \\
&= m_1 \mathbf{r}_1 \times \dot{\mathbf{r}}_1 + m_2 \mathbf{r}_2 \times \dot{\mathbf{r}}_2 \\
&= m_1 \frac{m_2}{M} \mathbf{r} \times \frac{m_2}{M}\dot{\mathbf{r}} + m_2 -\frac{m_1}{M}\mathbf{r} \times (-\frac{m_1}{M}) \dot{\mathbf{r}} \\
&= frac{m_1}{m_2}{M^2} (m_2 \mathbf{r} \times \dot{\mathbf{r}} + m_1 \mathbf{r} \times \dot{\mathbf{r}}) \\
&= \mu \mathbf{r} \times \dot{\mathbf{r}}
\end{align}$$

Since angular momentum $\mathbf{L}$ is conserved, we can also state the quantity $\mathbf{r} \times \dot{\mathbf{r}}$ is constant. Particularly, its direction is constant, which means the components remain in a fixed plane. We choose this plane, so this now becomes a two-body problem.

Let us switch to polar coordinates. We know that $\dot{\mathbf{r}}^2 = \dot{r}^2 + r^2 \dot{\phi}^2$. Thus, the Lagrangian becomes

$$\mathcal{L} = \frac{1}{2} \mu \dot{\mathbf{r}}^2 - U(r) = \frac{1}{2}({\mathbf{r}}^2 = \dot{r}^2 + r^2 \dot{\phi}^2) - U(R)$$

We can see that $\phi$ is ignorable, meaning $\mu r^2 \dot{\phi}$ is constant. We know that this quantity is the angular momentum, so $\ell = \ell_z = \mu r^2 \dot{\phi}$.

**Definition**. The Lagrangian equation for $r$, or the *radial equation*, becomes

$$\mu r \dot{\phi}^2 - \frac{dU}{dr} = \mu \ddot{r}$$

We can rewrite this to see that

$$-\frac{dU}{dr} = \mu (\ddot{r} - r \dot{\phi}^2)$$

This then becomes the radial component of $\mathbf{F} = \mu \mathbf{a}$.

## Section 8.4 - The Equivalent One-Dimensional Problem

The angular momentum equation can be solved to see that $\dot{\phi} = \frac{\ell}{\mu r^2}$. We can thus eliminate $\dot{\phi}$ in the radial equation to see that

$$\mu \ddot{r} = - \frac{dU}{dr} + \mu r \dot{\phi}^2 = -\frac{dU}{dr} + F_{cr}$$

Here, we define $F_{cr}$ as some fictitious centrifugal force defined such that

$$F_{cr} = \mu r \dot{\phi}^2 = \frac{\ell^2}{\mu r^3} = -\frac{d}{dr}(\frac{\ell^2}{2\mu r^2}) = - \frac{dU_{cf}}{dr}$$

Thus, with $U_{cr}(r) = \frac{\ell^2}{2\mu r^2}$ this force is conservative.

**Definition**. *Effective potential energy* is defined as $U_{eff}(r) = U(r) + U_{cf}(r)$, so that $\mu \ddot{r} = -\frac{d}{dr} U_{eff}(r)$. Then, the radial motion of the particle is exactly the same as if the particle were moving in one dimension with the effective potential energy.

We can thus multiply through by $\dot{r}$ to see that

$$\begin{align}
\mu \ddot{r} \dot{r} &= -\dot{r}\frac{d}{dr} U_{eff}(r) \\
\frac{d}{dt}(\frac{1}{2} \mu \dot{r}^2) &= -\frac{dr}{dt} \frac{d}{dr} U_{eff}(r) \\
&= -\frac{d}{dt}U_{eff}(r)
\end{align}$$

For this to be true for any positions $\dot{r}$ and $r$, we see that $\frac{1}{2} \mu \dot{r} + U_{eff}(r)$ must be a constant. We can substitute to see that

$$\begin{align}
\frac{1}{2} \mu \dot{r} + U_{eff}(r) &= \frac{1}{2} \mu \dot{r} + U(r) + \frac{\ell^2}{2\mu r^2} \\
&= \frac{1}{2} \mu \dot{r} + U(r) + \frac{(\mu r^2 \dot{\phi})^2}{2\mu r^2} \\
&= \frac{1}{2} \mu \dot{r} + U(r) + \frac{1}{2}\mu r^2 \dot{\phi}^2 \\
&= \frac{1}{2} \mu \dot{r} + \frac{1}{2}\mu r^2 \dot{\phi}^2 \\
&= E
\end{align}$$

This is simply conservation of energy.

## Section 8.5 - The Equation of the Orbit

This gives us an equation for $r(t)$. However, we are also interested in $r = r(\phi)$.

We know that $\mu \ddot{r} = F(r) + F_{cr}(r) = F(r) + \frac{\ell}{\mu r^3}$ This is a bit annoying to work with, so we will replace $r$ with $u$ by

$$u = \frac{1}{r}$$

Now, we can use the chain rule to see that, since $\ell = \mu r^2 \dot{\phi}$, we can write

$$\frac{d}{dt} = \frac{d\phi}{dt} \frac{d}{d\phi} = \dot{\phi} \frac{d}{d\phi} = \frac{\ell}{\mu r^2} \frac{d}{d\phi} = \frac{\ell u^2}{\mu} \frac{d}{d\phi}$$

Then, we can see that

$$\dot{r} = \frac{d}{dt}r = \frac{\ell u^2}{\mu} \frac{d}{d\phi} \frac{1}{u} = -\frac{\ell}{\mu} \frac{du}{d\phi}$$

Subsequently,

$$\ddot{r} = \frac{d}{dt}\dot{r} = \frac{\ell u^2}{\mu} \frac{d}{d\phi} (-\frac{\ell}{\mu} \frac{du}{d\phi}) = -\frac{\ell^2 u^2}{\mu^2} \frac{d^2 u}{d\phi^2}$$

We can substitute this into the differential equation to see that

$$-\frac{\ell^2 u^2}{\mu} \frac{d^2 u}{d\phi^2} = F + \frac{\ell^2 u^3}{\mu}$$

We can then rewrite this as

$$u''(\phi) = -u(\phi) = \frac{\mu}{\ell^2 u(\phi)^2} F$$

## Section 8.6 - The Kepler Orbits

Let us assume our force can be written in the form

$$F(r) = -\frac{\gamma}{r^2} = -\gamma u^2$$

Here, $\gamma$ is the force constant. For gravity, $\gamma = G m_1 m_2$. For the Coulomb force, $\gamma = k q_1 q_2$

This then tells us that

$$u''(\phi) = -u(\phi) = \frac{\gamma\mu}{\ell^2}F$$

We can then substitute $w(\phi) = u(\phi) - \gamma \mu/\ell^2$, and as $\ddot{w} = \ddot{u}$, see that $w'' = -w$ and so

$$w(\phi) = A \cos(\phi - \delta)$$

For a choice of $\phi = 0$, we can cancel $\delta$, so that

$$u(\phi) = \frac{\gamma \mu}{\ell^2} + A \cos \phi = \frac{\gamma \mu}{\ell^2}(1 + \epsilon \cos \phi)$$

Here, we define $\epsilon$ as $\epsilon = A \ell^2 / \gamma \mu$.

We then define some constant $c$ such that $1/c = \gamma \mu / \ell^2$. Then,

$$u = \frac{1}{r} = \frac{1}{c}(1 + \epsilon \phi)$$

This allows us to solve for $r(\phi)$ as

$$r(\phi) = \frac{c}{1 + \epsilon \cos \phi}$$

Given $\epsilon < 1$, we see the orbit is bounded as the denominator never vanishes. Then, we can see minimum and maximum values for $\cos \phi = \pm 1$ Then,

$$r_{min} = \frac{c}{1 + \epsilon} \; \text{ and } r_{max} = \frac{c}{1-\epsilon}$$

**Definition**. The *perihelion* is where $r = r_{min}$. The *aphelion* is where $r = r_{max}$.

We can transform this into an ellipse with the form

$$\frac{(x+d)^2}{a^2} + \frac{y^2}{b^2} = 1$$

This assumes that $a = \frac{c}{1-\epsilon^2}$, $b = \frac{c}{\sqrt{1-\epsilon^2}}$, $d = a\epsilon$.

**Definition**. Now, we see that $b/a = \sqrt{1-\epsilon^2}$, This allows us to define $\epsilon$ as the *eccentricity*. Note if $\epsilon=0$, we recover a circle.

**Theorem**. *Kepler's First Law*. The position of the sun is one of the ellipse's foci.

**Theorem**. *Kepler's Second Law*. The rate at which the line from the sun to a comet sweeps out area is

$$\frac{dA}{dt} = \frac{\ell}{2\mu}$$

We know that $A_{ellipse} = \pi a b$, so the period becomes

$$\tau = \frac{A}{dA/dt} = \frac{(\pi a b) 2\mu}{\ell}$$

We can square both sides, then replace $b^2$ with $a^2(1-\epsilon^2)$, and replace $a(1-\epsilon^2)$ with $c$.

$$\tau^2 = 4\pi^2 \frac{a^2(1-\epsilon^2)\mu^2}{\ell^2} = 4\pi^2 \frac{a^3 c\mu^2}{\ell^2}$$

We then know that $c = \ell^2 / \gamma \mu$, telling us that

$$\tau^2 = 4\pi^2 \frac{a^e \mu}{\gamma}$$

Now, consider energy. We know that $E = U_{eff}(r_{min})$, as we don't want to consider velocity at $r_{max}$ - that's complicated and annoying. Then, we know that

$$U_{eff}(r_{min}) = -\frac{\gamma}{r_{min}} + \frac{\ell^2}{2\mu r_{min}^2} = \frac{1}{2r_{min}}$$

We can recall that $r_{min} = c/(1 + \epsilon)$, and that $c = \ell^2 / \gamma \mu$. Then, we can see that

$$r_{min} = \frac{\ell^2}{\gamma \mu (1+\epsilon)}$$

We can then apply some annoying algebra to see that

$$E = \frac{\gamma \mu(1 + \epsilon)}{2\ell^2}(\gamma(1+\epsilon) - 2\gamma) = \frac{\gamma^2\mu}{2\ell^2}(\epsilon^2-1)$$

Note that negative energies correspond with eccentricities $\epsilon < 1$, which in turn correspond to bounded orbits.

## Section 8.7 - The Unbounded Kepler Orbits

When $\epsilon \geq 1$, then we see that

$$r(\phi) = \frac{c}{1 + \epsilon \cos \phi}$$

has an asymptote. When $\epsilon = 0$ (or $E = 0$), we see that when $\epsilon = \pm \pi$, $r \rightarrow \infty$. Converting to cartesian equations allows us to recover

$$y^2 = c^2 - 2cx$$

This is a parabola.

When $\epsilon > 1$ or $E > 0$, we see that the denominator vanishes when $\epsilon \cos \phi = -1$. Thus, we can find the maximum allowed angle $\phi_{max}$ as

$$\epsilon \cos(\phi_max) = -1$$

We are then confined to the angles $\phi \in (-\phi_{max}, \phi_{max})$. We can then rewrite the equation of motion as

$$\frac{(x-\delta)^2}{\alpha^2}-\frrac{y^2}{\beta^2}=1$$

## Section 8.8 - Changes of Orbit

Let us consider a satellite in orbit.

**Definition**. For a satellite orbiting Earth, the closest and furthest points are referred to as the *perigee* and *apogee* (instead of perihelion and aphelion for the sun).

We know our orbit will follow the path

$$r(\theta) = \frac{c}{1 + \epsilon \cos(\phi - \delta)}$$

We cannot eliminate the $\delta$ parameter via a clever choice of $\phi$ as we are dealing with multiple orbits.

Now, assume the spacecraft is initially in an orbit with energy $E_1$, angular momentum $\ell_1$, and orbital parameters $c_1$, $\epsilon_1,$ and $\delta_1$. Now, to shift orbits, apply an impulse at $\phi = \phi_0$ and causes an instantaneous change of velocity such that the new energy is $E_2$ and new angular momentum is $\ell_2$. We can then calculate the new orbital parameters $c_2$, $\epsilon_2$, and $\delta_2$.

Now, as the orbits must join at $\phi_0$, we can see that

$$\frac{c_1}{1 + \epsilon_1 \cos(\phi_0 - \delta_1)} = \frac{c_2}{1 + \epsilon_2 \cos(\phi_0 - \delta_2)}$$

This is tedious, and if possible, we'd like to avoid it.

Let us assume that we only apply an impulse at the perigee of the initial orbit, and only in the direction of motion. Then, we can use a choice of axis so this occurs  at $\phi = 0$, and thus $\phi_0 = 0$ and $\delta_1 = 0$. As this is the perigee of the final orbit, we also set $\delta_2 = 0$.

Now, we see that

$$\frac{c_1}{1 + \epsilon_1} = \frac{c_2}{1 + \epsilon_2}$$

**Definition**. The *thrust factor* $\gamma$ is a constant such that $v_2 = \gamma v_1$.

As at the perigee, the angular momentum is $\ell = \mu r v$, and as $r$ is fixed during the impulse, we know that $\ell_2 = \gamma \ell_1$. Furthermore, as $c = \ell / \gamma \mu$, we know that $c_2 = \gamma^2 c_1$.

Then, we can apply the equation above to see that

$$\epsilon_2 = \gamma^2 \epsilon_1 + \gamma^2 - 1$$

Notably, if $\gamma > 1$ (a thrust in the direction of motion), then $\epsilon_2 > \epsilon_1$ and vice-versa.
