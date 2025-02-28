# Chapter 6 - Calculus of Variations

## Section 6.1 - Two Examples

Consider two points $(x_1, y_1)$ and $(x_2, y_2)$, and some path $y = y(x)$ joining them. Then, we know that the length of a path segment is $ds = \sqrt{dx^2 + dy^2}$. Then, we know $dy = \frac{dy}{dx}dx = y'(x) dx$, so we can rewrite $ds$ as

$$ds = \sqrt{1 + y'(x)^2} dx$$

This allows us to say that $L = \int_1^2 ds = \int_{x_1}^{x_2} \sqrt{1 + y'(x)^2} dx$. Now, to minimize $L$,  we must find a value of $y'(x)$ that makes the integral minimal.

Now, consider light. The time $dt$  for light to travel $ds$ is $ds/v$ where $n = c / v$ tells us that $dt = n / c ds$. Then, we see that

$$t = \frac{1}{c} \int_1^2 n ds$$

Now, we assume that $n = n(x, y)$, so then

$$int_1^2 n(x, y)ds = \int_{x_1}^{x_2} n(x, y) \sqrt{1 + y'(x)^2} dx$$

Thus, to find the shortest path, we must minimize again.

We know that for some function $f(x)$, a critical point is when $df / dx = 0$. A critical point is a minimum depending on the sign of $df^2 / d^2x$, or neither of it equals zero.

**Definition**. A *stationary point* $x_0$ is a critical point in which the minimum/maximum status is unknown.

## Section 6.2 - The Euler-Lagrange Equation

We have an integral of the form

$$S = \int_{x_1}^{x_2} f[y(x), y'(x), x] dx$$

Here, $f$ depends only on $x$ and functions of $x$.

Now, let $y(x)$ represent the path that minimizes $S$. Then, we can say that any other path can be represented as $Y(x) = y(x) + \alpha\eta$, with the boundary points forcing $\eta(x_1) = \eta(x_2) = 0$. Then, when $\alpha = 0, Y(x) = y(x)$. We can then parameterize $S$ as

$$S(\alpha) = \int_{x_1}^{x_2} f(Y, Y', x) dx = \int_{x_1}^{x_2} f(y + \alpha \eta, y' + \alpha \eta', x) dx$$

Then, we can find $\partial S / \partial \alpha$ as $\int \partial f / \partial \alpha dx$. Applying the chain rule, $\partial f / \partial \alpha = \eta \frac{\partial f}{\partial y} + \eta' \frac{\partial f}{\partial y'}$. Then, we can minimize $S$ by setting its derivative to zero so that

$$0 = \frac{dS}{d\alpha}\int_{x_1}^{x_2}\frac{\partial f}{\partial \alpha}dx = \int_{x_1}^{x_2}(\eta \frac{\partial f}{\partial y} + \eta' \frac{\partial f}{\partial y'})dx = 0$$

Then, we can rewrite the second term by integrating by parts so that

$$\int_{x_1}^{x_2} = \eta'(x) \frac{\partial f}{\partial y'} dx = [\eta(x) \frac{\partial f}{\partial y'}]_{x_1}^{x_2} - \int_{x_1}^{x_2} \eta(x) \frac{d}{dx}(\frac{\partial f}{\partial y'})dx$$

The first term is zero due to the conditions on $\eta(x)$. Then, we see that

$$\int_{x_1}^{x_2} = \eta'(x) \frac{\partial f}{\partial y'} dx = - \int_{x_1}^{x_2} \eta(x) \frac{d}{dx}(\frac{\partial f}{\partial y'})dx$$

We can substitute this into the above equation for the minimal location of $S$ to see that

$$\int_{x_1}^{x_2} \eta(x) (\frac{\partial f}{\partial y} - \frac{d}{dx} \frac{\partial f}{\partial y'}) dx = 0$$

This must be true for any $\eta(x)$. If we let $\eta(x)$ be an arbitrary function with the same sign as the differential terms over the integral, we see that the integral would be non-negative. This forces the differential terms to be zero.

**Definition**. The Euler-Lagrange Equation. The following criteria holds true for all $f(y(x), y'(x), x)$:

$$\frac{\partial f}{\partial y} - \frac{d}{dx}\frac{\partial f}{\partial y'} = 0$$

## Section 6.3 - Applications of the Euler-Lagrange Equation

Recall the distance between two points, in which $f(y, y', x) = \sqrt{1 + y'^2}$. Then, the Euler-Lagrange Equation becomes $\frac{d}{dx} \frac{\partial f}{\partial y'} = 0$, so $\frac{\partial f}{\partial y'} = \frac{y'}{\sqrt{1 + y'^2}}$ is a constant with regards to $x$, which implies that $y'$ is a constant and thus this is a straight line.

Now consider a case where a fixed, frictionless track is placed in a gravitational field. What is the most efficient track from point $1$ to $2$, assuming some horizontal displacement?

We know that due to conservation of energy, $v = \sqrt{2gy}$. From time equations, $t = \int_1^2 \frac{ds}{v}$, so that $t = \int_0^{y_2} \frac{\sqrt{x'(y)^2 + 1}}{\sqrt{2gy}}dy$. Then, $f(x, x', y) = \frac{\sqrt{x'^2 + 1}}{\sqrt{y}}$, and the Euler-Lagrange Equation tells us that $y = a(1 - \cos \theta)$ and $x = a(\theta - \sin \theta) + C$, for some $\theta$.

Note that in no case did we check that the paths found were minimal and not maximal. We  only know that these are statioary points.

## Section 6.4 - More than T wo Variables

Consider $x = x(u), y = y(u)$. Then, $ds = \sqrt{x'(u)^2 + y'(u)^2}du$, so that $L = \int_{u_1}^{u_2} \sqrt{x'(u)^2 + y'(u)^2}du$. Then, $f = f(x, y, x', y', u)$ so that $S = \int_{u_1}^{u_2} f du$. Now, if $x = x(u) + \alpha \xi(u)$ and $y = y(u) + \beta \eta(u)$, we see that $\partial S / \partial \alpha = 0 = \partial S / \partial \Beta$, so that $\frac{\partial f}{\partial x} = \frac{d}{dx} \frac{\partial f}{\partial x'}$, and the same respectively with $y$.

**Definition**. Now, we can say that for a system with $n$ coordinates, we have $q_1, q_2, \ldots, q_n$ position vectors, otherwise known as *generalized coordinates*. Then, we can think of $n$ generalized coordinates as defining a point in an $n$-dimensional *configuration space*.
