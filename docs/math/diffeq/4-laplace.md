# Section 4 - Laplace Transformations

## Section 4.1 - Definition

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/LaplaceDefinition.aspx).

**Definition**. The *Laplace transform* of a function is given by the following:

$$
\mathcal{L} \{f(t)\}(s) = F(s) = \int_0^{\infty} e^{-st}f(t) dt
$$

## Section 4.2 - Properties

The Laplace Transformation is a linear transformation over functions in $\mathbb{R}[t]$. That is, given $a, b \in \mathbb{R}, f(t), g(t) \in \mathbb{R}[t]$, we know that

$$
\mathcal{L} \{a f(t)\ + b g(t) \}(s) = a F(s) + b G(s)
$$

## Section 4.3 - Inverse Laplace Transformation

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

**Theorem**. Given a function $f(t)$ with $C^n$ continuity, then

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

## Section 4.6 - Non-constant Coefficient IVPs

If $f(t)$ is piecewise continuous on $[0, \infty)$, then $\lim_{s \rightarrow \infty} F(s) = 0$.

**Definition**. A function $f(t)$ is said to be of exponential order $\alpha$ if there exists positive constants $T, M$ such that for all $t \geq T$, $|f(t)| \leq Me^{\alpha t}$.

To check this, simply compute $\lim_{t \rightarrow \infty} \frac{|f(t)|}{e^{\alpha t}}$. If this is finite for some $\alpha$, then the function is of exponential order $\alpha$.

## Section 4.7 - IVPs with Step Functions

Recall that $\mathcal{L} \{u_c(t)f(t-c)\} = e^{-cs}F(s)$. Then, we can solve IVPs involving step functions.

## Section 4.8 - Dirac Delta Function

The Dirac Delta function has several properties. First, $\delta(t - a) = 0$ when $t \neq a$. Notably, though,

$$\int_{\mathbb{R}} f(t) \delta(t - a) dt = f(a)$$

Note that this is not an actual function, buy instead a *generalized function* or *distribution*, as several functions can express this property using infinite limits.

Then, we can see that $\mathcal{L} \{\delta(t-a)\} = \int_0^\infty e^{-st} \delta(t-a) dt$ by definition. Then, applying the properties of the Delta function, $\mathcal{L} \{\delta(t-a)\} = e^{-as}$, given $a > 0$.

## Section 4.9 - Convolution Integrals

Consider two functions $F(s)$ and $G(s)$ such that $F(s) G(s) = H(s)$, of which we want to find an inverse Laplace transform.

We define a *convolution integral* $(f*g)(t)$ as

$$(f*g)(t) = \int_0^t f(t - \tau)(g - \tau) d\tau$$

A unique property of this integral is that $(f*g) = (g*f)$.

With this, we see that $\mathcal{L} \{f * g\} = F(s)G(s)$, or that $\mathcal{L}^{-1} \{F(s)G(s)\} = (f * g)(t)$.
