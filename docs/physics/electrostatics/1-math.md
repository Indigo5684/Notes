# Chapter 1 - Mathematics
## 1.5 - Dyads and Tensors

**Definition**. A *dyadic* is a representation of two-ish vectors.

$$
\stackrel{\leftrightarrow}{\vb{D}} = \begin{matrix}
    D_{xx} \vu{x}\vu{x} &+ D_{xy} \vu{x}\vu{y} &+ D{xz} \vu{x}\vu{z} \\
    + D_{yx} \vu{y}\vu{x} &+ D_{yy} \vu{y}\vu{y} &+ D{yz} \vu{y}\vu{z} \\
    + D_{zx} \vu{z}\vu{x} &+ D_{zy} \vu{z}\vu{y} &+ D{zz} \vu{z}\vu{z}
\end{matrix}
$$

**Definition**. If a dyadic can be written as a composition of two vectors $\vb{A}$ and $\vb{B}$, it is called a *dyad*.

$$
\vb{AB} = \begin{matrix}
    A_x B_x \vu{x}\vu{x} &+ A_x B_y \vu{x}\vu{y} &+ A_x B_z \vu{x}\vu{z} \\
    + A_y B_x \vu{y}\vu{x} &+ A_y B_y \vu{y}\vu{y} &+ A_y B_z \vu{y}\vu{z} \\
    + A_z B_x \vu{z}\vu{x} &+ A_z B_y \vu{z}\vu{y} &+ A_z B_z \vu{z}\vu{z}
\end{matrix}
$$

The dot product of a dyad $\stackrel{\leftrightarrow}{\vb{D}} = \vb{AB}$ and vector $\va{v}$ can be written as follows:

$$
(\vb{AB}) \vdot \va{v} = \vb{A} (\vb{B} \vdot \va{v})
$$

**Definition**. A *symmetric/antisymmetric* dyadic is defined the same way that a matrix is.

**Definition**. The *identity dyadic* is $\stackrel{\leftrightarrow}{\vb{I}} = \vu{x}\vu{x} + \vu{y}\vu{y} + \vu{z}\vu{z}$.

**Definition**. FOr a *tensor*, with coordinates $u^i$, we have two sets of basis vectors:

$$
\vb{e}_i = \pdv{\vb{r}}{u^i}
$$

$$
\vb{e}^i = \grad{u^i}
$$

## 1.9 - Helmholtz Theorem

Given an arbitrary vector field $\vb{F}(\vb(r))$, we can write said field as a composition of a curl-free component $\vb{\Phi}(\vb{r})$ and a divergence-free component $\vb{A}(\vb{r})$ as follows:

$$
\vb{F}(\vb{r}) = - \grad{\vb{\Phi}(\vb{r})} + \curl{\vb{A}(\vb{r})}
$$

**Definition**. Here, the gradient of the scalar potential is $\grad{\vb{\Phi}(\vb{r})}$ and the curl of the vector potential is $\curl{\vb{A}(\vb{r})}$. Thus, the scalar potential is $\vb{\Phi}(\vb{r})$ and the vector potential is $\vb{A}(\vb{r})$.

Letting said field be over bounded volume $V$ with closed surface $\partial V$, and the functions $\vb{C}(\vb{r}) = \curl{\vb{F}(\vb{r})}$ and $\vb{D}(\vb{r}) = \div{\vb{F}(\vb{r})}$ are known, we can say that

$$
\vb{\Phi}(\vb{r}) = \frac{1}{4 \pi} \int_V \frac{D(\vb{r}')}{\abs{\vb{r}-\vb{r}'}} \dd{V'} - \frac{1}{4 \pi} \int_{\partial V} \frac{\vb{F}(\vb{r}') \vdot \va{n}'}{\abs{\vb{r}-\vb{r}'}} \dd{S'}
$$

$$
\vb{A}(\vb{r}) = \frac{1}{4 \pi} \int_V \frac{C(\vb{r}')}{\abs{\vb{r}-\vb{r}'}} \dd{V'} - \frac{1}{4 \pi} \int_{\partial V} \va{n}' \cross \frac{\vb{F}(\vb{r}')}{\abs{\vb{r}-\vb{r}'}} \dd{S'}
$$

Now, assume that $\lim(\frac{\vb{F}(\vb{r})}{\vb{r}}) = 0$ as $\vb{r} \rightarrow \infty$, with a large enough volume, we see that the second terms vanish.

$$
\vb{\Phi}(\vb{r}) = \frac{1}{4 \pi} \int_V \frac{D(\vb{r}')}{\abs{\vb{r}-\vb{r}'}} \dd{V'}
$$

$$
\vb{A}(\vb{r}) = \frac{1}{4 \pi} \int_V \frac{C(\vb{r}')}{\abs{\vb{r}-\vb{r}'}} \dd{V'}
$$
