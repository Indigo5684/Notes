# Chapter 11 - Potential Formulation of Electrodynamics

## Section 11.1 - Forces, Fields, Potentials, and Greens Functions

## Section 11.1.1 - Potentials for Time-independent Fields

We know that when the electric and magnetic fields are time-independent, $\nabla \times \mathbf{E} = -\mathbf{J}_m$ and $\nabla \times \mathbf{H} = \mathbf{J}_e$.

We also know that Helmholtz theorem tells us that we can write the fields such that

$$\begin{align}
\mathbf{E} &= -\nabla V_E + \nabla \times \mathbf{A}_E \\
\mathbf{H} &= -\nabla V_H + \nabla \times \mathbf{A}_H
\end{align}$$

We can then recall that

$$\begin{align}
V_E(\mathbf{r}) &= \frac{1}{4\pi} \int_{V'} \frac{1}{|\mathbf{r} - \mathbf{r}'|} \frac{\rho_e(\mathbf{r}')}{\varepsilon_0} dV' \\
V_H(\mathbf{r}) &= \frac{1}{4\pi} \int_{V'} \frac{1}{|\mathbf{r} - \mathbf{r}'|} \frac{\rho_e(\mathbf{r}')}{\mu_0} dV' \\
A_E(\mathbf{r}) &= \frac{1}{4\pi} \int_{V'} \frac{1}{|\mathbf{r} - \mathbf{r}'|} (-s\mathbf{J}_m(\mathbf{r})) dV' \\
A_H(\mathbf{r}) &= \frac{1}{4\pi} \int_{V'} \frac{1}{|\mathbf{r} - \mathbf{r}'|} (\mathbf{J}_e(\mathbf{r})) dV'
\end{align}$$

We can verify this by taking the curl or divergence of the fields and seeing that Maxwell's equations hold true.

A notable result is that for the Laplace operator $\nabla^2$, the function $-\frac{1}{4\pi |\mathbf{r} - \mathbf{r}'|}$ is the Green function for the operator. That is, $\nabla^2 G = \delta(\mathbf{r} - \mathbf{r}')$.

We can show $\nabla \times (\nabla \times \mathbf{A}_E) = -\mathbf{J}_m$ and likewise as $\nabla \times (\nabla \times \mathbf{A}) = -\nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A}$. We now claim that $\nabla \cdot \mathbf{A} = 0$

This would them imply that $\nabla \times (\nabla \times \mathbf{A}_E) = -\nabla^2 \mathbf{A}_E = -\mathbf{J}_m$.

To justify setting $\nabla \cdot \mathbf{A} = 0$, let us assume otherwise. Assume that $\nabla \cdot \mathbf{A} = \psi(\mathbf{r})$. Then, there exists some $\mathbf{A}'(\mathbf{r}) = \mathbf{A}(\mathbf{r}) + \nabla f(\mathbf{r})$.  It is clear that $\nabla \times \mathbf{A}'(\mathbf{r}) = \nabla \times \mathbf{A}(\mathbf{r})$.

We can see that $\nabla \cdot \mathbf{A}(\mathbf{r}) = \nabla \cdot \mathbf{A}(\mathbf{r}) + \nabla^2 f(\mathbf{r}) = \psi(\mathbf{r}) + \nabla^2 f(\mathbf{r})$. Now, if we assert $-\nabla^2 f(\mathbf{r}) = \psi(\mathbf{r})$, that is,

$$f(\mathbf{r}) = \frac{1}{4\pi} \int_V \frac{\psi(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} dV'$$

Under this assumption, we see that $\nabla \cdot \mathbf{A}' = 0$. Notably, we do not need to calculate $f(\mathbf{r})$. it is sufficient to show that it exists. By the Helmholtz theorem, it does,a s $\nabla f$ is a vector field with divergence $-\phi$ and no curl, so $\nabla f$ is the gradient of a scalar potential given by the above integral.

