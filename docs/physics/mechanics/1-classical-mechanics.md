# Chapter 1 - Classical Mechanics

## Section 1.2 - Space and Time

Each point $P \in \mathbb{R}^3$ can be written as $(x, y, z)$. However, we will utilize the convention below:

$$\mathbf{r} = x \hat{\mathbf{x}} + y \hat{\mathbf{y}} + z \hat{\mathbf{z}}$$

However, when working with ambiguous unit basis, it may be better to use the following:

$$\mathbf{r} = r_1 \hat{\mathbf{e_1}} + r_2 \hat{\mathbf{e_2}} + r_3 \hat{\mathbf{e_3}}$$

Here, $r_1 = x, r_2 = y, r_3 = z$ and $\hat{\mathbf{e_1}} = \hat{\mathbf{x_1}}, \ldots$. That is, $\mathbf{r} = \sum r_i \hat{\mathbf{e_i}}$.

Vectors are an $\mathbb{R}$-module, with addition defined component-wise. Additionally, the scalar (dot) product and vector (cross) product are defined as usual.

Regarding time, classically, time is universal.

**Definition**. *Reference frames* are frames of motion with a defined coordinate system and origin position.

**Definition**. *Inertial frames* are reference frames in which Newton's laws of motion hold true. An inertial frame may not be accelerating.

## Section 1.3 - Mass and Force

**Definition**. The *mass* $m$ of an object characterizes its translational inertia, and is measured in kilograms (kg)

**Definition**. The *force* $\mathbf{F}$ exerted on an object is a push or pull on said object and is measured in Newtons (N). Note that force is a vector.

## Section 1.4 - Newton's First and Second Laws; Inertial Frames

**Definition**. A *point mass* or *particle* is a convenient fiction, in which an object with mass has no size. It may move in space but has no internal degrees of freedom. Additionally, it may not have any rotational or vibrational kinetic energy.

**Theorem**. Newton's First Law. In the absence of external forces, a particle moves with constant velocity $\mathbf{v}$.

**Theorem**. Newton's Second Law. Given any particle with mass $m$, the net force $\mathbf{F}$ on the particle is always equal to the particle's mass times its acceleration. That is,

$$\mathbf{F} = m\mathbf{a} = m dot{\mathbf{r}}$$

This can also be rewritten in terms of momentum. We know that momentum $\mathbf{p}$ can be written as $\mathbf{p} = m\mathbf{v} = m \dot{\mathbf{r}}$. Then,

$$\mathbf{F} = m\mathbf{a} = m \dot{\mathbf{p}} = m dot{\mathbf{r}}$$

If we have a constant force $\mathbf{F} = F_0 \hat{\mathbf{x}}$, we can write $dot{\hat{\mathbf{x}}}(t) = \frac{F_0}{m}$. Then,

$$\dot{\mathbf{x}}(t) = \int dot{\mathbf{x}} dt = v_0 + \frac{F_0}{m}t$$

$$\mathbf{x}(t) = \int \dot{\mathbf{x}} dt = x_0 + v_0t + \frac{F_0}{2m}t^2$$

**Definition**. An *inertial frame* is a reference frame relative to some fixed frame if they are moving with constant velocity in regards to each other. Otherwise, the frames are *non-inertial*.

## Section 1.5 - The Third Law and Conservation of Momentum

**Definition**. Newton's Third Law. Every force has an equal and opposite. If $F_{21}$ is the force exerted on object $2$ by object $1$, there exists some force with equal magnitude $F_{12}$ exerted on object $1$ by object $2$.

**Definition**. Force pairs that operate in the same line as each other (eg. gravitational attraction) are called *central forces*.

Recall that the change in momentum of any particle can be defined as $\dot{\mathbf{p}}_1 = \mathbf{F}_1 = \mathbf{F}_{12} + \mathbf{F}_{1}^{ext}$. Then, $\dot{\mathbf{p}}_2 = \mathbf{F}_{21} + \mathbf{F}_2^{ext}$. As $\mathbf{P} = \mathbf{p}_1 + \mathbf{p}_2$, we can see that

$$\dot{\mathbf{P}} = \mathbf{p}_1 + \mathbf{p}_2 = \mathbf{F}_{12} +\mathbf{F}_{21} + \mathbf{F}_{1}^{ext} + \mathbf{F}_{2}^{ext} = \mathbf{F}_{1}^{ext} + \mathbf{F}_{2}^{ext} = \mathbf{F}^{ext}$$

From this, we can see that if $\mathbf{F}^{ext} = 0$, then $\mathbf{P}$ is a constant.

This argument can be generalized to multi-particle systems. Consider particle $\alpha$. Then, $\dot{\mathbf{p}}_\alpha = \mathbf{F}_\alpha = \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta} + \mathbf{F}_\alpha^{ext}$. We  can then see that

$$\dot{\mathbf{P}} = \sum_\alpha \mathbf{p}_\alpha = \sum_\alpha \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta} + \sum_\alpha \mathbf{F}_\alpha^{ext}$$

With $\sum_\alpha \sum_{\beta \neq \alpha} \mathbf{F}_{\alpha\beta} = \sum_\alpha \sum_{\beta > \alpha} \mathbf{F}_{\alpha\beta}( + \mathbf{F}_{\beta\alpha})$, we can see that $\dot{\mathbf{P}} = \sum_\alpha \mathbf{F}_\alpha^{ext}$.

---

Note that Newton's Third Law breaks down as the relative objects approach the speed of light, as it presumes the forces are equal at the same time. As events that are coincident in time in one frame may not be in another, it is clear that this law cannot hold.

## Section 1.6 - Newton's Second Law in Cartesian Coordinates

This is trivial. Skipped.

## Section 1.7 - Two-Dimensional Polar Coordinates

This is trivial. Skipped.
