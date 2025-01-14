# Chapter 1 - Classical Mechanics

## Section 1.2 - Space and Time

Each point $P \in \mathbb{R}^3$ can be written as $(x, y, z)$. However, we will utilize the convention below:

$$\vb{r} = x \vu{x} + y \vu{y} + z \vu{z}$$

However, when working with ambiguous unit basis, it may be better to use the following:

$$\vb{r} = r_1 \vu{e_1} + r_2 \vu{e_2} + r_3 \vu{e_3}$$

Here, $r_1 = x, r_2 = y, r_3 = z$ and $\vu{e_1} = \vu{x_1}, \vdots$. That is, $\vb{r} = \sum r_i \vu{e_i}$.

Vectors are an $\mathbb{R}$-module, with addition defined component-wise. Additionally, the scalar (dot) product and vector (cross) product are definedas usual.

Regarding time, classically, time is universal.

**Definition**. *Reference frames* are frames of motion with a defined coordiante system and origin position.

**Definition**. *Intertial frames* are reference frames in which Newton's laws of motion hold true. An inertial frame may not be accelerating.

## Section 1.3 - Mass and Force

**Definition**. The *mass* $m$ of an object characterizes its translational inertia, and is measured in kilograms (kg)

**Definition**. The *force* $\vb{F}$ exerted on an object is a push or pull on said object and is measued in Newtons (N). Note ethat force is a vector.

## Section 1.4 - Newton's First and Second Laws; Intertial Frames

**Definition**. A *point mass* or *particle* is a convenient fiction, in which an object with mass has no size. It may move in space but has no internal degrees of freedom. Additionally, it may not have any rotational or vibrational kinetic energy.

**Theorem**. Newton's First Law. In the absence of external forces, a particle moves with constant velocity $\vb{v}$.

**Theorem**. Newton's Second Law. Given any particle with mass $m$, the net force $\vb{F}$ on the particle is always equal to the particle's mass times its acceleration. That is,

$$\vb{F} = m\vb{a} = m \ddot{\vb{r}}$$

This can also be rewritten in terms of momentum. We know that momentup $\vb{p}$ can be written as $\vb{p} = m\vb{v} = m \dot{\vb{r}}$. Then,

$$\vb{F} = m\vb{a} = m \dot{\vb{p}} = m \ddot{\vb{r}}$$

If we have a constantt force $\vb{F} = F_0 \vu{x}$, we can write $\ddot{\vu{x}}(t) = \frac{F_0}{m}$. Then,

$$\dot{\vb{x}}(t) = \int \ddot{\vb{x}} dt = v_0 + \frac{F_0}{m}t$$

$$\vb{x}(t) = \int \dot{\vb{x}} dt = x_0 + v_0t + \frac{F_0}{2m}t^2$$

**Definition**. An *inertial frame* is a reference frame reltaive to some fixed frame if they are moving with constant velocity in regards to eachother. Otherwise, the frames are *non-interial*.
