# Chapter 5 - Oscillations

## Section 5.1 - Hooke's Law

**Theorem**. Hooke's Law. The force exerted by a spring has the form $F_x = -kx$, where $x$ is the displacement from its equilibrium length and $k$ is the spring constant.

From this, knowing $F = -\nabla U$, we see that the potential energy of a spring is $U(x) = \frac{1}{2} kx^2$.

## Section 5.2 - Simple Harmonic Motion

From $F = m\ddot{x} = -kx$, we see that $\ddot{x} = -\frac{k}{m} x$. We now establish $\omega = \sqrt{\frac{k}{m}}$, or the *angular frequency*. This allows us to state

$$\ddot{x} = -\omega^2 x$$

This may also be written as $\ddot{x} + \omega^2 x = 0$, leading to the characteristic equation $r = \pm \omega i$. Now, we can write the solutions as $x(t) = e^{\pm i \omega t}$, so that $x(t) = C_1 e^{i \omega t} + C_2 e^{-i \omega t}$ by superposition.

We know from Differential Equations that for $r = a \pm bi$, we can apply Euler's formula to see the solution is $e^a(A \cos(b t) + B \sin(bt))$, where $A = C_1 + C_2$ and $B = i(C_1 - C_2)$. Applying this to the spring, we see that

$$x(t) = B_1 \cos (\omega t) + B_2 \sin(\omega t)$$

The displacement function being real thus mandates that $B_2$ is real.

Notably, at $t = 0$, we see that $x(0) = B_1$, and $\dot{x}(0) = B_2$.

**Definition**. The period $\tau$ is the time in which a function repeats itself. The period for $\sin$ and $\cos$ are $\tau = 2\pi$, so the period for this oscillator is $\tau = \frac{2\pi}{\omega} = 2\pi \sqrt{\frac{m}{k}}.

Now, let us simplify. We can write $x$ as

$$x(t) = \sqrt{B_1^2 + B_2^2}[\frac{B_1}{\sqrt{B_1^2 + B_2^2}} \cos(\omega t) + \frac{B_2}{\sqrt{B_1^2 + B_2^2}} \sin(\omega t)]$$

Now, if we have a right triangle with legs $B_1$ and $B_2$, we can define some $\delta$ in said triangle such that $\cos(\delta) = \frac{B_1}{\sqrt{B_1^2 + B_2^2}}$ and $\sin(\delta) = \frac{B_2}{\sqrt{B_1^2 + B_2^2}}$. Note that by this definition, $\tan(\delta) = \frac{B_2}{B_1}$. We  can thus simplify the equation for $x$ to

$$x(t) = \sqrt{B_1^2 + B_2^2}[\cos(\delta) \cos(\omega t) + \sin(\delta) \sin(\omega t)] = \sqrt{B_1^2 + B_2^2} \cos(\omega t - \delta)$$

A different way to see this is to write $C_1 = \frac{1}{2}(B_1 - iB_2)$ and $C_2 = \frac{1}{2}(B_1 + iB_2)$. We can then say that $C_2 = C_1^*$. Then, $x(t) = C_1 e^{i\omega t} + C_1^* e^{-i\omega t}$

We can then solve to see $x(t) = 2\Re(C_1 e^{i \omega t})$, as $x(t) \in \mathbb{R}$. Then, we can see that $2C_1 = B_1 - i B_2 = \frac{1}{\sqrt{B_1^2 + B_2^2}} e^{-i \delta}$. This implies that $x(t) = \Re 2C_1 e^{i \omega t} = \Re \frac{1}{\sqrt{B_1^2 + B_2^2}} A e^{i(\omega t - \delta)}$

If we consider energy, we see that $U = \frac{1}{2}kx^2 = \frac{1}{2}kA^2 \cos^2(\omega t - \delta)$, and that $T = \frac{1}{2}m \dot{x}^2 = \frac{1}{2}m \omega^2 A^2 \sin^2(\omega t - \delta) = \frac{1}{2} k A^2 \sin^2 (\omega t - \delta)$, as $\omega^2 = k/m$ from the original differential equation.

Note that this implies the total energy is a constant, where $E = T + U = \frac{1}{2}kA^2$.

## Section 5.3 - Two-Dimensional Oscillators

**Definition**. An *isotropic harmonic oscillator* is an oscillator in which $\mathbf{F} = -k \mathbf{r}$. That is, $F_x = -kx$, F_y = -ky$, and $F_z = -kz$. Then, with $\omega = \sqrt{k/m}$, we see that $x(t) = A_x \cos(\omega t - \delta_x)$, and $y(t) = A_y \cos(\omega t - \delta_y)$. We can redefine the origin of time such that $\delta_x = 0$ and $\delta_y = delta$.

**Definition**. An $anisotropic oscillator$ is one in which $k_x \neq k_y$. Then, we see that $x(t) = A_x \cos(\omega_x t)$ and $y(t) = A_y \cos(\omega_y t - \delta)$.

## Section 5.4 - Damped Oscillations

We now consider a damping term, in which $\mathbf{F}_{damping} = -b \hat{\mathbf{x}}$. Then, we write

$$m\ddot{x} + b\dot{x} + kx = 0$$

An important note is that this similar to an RLC circuit, in which

$$L\ddot{q} + R\dot{q} + \frac{1}{C}q=0$$

**Definition**. We will define a damping constant $2\beta = \frac{b}{m}$. Additionally, we will rename the constant $\omega_0^2 = k/m$, which denotes the *natural frequency*, or the frequency the system operates at for $b = 0$, that is, there are no resistive forces present. This allows us to rewrite the differential equation as

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = 0$$

Solving the characteristic (or, as this textbook calls it, the *auxiliary equation*), we see that $r = -\beta \pm \sqrt{\beta^2 - \omega_0^2}$. Then, we can write $x(t) = e^{-\beta t}(C_1 e^{\sqrt{\beta^2 - \omega_0^2}t} + C_2 e^{-\sqrt{\beta^2 - \omega_0^2}t})$.

Applying $\beta = 0$, we recover the solution for an undamped oscillator.

Now, consider $\beta \leq \omega_0$, which we call *underdamping*. In this case, $\sqrt{\beta^2 - \omega_0^2} = i\sqrt{\omega_0^2 - \beta^2} = i \omega_1$, where $\omega_1 = \sqrt{\omega_0^2 - \beta^2}$. We can then write $x(t) = e^{-\beta t}(C_1 e^{i\omega_1 t} + C_2 e^{-i\omega_1 t}) = Ae^{-\beta t}\cos(\omega_1 t - \delta)$.

Conversely, when $\beta > \omega_0$, we see *overcamping*. Here, $x(t) = C_1 e^{-\beta + \sqrt{\beta^2 - \omega_0^2}} + C_2 e^{-\beta - \sqrt{\beta^2 - \omega_0^2}}$.

When $\beta = \omega_0$, we are critically damped, in which case $x(t) = C_1 e^{-\beta t} + C_2 t e^(-\beta t)$.

## Section 5.5 - Driven Damped Oscillations

Consider an external force $F(x)$, such that $m\ddot{x} + b\dot{x} + kx = F(x)$. Then, for $f(t) = F(t) / m$,

$$\ddot{x} = 2\beta\dot{x} + \omega_0^2 x = f(t)$$

We can write the differential operator $D = \frac{d^2}{dt^2} + 2\beta \frac{d}{dt} + \omega_0^2$, so that the differential equation becomes $Dx = f$. Notably, this operator is linear.

**Definition**. The equation $Dx = 0$ is the *homogenous* equation.

**Definition**. Some $x_p(t)$ that satisfies $Dx = f$ is a *particular solution*.

**Definition**. Any $x_h(t)$ that satisfies $Dx = 0$ is a *homogenous solution*.

Note that if $x_p$ is a solution to a differential equation, by the linearity of $D$, so is $x_p + x_h$.

Now consider $f(t) = f_0 \cos(\omega t)$, or a driving force with frequency $\omega$. Then, by the method of undetermined coefficients, our particular solution is $x_p = A \cos (\omega t) + B \sin (\omega t)$. However, we're not allowed to use that. We are only allowed to assume there is a second solution $y(t)$ that satisfies $f(t) = f_0 \sin(\omega t)$ instead that also satisfies the differential equation for the original function.

Then, we set $z(t) = x(t) + i y(t)$ and rewrite the differential equation in terms of $z$, where $f(t) = f_0 e^{i \omega t}$. We can then try the solution $C e^{i \omega t}$ to see that $C = \frac{f_0}{\omega_0^2 - \omega^2 + 2 i \beta \omega}$. Then, we can define some $A, \delta$ such that $C = Ae^{-i \delta}$, and applying $A^2 = C C^*$, we see that $A^2 = \frac{f_0^2}{(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2}$, and $\delta = \arctan(\frac{2\beta \omega}{\omega_0^2 - \omega^2})$.

We can then take the real part of $z$ to see $x(t) = A \cos(\omega t - \delta)$.

**Definition**. Any term that dies out exponentially as time passes is called *transient*. The motion that remains is called the *attractor*, as it can arise from many different initial conditions.

## Section 5.6 - Resonance

When $\beta$ is small, we see the second term in the denominator becomes small. Then, if the driving and natural frequency are very different, the amplitude of the resulting wave becomes small. Conversely, if the driving and natural frequency are close together, the amplitude of the wave becomes large.

Notably, if we try and force the oscillator to move at a frequency $\omega$, when close to $\omega_0$, the oscillator responds well, but fails to respond significantly otherwise. This is known as *resonance*.

Then, we can see that $\omega_2 = \sqrt{\omega_0^2 - 2 \beta^2}$ is the frequency at which the response is maximum. This then lets us see that $A_{max} \approx \frac{f_0}{2\beta \omega_0}$.

We can then calculate the FWHM, or full-width at half maximum, and the HWHM, or the half width at half maximum. These are the distance between the two points in which $A^2$ is at half its maximum value. Note that $\omega \approx \omega_0 \pm \beta$, so $\text{FWHM} \approx 2\beta$ and $\text{HWHM} \approx \beta$.

We can then calculate the sharpness of the peak as the natural frequency over the FWHM, or $Q = \frac{\omega_0}{2\beta} = \pi \frac{1 / \beta}{2\pi \omega_0} = \pi \frac{\text{decay time}}{\text{period}}$.

Additionally, we see that $\delta = \arctan(\frac{2\beta \omega}{\omega_0^2 - \omega^2})$. At resonance, this implies that $\delta = \pi / 2$.

## Section 5.7 - Fourier Series

Skipped.

## Section 5.8 - Fourier Series Solution for the Driven Oscillator

If we set $f(t) = f_1(t) + f_2(t)$, we can write $Dx_1 = f_1$ and $Dx_2 = f_2$ such that $D_x = D(x_1 + x_2) = f_1 + x_2 = f$ so then $D_x = f$.

Then, we let $f(t) = \sum_{n=0}^\infty f_n \cos(n \omega t)$, where $f_n$ is a constant.

We then find that $\omega = 2\pi / \tau$.

We can then set $x_n(t) = A_n \cos(n  \omega t - \delta_n)$, where

$$A_n = \frac{f_n}{\sqrt{(\omega_0^2 - n^2 \omega^2)^2 + 4\beta^2n^2\omega^2}}$$

We also see that

$$\delta_n = \arctan(\frac{2\beta n \omega}{\omega_0^2 - n^2 \omega^2})$$

## Section 5.9 - The RMS Displacement; Parseval's Theorem

We know that $x_{rms} = \sqrt{\langle x^2 \rangle}$. Then, we see that $\langle x^2 \rangle = \frac{1}{\tau} \int_{-\tau/2}^{\tau/2}x^2 dt$. In this case,

$$\langle x^2 \rangle = \frac{1}{\tau} \int_{-\tau/2}^{\tau/2} \sum_n \sum_m A_n \cos(n\omega t - \delta_n) A_m \cos(n \omega t - \delta_m) dt$$

We can then apply identities to see that

$$\langle x^2 \rangle = A_0^2 + \frac{1}{2} \sum_{n=1}^\infty A_n^2$$

This assumes that $A_0$ is defined differently than $A_{n \geq 1}$.

This is known as *Parseval's theorem*, and allows us to find the response of an oscillator.
