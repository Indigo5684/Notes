# Chapter 2 - Coulomb's Laws, Electric and Magnetic Fields

## Section 2.2 - Parallel Treatment of Electric and Magnetic Fields

Consider two point charges, $q$ and $Q$, with the latter being at the origin of the coordinate system. Let $q$ be located at point $\vb{r}$ relative to the origin.

Thus, according to Coulomb's Law,

$$
\begin{align}
    F^e_{qQ}(\vb{r}) &= \frac{q_e Q_e}{4 \pi \varepsilon_0} \frac{\vu{r}}{\abs{\vb{r}}^2} \\
    F^m_{qQ}(\vb{r}) &= \frac{q_m Q_m}{4 \pi \mu_0} \frac{\vu{r}}{\abs{\vb{r}}^2}
\end{align}
$$

Divide by the charge $q$ to obtain the *electric or magnetic field* at point $\vb{r}$.

$$
\begin{align}
    E(\vb{r}) &= \frac{Q_e}{4 \pi \varepsilon_0} \frac{\vu{r}}{\abs{\vb{r}}^2} \\
    H(\vb{r}) &= \frac{Q_m}{4 \pi \mu_0} \frac{\vu{r}}{\abs{\vb{r}}^2}
\end{align}
$$

Now, let $Q$ be at point $\vb{r'}$. Then, the unit vector becomes $\frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}}$, and we see the following.

$$
\begin{align}
    E(\vb{r}) &= \frac{Q_e}{4 \pi \varepsilon_0} \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3} \\
    H(\vb{r}) &= \frac{Q_m}{4 \pi \mu_0} \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3}
\end{align}
$$

With multiple charges, we can apply the *superposition principal* to see the following:

$$
\begin{align}
    E(\vb{r}) &= \frac{1}{4 \pi \varepsilon_0} \sum_{i=1}^N Q_e \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3} \\
    H(\vb{r}) &= \frac{1}{4 \pi \mu_0} \sum_{i=1}^N Q_m \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3}
\end{align}
$$

We can convert this to an integral as $N$ goes to infinity.

$$
\begin{align}
    E(\vb{r}) &= \frac{1}{4 \pi \varepsilon_0} \int_V \rho_e(\vb{r'}) \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3} \dd V' \\
    H(\vb{r}) &= \frac{1}{4 \pi \mu_0} \int_V \rho_m(\vb{r'}) \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3} \dd V'
\end{align}
$$

## Section 2.3 - Divergence and Curl of the Electrostatic or Magnetostatic Field

From a lot of advanced math, we know that

$$
\div{\frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3}} = 4 \pi \delta(\vb{r}-\vb{r'})
$$

Now, apply the divergence operator over $\vb{r}$ to the electrostatic and magnetostatic fields.

$$
\begin{align}
    \div{E(\vb{r})} &= \div{(\frac{1}{4 \pi \varepsilon_0} \int_V \rho_e(\vb{r'}) \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3} \dd V')} \\
    \div{H(\vb{r})} &= \div{(\frac{1}{4 \pi \mu_0} \int_V \rho_m(\vb{r'}) \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3} \dd V')}
\end{align}
$$

As the divergence operator does not operate on $\vb{r'}$, we see that

$$
\begin{align}
    \div{E(\vb{r})} &= \frac{1}{4 \pi \varepsilon_0} \int_V \rho_e(\vb{r'}) \div{(\frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3})} \dd V' \\
        &= \frac{1}{4 \pi \varepsilon_0} 4 \pi \int_V \rho_e(\vb{r'}) \delta(\vb{r}-\vb{r'}) \dd V' \\
        &= \frac{\rho_e(\vb{r})}{\varepsilon_0} \\
    \div{H(\vb{r})} &= \frac{1}{4 \pi \mu_0} \int_V \rho_m(\vb{r'}) \div{(\frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3})} \dd V' \\
        &= \frac{1}{4 \pi \mu_0} 4 \pi \int_V \rho_m(\vb{r'}) \delta(\vb{r}-\vb{r'}) \dd V' \\
        &= \frac{\rho_m(\vb{r})}{\mu_0}
\end{align}
$$

The curl of an electrostatic or magnetostatic is relatively simple.

$$
\begin{align}
    \curl{E(\vb{r})} &= \frac{1}{4 \pi \varepsilon_0} \int_V \rho_e(\vb{r'}) \curl{(\frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3})} \dd V' \\
    \curl{H(\vb{r})} &= \frac{1}{4 \pi \mu_0} \int_V \rho_m(\vb{r'}) \curl{(\frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3})} \dd V' \\
\end{align}
$$

Additionally, we know $\curl{f\vb{A}} = f \curl{\vb{A}} + \grad{f}\cross\vb{A}$. Thus,

$$
\begin{align}
    \curl{(\frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^3})} &= \frac{1}{\abs{\vb{r}-\vb{r'}}^3} \curl{(\vb{r}-\vb{r'})} + (\curl{\frac{1}{\abs{\vb{r}-\vb{r'}}^3}}) \cross (\vb{r}-\vb{r'}) \\
\end{align}
$$

We can verify that $\curl{(\vb{r}-\vb{r'})} = 0$, cancelling the first term. Additionally, $\curl{\frac{1}{\abs{\vb{r}-\vb{r'}}^3}} = -3 \frac{\vb{r}-\vb{r'}}{\abs{\vb{r}-\vb{r'}}^5}$, which when crossed with $\vb{r}-\vb{r'}$, will cancel. Thus, all terms in the curl cancel, so for a static field, the curl is zero.

## Section 2.4 - Electric and Magnetic Flux Densities

The electric and magnetic flux density vectors are given by $\varepsilon_0 \vb{E}$ and $\mu_0 \vb{H}$.

Now, given $S$ is a surface enclosing $Q_e$ or $Q_m$ total charge, we denote flux as following:

$$
\Phi_e = \varepsilon_0 \int_S \vb{E} \vdot \vu{n} \dd = Q_e S \text{ or } \Phi_m = \mu_0 \int_S \vb{H} \vdot \vu{n} \dd S = Q_m
$$

Thus, applying divergence theorem,

$$
Q_e = \Phi_e = \varepsilon_0 \int_S \vb{E} \vdot \vu{n} \dd = \varepsilon_0 \int_V \div{\vb{E}} \dd V
$$

$$
Q_m = \Phi_m = \mu_0 \int_S \vb{H} \vdot \vu{n} \dd = \varepsilon_0 \int_V \div{\vb{H}} \dd V
$$

Since $Q_e = \int_V \rho_e \dd V$ and $Q_m = \int_V \rho_m \dd V$, we see that

$$
\begin{align}
    \int_V \rho_e \dd V &= \varepsilon_0 \int_V \div{\vb{E}} \dd V \\
    \rho_e &= \varepsilon_0 \int_V \div{\vb{E}} \dd V \\
    \int_V \rho_m \dd V &= \mu_0 \int_V \div{\vb{H}} \dd V \\
    \rho_m &= \mu_0 \int_V \div{\vb{H}} \dd V \\
\end{align}
$$

**Definition**. This is known as *Gauss' Law*.

With applicable symmetry, the integral factor becomes simply $E(r)*A$, where $A$ is the area of the surface at $r$.
