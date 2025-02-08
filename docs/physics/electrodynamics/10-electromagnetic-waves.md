# Chapter 10 - Electromagnetic Waves

## Section 10.1 - Time-Dependent Electromagnetic Fields in a Vacuum Satisfy the Wave Equation

Consider an empty space. Then, it is evident that

$$\begin{align}
\div \vb{E} &= 0 \\
\div \vb{H} &= 0
\end{align}$$

$$\begin{align}
\curl \vb{E} + \frac{\partial \vb{B}}{\partial t} &= 0 \\
\curl \vb{H} - \frac{\partial \vb{D}}{\partial t} &= 0
\end{align}$$

As $\vb{B} = \mu_0 \vb{H}$ and $\vb{D} = \varepsilon_0 \vb{E}$ in a vacuum, the third and fourth equations can be rewritten as

$$\begin{align}
\curl \vb{E} + \mu_0 \frac{\partial \vb{H}}{\partial t} &= 0 \\
\curl \vb{H} - \varepsilon_0 \frac{\partial \vb{E}}{\partial t} &= 0
\end{align}$$

We can take the curl of both equations and then substitute to see that

$$\begin{align}
\curl \curl \vb{E} + \mu_0 \varepsilon_0 \frac{\partial^2 \vb{E}}{\partial t^2} &= 0 \\
\curl \curl \vb{H} + \mu_0 \varepsilon_0 \frac{\partial^2 \vb{H}}{\partial t^2} &= 0
\end{align}$$

We can apply a vector identity to see

$$\begin{align}
-\nabla^2 \vb{E} + \mu_0 \epsilon_0 \frac{\partial^2 \vb{E}}{\partial t^2} &= 0 \\
-\nabla^2 \vb{H} + \mu_0 \epsilon_0 \frac{\partial^2 \vb{H}}{\partial t^2} &= 0
\end{align}$$

### Section 10.1.1 - The Wave Equation and Plane Waves

**Definition**. The equation $[\frac{\partial^2}{\partial x^2} - \frac{1}{v^2} \frac{\partial^2}{\partial t^2}] f(x, t) = 0$ is well-known to mathematicians (see [Differential Equations](../../todo.md)), and is known as the **wave equation**. In physics, the speed of the wave is $v = c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$.

Consider some function $f(s)$. If $s = x - vt$ or $x + vt$, it is trivial to see that $f(x)$ satisfies the wave equation.

**Definition**. A *plane wave* is a solution to the Laplacian form of the last two Maxwell equations for empty space that also satisfy the one-dimensional wave equation. However, these solutions may not be valid electromagnetic waves as they are not guaranteed to satisfy the first two Maxwell equations.

Notably, the functions for $\vb{E} = \vb{E}_0 f(s)$ and $\vb{H} = \vb{H}_0 g(s)$ do not have to be equal. However, $v = c$.

**Definition**. A *plane electromagnetic wave* is a plane wave which satisfies the first two Maxwell equations. The divergence equations restrict $\vb{E}_0$ and $\vb{H}_0$ to be in the plane normal to the direction of motion. That is, electomagnetic plane waves are transverse, not longitudinal.

Additionally, the curl equations force $f(s) = g(s)$, such that $H_0 = E_0 \sqrt{\frac{\varepsilon_0}{\mu_0}}$.

**Definition**. The quantity $Y_0 = \sqrt{\frac{\varepsilon_0}{\mu_0}}$ is the *vacuum admittance* and its inverse, $Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}}$ is the *vacuum impedance*.

If we assume the direction of propagation can be written as $\vu{k}$, we can write $f(s) = f(\vu{k} \vdot \vb{r} - vt)$, such that $\vb{E}(\vb{r}, t) = \vb{E}_0 f(\vu{k}\vdot\vb{r} - vt)$, where $\vu{k}\vdot\vb{E}_0 = 0$.

From this, we can see that $\vb{H}(\vb{r}, t) = \sqrt{\frac{\epsilon_0}{\mu_0}} \vu{k} \times \vb{E}_0 f(\vu{k} \vdot \vb{r} - vt)$. Similarly, $\vu{k} \vdot \vb{H} = 0$.

Additionally, we can compute $\vb{S} = \vb{E} \times \vb{H} = c \epsilon_0 E_0^2 f^2(\vu{k} \vdot \vb{r} - vt) \vu{k}$. We can also see that $\epsilon_0 E^2 = \mu_0 H^2$ at any given time.

### Section 10.1.2 - Monochromatic Plane Waves

In any simple material, we like to say that $\vb{D} = \epsilon \vb{E}$ and $\vb{B} = \mu \vb{H}$. However, this only holds true at a fixed frequency $\omega$. For multiple frequencies, we see that $\vb{D}(\omega) = \epsilon{\omega}\vb{E}(\omega)$ and $\vb{B}(\omega) = \mu(\omega)\vb{H}(\omega)$. This causes problems. As such, we will want to consider waves that are only composed of one frequency under Fourier decomposition.

**Definition**. A *monochromatic* plane wave is a plane wave in which the full Fourier series of $f(x)$ has only one term. That is, $f(x)$ is $\sin(x)$ or $\cos(x)$. We furthermore define a *wave vector* $\vb{k}$ as $\vb{k} = k \vu{k}$, so that $\omega = kc$. Then,

$$\begin{align}
\vb{E}(\vb{r}, t) &= \vb{E_0} \cos(\vb{k} \vdot \vb{r} - \omega t) \\
\vb{H}(\vb{r}, t) &= \sqrt{\frac{\epsilon_0}{\mu_0}} \vu{k} \times \vb{E}_0 \cos(\vb{k} \vdot \vb{r} - \omega t)
\end{align}$$

Notably, the frequency, or number of cycles per second, is $f = \frac{\omega}{2\pi}$, and wavelength $\lambda = \frac{2\pi}{k}$.

We can calculate the energy density $u$, energy current density $\vb{S}$, momentum density $\vb{g}$, and momentum current density $-\overleftrightarrow{\vb{T}}$

### Section 10.1.3 - Monochromatic Plane Waves in a Linear Model

Monochromatic plane waves with frequency $\omega$ in a simple linear material are similar to monochromatic plane waves in a vacuum, except when in a material, we know that the magnitude of the wave vector $k = \frac{\omega}{v}$, and $v = \frac{1}{\sqrt{\mu \varepsilon}}$.

### Section 10.1.4 - Polarization of Monochromatic Plane Waves

Any plane wave described in such a way that $\vb{E} = \vb{E}_0 f(\vb{k} \vdot \vb{r} - ct)$ is linearly polarized in the direction of $\vb{E}_0$. That is, the direction of polarization is the direction of $\vb{E}$, and if that direction is unchanging, the wave is linearly polarized.

Notably, an elliptically polarized wave can be described as follows:

$$\begin{align}
\vb{E}(\vb{r}, t) &= E_{x0} \vu{x} \cos(kz - \omega t) + E_{y0} \vu{y} \sin(kz - \omega t) \\
\vb{H}(\vb{r}, t) &= \sqrt{\frac{\varepsilon}{\mu}} (E_{x0} \vu{y} \cos(kz - \omega t) - E_{y0} \vu{x} \sin(kz - \omega t))
\end{align}$$

If $E_{x0} = E_{y0}$, the wave is said to be circularly polarized.

## Section 10.2 - Reflection and Refraction of Plane Electromagnetic Waves at a a Planar Interface

This section will focus on plane monochromatic waves incident from material 1 onto material 2, where both materials are homogenous insulators and the surface between the two materials is smooth (on the scale of the wavelength).

In this case, we must re-consider Maxwell's equations. We know from previous sections that $\div \vb{E} = \frac{\vb{\rho_e}}{\varepsilon_0}$ and $\div \vb{H} = \frac{\vb{\rho_m}}{\mu_0}$. We also know that $\div \vb{D} = \rho_{ef}$ and $\div \vb{B} = \rho_{mf}$.

Consider the boundary between the two materials. If we consider $\div \vb{D}$, and take the integral over a Gaussian pillbox on the boundary, we can apply divergence theorem to see that $\int_V \div \vb{D} dV = \int_{SofV} D \vdot \vu{n} dS = \rho_{efree}$. If we assume the materials are insulating, we do not expect to find any electrical charge, so $\rho_{efree} = 0$. Thus, we can say that $\int_{SofV} D \vdot \vu{n} = 0$, so $\vb{D}_1 \vdot \vu{n} + \vb{D}_2 \vdot \vu{n} = \vb{D_1} \vdot \vu{z} + \vb{D}_1 \vdot (-\vu{n}) = 0$. Then, we can say that $\vb{D}_1 \vdot{z} = \vb{D}_2 \vdot{z}$, or in simpler terms, $\vdot{D}_1^\perp = \vdot{D}_2^\perp$.

Applying the same logic to $\vb{B}$, we see that $\vdot{B}_1^\perp = \vdot{B}_2^\perp$. Note that due to the existence of polarization and magnetization, we cannot say the same regarding $\mathbf{E}$ or $\mathbf{H}$.