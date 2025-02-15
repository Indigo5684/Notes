# Chapter 3 - Momentum and Angular Momentum

## Section 3.1 - Conservation of Momentum

Consider a system of $N$ particles, indexed with $\alpha \in {1, 2, \ldots, N}$. We found that as long as Newton's third law applies, $\mathbf{P} = \mathbf{p}_1 + \ldots + \mathbf{p}_N = \sum \mathbf{p}_\alpha$ is determined entirely by external forces. That is, $\dot{\mathbf{P}} = F^{ext}$.

## Section 3.2 - Rockets

Consider a rocket with mass $m$ traveling in the $\hat{\mathbf{x}}$ direction and exhausting fuel at a rate of $dm$ at speed $v_{ex}$. At time $t$, the rocket's momentum is $P(t) = mv$. Then, $P(t + dt) = (m + dm)(v + dv)$, where the fuel ejected in time $dt$ has mass $-dm$ and velocity $v - v_{ex}$ relative to the ground. Thus, the total momentum becomes $P(t + dt) = (m + dm)(v + dv) - dm(v - v_{ex}) = mv + m dv + dm v_{ex}$, as $dm dv$ becomes infinitesimally small.

Then, $dP = P(t + dt) - P(t) = m dv + dm v_{ex}$. If there is a net external force, this would equal $F^{ext}dt$. In this case, we assume $F^{ext} = 0$. Then, $m dv = -dm v_ex$, or $m \dot{v} = -\dot{m} v_ex$. This is Newton's second law, where $F = m \dot{v} = -\dot{m} v_ex$.

**Definition**. Conventionally, we say *thrust* is $-\dot{m} v_{ex}$.

We  can solve this via separation of variables. If $v_{ex}$ is constant, we see $v - v_0 = v_{ex} \ln\frac{m_0}{m}$.

## Section 3.3 - The Center of Mass

**Definition**. Given a system of $\alpha \in {1, \ldots, N}$ particles, we define the *center of mass* of the system with respect to the origin O is

$$\mathbf{R} = \frac{1}{M} \sum_{\alpha = 1}^{N} m_\alpha \mathbf{r}_\alpha$$

This is effectively a weighted average of the positions with masses as weights. Using this definition, we can rewrite the total momentum as

$$\mathbf{P} = \sum_\alpha \mathbf{p}_\alpha = \sum_\alpha m_\alpha \dot{\mathbf{r}}_\alpha = M \dot{\mathbf{R}}$$

Notably, this says that the total momentum of a mass of particles can be replaced by one particle with the same momentum of the center of mass.

We know that $\dot{\mathbf{P}} = \mathbf{F}^{ext}$, so we can then say that $\mathbf{F}^{ext} = M \ddot{\mathbf{R}}$. That is, the center of mass moves as if it was a single particle with mass $M$ subject to the net external force. This is why we can approximate bodies as single point masses.

Note that when mass is distributed evenly, we see that if

$$\mathbf{R} = \frac{1}{M} \int \mathbf{r} dm = \frac{1}{m} \int \rho \mathbf{r} dV$$

## Section 3.4 - Angular Momentum for a Single Particle

**Definition**. Angular momentum for a single particle is defined as $\mathbf{\ell} = \mathbf{r} \times \mathbf{p}$. Note that as $\mathbf{r}$ is origin-dependent, so is $\mathbf{\ell}$. With a vector identity, we see that

$$\dot{\mathbf{\ell}} = \frac{d}{dt}(\mathbf{r} \times \mathbf{p}) = (\dot{\mathbf{r}} \times \mathbf{p}) + (\mathbf{r} \times \dot{\mathbf{p}})$$

Notably, we can replace $\mathbf{p} = m \dot{\mathbf{r}}$, so we say that $\dot{\mathbf{r}} \times \mathbf{p} = \dot{\mathbf{r}} \times m \dot{\mathbf{r}} = 0$, so

$$\dot{\mathbf{\ell}} = \mathbf{r} \times \dot{\mathbf{p}} = \mathbf{r} \times m \ddot{\mathbf{r}} = \mathbf{r} \times \mathbf{F} = \mathbf{\Gamma}$$

Here, $\mathbf{\Gamma}$ represents the net torque about the origin $O$ on the particle, defined as $\mathbf{r} \times \mathbf{F}$. This is often described as the rotational form of Newton's second law.

Note that in many one-particle systems, the origin $O$ is deliberately chosen such that $\mathbf{\Gamma} = 0$, so that the angular momentum is constant.

**Definition**. For a *central* force between objects, $\mathbf{F}$ is parallel to the vector between the two objects.

We will now attempt to prove Kepler's Second Law. Consider a planet at position $\mathbf{r}$ orbiting a star at the origin $O$. Then, we define $d\mathbf{r} = \mathbf{v} dt$ as the planet moves from position $P$ to position $Q$ in its orbit. The area swept out by the planet when orbiting thus becomes $dA = \frac{1}{2} |\mathbf{r} \times d\mathbf{r} = \frac{1}{2} |\mathbf{r} \times \mathbf{v} dt|$. As $\mathbf{p} = m\mathbf{v}$, we can say that $\mathbf{v} = \frac{\mathbf{p}}{v}$, so that $dA = \frac{1}{2m} |\mathbf{r} \times \mathbf{p}| = \frac{\ell dt}{2m}$, and we can say that $\frac{dA}{dt} = \frac{\ell}{2m}$. This is constant.

An alternative proof shows that $\ell = mr^2 \omega$ where $\omega = \dot{\phi}$, so that $\frac{dA}{dt} = \frac{1}{2} r^2 \omega$.

## Section 3.5 - Angular Momentum for Several Particles

Next, define a system with $\alpha$ particles, where each particle has angular momentum $\mathbf{\ell}_\alpha = \mathbf{r}_\alpha \times \mathbf{p}_\alpha$, with common origin $O$. We can then define total angular momentum as

$$\mathbf{L} = \sum_{\alpha=1}^N \mathbf{\ell}_\alpha = \sum_{\alpha = 1}^N \mathbf{r}_\alpha \times \mathbf{p}_\alpha$$

We can then differentiate to see that

$$\dot{\mathbf{L}} = \sum_{\alpha=1}^N \dot{\mathbf{\ell}}_\alpha = \sum_{\alpha = 1}^N \mathbf{r}_\alpha \times \mathbf{F}_\alpha$$

Then, we see the rate of change of angular momentum is simply net torque on the system.

We can then state that $\mathbf{F}_alpha = \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta} + \mathbf{F}_\alpha^{ext}$. Then,

$$\dot{\mathbf{L}} = \sum_\alpha \sum_{\beta \neq \alpha} \mathbf{r}_\alpha \times \mathbf{F}_{\alpha \beta} + \sum_\alpha \mathbf{r}_\alpha \times \mathbf{F}_\alpha^{ext}$$

Now, we cam convert the force between particles in the double sum by pairing forces.

$$\sum_\alpha \sum_{\beta \neq \alpha} \mathbf{r}_\alpha \times \mathbf{F}_{\alpha \beta} = \sum_\alpha \sum_{\beta > \alpha} (\mathbf{r}_\alpha \times \mathbf{F}_{\alpha \beta} + \mathbf{r}_\beta \times \mathbf{F}_{\beta \alpha})$$

Then, if we assume all internal forces obey the third law such that $\mathbf{F}_{\alpha \beta} = -\mathbf{F}_{\beta\alpha}$, we can write that

$$\sum_\alpha \sum_{\beta > \alpha} (\mathbf{r}_\alpha \times \mathbf{F}_{\alpha \beta} + \mathbf{r}_\beta \times \mathbf{F}_{\beta \alpha}) = \sum_\alpha \sum_{\beta > \alpha} (\mathbf{r}_\alpha \times \mathbf{F}_{\alpha \beta} - \mathbf{r}_\beta \times \mathbf{F}_{\alpha\beta}) = \sum_\alpha \sum_{\beta > \alpha} (\mathbf{r}_\alpha - \mathbf{r}_\beta) \times \mathbf{F}_{\alpha\beta}$$

We can denote $\mathbf{r}_{\alpha}{\beta} = \mathbf{r}_\alpha - \mathbf{r}_\beta$ as the vector pointing from $\beta$ to $\alpha$. Thus,

$$\sum_\alpha \sum_{\beta \neq \alpha} \mathbf{r}_\alpha \times \mathbf{F}_{\alpha \beta} = \sum_\alpha \sum_{\beta > \alpha} (\mathbf{r}_\alpha - \mathbf{r}_\beta) \times \mathbf{F}_{\alpha\beta}$$

If the internal forces are all central, the cross product becomes zero. Then, the rate of change of angular momentum becomes

$$\dot{\mathbf{L}} = \sum_\alpha \mathbf{r}_\alpha \times \mathbf{F}_\alpha^{ext} = \mathbf{\Gamma}^{ext}$$

where $\mathbf{\Gamma}^{ext}$ is the net external torque. Notably, if this value is $0$, the total angular momentum is a constant.

**Definition**. About any axis of rotation $\hat{\mathbf{k}}$, if an object is rotating at angular velocity $\omega$, then $L_k$, the angular momentum in the $\hat{\mathbf{k}}$-direction, can be written as $L_k = O \omega$, where $I$ is the *moment of inertia* of the object. For any multi-particle system, $I = \sum m_\alpha \rho_\alpha^2$, where $\rho_\alpha$ is the distance from particle $\alpha$ to the axis of rotation.
