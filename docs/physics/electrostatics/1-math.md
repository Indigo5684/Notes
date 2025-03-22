# Chapter 1 - Mathematics

## 1.5 - Dyads and Tensors

**Definition**. A *dyadic* is a representation of two-ish vectors.

$$
\stackrel{\leftrightarrow}{\mathbf{D}} = \begin{matrix}
    D_{xx} \hat{\mathbf{x}}\hat{\mathbf{x}} &+ D_{xy} \hat{\mathbf{x}}\hat{\mathbf{y}} &+ D{xz} \hat{\mathbf{x}}\hat{\mathbf{z}} \\
    + D_{yx} \hat{\mathbf{y}}\hat{\mathbf{x}} &+ D_{yy} \hat{\mathbf{y}}\hat{\mathbf{y}} &+ D{yz} \hat{\mathbf{y}}\hat{\mathbf{z}} \\
    + D_{zx} \hat{\mathbf{z}}\hat{\mathbf{x}} &+ D_{zy} \hat{\mathbf{z}}\hat{\mathbf{y}} &+ D{zz} \hat{\mathbf{z}}\hat{\mathbf{z}}
\end{matrix}
$$

**Definition**. If a dyadic can be written as a composition of two vectors $\mathbf{A}$ and $\mathbf{B}$, it is called a *dyad*.

$$
\mathbf{AB} = \begin{matrix}
    A_x B_x \hat{\mathbf{x}}\hat{\mathbf{x}} &+ A_x B_y \hat{\mathbf{x}}\hat{\mathbf{y}} &+ A_x B_z \hat{\mathbf{x}}\hat{\mathbf{z}} \\
    + A_y B_x \hat{\mathbf{y}}\hat{\mathbf{x}} &+ A_y B_y \hat{\mathbf{y}}\hat{\mathbf{y}} &+ A_y B_z \hat{\mathbf{y}}\hat{\mathbf{z}} \\
    + A_z B_x \hat{\mathbf{z}}\hat{\mathbf{x}} &+ A_z B_y \hat{\mathbf{z}}\hat{\mathbf{y}} &+ A_z B_z \hat{\mathbf{z}}\hat{\mathbf{z}}
\end{matrix}
$$

The dot product of a dyad $\stackrel{\leftrightarrow}{\mathbf{D}} = \mathbf{AB}$ and vector $\mathbf{v}$ can be written as follows:

$$
(\mathbf{AB}) \cdot \mathbf{v} = \mathbf{A} (\mathbf{B} \cdot \mathbf{v})
$$

**Definition**. A *symmetric/antisymmetric* dyadic is defined the same way that a matrix is.

**Definition**. The *identity dyadic* is $\stackrel{\leftrightarrow}{\mathbf{I}} = \hat{\mathbf{x}}\hat{\mathbf{x}} + \hat{\mathbf{y}}\hat{\mathbf{y}} + \hat{\mathbf{z}}\hat{\mathbf{z}}$.

**Definition**. For a *tensor*, with coordinates $u^i$, we have two sets of basis vectors:

$$
\mathbf{e}_i = \pdv{\mathbf{r}}{u^i}
$$

$$
\mathbf{e}^i = \nabla{u^i}
$$

## 1.9 - Helmholtz Theorem

Given an arbitrary vector field $\mathbf{F}(\mathbf(r))$, we can write said field as a composition of a curl-free component $\mathbf{\Phi}(\mathbf{r})$ and a divergence-free component $\mathbf{A}(\mathbf{r})$ as follows:

$$
\mathbf{F}(\mathbf{r}) = - \nabla{\mathbf{\Phi}(\mathbf{r})} + \nabla \times{\mathbf{A}(\mathbf{r})}
$$

**Definition**. Here, the gradient of the scalar potential is $\nabla{\mathbf{\Phi}(\mathbf{r})}$ and the curl of the vector potential is $\nabla \times{\mathbf{A}(\mathbf{r})}$. Thus, the scalar potential is $\mathbf{\Phi}(\mathbf{r})$ and the vector potential is $\mathbf{A}(\mathbf{r})$.

Letting said field be over bounded volume $V$ with closed surface $\partial V$, and the functions $\mathbf{C}(\mathbf{r}) = \nabla \times{\mathbf{F}(\mathbf{r})}$ and $\mathbf{D}(\mathbf{r}) = \nabla \cdot \mathbf{F}(\mathbf{r})$ are known, we can say that

$$
\mathbf{\Phi}(\mathbf{r}) = \frac{1}{4 \pi} \int_V \frac{D(\mathbf{r}')}{|{\mathbf{r}-\mathbf{r}'}|} d{V'} - \frac{1}{4 \pi} \int_{\partial V} \frac{\mathbf{F}(\mathbf{r}') \cdot \mathbf{n}'}{|{\mathbf{r}-\mathbf{r}'}|} d{S'}
$$

$$
\mathbf{A}(\mathbf{r}) = \frac{1}{4 \pi} \int_V \frac{C(\mathbf{r}')}{|{\mathbf{r}-\mathbf{r}'}|} d{V'} - \frac{1}{4 \pi} \int_{\partial V} \mathbf{n}' \times \frac{\mathbf{F}(\mathbf{r}')}{|{\mathbf{r}-\mathbf{r}'}|} d{S'}
$$

Now, assume that $\lim(\frac{\mathbf{F}(\mathbf{r})}{\mathbf{r}}) = 0$ as $\mathbf{r} \rightarrow \infty$, with a large enough volume, we see that the second terms vanish.

$$
\mathbf{\Phi}(\mathbf{r}) = \frac{1}{4 \pi} \int_V \frac{D(\mathbf{r}')}{|{\mathbf{r}-\mathbf{r}'}|} d{V'}
$$

$$
\mathbf{A}(\mathbf{r}) = \frac{1}{4 \pi} \int_V \frac{C(\mathbf{r}')}{|{\mathbf{r}-\mathbf{r}'}|} d{V'}
$$
