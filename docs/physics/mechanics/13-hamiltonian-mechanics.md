# Chapter 13 - Hamiltonian Mechanics

## Section 13.1 - The Basic Variables

**Definition**. Consider a Laplacian defined as $\mathcal{L} = \mathcal{L}(q_1, \ldots, q_n, \dot{q}_1, \ldots, \dot{q}_n, t)$. Then, the set of coordinates $q_1, \ldots, q_n$ are the *configuration space* while the set of coordinates $q_1, \ldots, q_n, \dot{q}_1, \ldots, \dot{q}_n$ are known as the *state space*.

Recall that the generalized momenta $p_i$ is also defined such that

$$p_i = \frac{\partial \mathcal{L}}{\partial \dot{q}_i}$$

**Definition**. The generalized momenta is also called the *canonical momentum* or the *momentum conjugate to $q_i$*.

**Definition**.  The *Hamiltonian* is defined as

$$\mathcal{H} = \sum_{i = 1}^n p_i \dot{q_i} - \mathcal{L}$$

## Section 13.2 - Hamilton's Equations for One-Dimensional Systems

We see that for a pendulum, $\mathcal{L} = \frac{1}{2} m L^2 \dot{\phi}^2 - mgL(1 - \cos \phi)$. For a bead sliding on a frictionless wire of height $y = f(x)$, we see $\mathcal{L} = \frac{1}{2}m[1 + f'(x)^2] - mgf(x)$.

Notably, using natural coordinates, $\mathcal{L} = \frac{1}{2}A(q)\dot{q}^2 - U(q)$. Then, we can define $\mathcal{H} = p\dot{q} - \mathcal{L}$.

We know that $p = \frac{\partial \mathcal{L}}{\partial \dot{q}} = A(q)\dot{q}$. Then, $\mathcal{H} = p\dot{q} - \mathcal{L} = A(q)\dot{q}^2 - \frac{1}{2} A(q) \dot{q}^2 + U(q) = 2T - T + U = T + U$

Similarly, we can solve for $\dot{q}$ from the definition of the generalized momentum to see that $\dot{q} = \frac{q}{A(q)}$.

Deriving Hamilton's Equations is thus simple. We see that $\frac{\partial \mathcal{H}}{\partial q} = p \frac{\partial \dot{q}}{\partial q} - [\frac{\partial \mathcal{L}}{\partial q} + \frac{\mathcal{L}}{\partial \dot{q}} \frac{\partial \dot{q}}{\partial q}] = p \frac{\partial \dot{q}}{\partial q} - [\frac{\partial \mathcal{L}}{\partial q} + q\frac{\partial \dot{q}}{\partial q}] = -\frac{\partial \mathcal{L}}{\partial q} = -\dot{p}$

Differentiating instead with respect to $p$, we see that $\frac{\partial \mathcal{H}}{\partial p} = [\dot{q} + p \frac{\partial \dot{q}}{\partial p}] - \frac{\partial \mathcal{L}}{\partial \dot{q}} \frac{\partial \dot{q}}{\partial p} = [\dot{q} + p \frac{\partial \dot{q}}{\partial p}] - p \frac{\partial \dot{q}}{\partial p} = \dot{q}$

## Section 13.3 - Hamilton's Equations in Several Dimensions

We know that

$$\mathcal{H} = \sum_{i = 1}^N p_i \dot{q}_i - \mathcal{L}$$

Here, the generalized momenta are defined as

$$p_i = \frac{\partial \mathcal{L}(\mathbf{q}, \dot{\mathbf{q}}, t)},{\partial \dot{q}_i}$$

This tells us that $\dot{\mathbf{q}} = \dot{\mathbf{q}}(\mathbf{q}, \mathbf{p}, t)$. Then, we can define the Hamiltonian as

$$\mathcal{H} = \mathcal{H}(\mathbf{q}, \mathbf{p}, t) = \sum_{i = 1}^N p_i \dot{q}_i(\mathbf{q}, \mathbf{p}, t) - \mathcal{L}(\mathbf{q}, \dot{\mathbf{q}}(\mathbf{q}, \mathbf{p}, t), t)$$

We can differentiate with respect to $p_i$ to see that

$$\dot{q}_i = \frac{\partial \mathcal{H}}{\partial p_i}$$

We can differentiate with respect to $q_i$ to see that

$$\dot{p}_i = - \frac{\partial \mathcal{H}}{\partial q_i}$$

For a system with $n$ coordinates, this gives us $2n$ first-order differential equations rather than $n$ second-order differential equations as seen in the Lagrange equations.

We then can calculate

$$\frac{d \mathcal{H}}{dt} = \sum_{i=1}^N (\frac{\partial \mathcal{H}}{\partial q_i} \dot{q}_i + \frac{\partial \mathcal{H}}{\partial p_i} \dot{p}_i) + \frac{\partial \mathcal{H}}{\partial t}$$

We can then substitute Hamilton's equations to see that

$$\frac{d \mathcal{H}}{dt} = \frac{\partial \mathcal{H}}{\partial t}$$

From section 7.8, we know that if the relation from the generalized coordinates to rectangular coordinates is independent of $t$ (that is, our generalized coordinates are natural), than $\mathcal{H} = T + U$.

## Section 13.4 - Ignorable Coordinates

**Definition**. If $\mathcal{H}$ is independent of a coordinate $q_i$, it immediately follows that $\dot{p}_i = 0$ and thus $p_i$ is a constant. Note that this definition immediately follows from the Lagrangian definition.

## Section 13.5 - Lagrange's Equations vs. Hamilton's Equations

Skipped.

## Section 13.6 - Phase-Space Orbits

Skipped.

## Section 13.7 - Liouville's Theorem

Skipped.