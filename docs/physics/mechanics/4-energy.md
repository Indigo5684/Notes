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

## Section 4.8 - Central Forces

## Section 4.9 - Energy Interaction of Two Particles

## Section 4.10 - The Energy of a Multiparticle System
