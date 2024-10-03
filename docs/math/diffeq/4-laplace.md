# Section 4 - Laplace Transformations
## Section 4.1 - Definition

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/LaplaceDefinition.aspx).

**Definition**. The *Laplace transform* of a function is given by the following:

$$
\mathcal{L} \{f(t)\}(s) = F(s) = \int_0^{\infty} e^{-st}f(t) dt
$$

## Section 4.2 - Properties

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/LaplaceTransforms.aspx).

The Laplace Transformation is a linear transformation over functions in $\mathbb{R}[t]$. That is, given $a, b \in \mathbb{R}, f(t), g(t) \in \mathbb{R}[t]$, we know that

$$
\mathcal{L} \{a f(t)\ + b g(t) \}(s) = a F(s) + b G(s)
$$

## Section 4.3 - Inverse Laplace Transformation

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/InverseTransforms.aspx).

Given $F(s)$, we define the Inverse Laplace Transformation as the following;

$$
f(t) = \mathcal{L}^{-1} \{F(s)\}
$$

## Section 4.4 - Step Function

The step/Heaviside function $u_c(t)$ is defined as 0 if $t < c$, and 1 if $t > c$.

Alternatively, $u(t - c) = H(t - c)$ is 0 if $t < c$, and 1 if $t > c$.

Applying this to the Laplace transform,

$$
\begin{align}
    \mathcal{L} \{ u_c(t) f(t-c) \} &= \int_0^{\infty} e^{-st}u_c(t)f(t) dt \\
    &= \int_c^{\infty} e^{-st}f(t) dt
\end{align}
$$

If we let $u = t - c$,

$$
\begin{align}
    \mathcal{L} \{ u_c(t) f(t-c) \} &= \int_0^{\infty} e^{-s(u+c)}f(u) du \\
    &= \int_0^{\infty} e^{-su}e^{-cs}f(u) du \\
    &= e^{-cs} \int_0^{\infty} e^{-su}f(u) du \\
    &= e^{-cs} F(s)
\end{align}
$$

## Section 4.5 - Laplace Transformation applied to IVPs

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/IVPWithLaplace.aspx).

**Theorum**. Given a function $f(t)$ with $C^n$ continuity, then

$$
\mathcal{L} \{ f^{(n)} (t) \} = s^n F(s) - s^{n-1} f(0) - s^{n-2} f'(0) - \ldots - s f^{(n-2)} (0) - f^{(n-1)} (0)
$$

For $n=1, 2$ we see that

$$
\begin{align}
    \mathcal{L} \{ y' \} &= sY(s) - y(0) \\
    \mathcal{L} \{ y'' \} &= s^2 Y(s) - s y(0) - y'(0)
\end{align}
$$

We can take the Laplace transformation of an IVP, solve for $Y(s)$, then take the inverse to find the solution.

## Section 4.6 - Nonconstant Coefficient IVPs

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/IVPWithNonConstantCoefficient.aspx).