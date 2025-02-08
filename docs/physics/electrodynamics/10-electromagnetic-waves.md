# Chapter 10 - Electromagnetic Waves

## Section 10.1 - Time-Dependent Electromagnetic Fields in a Vacuum Satisfy the Wave Equation

Consider an empty space. Then, it is evident that

$$\begin{align}
    \nabla \cdot \mathbf{E} &= 0 \\
    \nabla \cdot \mathbf{H} &= 0
\end{align}$$

$$\begin{align}
\nabla \times \mathbf{E} + \frac{\partial \mathbf{B}}{\partial t} &= 0 \\
\nabla \times \mathbf{H} - \frac{\partial \mathbf{D}}{\partial t} &= 0
\end{align}$$

As $\mathbf{B} = \mu_0 \mathbf{H}$ and $\mathbf{D} = \varepsilon_0 \mathbf{E}$ in a vacuum, the third and fourth equations can be rewritten as

$$\begin{align}
\nabla \times \mathbf{E} + \mu_0 \frac{\partial \mathbf{H}}{\partial t} &= 0 \\
\nabla \times \mathbf{H} - \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} &= 0
\end{align}$$

We can take the curl of both equations and then substitute to see that

$$\begin{align}
\nabla \times \nabla \times \mathbf{E} + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} &= 0 \\
\nabla \times \nabla \times \mathbf{H} + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{H}}{\partial t^2} &= 0
\end{align}$$

We can apply a vector identity to see

$$\begin{align}
-\nabla^2 \mathbf{E} + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} &= 0 \\
-\nabla^2 \mathbf{H} + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{H}}{\partial t^2} &= 0
\end{align}$$

### Section 10.1.1 - The Wave Equation and Plane Waves

**Definition**. The equation $[\frac{\partial^2}{\partial x^2} - \frac{1}{v^2} \frac{\partial^2}{\partial t^2}] f(x, t) = 0$ is well-known to mathematicians (see [Differential Equations](../../todo.md)), and is known as the **wave equation**. In physics, the speed of the wave is $v = c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$.

Consider some function $f(s)$. If $s = x - vt$ or $x + vt$, it is trivial to see that $f(x)$ satisfies the wave equation.

**Definition**. A *plane wave* is a solution to the Laplacian form of the last two Maxwell equations for empty space that also satisfy the one-dimensional wave equation. However, these solutions may not be valid electromagnetic waves as they are not guaranteed to satisfy the first two Maxwell equations.

Notably, the functions for $\mathbf{E} = \mathbf{E}_0 f(s)$ and $\mathbf{H} = \mathbf{H}_0 g(s)$ do not have to be equal. However, $v = c$.

**Definition**. A *plane electromagnetic wave* is a plane wave which satisfies the first two Maxwell equations. The divergence equations restrict $\mathbf{E}_0$ and $\mathbf{H}_0$ to be in the plane normal to the direction of motion. That is, electomagnetic plane waves are transverse, not longitudinal.

Additionally, the curl equations force $f(s) = g(s)$, such that $H_0 = E_0 \sqrt{\frac{\varepsilon_0}{\mu_0}}$.

**Definition**. The quantity $Y_0 = \sqrt{\frac{\varepsilon_0}{\mu_0}}$ is the *vacuum admittance* and its inverse, $Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}}$ is the *vacuum impedance*.

If we assume the direction of propagation can be written as $\hat{\mathbf{k}}$, we can write $f(s) = f(\hat{\mathbf{k}} \cdot \mathbf{r} - vt)$, such that $\mathbf{E}(\mathbf{r}, t) = \mathbf{E}_0 f(\hat{\mathbf{k}}\cdot\mathbf{r} - vt)$, where $\hat{\mathbf{k}}\cdot\mathbf{E}_0 = 0$.

From this, we can see that $\mathbf{H}(\mathbf{r}, t) = \sqrt{\frac{\varepsilon_0}{\mu_0}} \hat{\mathbf{k}} \times \mathbf{E}_0 f(\hat{\mathbf{k}} \cdot \mathbf{r} - vt)$. Similarly, $\hat{\mathbf{k}} \cdot \mathbf{H} = 0$.

Additionally, we can compute $\mathbf{S} = \mathbf{E} \times \mathbf{H} = c \varepsilon_0 E_0^2 f^2(\hat{\mathbf{k}} \cdot \mathbf{r} - vt) \hat{\mathbf{k}}$. We can also see that $\varepsilon_0 E^2 = \mu_0 H^2$ at any given time.

### Section 10.1.2 - Monochromatic Plane Waves

In any simple material, we like to say that $\mathbf{D} = \varepsilon \mathbf{E}$ and $\mathbf{B} = \mu \mathbf{H}$. However, this only holds true at a fixed frequency $\omega$. For multiple frequencies, we see that $\mathbf{D}(\omega) = \varepsilon(\omega)\mathbf{E}(\omega)$ and $\mathbf{B}(\omega) = \mu(\omega)\mathbf{H}(\omega)$. This causes problems. As such, we will want to consider waves that are only composed of one frequency under Fourier decomposition.

**Definition**. A *monochromatic* plane wave is a plane wave in which the full Fourier series of $f(x)$ has only one term. That is, $f(x)$ is $\sin(x)$ or $\cos(x)$. We furthermore define a *wave vector* $\mathbf{k}$ as $\mathbf{k} = k \hat{\mathbf{k}}$, so that $\omega = kc$. Then,

$$\begin{align}
\mathbf{E}(\mathbf{r}, t) &= \mathbf{E_0} \cos(\mathbf{k} \cdot \mathbf{r} - \omega t) \\
\mathbf{H}(\mathbf{r}, t) &= \sqrt{\frac{\varepsilon_0}{\mu_0}} \hat{\mathbf{k}} \times \mathbf{E}_0 \cos(\mathbf{k} \cdot \mathbf{r} - \omega t)
\end{align}$$

Notably, the frequency, or number of cycles per second, is $f = \frac{\omega}{2\pi}$, and wavelength $\lambda = \frac{2\pi}{k}$.

We can calculate the energy density $u$, energy current density $\mathbf{S}$, momentum density $\mathbf{g}$, and momentum current density $-\overleftrightarrow{\mathbf{T}}$

### Section 10.1.3 - Monochromatic Plane Waves in a Linear Model

Monochromatic plane waves with frequency $\omega$ in a simple linear material are similar to monochromatic plane waves in a vacuum, except when in a material, we know that the magnitude of the wave vector $k = \frac{\omega}{v}$, and $v = \frac{1}{\sqrt{\mu \varepsilon}}$.

### Section 10.1.4 - Polarization of Monochromatic Plane Waves

Any plane wave described in such a way that $\mathbf{E} = \mathbf{E}_0 f(\mathbf{k} \cdot \mathbf{r} - ct)$ is linearly polarized in the direction of $\mathbf{E}_0$. That is, the direction of polarization is the direction of $\mathbf{E}$, and if that direction is unchanging, the wave is linearly polarized.

Notably, an elliptically polarized wave can be described as follows:

$$\begin{align}
\mathbf{E}(\mathbf{r}, t) &= E_{x0} \hat{\mathbf{x}} \cos(kz - \omega t) + E_{y0} \hat{\mathbf{y}} \sin(kz - \omega t) \\
\mathbf{H}(\mathbf{r}, t) &= \sqrt{\frac{\varepsilon}{\mu}} (E_{x0} \hat{\mathbf{y}} \cos(kz - \omega t) - E_{y0} \hat{\mathbf{x}} \sin(kz - \omega t))
\end{align}$$

If $E_{x0} = E_{y0}$, the wave is said to be circularly polarized.

## Section 10.2 - Reflection and Refraction of Plane Electromagnetic Waves at a a Planar Interface

This section will focus on plane monochromatic waves incident from material 1 onto material 2, where both materials are homogenous insulators and the surface between the two materials is smooth (on the scale of the wavelength).

In this case, we must re-consider Maxwell's equations. We know from previous sections that $\nabla \cdot \mathbf{E} = \frac{\mathbf{\rho_e}}{\varepsilon_0}$ and $\nabla \cdot \mathbf{H} = \frac{\mathbf{\rho_m}}{\mu_0}$. We also know that $\nabla \cdot \mathbf{D} = \rho_{ef}$ and $\nabla \cdot \mathbf{B} = \rho_{mf}$.

Consider the boundary between the two materials. If we consider $\nabla \cdot \mathbf{D}$, and take the integral over a Gaussian pillbox on the boundary, we can apply divergence theorem to see that $\int_V \nabla \cdot \mathbf{D} dV = \int_{SofV} \mathbf{D} \cdot \hat{\mathbf{n}} dS = \rho_{efree}$. If we assume the materials are insulating, we do not expect to find any electrical charge, so $\rho_{efree} = 0$. Thus, we can say that $\int_{SofV} D \cdot \hat{\mathbf{n}} = 0$, so $\mathbf{D}_1 \cdot \hat{\mathbf{n}} + \mathbf{D}_2 \cdot \hat{\mathbf{n}} = \mathbf{D_1} \cdot \hat{\mathbf{z}} + \mathbf{D}_1 \cdot (-\hat{\mathbf{n}}) = 0$. Then, we can say that $\mathbf{D}_1 \cdot \hat{\mathbf{n}} = \mathbf{D}_2 \cdot \hat{\mathbf{n}}$, or in simpler terms, $\mathbf{D}_1^\perp = \mathbf{D}_2^\perp$.

Applying the same logic to $\mathbf{B}$, we see that $\mathbf{B}_1^\perp = \mathbf{B}_2^\perp$. Note that due to the existence of polarization and magnetization, we cannot say the same regarding $\mathbf{E}$ or $\mathbf{H}$.