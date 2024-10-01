# Section 1 - Basic Concepts

## Section 1.1 - Definitions

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/classes/de/Definitions.aspx).

**Definition**. A *differential equation* is an equation that describes a function in terms of its derivatives. Examples of differential equations include Newton's Laws, among others.

**Definition**. The *order* of a differential equation is the largest derivative present in the equation with a non-zero constant.

**Definition**. A differential equation that only involves derivatives with respect to one variable is called an *ordinary* differential equation (ODE).

**Definition**. A differential equation that describes a function in terms of derivatives with respect to more than one linearly-independent variable is called a *partial* equation.

**Definition**. A *linear* differential equation is any differential equation that cn be written in the following form:

\[ a_n(t)y^{(n)}(t) + a_{n-1}(t)+y^{n-1}(t) + . . . + a_1(t)y'(t) + a_0(t)y(t) = g(t) \]

Note that $a_n(t)$ does not depeond on any derivative of $y$, so the presence of terms such as $e^y$ or $\sqrt{y'}$ signal that the equation is *nonlinear*.

**Definition**. The *solution(s)* to a differential equation over an inverval $\alpha < t < \beta$ are any funcion(s) $y(t)$ that satisfy the differential equation.

**Definition**. The *initial conditions* are a condition or set of conditions that constrain the possible solution sets.

**Definition**. An *Initial Value Problem* is a differential equation along with the appropriate boundary or initial conditions.

**Definition**. The *integral of validity* for a solution to a differential equation is the largest possible interval containing the initial coniditions for which the solution is valid.

**Definition**. The *general solution* to a differential equation is the most general form a solution to a differential equation can take without requiring the initial conditions.

**Definition**. The *actual solution* to a differential equation is the specific solution that satisfies the differential equation and the boundary conditions.

**Definition**. A solution is said to be *explicit* if it can be written in the form $y = y(t)$. Otherwise, it is said to be *implicit*.

## Section 1.2 - Directional Fields

This section is from [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/DE/DirectionFields.aspx).

**Definition**. A directional field is the graph of a $t$ vs. $y(t)$, with vectors drawn at each point with a slope corresponding to $y'(t)$. Notably, each arrow will be pointed right (towards increasing $t$).