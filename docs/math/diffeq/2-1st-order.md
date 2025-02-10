# Section 2 - First Order Differential Equations

## Section 2.1 - Linear Differential Equations

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/Linear.aspx).

Let the following first-order linear differential equation be given, with $p(t)$ and $g(t)$ continuos.

$$
\frac{dy}{dt} + p(t)y = g(t)
$$

### Deriving the Solution

Next, we let $\mu(t)$ be our *integrating factor*. Multiply both sides of the equation through by $\mu(t)$.

$$
\mu(t)\frac{dy}{dt} + \mu(t)p(t)y = \mu(t)g(t)
$$

Now, define $\mu(t)$ so that $\mu(t)p(t) = \mu'(t)$. Thus, we can state the following:

$$
\mu(t)\frac{dy}{dt} + \mu'(t)y = \mu(t)g(t)
$$

The left of the preceding equation is simply the product rule, so we can write $(\mu(t)y(t))' = \mu(t)g(t)$. Take the integral of both sides.

\begin{align}
    \int (\mu(t)y(t))' dt &= \int \mu(t)g(t) \\
    \mu(t)y(t) + C &= \int \mu(t)g(t) dt \\
    y(t) &= \frac{\int \mu(t)g(t) dt - C}{\mu(t)}
\end{align}

Let $C$ absorb the negative sig, and we see the following.

$$
y(t) = \frac{\int \mu(t)g(t) dt + C}{\mu(t)}
$$

This is the general solution to the differential equation. However, it is incomplete, as we do not know $\mu(t)$

To derive the function, recall that we defined $\mu(t)p(t) = \mu'(t)$. Thus, we can rewrite this equation.

\begin{align}
    \frac{\mu'(t)}{\mu(t)} &= p(t) \\
    (\ln \mu(t))' &= p(t) \\
\end{align}

Integrate both sides.

\begin{align}
    \ln \mu(t) + k = \int p(t) dt \\
    \mu(t) &= e^{\int p(t) dt + k} \\
    &= e^k e^{\int p(t) dt}
\end{align}

As $k$ is an unknown constant, rewrite this as $\mu(t) = k \exp(\int p(t) dt)$.

### Summary

The following differential equation is given.

$$
\frac{dy}{dt} + p(t)y = g(t)
$$

To find a solution to this differential equation, construct the **integrating factor**. $\mu(t)$.

$$\mu(t) = k \exp(\int p(t) dt)$$

Thus, the solution to the differential equation can be written as the following.

$$
y(t) = \frac{\int \mu(t)g(t) dt + C}{\mu(t)}
$$

## Section 2.2 - Separable Differential Equations

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/Separable.aspx).

Let the following differential equation of the following forms be given.

\begin{align}
    N(y) \frac{dy}{dx} &= M(x)
    \frac{dy}{dx} &= \frac{M(x)}{N(y)} \\
    \frac{dy}{dx} &= \frac{N(y)}{M(x)} \\
    \frac{dy}{dx} &= N(y)M(x) \\
\end{align}.

For the sake of simplicity, select the following form:

$$
N(y) \frac{dy}{dx} = M(x)
$$

Thus, integrate both sides with respect to $x$.

$$
\int N(y) \frac{dy}{dx} dx = \int M(x) dx
$$

Since $y$ is really $y(x)$, we can make the following substitution:

$$
u = y(x) \text{ and } du = y'(x)dx = \frac{dy}{dx} dx
$$

This reduces the integral to the following:

$$
\int N(u) du = \int M(x) dx
$$

This is solvable from here.

## Section 2.4 - Bernoulli Equations

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/Bernoulli.aspx).

Let a differential equation of the following form be given, with $n \in \mathbb{N}; n \geq 2$

$$
y' + p(x)y = q(x)y^n
$$

This is a *Bernoulli equation*.

Divide by $y^n$.

$$
y^{-n}y' + p(x)y^{1-n} = q(x)
$$

Now, make the substitution $v = y^{1-n}$. Thus, the derivative is as follows.

$$
v' = (1-n)y^{-n}y'
$$

Substituting into the first equation yields the following.

$$
\frac{1}{1-n}v' + p(x)v = q(x)
$$

After solving, be sure to rewrite in terms of $y$.
