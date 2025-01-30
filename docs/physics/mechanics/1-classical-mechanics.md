# Chapter 1 - Classical Mechanics

## Section 1.2 - Space and Time

Each point $P \in \mathbb{R}^3$ can be written as $(x, y, z)$. However, we will utilize the convention below:

$$\vb{r} = x \vu{x} + y \vu{y} + z \vu{z}$$

However, when working with ambiguous unit basis, it may be better to use the following:

$$\vb{r} = r_1 \vu{e_1} + r_2 \vu{e_2} + r_3 \vu{e_3}$$

Here, $r_1 = x, r_2 = y, r_3 = z$ and $\vu{e_1} = \vu{x_1}, \vdots$. That is, $\vb{r} = \sum r_i \vu{e_i}$.

Vectors are an $\mathbb{R}$-module, with addition defined component-wise. Additionally, the scalar (dot) product and vector (cross) product are defined as usual.

Regarding time, classically, time is universal.

**Definition**. *Reference frames* are frames of motion with a defined coordinate system and origin position.

**Definition**. *Inertial frames* are reference frames in which Newton's laws of motion hold true. An inertial frame may not be accelerating.

## Section 1.3 - Mass and Force

**Definition**. The *mass* $m$ of an object characterizes its translational inertia, and is measured in kilograms (kg)

**Definition**. The *force* $\vb{F}$ exerted on an object is a push or pull on said object and is measured in Newtons (N). Note that force is a vector.

## Section 1.4 - Newton's First and Second Laws; Inertial Frames

**Definition**. A *point mass* or *particle* is a convenient fiction, in which an object with mass has no size. It may move in space but has no internal degrees of freedom. Additionally, it may not have any rotational or vibrational kinetic energy.

**Theorem**. Newton's First Law. In the absence of external forces, a particle moves with constant velocity $\vb{v}$.

**Theorem**. Newton's Second Law. Given any particle with mass $m$, the net force $\vb{F}$ on the particle is always equal to the particle's mass times its acceleration. That is,

$$\vb{F} = m\vb{a} = m \ddot{\vb{r}}$$

This can also be rewritten in terms of momentum. We know that momentum $\vb{p}$ can be written as $\vb{p} = m\vb{v} = m \dot{\vb{r}}$. Then,

$$\vb{F} = m\vb{a} = m \dot{\vb{p}} = m \ddot{\vb{r}}$$

If we have a constant force $\vb{F} = F_0 \vu{x}$, we can write $\ddot{\vu{x}}(t) = \frac{F_0}{m}$. Then,

$$\dot{\vb{x}}(t) = \int \ddot{\vb{x}} dt = v_0 + \frac{F_0}{m}t$$

$$\vb{x}(t) = \int \dot{\vb{x}} dt = x_0 + v_0t + \frac{F_0}{2m}t^2$$

**Definition**. An *inertial frame* is a reference frame relative to some fixed frame if they are moving with constant velocity in regards to each other. Otherwise, the frames are *non-inertial*.

## Section 1.5 - The Third Law and Conservation of Momentum

**Definition**. Newton's Third Law. Every force has an equal and opposite. If $F_{21}$ is the force exerted on object $2$ by object $1$, there exists some force with equal magnitude $F_{12}$ exerted on object $1$ by object $2$.

**Definition**. Force pairs that operate in the same line as each other (eg. gravitational attraction) are called *central forces*.

Recall that the change in momentum of any particle can be defined as $\dot{\vb{p}}_1 = \vb{F}_1 = \vb{F}_{12} + \vb{F}_{1}^{ext}$. Then, $\dot{\vb{p}}_2 = \vb{F}_{21} + \vb{F}_2^{ext}$. As $\vb{P} = \vb{p}_1 + \vb{p}_2$, we can see that

$$\dot{\vb{P}} = \vb{p}_1 + \vb{p}_2 = \vb{F}_{12} +\vb{F}_{21} + \vb{F}_{1}^{ext} + \vb{F}_{2}^{ext} = \vb{F}_{1}^{ext} + \vb{F}_{2}^{ext} = \vb{F}^{ext}$$

From this, we can see that if $\vb{F}^{ext} = 0$, then $\vb{P}$ is a constant.

This argument can be generalized to multi-particle systems. Consider particle $\alpha$. Then, $\dot{\vb{p}}_\alpha = \vb{F}_\alpha = \sum_{\beta \neq \alpha} \vb{F}_{\alpha\beta} + \vb{F}_\alpha^{ext}$. We  can then see that

$$\dot{\vb{P}} = \sum_\alpha \vb{p}_\alpha = \sum_\alpha \sum_{\beta \neq \alpha} \vb{F}_{\alpha\beta} + \sum_\alpha \vb{F}_\alpha^{ext}$$

With $\sum_\alpha \sum_{\beta \neq \alpha} \vb{F}_{\alpha\beta} = \sum_\alpha \sum_{\beta > \alpha} \vb{F}_{\alpha\beta}( + \vb{F}_{\beta\alpha})$, we can see that $\dot{\vb{P}} = \sum_\alpha \vb{F}_\alpha^{ext}$.

---

Note that Newton's Third Law breaks down as the relative objects approach the speed of light, as it presumes the forces are equal at the same time. As events that are coincident in time in one frame may not be in another, it is clear that this law cannot hold.

## Section 1.6 - Newton's Second Law in Cartesian Coordinates

This is trivial. Skipped.

## Section 1.7 - Two-Dimensional Polar Coordinates

This is trivial. Skipped.
