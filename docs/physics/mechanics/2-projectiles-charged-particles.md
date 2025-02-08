# Chapter 2 - Projectiles and Charged Particles

## Section 2.1 - Air Resistance

**Definition**. The *drag*, or resistive force on an object due to the atmosphere, is denoted as $\vb{f}$. Note that this is **not** the force density, but the overall force. In most cases, this force directly opposes the direction of motion. If not, the other component is known as *lift*, however this is mostly negligible.

We define air resistance as $\vb{f} = -f(v) \vu{v}$. We consider two types in this text: linear, where $f(v) = f_{lin} = bv$, and quadratic, where $f(v) = f_{quad} = cv^2$. Note that often times we consider both, and state that $f(v) = f_{lin} + f_{quad} = bv + cv^2$.

The linear term comes from viscous drag and is generally proportional to the viscosity of the medium, while quadratic drag tends to arise from the particle needing to accelerate the mass of air which it is constantly colliding against.

In some cases, we can calculate these coefficients. With $D$ as the diameter of a spherical object, and $\beta$ and $\gamma$ as properties of the medium, we can state that $b = \beta D$ and $c = \gamma D^2$. In air at STP, $\beta = 1.6 \times 10^{-4} \text{N} \vdot \text{s}/\text{m}^2$, and $\gamma = 0.25 \text{N} \vdot \text{s}^2/\text{m}^4$.

Oftentimes, one factor is far more impactful than the other, meaning that the smaller of the two may be neglected. To do so, compute the following ratio:

$$\frac{f_{quad}}{f_{lin}} = \frac{cv^2}{bv} = \frac{\gamma D}{\beta}v$$

Note that the result is expected to be of the same order of magnitude as the *Reynolds number* $R = Dv \mathcal{Q}/\eta$, where $\mathcal{Q}$ is the density of the medium and $\eta$ the viscosity.

## Section 2.2 - Linear Air Resistance

First, consider the case in which the drag force is negligible. Then, we see that with $\vb{F}_g = \vb{w} = mg$ and $\vb{F}_{drag} = \vb{f} = -b\vb{v}$, then Newton's second law tells us that

$$\vb{F} = m \dot{\vb{v}} = m\vb{g} - b\vb{b}$$

This separates into two equations:

$$\begin{align}
\dot{v}_x &= -\frac{b}{m}v_x \\
\dot{v}_y &= g - \frac{b}{m}v_y
\end{align}$$

These are separable equations and can be trivially solved.

For an object on a surface in which the only motion is in the $x$-direction, only the first of the above equations applies. Then, we can define $k = \frac{b}{m}$, so that $\dot{v_x} = -k v_x$. This can be integrated to see that $v_x(t) = Ae^{-kt}$. We can also define $\tau = \frac{1}{t} = \frac{m}{b}$, so that $v(t) = Ae^{-\frac{t}{\tau}}$

Now, consider the second equation. This is still separable, however, the math is more complicated. Note that when we set $\dot{v}_y = 0$, we are at some maximum (terminal) velocity $v_{ter}$. Solving, we see that $v_{ter} = \frac{mg}{b}$. Then, we can rewrite our equation as

$$m\dot{v}_y = -b(v_y - v_ter)$$

This can be solved to see that $v(y) = v_{ter} + (v_{y0} - v_{ter})e^{-\frac{t}{\tau}}$.

## Section 2.3 - Trajectory and Range in a Linear Medium

From the velocity functions in the previous section, we can integrate to obtain the position functions.

$$\begin{align}
x(t) &= v_{x0}\tau(1-e^{-\frac{t}{\tau}}) \\
y(t) &= (v_{y0} + v_{ter})\tau(1-e^{-\frac{t}{\tau}})-v_{ter}t
\end{align}$$

We can then solve the first equation for $t$ and substitute into the second to see that

$$y(t) = \frac{v_{y_0} + v_{ter}}{v_{x0}} + v_{ter} \tau \ln(1 - \frac{x}{v_{x0}\tau})$$

Note the trajectory has a vertical asymptote at $x = v_{x0} \tau$.

We can find the horizontal range by setting $y(R) = 0$. This results in an equation that contains many exponential terms, so we want to find an approximation. Truncating the Taylor series for $\ln(1 - \varepsilon)$, we see that $R \approx R_{vac}(1 - \frac{4}{3} \frac{v_{y0}}{v_{ter}})$, where $R_{vac}$, or the air resistance assuming no air resistance, is $R_{vac} = \frac{2 v_{x0}v_{y0}}{g}$.

## Section 2.4 - Quadratic Air Resistance

In the case of quadratic air resistance, we see that $\vb{f} = -c v^2 \vu{v}$. Then, we can see that in the horizontal case, $m\frac{dv}{v_x^2} = -c dt$. Thus,

$$v_x(t) = \frac{v_{x0}}{1+cv_{x0}t/m} = \frac{v_{x0}}{1+\tau/t}$$

where $\tau = m/cv_{x0}$. We can see that at $t = \tau$, $v = v_{x0}/2$.

Thus, $x(t) = v_{x0} \tau \ln(1 + t / \tau)$.

For exclusively vertical motion, we first define $v_{ter} = \sqrt{\frac{mg}{c}}$. Then, we see that $\dot{v_y} = g(1 - \frac{v^2}{v_{ter}^2})$. Solving via separation of variables yields

$$v_y(t) = v_{ter}\tanh(\frac{gt}{v_{ter}})$$

Then, we see that

$$y(t) = \frac{v_{ter}^2}{g} \ln(\cosh(\frac{gt}{v_{ter}}))$$

In the case where there is both vertical and horizontal motion, the differential equation no longer has an analytic solution.

## Section 2.5 - Motion of a Charge in a Uniform Magnetic Field

