# Chapter 11 - Potential Formulation of Electrodynamics

## Section 11.1 - Forces, Fields, Potentials, and Greens Functions

### Section 11.1.1 - Potentials for Time-Independent Fields

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

Now, we can see that $\mathbf{H} = \int_V (-\frac{1}{4|\mathbf{r} - \mathbf{r'}|}) \mathbf{J}_e(\mathbf{r'}) dV' = \int_V G(\mathbf{r} - \mathbf{r'}) \mathbf{J}_e(\mathbf{r'}) dV'$.

From this, by knowing $\nabla G(\mathbf{r} - \mathbf{r'}) = -\nabla' G(\mathbf{r} - \mathbf{r'})$ we can find the divergence is

$$\begin{align}
\nabla \cdot \mathbf{A}_h &= \int_V \nabla \cdot(G(\mathbf{r} - \mathbf{r'}) \mathbf{J}_e(\mathbf{r'})) dV' \\
&= \int_V \mathbf{J}_e(\mathbf{r}') (-\nabla G(\mathbf{r} - \mathbf{r'})) dV \\
&= \int_V G(\mathbf{r} - \mathbf{r'}) \nabla' \cdot \mathbf{J}_e(\mathbf{r}') dV \\
\end{align}$$

We  can then apply the  continuity equation to see that

$$\nabla \cdot \mathbf{A}_H = \int_V G(\mathbf{r} - \mathbf{r'}) (-\frac{\partial \rho_e(\mathbf{r}')}{\partial t})$$

However, as we are working with time-independent fields, we set $\frac{\partial rho}{\partial t} = 0$, which forces the divergence to zero.

#### Conventional Approach

Using the constructive equations, and in the absence of magnetic current density, we see that $\nabla \times \mathbf{E} = 0$ in the time-independent case. Additionally, we can see that $\nabla \cdot \mathbf{B} = 0$ and $\nabla \times \mathbf{B} = \mu_0 \mathbf{J}_e + \nabla \times \mathbf{M}$.

This lets us write that $\mathbf{E} = -\nabla V_E$ and $\mathbf{B} = \nabla \times \mathbf{A}_B$ by the Helmholtz theorem.

We can now see that in the electric case, the Maxwell equations tell us that

$$\nabla \cdot \mathbf{E} = \frac{\rho_e}{\varepsilon_0} \rightarrow V_E(\mathbf{r}) = \int_{V'} \frac{1}{4\pi |\mathbf{r} - \mathbf{r'}|} \frac{\rho_e(\mathbf{r})}{\varepsilon_0} dV'$$

In the magnetic case, we again see that as $\nabla \times \mathbf{A_B} = 0$ under gauge transformation, we can write

$$\mathbf{A}_B(\mathbf{r}) = \int_{V'} \frac{1}{4\pi |\mathbf{r} - \mathbf{r'}|}(\mu_0 \mathbf{J}_e(\mathbf{r}) + \nabla' \times \mathbf{M}(\mathbf{r}')) dV'$$

### Section 11.1.2 - Potentials for Time-Dependent Fields

Let us now consider the time-dependent cases, in which Maxwell's equations can be written as

$$\begin{align}
\nabla \times \mathbf{E} &= -\mathbf{J}_m - \frac{\partial}{\partial t}(\mu_0 \mathbf{H} + \mathbf{M}) \\
\nabla \times \mathbf{H} &= \mathbf{J}_e - \frac{\partial}{\partial t}(\varepsilon_0 \mathbf{E} + \mathbf{P})
\end{align}$$

We can now write

$$\begin{align}
\mathbf{E} &= -\nabla V_E + \nabla \times \mathbf{A}_E - \mu_0 \frac{\partial}{\partial t} \mathbf{A}_H \\
\mathbf{H} &= -\nabla V_H + \nabla \times \mathbf{A}_H + \varepsilon_0 \frac{\partial}{\partial t} \mathbf{A}_E
\end{align}$$

We can then take the divergence of both sides to see that

$$\begin{align}
\nabla \cdot \mathbf{E} &= -\nabla^2 V_E - \mu_0 \frac{\partial}{\partial t} \nabla \cdot \mathbf{A}_H = \frac{\rho_e}{\varepsilon_0} \\
\nabla \cdot \mathbf{H} &= -\nabla^2 V_H + \varepsilon_0 \frac{\partial}{\partial t} \nabla \cdot \mathbf{A}_E = \frac{\rho_m}{\mu_0}
\end{align}$$

Meanwhile, the curl equations tell us that

$$\begin{align}
\nabla \times \mathbf{E} &= \nabla \times (\nabla \times \mathbf{A}_E) - \mu_0 \frac{\partial}{\partial t} (\nabla \times \mathbf{A}_H) + \mu_0 \frac{\partial}{\partial t} \mathbf{H} &= -\mathbf{J}_m - \frac{\partial}{\partial t} \mathbf{M} \\
\nabla \times \mathbf{H} &= \nabla \times (\nabla \times \mathbf{A}_H) + \varepsilon_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{A}_E) - \varepsilon_0 \frac{\partial}{\partial t} \mathbf{E} &= \mathbf{J}_e + \frac{\partial}{\partial t} \mathbf{P}
\end{align}$$

We can expand the double curl and substitute the fields to see that

$$\begin{align}
\nabla (\nabla \cdot \mathbf{A}_E) - \nabla^2 \mathbf{A}_E - \mu_0 \frac{\partial}{\partial t} (\nabla \times \mathbf{A}_H) + \mu_0 \frac{\partial}{\partial t} (-\nabla V_H + \nabla \times \mathbf{A}_H + \varepsilon_0 \frac{\partial}{\partial t} \mathbf{A}_E) &= -\mathbf{J}_m - \frac{\partial}{\partial t} \mathbf{M} \\
\nabla(\nabla \cdot \mathbf{A}_H) - \nabla^2 \mathbf{A}_H + \varepsilon_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{A}_E) - \varepsilon_0 \frac{\partial}{\partial t} (-\nabla V_E + \nabla \times \mathbf{A}_E - \mu_0 \frac{\partial}{\partial t} \mathbf{A}_H) &= \mathbf{J}_e + \frac{\partial}{\partial t} \mathbf{P}
\end{align}$$

We can simplify this - the remaining curl terms cancel out.

$$\begin{align}
\nabla (\nabla \cdot \mathbf{A}_E) - \nabla^2 \mathbf{A}_E + \mu_0 \frac{\partial}{\partial t} (-\nabla V_H + \varepsilon_0 \frac{\partial}{\partial t} \mathbf{A}_E) &= -\mathbf{J}_m - \frac{\partial}{\partial t} \mathbf{M} \\
\nabla(\nabla \cdot \mathbf{A}_H) - \nabla^2 \mathbf{A}_H - \varepsilon_0 \frac{\partial}{\partial t} (-\nabla V_E - \mu_0 \frac{\partial}{\partial t} \mathbf{A}_H) &= \mathbf{J}_e + \frac{\partial}{\partial t} \mathbf{P}
\end{align}$$

Now, rearrange terms.

$$\begin{align}
-\nabla^2 \mathbf{A}_E + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{A}_E}{\partial t^2} + \nabla (\nabla \cdot \mathbf{A}_E - \mu_0 \frac{\partial V_H}{\partial t}) &= -\mathbf{J}_m - \frac{\partial}{\partial t} \mathbf{M} \\
- \nabla^2 \mathbf{A}_H + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{A}_H}{\partial t^2} + \nabla(\nabla \cdot \mathbf{A}_H + \varepsilon_0 \frac{\partial V_E}{\partial t}) &= \mathbf{J}_e + \frac{\partial}{\partial t} \mathbf{P}
\end{align}$$

Now, we can choose a gauge such that $\nabla \cdot \mathbf{A_E} = \mu_0 \frac{\partial V_H}{\partial t}$ and $\nabla \cdot \mathbf{A_H} = - \varepsilon_0 \frac{\partial V_E}{\partial t}$. This allows us to write $V_E \mapsto V_E - \mu_0 \frac{\partial \lambda}{\partial t}$, $V_H \mapsto V_H + \varepsilon_0 \frac{\partial \psi}{\partial t}$. If we then say that $\mathbf{A}_E \mapsto \mathbf{A}_E + \nabla \psi$ and $\mathbf{A}_H \mapsto \mathbf{A}+H + \nabla \lambda$, we can then solve $\nabla \cdot \mathbf{A}_E - \mu_0 \frac{\partial V_H}{\partial t} = f(\mathbf{r}, t)$ and $\nabla \cdot \mathbf{A}_H - \varepsilon_0 \frac{\partial V_E}{\partial t} = g(\mathbf{r}, t)$ to find wave equations, which have a Green function and thus have guaranteed solutions.

Substituting this gauge into the previous equations, we see that

$$\begin{align}
(-\nabla^2 + \mu_0 \varepsilon_0 \frac{\partial^2}{\partial t^2}) \mathbf{A}_E &= -\mathbf{J}_m - \frac{\partial}{\partial t} \mathbf{M} \\
(-\nabla^2 + \mu_0 \varepsilon_0 \frac{\partial^2}{\partial t^2}) \mathbf{A}_H &= \mathbf{J}_e + \frac{\partial}{\partial t} \mathbf{P}
\end{align}$$

We also know previously that

$$\begin{align}
-\nabla^2 V_E - \mu_0 \frac{\partial}{\partial t} \nabla \cdot \mathbf{A}_H = \frac{\rho_e}{\varepsilon_0} \\
-\nabla^2 V_H + \varepsilon_0 \frac{\partial}{\partial t} \nabla \cdot \mathbf{A}_E = \frac{\rho_m}{\mu_0}
\end{align}$$

We can substitute our gauge to see that

$$\begin{align}
-\nabla^2 V_E + \mu_0 \frac{\partial}{\partial t} \varepsilon_0 \frac{\partial V_E}{\partial t} = \frac{\rho_e}{\varepsilon_0} \\
-\nabla^2 V_H + \varepsilon_0 \frac{\partial}{\partial t} \mu_0 \frac{\partial V_H}{\partial t} = \frac{\rho_m}{\mu_0}
\end{align}$$

Simplifying, we see that

$$\begin{align}
-(\nabla^2 + \mu_0 \varepsilon_0 \frac{\partial^2}{\partial t^2}) V_E = \frac{\rho_e}{\varepsilon_0} \\
-(\nabla^2 + \mu_0 \varepsilon_0 \frac{\partial^2}{\partial t^2}) V_H = \frac{\rho_m}{\mu_0}
\end{align}$$

#### Conventional Approach to Potentials for Time-Dependent Fields

In the conventional approach, we use the $\mathbf{E}$-$\mathbf{B}$ form of our Maxwell's equations, and presume no magnetic current nor charge to see that

$$\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho_e}{\varepsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} + \frac{\partial \mathbf{B}}{\partial t} &= 0 \\
\nabla \times \mathbf{B} - \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} &= \mu_0 \mathbf{J}_e + \mu_0 \frac{\partial \mathbf{P}}{\partial t} + \nabla \times \mathbf{M}
\end{align}$$

This allows us to cancel terms in our Helmholtz construction, leading to

$$\begin{align}
\mathbf{B} &= \nabla \times \mathbf{A}_B \\
\mathbf{E} &= -\nabla V_E - \frac{\partial \mathbf{A}_B}{\partial t}
\end{align}$$

Taking the divergence of $\mathbf{E}$, we see that

$$\nabla \cdot(-\nabla V_E - \frac{\partial}{\partial t} \mathbf{A_B}) = \frac{\rho_e}{\varepsilon_0}$$

Taking the curl of $\mathbf{B}$ and rearranging, we see that

$$\begin{align}
\nabla \times (\nabla \times \mathbf{A}_B) - \mu_0 \varepsilon_0 \frac{\partial}{\partial t}[-\nabla V_E - \frac{\partial \mathbf{A}_B}{\partial t}] &= \mu_0 \mathbf{J}_e + \mu_0 \frac{\partial \mathbf{P}}{\partial t} + \nabla \times \mathbf{M} \\
-\nabla^2 \mathbf{A}_B + \nabla(\nabla \cdot \mathbf{A}_B) + \mu_0 \varepsilon_0 \frac{\partial}{\partial t} \nabla V_E + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{A}_B}{\partial t^2} &= \mu_0 \mathbf{J}_e + \mu_0 \frac{\partial \mathbf{P}}{\partial t} + \nabla \times \mathbf{M} \\
-\nabla^2 \mathbf{A}_B + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{A}_B}{\partial t^2} + \nabla(\nabla \cdot \mathbf{A}_B + \mu_0 \varepsilon_0 \frac{\partial V_E}{\partial t})  &= \mu_0 \mathbf{J}_e + \mu_0 \frac{\partial \mathbf{P}}{\partial t} + \nabla \times \mathbf{M} \\
\end{align}$$

Now, choose a gauge that sets $\nabla \cdot \mathbf{A}_B = -\mu_0 \varepsilon_0 \frac{\partial V_E}{\partial t}$.

This will give us the wave equation

$$(-\nabla^2 + \mu_0 \varepsilon_0 \frac{\partial^2}{\partial t^2}) \mathbf{A}_B = \mu_0 \mathbf{J}_e + \mu_0 \frac{\partial \mathbf{P}}{\partial t} + \nabla \times \mathbf{M}$$

Applying the gauge to the divergence equation shows us that

$$(-\nabla^2 + \mu_0 \varepsilon_0 \frac{\partial^2}{\partial t^2}) V_E = \frac{\rho_e}{\varepsilon_0}$$

### Section 11.1.3 - Green Function for the Wave Equation

We know the Green function for the Laplacian is

$$G(\mathbf{r} - \mathbf{r}') = -\frac{1}{4 \pi |\mathbf{r} - \mathbf{r}'}$$

That is, $\nabla^2 G(\mathbf{r} - \mathbf{r}') = \delta(\mathbf{r} - \mathbf{r}')$.

How, we want to find the Green function for the wave equation. That is, we want to find the function that satisfies

$$(\nabla^2 - \frac{1}{c^2} \frac{\partial^2}{\partial t^2}) G(\mathbf{r} - \mathbf{r}', t - t') = \delta(\mathbf{r} - \mathbf{r}', t - t')$$

We know that the wave equation shares values upon characteristic lines through $\mathbf{r}$-$t$ space. That is, if $t - \frac{1}{c} |\mathbf{r} - \mathbf{r}'|$ is a constant, we are on a characteristic line and the function shares a value. We can call this value $t_r$ and define it as

$$t_r = t - \frac{1}{c} |\mathbf{r} - \mathbf{r}'|$$

Now, we will make a guess for the Green function as

$$G(\mathbf{r} - \mathbf{r}', t - t') = -\frac{1}{4\pi |\mathbf{r} - \mathbf{r}'|} \delta(t - t' + \frac{1}{c}|\mathbf{r} - \mathbf{r}'|)$$

## Section 11.2 - Potentials and Fields of Time-Dependent Electric Charge Distributions

### Section 11.2.1 - Potentials of Continuous Charge and Current Distributions

### Section 11.2.2 - Fields of Continuous Charge and Current Distributions

### Section 11.2.3 - Fields of a Moving Electric Point Charge
