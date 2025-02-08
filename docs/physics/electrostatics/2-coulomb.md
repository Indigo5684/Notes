# Chapter 2 - Coulomb's Laws, Electric and Magnetic Fields

## Section 2.2 - Parallel Treatment of Electric and Magnetic Fields

Consider two point charges, $q$ and $Q$, with the latter being at the origin of the coordinate system. Let $q$ be located at point $\mathbf{r}$ relative to the origin.

Thus, according to Coulomb's Law,

$$
\begin{align}
    F^e_{qQ}(\mathbf{r}) &= \frac{q_e Q_e}{4 \pi \varepsilon_0} \frac{\hat{\mathbf{r}}}{|\mathbf{r}|^2} \\
    F^m_{qQ}(\mathbf{r}) &= \frac{q_m Q_m}{4 \pi \mu_0} \frac{\hat{\mathbf{r}}}{|\mathbf{r}|^2}
\end{align}
$$

Divide by the charge $q$ to obtain the *electric or magnetic field* at point $\mathbf{r}$.

$$
\begin{align}
    E(\mathbf{r}) &= \frac{Q_e}{4 \pi \varepsilon_0} \frac{\hat{\mathbf{r}}}{|\mathbf{r}|^2} \\
    H(\mathbf{r}) &= \frac{Q_m}{4 \pi \mu_0} \frac{\hat{\mathbf{r}}}{|\mathbf{r}|^2}
\end{align}
$$

Now, let $Q$ be at point $\mathbf{r'}$. Then, the unit vector becomes $\frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}}|$, and we see the following.

$$
\begin{align}
    E(\mathbf{r}) &= \frac{Q_e}{4 \pi \varepsilon_0} \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3} \\
    H(\mathbf{r}) &= \frac{Q_m}{4 \pi \mu_0} \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3}
\end{align}
$$

With multiple charges, we can apply the *superposition principal* to see the following:

$$
\begin{align}
    E(\mathbf{r}) &= \frac{1}{4 \pi \varepsilon_0} \sum_{i=1}^N Q_e \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3} \\
    H(\mathbf{r}) &= \frac{1}{4 \pi \mu_0} \sum_{i=1}^N Q_m \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3}
\end{align}
$$

We can convert this to an integral as $N$ goes to infinity.

$$\begin{align}
E(\mathbf{r}) &= \frac{1}{4 \pi \varepsilon_0} \int_V \rho_e(\mathbf{r'}) \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3} d V' \\
H(\mathbf{r}) &= \frac{1}{4 \pi \mu_0} \int_V \rho_m(\mathbf{r'}) \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3} d V'
\end{align}$$

## Section 2.3 - Divergence and Curl of the Electrostatic or Magnetostatic Field

From a lot of advanced math, we know that

$$\nabla \cdot \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3} = 4 \pi \delta(\mathbf{r}-\mathbf{r'})$$

Now, apply the divergence operator over $\mathbf{r}$ to the electrostatic and magnetostatic fields.

$$\begin{align}
\nabla \cdot E(\mathbf{r}) &= \nabla \cdot (\frac{1}{4 \pi \varepsilon_0} \int_V \rho_e(\mathbf{r'}) \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3} d V') \\
\nabla \cdot H(\mathbf{r}) &= \nabla \cdot (\frac{1}{4 \pi \mu_0} \int_V \rho_m(\mathbf{r'}) \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3} d V')
\end{align}$$

As the divergence operator does not operate on $\mathbf{r'}$, we see that

$$\begin{align}
\nabla \cdot E(\mathbf{r}) &= \frac{1}{4 \pi \varepsilon_0} \int_V \rho_e(\mathbf{r'}) \nabla \cdot (\frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3}) d V' \\
    &= \frac{1}{4 \pi \varepsilon_0} 4 \pi \int_V \rho_e(\mathbf{r'}) \delta(\mathbf{r}-\mathbf{r'}) d V' \\
    &= \frac{\rho_e(\mathbf{r})}{\varepsilon_0} \\
\nabla \cdot H(\mathbf{r}) &= \frac{1}{4 \pi \mu_0} \int_V \rho_m(\mathbf{r'}) \nabla \cdot (\frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3}) d V' \\
    &= \frac{1}{4 \pi \mu_0} 4 \pi \int_V \rho_m(\mathbf{r'}) \delta(\mathbf{r}-\mathbf{r'}) d V' \\
    &= \frac{\rho_m(\mathbf{r})}{\mu_0}
\end{align}$$

The curl of an electrostatic or magnetostatic is relatively simple.

$$
\begin{align}
    \nabla \times{E(\mathbf{r})} &= \frac{1}{4 \pi \varepsilon_0} \int_V \rho_e(\mathbf{r'}) \nabla \times{(\frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3})} d V' \\
    \nabla \times{H(\mathbf{r})} &= \frac{1}{4 \pi \mu_0} \int_V \rho_m(\mathbf{r'}) \nabla \times{(\frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3})} d V' \\
\end{align}
$$

Additionally, we know $\nabla \times{f\mathbf{A}} = f \nabla \times{\mathbf{A}} + \nabla{f}\times\mathbf{A}$. Thus,

$$
\begin{align}
    \nabla \times{(\frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^3})} &= \frac{1}{|\mathbf{r}-\mathbf{r'}|^3} \nabla \times{(\mathbf{r}-\mathbf{r'})} + (\nabla \times{\frac{1}{|\mathbf{r}-\mathbf{r'}|^3}}) \times (\mathbf{r}-\mathbf{r'}) \\
\end{align}
$$

We can verify that $\nabla \times{(\mathbf{r}-\mathbf{r'})} = 0$, cancelling the first term. Additionally, $\nabla \times{\frac{1}{|\mathbf{r}-\mathbf{r'}|^3}} = -3 \frac{\mathbf{r}-\mathbf{r'}}{|\mathbf{r}-\mathbf{r'}|^5}$, which when crossed with $\mathbf{r}-\mathbf{r'}$, will cancel. Thus, all terms in the curl cancel, so for a static field, the curl is zero.

## Section 2.4 - Electric and Magnetic Flux Densities

The electric and magnetic flux density vectors are given by $\varepsilon_0 \mathbf{E}$ and $\mu_0 \mathbf{H}$.

Now, given $S$ is a surface enclosing $Q_e$ or $Q_m$ total charge, we denote flux as following:

$$
\Phi_e = \varepsilon_0 \int_S \mathbf{E} \cdot \hat{\mathbf{n}} d = Q_e S \text{ or } \Phi_m = \mu_0 \int_S \mathbf{H} \cdot \hat{\mathbf{n}} d S = Q_m
$$

Thus, applying divergence theorem,

$$
Q_e = \Phi_e = \varepsilon_0 \int_S \mathbf{E} \cdot \hat{\mathbf{n}} d = \varepsilon_0 \int_V \nabla \cdot \mathbf{E} d V
$$

$$
Q_m = \Phi_m = \mu_0 \int_S \mathbf{H} \cdot \hat{\mathbf{n}} d = \varepsilon_0 \int_V \nabla \cdot \mathbf{H} d V
$$

Since $Q_e = \int_V \rho_e d V$ and $Q_m = \int_V \rho_m d V$, we see that

$$
\begin{align}
    \int_V \rho_e d V &= \varepsilon_0 \int_V \nabla \cdot \mathbf{E} d V \\
    \rho_e &= \varepsilon_0 \int_V \nabla \cdot \mathbf{E} d V \\
    \int_V \rho_m d V &= \mu_0 \int_V \nabla \cdot \mathbf{H} d V \\
    \rho_m &= \mu_0 \int_V \nabla \cdot \mathbf{H} d V \\
\end{align}
$$

**Definition**. This is known as *Gauss' Law*.

With applicable symmetry, the integral factor becomes simply $E(r)*A$, where $A$ is the area of the surface at $r$.
