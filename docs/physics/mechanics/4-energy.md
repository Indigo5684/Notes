# Chapter 4 - Energy

## Section 4.1 - Kinetic Energy and Work

**Theorem**. Work-Energy Theorem. $\frac{dT}{dt} = \frac{1}{2} m \frac{d}{dT}v^2 = \frac{1}{2} m \frac{d}{dT}(\mathbf{v} \cdot \mathbf{v}) = \frac{1}{2} m (\dot{\mathbf{v}} \cdot \mathbf{v} + \mathbf{v} \cdot \dot{\mathbf{v}}) = m \dot{\mathbf{v}} \cdot \mathbf{v} = \mathbf{F} \cdot \mathbf{v}$. Then, we can see that $dT = \mathbf{F} \cdot d\mathbf{r}$, where $\mathbf{F} \cdot d\mathbf{r}$ is the work done by force $\mathbf{F}$ over a small displacement $d\mathbf{r}$.

## Section 4.2 - Potential Energy and Conservative Forces

**Theorem**. For a force to be conservative, it must be able to be written as some $\mathbf{F}(\mathbf{r}) = f(r) \hat{\mathbf{r}}$.

**Theorem**. For a conservative force (and thus a conservative vector field), we can apply the *Fundamental Theorem of Line Integrals* to see that $\int_1^2 \mathbf{F} \cdot d\mathbf{r} = F(2) - F(1)$, where $F$ is the antiderivative of the integral. That is, the work done by said force is independent of the path taken.

**Theorem**. For a conservative force, we can find some function $U(r)$, where $U(r)$ is the *potential* of said force. This function will make the *mechanical energy* of a system $E = T + U$ a constant.

In the presence of a nonconservative force, we see that $W = W_{cons} + W_{nc}$. We can then rewrite $\Delta E = \Delta(T + U) = W_{nc}$. Mechanical energy is no longer conserved, but the change in energy is equal to the work done by nonconservative forces.

## Section 4.3 - Force as the Gradient of Potential Energy

We know that $W = \mathbf{F} \cdot d\mathbf{r} = F_x dx + F_y dy + F_z dz$.

Additionally, $W = -dU = -[U(\mathbf{r} + d\mathbf{r}) - U(\mathbf{r})] = -[U(x + dx, y + dy, z + dz) - U(x, y, z)] = -[\frac{\partial U}{\partial x}dx + \frac{\partial U}{\partial y} dy + \frac{\partial U}{\partial z} dz]$.

We can match terms to see that $F_x = -\frac{\partial U}{\partial x}$ and so on, so that $\mathbf{F} = -[\hat{\mathbf{x}} \frac{\partial U}{\partial x} + \hat{\mathbf{y}} \frac{\partial U}{\partial y} + \hat{\mathbf{z}} \frac{\partial U}{\partial z}] = -\nabla U$

## Section 4.4 - The Second Condition that F be Conservative

An easier way to prove a force is conservative is to show that $\nabla \times \mathbf{F} = 0$.

If this is true, then $\oint_\Gamma (\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} = 0$. We can split the curve $\Gamma$ into $\mathbf{r}_1$ and $\mathbf{r}_2$, to show that $0 = \int_1^2 \mathbf{F} \cdot d\mathbf{r}_1 + \int_2^1 \mathbf{F} \cdot d\mathbf{r}_2$, so then $\int_1^2 \mathbf{F} \cdot d\mathbf{r}_1 = \int_1^2 \mathbf{F} \cdot d\mathbf{r}_2$ and thus the integral is path independent.

## Section 4.5 - Time-Dependent Potential Energy

Sometimes, $\mathbf{F} = \mathbf{F}(\mathbf{r}, t)$. Then, if the curl of the force is zero, the work integral is now path-independent. We can define the potential as $U(\mathbf{r}, t) = -\int_{\mathbf{r}_0}^\mathbf{r} \mathbf{F}(\mathbf{r}', t) \cdot d\mathbf{r}'$.

In this case, it is still true that $\mathbf{F}(\mathbf{r}, t) = -\nabla U(\mathbf{r}, t)$. Again, $dT = \frac{dT}{dt} dt = (m \hat{\mathbf{v}} \cdot \mathbf{v}) dt = \mathbf{F} \cdot d\mathbf{r}$.

However, we see that $dU = \frac{\partial U}{\partial x}dx + \frac{\partial U}{\partial y} dy + \frac{\partial U}{\partial z} + \frac{\partial U}{\partial t} dt$. Then, we see that $dU = -\mathbf{F} \cdot d\mathbf{r} + \frac{\partial U}{\partial t} dt$.

Then, $dE = d(T + U) = \frac{\partial U}{\partial t} dt$. So, energy is only conserved if $\frac{\partial U}{\partial t} = 0$.

## Section 4.6 - Energy for Linear One-Dimensional Systems

For a particle only moving in the $x$-direction, we can define $U(x) = -\int_{x_0}^x F_x(x') dx'$. If we let $F_x = -kx$ (by Hooke's law), we see that $U = \frac{1}{2} kx^2$.

We can plot the potential energy as a function of $x$, and visually see what position an object will tend towards. Notably, where $dU/dx = 0$ and $U$ is at a minimum or maximum, net force is zero.

**Definition**. When $d^2 U/dx^2 > 0$ and $U(x)$ is at a minimum, the particle is said to be at *stable* equilibrium. That is, a small displacement will lead to a corrective force. When $d^2 U / dx^2 < 0$ and $U(x)$ is at a maximum, the particle is said to be *unstable*. In this case, a small displacement will result in a force moving the particle further from equilibrium.

Additionally, in one-dimensional systems, $E = T + U(x)$ and $T(x) = \frac{1}{2} m \dot{x} = E - U(x)$, so we can solve for $\dot(x) = \pm \sqrt{\frac{2}{m}} \sqrt{E - U(x)}$

If we then let $dt = \frac{dx}{\dot{x}}$, so that $t = \sqrt{\frac{m}{2}} \int_{x_0}^x \frac{dx'}{\sqrt{E - U(x')}}$, we can then perform the integral and solve for $x$.

## Section 4.7 - Curvilinear One-Dimensional Systems

Consider the direction of motion $s$ such that $T = \frac{1}{2} m \dot{s}$, in which the direction of motion is not in a fixed direction. Notably, the normal force is constraining the object to a fixed path, yet doesn't move the object and thus does no work. Thus, it is the force tangential to the path that does work. We can see then that

$$F_{\perp} = m \ddot{s}$$

Here, we can define a potential $U(s)$ such that $F_{tang} = -dU/ds$ and the total mechanical energy $E = T + U(s)$ is constant.

**Definition**. In an Atwood machine, there are two masses of mass $m_1$ and m_2$, suspended with an inextensible massless string over a pulley. The system can be constrained by a single parameter $x$, where $x$ is the vertical distance from the center of the pulley and the center of mass of $m_1$.

Then, we can see that $\Delta T_1  + \Delta U_1 = W_1^{tension}$, and respectively $\Delta T_2 + \Delta U_2 = W_2^{tension}$. Then, we can see that $W_1^{tension} = -W_2^{tension}$, so $\Delta(T_1 + U_1 + T_2 + U_2) = 0$. That is, $E = T_1 + U_1 + T_2 + U_2$, which is conserved.

Notably, if all forces are conservative, we can define a potential $U_\alpha$ for each particle $\alpha$ such that

$E = \sum_\alpha^N (T_\alpha U_\alpha)$

## Section 4.8 - Central Forces

**Definition**. A central force is some force such that $\mathbf{F}(\mathbf{r}) = f(\mathbf{r}) \hat{\mathbf{r}}$..

**Definition**. A *spherically symmetric* or *rotationally invariant* force is a force such that $f(\mathbf{r}) = f(r)$. Notably, this is equivalent to the force being conservative.

This book uses spherical polar coordinates.

**Definition**. $\phi$, the *azimuth*, is the angle between the $x$-axis and the projection of the vector $\mathbf{r}$ on the $x$-$y$ plane.

This book uses the convention of $r$, $\theta$, and $\phi$, where $x = r \sin \theta \cos \phi$, $y = r \sin \theta \sin \phi$, and $z = r \cos \theta$. That is, $\theta$ is the only angle extending into the $z$-direction.

Recall that the dot product is defined as normal.

Additionally, we see that $d\mathbf{r} = dr \hat{\mathbf{r}} + r d\theta \hat{\mathbf{\theta}} + r \sin \theta d \phi$. Then, as $df = \nabla f \cdot d\mathbf{r}$, we see that $df = (\nabla f)_r dr + (\nabla f)_\theta r d\theta + (\nabla f)_\phi r \sin \theta d\phi$.

Notably, $(\nabla f)_r = \frac{\partial f}{\partial r}$, $(\nabla f)_\theta = \frac{1}{r} \frac{\partial f}{\partial \theta}$, and $(\nabla f)_\phi = \frac{1}{r \sin \theta} \frac{\partial f}{\partial \phi}$.

An important detail is that for $\mathbf{F}(\mathbf{r}) = -\nabla U = f(r) \hat{\mathbf{r}}$, this forces $U = U(r)$.

## Section 4.9 - Energy Interaction of Two Particles

Consider two particles, with forces $\mathbf{F}_{12}$ the force on particle $1$ by particle $2$ and the equal and opposite force $\mathbf{F}_{21}$. Notably, we can write $\mathbf{F}_{12} = f(r) \hat{\mathbf{r}} = f(r) \frac{\mathbf{r}}{r}$.

For two forces not at the origin, we see that $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$ for $\mathbf{F}_{12}$. As a consequence, we tend to write $\mathbf{F}_{12} = \mathbf{F}_{12} (\mathbf{r}_1 - \mathbf{r}_2)$.

We can extend this to the potential. If we fix $\mathbf{r}_2$, we see that $\mathbf{F}_{12} = -\nabla_1 U(\mathbf{r}_1)$, and for an unfixed second particle, $\mathbf{F}_{12} = -\nabla_1 U(\mathbf{r}_1 - \mathbf{r}_2)$.

An important note is that $\nabla_1 U(\mathbf{r}_1 - \mathbf{r}_2) = -\nabla_2 U(\mathbf{r}_1 - \mathbf{r}_2)$. We can then say that $\mathbf{F}_{21} - \nabla_2 U(\mathbf{r}_1 - \mathbf{r}_2)$.

Now, we can generalize this to see that $W_{tot} = d\mathbf{r}_1 \cdot \mathbf{F}_{12} + d\mathbf{r}_2 \cdot \mathbf{F}_{21} = (d\mathbf{r}_1 - d\mathbf{r}_2) \cdot \mathbf{F}_{12} = d(\mathbf{r}_1 - \mathbf{r}_2) \cdot [-\nabla_1 U(\mathbf{r}_1 - \mathbf{r}_2)] = -dU$. We then see that $d(T + U) = 0$. That is, $E = T_1 + T_2 + U$.

Recall elastic collisions, in which $T_{in} = T_{fin}$.

## Section 4.10 - The Energy of a Multiparticle System

Consider a system with $N$ particles, each donated $\alpha. Then, we see that

$$T = \sum_\alpha T_\alpha = \sum_\alpha \frac{1}{2}m_\alpha v_\alpha^2$$

Assuming all forces are conservative, for each pair of particles $\alpha \beta$, there exists a potential energy $U_{\alpha\beta}$ between the two. Then, total potential energy can be written as

$$U = U^{int}+U^{ext} = \sum_\alpha \sum_{\beta > \alpha} U_{\alpha \beta} + \sum_\alpha U_\alpha$$

With this, the net force on any particle is given by $-\nabla_\alpha U$, and total energy is conserved given no external potential energy.

For a rigid body, we can they state $U^{int} = \sum_\alpha \sum_{\beta > \alpha} U_{\alpha \beta}(\mathbf{r}_\alpha - \mathbf{r}_\beta)$. In the case that the forces are central, $U^{int} = \sum_\alpha \sum_{\beta > \alpha} U_{\alpha \beta}(|\mathbf{r}_\alpha - \mathbf{r}_\beta|)$.
