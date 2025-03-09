# Chapter 7 - Lagrange's Equations

## Section 7.1 - Lagrange's Equations for Unconstrained Motion

Consider a particle experiencing unconstrained motion in three dimensions and subject to some conservative net force $\mathbf{F}(\mathbf{r})$. Then, we see that

$$T = \frac{1}{2}mv^2 = \frac{1}{2}m\dot{\mathbf{r}}^2 = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2)$$

Naturally, $U = U(\mathbf{r}) = U(x, y, z)$.

**Definition**. The *Lagrangian function* or *Lagrangian* is then $\mathcal{L} = T - U$.

We can calculate that $\frac{\partial \mathcal{L}}{\partial x} = -\frac{\partial U}{\partial x} = F_x$, and which by Newton's second law, $F_x = \dot{p}_x$. Additionally, we can see that $\frac{\partial \mathcal{L}}{\partial \dot{x}} = m\dot{x} = p_x$, so then $\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{q_i}} = \dot{p}_x$. An important note is that these derivatives are taken holding the higher and lower order derivatives constant. Thus, we see that

$$\frac{\partial \mathcal{L}}{\partial x} = \frac{d}{dt} \frac{\partial \mathcal L}{\partial \dot{x}}$$

This holds true in $y$ and $z$ as well. This tells us that Newton's second law is equivalent to the Lagrange equations.

**Theorem**. Hamilton's Principle. The actual path in which a particle flows between points $1$ and $2$ in a given time $t_1$ to $t_2$ is such that the action integral $S$ is stationary on the given path. Here,

$$S = \int_{t_1}^{t_2} \mathcal{L} dt$$

It is important to note that if we switch to a coordinate system with coordinates $q_1, q_2, q_3$, in order for this criterion to hold, the Lagrangian must be written in an inertial reference frame (that is, $F_{q_i} = \dot{p_i}$).

**Definition**. The *generalized force* of a system can be expressed in terms of the Lagrangian, where $\frac{\partial \mathcal{L}}{\partial q_i}$ is the $i$-th component of generalized force.

**Definition**. The *generalized momentum* of a system can be expressed in terms of the Lagrangian, where $\frac{\partial \mathcal{L}}{\partial \dot{q}_i}$ is the $i$-th component of generalized momentum.

Notably, when using polar or cylindrical coordinates, the $\phi$-component of generalized momentum is the angular momentum of the system.

With $N$ unconstrained particles, we see $3N$ equations.

## Section 7.2 - Constrained Systems, an Example

Consider a pendulum with mass $m$, constrained by $\sqrt{x^2 + y^2} = l$. Now, we can clearly see that $T = \frac{1}{2} m v^2 = \frac{1}{2}l^2\dot{\phi}^2$, and $U = mgh = mgl(1 - \cos \phi)$. Then,

$$\mathcal{L} = T - U = \frac{1}{2}l^2\dot{\phi}^2 - mgl(1 - \cos \phi)$$

Then, we see that solving the $\phi$ component of Lagrange's equations,

$$-mgl \sin \phi = \frac{d}{dt}(ml^2 \dot{\phi})$$

We know that $ml^2 = I$ is the pendulum's moment of inertia, $(mg) * (-l)\sin\theta$ is the torque on the pendulum, and $\ddot{\phi}$$ is the angular acceleration $\alpha$, the equation then becomes

$$\Gamma = I \alpha$$

## Section 7.3 - Constrained Systems in General

Consider a system with $N$ particles, indexed by $\alpha = 1, \ldots, N$, and positions $\mathbf{r}_\alpha$. We can then say that $q_1, \ldots, q_n$ are a set of generalized coordinates for the system if and only if each $r_\alpha$ can be expressed as a function of the generalized coordinates and time, so that

$$\mathbf{r}_\alpha = \mathbf{r}_\alpha(q_1, \ldots, q_n, t)$$

Conversely, we can write each $q_i$ in terms of the positions and time, so that

$$q_i = q_i(\mathbf{r}_1, \ldots, \mathbf{r}_N, t)$$

Additionally, we require $n$ to be minimal. Then, this implies that $n \leq 3N$.

**Definition**. We define a set of coordinates $q_1, \ldots, q_n$ as *natural* if the transformation between the set and cartesian coordinates is time-independent.

**Definition**. The number of *degrees of freedom* of a system is the number of coordinates that can be independently varied in a small displacement. That is, it is the number of variables that are free parameters of the system.

**Definition**. A *constrained* $N$-particle system is one in which the number of degrees of freedom of the system is less than $3N$.

**Definition**. A *holonomic* system is one in which the number of degrees of freedom is the same as the number of generalized coordinates.

Consider a ball on a surface that is free to roll but not slide or spin. Then, it has two degrees of freedom ($x$ and $y$). However, to describe the system we must indicate rotation as well, so that it requires five generalize coordinates.

## Section 7.4 - Proof of Lagrange's Equations with Constraints

Let us consider the case of one particle constrained to a surface so that it can be described as a holonomic system with two generalized coordinates $q_1$ and $q_2$. Then, we can see that there are two kinds of forces on the particle: the force of constraint, and any non-constraint forces.

For this problem, we will denote the non-constraint forces as $\mathbf{F}$ such that $\mathbf{F} = -\nabla U(\mathbf{r}, t)$. Then, we can define the Lagrangian as usual, so that $\mathcal{L} = T - U$.

Now, consider any two points $\mathbf{r}_1$ and $\mathbf{r}_2$, at which the particle passes through at times $t_1$ and $t_2$ respectively. Then, we can denote the "correct" path as $\mathbf{r}(t)$ and any other path as $\mathbf{R}(t) = \mathbf{r}(t) + \mathbf{\epsilon}(t)$. By the endpoint constraints, we see that $\mathbf{\epsilon}(t_1) = \mathbf{\epsilon}(t_2) = 0$

Now, we can define the action integral $S$ as

$$S = \int_{t_1}^{t_2} \mathcal{L}(\mathbf{R}, \dot{\mathbf{R}}, t) dt$$

If we let $S_0$ be the value of $S$ when $\mathbf{R} = \mathbf{r}$, we see that then for some path, we can write $\delta S = S - S_0$ for some difference in paths $\mathbf{\epsilon}(t)$.

We can then substitute to see that $\delta \mathcal{L} = \mathcal{L}(\mathbf{R}, \dot{\mathbf{R}, t}) - \mathcal{L}(\mathbf{r}, \dot{\mathbf{r}}, t)$. Then, substituting the formulas for the Lagrangian and for any arbitrary path, we see that, neglecting any $\mathbf{\epsilon}^2$ terms,

$$\delta \mathcal{L} = \frac{1}{2}m [(\dot{\mathbf{r}} + \dot{\mathbf{\epsilon}})^2 - \dot{\mathbf{r}}^2] - [U(\mathbf{r} + \mathbf{\epsilon}, t) - U(\mathbf{r}, t)] = m \dot{\mathbf{r}} \cdot \dot{\mathbf{\epsilon}} - \mathbf{\epsilon} \cdot \nabla U$$

We can then see that

$$\delta S = \int_{t_1}^{t_2} \delta \mathcal{L} dt = \int_{t_1}^{t_2} [m \dot{\mathbf{r}} \cdot \dot{\mathbf{\epsilon}} - \mathbf{\epsilon} \cdot \nabla U] dt$$

This can be solved to see that $\delta S = -\int_{t_1}^{t_2} \mathbf{\epsilon} \cdot[m\ddot{\mathbf{r}} + \nabla U] dt$. We see then that $m \ddot{\mathbf{r} } = F_{tot} = F_{constraint} + F$, which implies that $\delta S = -\int_{t_1}^{t_2} \mathbf{\epsilon} \cdot \mathbf{F}_{constraint}$. As $\mathbf{\epsilon}$ is in the plane of motion and the constraint force is normal to the plane, we see that $\delta S = 0$.

## Section 7.5 - Examples of Lagrange's Equations

This is only examples. Skipped.

## Section 7.6 - Generalized Momenta and Ignorable Coordinates

We can  write the generalized equations for force and momentum as

$$F_i = \frac{d}{dt}p_i$$

In general, the generalized force and momenta are not the same as the usual, as the coordinate system is not usually cartesian.

**Definition**. If the Lagrangian is independent of a coordinate $q_i$, then the coordinate's momentum is conserved, and the coordinate is said to be *ignorable* or *cyclic*.

The connection between the invariance of the Lagrangian and certain conservation laws is known as *Noether's Theorem*.

## Section 7.7 - Conclusion

Skipped.

## Section 7.8 - More about Conservation Laws

Skipped.

## Section 7.9 - Lagrange's Equations for Magnetic Forces

Skipped.

## Section 7.10 - Lagrange Multipliers and Constraint Forces

Skipped.
