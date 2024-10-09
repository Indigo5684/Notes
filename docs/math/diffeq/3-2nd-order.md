# Section 3 - Second Order Differential Equations

## Section 3.1 - Basic Concepts

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/SecondOrderConcepts.aspx).

All second-order differential equations can be written in the following form:

$$ p(t) y'' + q(t) y' + r(t) y = g(t) $$

In the case where $p(t)$, $q(t)$, and $r(t)$ are constants, we write the equation as the following:

$$ ay'' + by' + cy = g(t) $$

This is a second-order differential equation with constant coefficients.

**Definition**. In the event that $g(t) = 0$, we say the equation is *homogenous*. Otherwise, the equation is *nonhomogenous*.

**Definition**. Principal of Superposition. Let $y_1(t)$ and $y_2(t)$ be solutions to a linear, homogenous differential equation. Then, any linear combination of said solutions is also a solution to the differential equation. In other words, with $c_1, c_2 \in \mathbb{R}$, the following is a solution to a differential equation.

$$ y(t) = c_1 y_1(t) + c_2 y_2(t) $$

Given a second-order homogenous differential equation with constant coeffictions, we assume solutions of the following form:

$$ y(t) = e^{rt} $$

Substituting this equation into the differential equationm, we see the following:

$$ e^{rt}(ar^2 + br + c) = 0 $$

Thus, we allow the *charactaristic equation* of the differential equation to be as follows:

$$ ar^2 + br + c = 0 $$

## Section 3.2 - Real & Distinct Roots

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/RealRoots.aspx).

When the two roots to the charactaristic equation are discrete roots in the real numbers, we see the following solutions.

$$ y_1(t) = e^{r_1 t} $$

$$ y_2(t) = e^{r_2 t} $$

Thus,

$$ y(t) = c_1 e^{r_1 t} + c_2 e^{r_2 t} $$

## Section 3.3 - Complex Roots

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/ComplexRoots.aspx).

Let the solutions to the charactaristic equation be of the following form:

$$ r_{1,2} = \lambda \pm \mu i $$

Thus, our two solutions are

$$ y_1(t) = e^{(\lambda + \mu i)t} $$

$$ y_2(t) = e^{(\lambda - \mu i)t} $$

Recall Euler's Formula:

$$ e^{i \theta} = \cos \theta + i \sin \theta $$

A colliloquy of Euler's formula is the following:

$$ e^{-i \theta} = \cos(-\theta) + i \sin(-\theta) = \cos \theta - i \sin \theta $$

Thus, we can write our solutions as the following:

\begin{align}
    y_1(t) &= e^{(\lambda + \mu i)t} &= e^{\lambda t} e^{i \mu t} &= e^{\lambda t}(\cos(\mu t) + i \sin(\mu t)) \\
    y_2(t) &= e^{(\lambda - \mu i)t} &= e^{\lambda t} e^{-i \mu t} &= e^{\lambda t}(\cos(\mu t) - i \sin(\mu t))
\end{align}

A linear combination of the two solutions can be written as the following:

$$ y(t) = c_1 e^{\lambda t} \cos(\mu t) + c_2 e^{\lambda t} \sin(\mu t) $$

## Section 3.4 - Repeated Roots

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/RepeatedRoots.aspx).

Assume the solutions to the charactaristic equations are $r = r_1 = r_2$. Thus, the two equations $y_t(t)$ and $y_2(t)$ are not linearly independent.

After a *lot* of algebra, we see that

$$y_1(t) = e^{rt}$$

$$y_2(t) = t e^{rt}$$

## Section 3.5 - Reduction of Order

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/ReductionofOrder.aspx).

Skipped.

## Section 3.6 - Fundamental Set of Solutions, Wronskian

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/FundamentalSetsofSolutions.aspx).

**Definition**. Given two functions $f(t)$, $g(t)$, the *Wronskian* is defined as

$$
W(f,g) = \det \begin{vmatrix}
  f(t) & g(t) \\
  f'(t) & g'(t)
\end{vmatrix}
$$

**Definition**. If $W(f, g) \neq 0$, then $f(t)$ and $g(t)$ are said to form a *fundamental set of solutions*, and can be superimposed to form the general solution.

## Section 3.8 - Nonhomogenous Differential Equations

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/NonhomogeneousDE.aspx).

Assume we have the differential equation as follows:

$$ y'' + p(t) y' + q(t) y = g(t) $$

The equivilent homogenous differential equation is

$$ y'' + p(t) y' + q(t) y = 0 $$

**Theorem**. Assume $Y_1(t)$, $Y_2(t)$ are solutions to the nonhomogenous differential equations. Then, $Y_1(t) - Y_2(t)$ is a solution to the homogenous differential equation. This can be proved by substitution.

Thus, with $y_h(t)$ the solution to the homogenous problem, and $y_p(t)$ the solution to this particular problem, we can say that the general form of the solution to this differential equation is

$$ y(t) = y_h(t) + y_p(t) $$

## Section 3.9 - Undetermined Coefficients

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/UndeterminedCoefficients.aspx).

We know the following guesses for functions.

| $g(t)$ | $y_p$ guess |
| :- | -: |
| $\alpha e^{\beta t}$ | $A e^{\beta t}$ |
| $a \cos(\beta t)$ | $A \cos(\beta t) + B \sin(\beta t)$ |
| $b \sin(\beta t)$ | $A \cos(\beta t) + B \sin(\beta t)$ |
| $a \cos(\beta t) + \sin(\beta t)$ | $A \cos(\beta t) + B \sin(\beta t)$ |
| n-th degree polynomial | $A_nt^n + A_{n-1}t^{n-1} + A_1 t + A_0$ |

Combine this with the following:

**Theorem**. Given $y_{p_1}(t)$ is a solution to $y'' + p(t)y' + q(t)y = g_1(t)$ and $y_{p_2}(t)$ is a solution to $y'' + p(t)y' + q(t)y = g_2(t)$, then the function $y_{p_1}(t) + y_{p_2}(t)$ is a solution to $y'' + p(t)y' + q(t)y = g_1(t) + g_2(t)$

## Section 3.10 - Variation of Parameters

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/VariationofParameters.aspx).

Assume we have the differential equation as follows:

$$ y'' + p(t) y' + q(t) y = g(t) $$

The equivilent homogenous differential equation is

$$ y'' + p(t) y' + q(t) y = 0 $$

For this method, we must have $y_1(t)$ and $y_2(t)$ known. Through a lot of math, we see that

$$
y_p = -y_1 \int \frac{y_2(t)g(t)}{W(y_1, y_2)} dt + y_2 \int \frac{y_1(t)g(t)}{W(y_1, y_2)} dt
$$
