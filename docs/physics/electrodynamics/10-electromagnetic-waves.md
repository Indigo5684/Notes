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

**Definition**. The equation $[\frac{\partial^2}{\partial x^2} - \frac{1}{\nu^2} \frac{\partial^2}{\partial t^2}] f(x, t) = 0$ is well-known to mathematicians (see [Differential Equations](../../todo.md)), and is known as the **wave equation**. In physics, the speed of the wave is $\nu = c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$.

Consider some function $f(s)$. If $s = x - \nu t$ or $x + \nu t$, it is trivial to see that $f(x)$ satisfies the wave equation.

**Definition**. A *plane wave* is a solution to the Laplacian form of the last two Maxwell equations for empty space that also satisfy the one-dimensional wave equation. However, these solutions may not be valid electromagnetic waves as they are not guaranteed to satisfy the first two Maxwell equations.

Notably, the functions for $\mathbf{E} = \mathbf{E}_0 f(s)$ and $\mathbf{H} = \mathbf{H}_0 g(s)$ do not have to be equal. However, $\nu = c$.

**Definition**. A *plane electromagnetic wave* is a plane wave which satisfies the first two Maxwell equations. The divergence equations restrict $\mathbf{E}_0$ and $\mathbf{H}_0$ to be in the plane normal to the direction of motion, as $\hat{\mathbf{K}} \cdot \mathbf{E}_0 = 0$. That is, electomagnetic plane waves are transverse, not longitudinal.

Additionally, the curl equations force $f(s) = g(s)$, such that $H_0 = E_0 \sqrt{\frac{\varepsilon_0}{\mu_0}}$.

**Definition**. The quantity $Y_0 = \sqrt{\frac{\varepsilon_0}{\mu_0}}$ is the *vacuum admittance* and its inverse, $Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}}$ is the *vacuum impedance*.

If we assume the direction of propagation can be written as $\hat{\mathbf{k}}$, we can write $f(s) = f(\hat{\mathbf{k}} \cdot \mathbf{r} - \nu t)$, such that $\mathbf{E}(\mathbf{r}, t) = \mathbf{E}_0 f(\hat{\mathbf{k}}\cdot\mathbf{r} - \nu t)$, where $\hat{\mathbf{k}}\cdot\mathbf{E}_0 = 0$.

From this, we can see that $\mathbf{H}(\mathbf{r}, t) = \sqrt{\frac{\varepsilon_0}{\mu_0}} \hat{\mathbf{k}} \times \mathbf{E}_0 f(\hat{\mathbf{k}} \cdot \mathbf{r} - \nu t)$. Similarly, $\hat{\mathbf{k}} \cdot \mathbf{H} = 0$.

Additionally, we can compute $\mathbf{S} = \mathbf{E} \times \mathbf{H} = c \varepsilon_0 E_0^2 f^2(\hat{\mathbf{k}} \cdot \mathbf{r} - \nu t) \hat{\mathbf{k}}$. We can also see that $\varepsilon_0 E^2 = \mu_0 H^2$ at any given time.

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

Monochromatic plane waves with frequency $\omega$ in a simple linear material are similar to monochromatic plane waves in a vacuum, except when in a material, we know that the magnitude of the wave vector $k = \frac{\omega}{\nu}$, and $\nu = \frac{1}{\sqrt{\mu \varepsilon}}$.

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

### Section 10.2.1 - Boundary Conditions at an Interface Between Two Materials

Consider the boundary between the two materials. If we consider $\nabla \cdot \mathbf{D}$, and take the integral over a Gaussian pillbox on the boundary, we can apply divergence theorem to see that $\int_V \nabla \cdot \mathbf{D} dV = \int_{SofV} \mathbf{D} \cdot \hat{\mathbf{n}} dS = \rho_{efree}$. If we assume the materials are insulating, we do not expect to find any electrical charge, so $\rho_{efree} = 0$. Thus, we can say that $\int_{SofV} D \cdot \hat{\mathbf{n}} = 0$, so $\mathbf{D}_1 \cdot \hat{\mathbf{n}} + \mathbf{D}_2 \cdot \hat{\mathbf{n}} = \mathbf{D_1} \cdot \hat{\mathbf{z}} + \mathbf{D}_1 \cdot (-\hat{\mathbf{n}}) = 0$. Then, we can say that $\mathbf{D}_1 \cdot \hat{\mathbf{n}} = \mathbf{D}_2 \cdot \hat{\mathbf{n}}$, or in simpler terms, $\mathbf{D}_1^\perp = \mathbf{D}_2^\perp$.

Applying the same logic to $\mathbf{B}$, we see that $\mathbf{B}_1^\perp = \mathbf{B}_2^\perp$. Note that due to the existence of polarization and magnetization, we cannot say the same regarding $\mathbf{E}$ or $\mathbf{H}$.

Now, consider a rectangular loop along the interface. If we then consider $\int_S (\nabla \times \mathbf{E}) \cdot d\mathbf{S} = \int_{\partial S} \mathbf{E} \cdot d\mathbf{l} = -\frac{\partial \Phi_B}{\partial t}$. If we let the width of the rectangle approach $0$, then $\int_{\partial S} \mathbf{E} \cdot d\mathbf{l} = \mathbf{E}_1 \cdot d\mathbf{l} + \mathbf{E}_2 \cdot d\mathbf{l} = 0$, which implies that $\mathbf{E}_1 \cdot d\mathbf{l} = \mathbf{E}_2 \cdot d\mathbf{l}$, or in other words, $\mathbf{E}_1^\parallel = \mathbf{E}_2^\parallel$.

Applying the same logic to the other Maxwell equation, we see that $\mathbf{H}_1^\parallel = \mathbf{H}_2^\parallel$.

### Section 10.2.2 - Normal Incidence

Consider a monochromatic plane wave that is incident normally from material 1 onto material 2. That is, the wave vector $\mathbf{k}$ is normal to the interface. In this case, we will let the interface be at $z=0$ on the $x-y$ plane, and $\hat{\mathbf{k}} = \hat{\mathbf{z}}$.

Here, we can write the incident wave as $\mathbf{E}_i (z, t) = E_i \hat{\mathbf{x}} \cos{k_1 z - \omega t}$. Then, Maxwell's equations give us $\mathbf{H}_i(z, t) = Y_1 E_i \hat{\mathbf{y}} \cos(k_1 z - \omega 2)$. By symmetry, we expect the reflected wave to be in the $-z$ direction, with some phase $\phi_r$ such that the wave is a function of $\cos(-k_1 z - \omega t + \phi_r)$. Additionally, we expect the transmitted wave to be of the form $\cos(k_2 z - \omega t + \phi_t)$. This gives for material 1

$$\begin{align}
\mathbf{E}_1(z, t) &= \mathbf{E}_i(z, t) + \mathbf{E}_r(z, t) &= E_i \hat{\mathbf{x}} \cos(k_1 z - \omega t) + \mathbf{E}_r \cos(k_1 z - \omega t - \phi_r) \\
\mathbf{H}_1(z, t) &= \mathbf{H}_i(z, t) + \mathbf{H}_r(z, t) &= Y_1 E_i \hat{\mathbf{y}} \cos(k_1 z - \omega t) + \mathbf{H}_r \cos(k_1 z - \omega t - \phi_r) \\
\end{align}$$

In material 2, we see that

$$\begin{align}
\mathbf{E}_2(z, t) &= \mathbf{E}_t \cos(k_2 z - \omega t - \phi_t) \\
\mathbf{H}_2(z, t) &= \mathbf{H}_t \cos(k_2 z - \omega t - \phi_t) \\
\end{align}$$

Now, break $\mathbf{E}_r$ into components such that $\mathbf{E}_r = E_{rx} \hat{\mathbf{x}} + E_{ry} \hat{\mathbf{y}}$. Then, we see that

$$\begin{align}
\mathbf{E}_r(z, t) &= (E_{rx} \hat{\mathbf{x}} + E_{ry} \hat{\mathbf{y}}) \cos(k_1 z - \omega t - \phi_r) \\
\mathbf{H}_r(z, t) &= -Y \hat{\mathbf{z}} \times (E_{rx} \hat{\mathbf{x}} + E_{ry} \hat{\mathbf{y}}) \cos(k_1 z - \omega t - \phi_r) \\
\end{align}$$

Evaluation at $z = 0$, we see that

$$\begin{align}
\mathbf{E}_1 &= \hat{\mathbf{x}} E_i \cos(-\omega t) + (E_{rx} \hat{\mathbf{x}} + E_{ry} \hat{\mathbf{y}}) \cos(-\omega t - \phi_r) \\
\mathbf{H}_1 &= \hat{\mathbf{y}} Y_1 E_i \cos(-\omega t) + Y_1(-E_{rx} \hat{\mathbf{y}} + E_{ry} \hat{\mathbf{x}}) \cos(-\omega t - \phi_r) \\
\end{align}$$

In material 2, we see that

$$\begin{align}
\mathbf{E}_2(z, t) &= (E_{tx} \hat{\mathbf{x}} + E_{ty} \hat{\mathbf{y}}) \cos(-\omega t - \phi_t) \\
\mathbf{H}_2(z, t) &= Y_2(E_{tx} \hat{\mathbf{y}} - E_{ty} \hat{\mathbf{x}}) \cos(-\omega t - \phi_t) \\
\end{align}$$

In this case, applying boundary conditions is as simple as matching components to obtain two (out of four) equations:

$$\begin{align}
\mathbf{E}_y &: E_{ry} \cos(-\omega t - \phi_r) &= E_{ty} \cos(-\omega t - \phi_t) \\
\mathbf{H}_x &: Y_1 E_{ry} \cos(-\omega t - \phi_r) &= -Y_2 E_{ty} \cos(-\omega t - \phi_t)
\end{align}$$

However, this would imply that $Y_1 = -Y_2$, which is not possible for ordinary materials. As such, we set $E_{ry} = 0$, which then implies $E_{ty} = 0$ (or vice-versa). Then, with $E_r = E_{rx}$ and $E_t = E_{tx}$, we see that the other two component-wise equations yield

$$\begin{align}
E_i \cos(\omega t) + E_r \cos(\omega t - \phi_r) &= E_t \cos(\omega t - \phi_t) \\
Y_1 E_i \cos(\omega t) - Y_1 E_r \cos(\omega t - \phi_r) &= Y_2 E_t \cos(\omega t - \phi_t) \\
\end{align}$$

From this, we can apply the identity $\cos(\omega t - \phi) = \cos(\omega t) \cos \phi + \sin(\omega t) \sin \phi$ to split each equation into two equations that must hold for any $t$. Then, comparing the $E \sin \omega t$ and $H \sin \omega t$ equations lead us to the conclusion that $\sin \phi_r = \sin \phi_t = 0$. Thus, we see that $E_i + E_r = E_t$ and $Y_1 (E_i - E_r) = Y_2 E_t$. We can solve this system to see

$$\begin{align}
E_t &= \frac{2Y_1}{Y_1 + Y_2} E_i \\
E_r = \frac{Y_1 - Y_2}{Y_1 + Y_2} E_i
\end{align}$$

If we assume $\mu_1 = \mu_2$, we can rewrite the equations in terms of wave numbers $k_i$, where $k_i = \frac{\omega}{\nu_i} = \omega \sqrt{\mu_i \varepsilon_i}$

$$\begin{align}
E_t &= \frac{2k_1}{k_1 + k_2} E_i \\
E_r = \frac{k_1 - k_2}{k_1 + k_2} E_i
\end{align}$$

**Definition**. We can also define the *index of refraction* for a material $n$ as $n_i = \sqrt{\frac{\varepsilon_i \mu_i}{\varepsilon_0 \mu_0}}$.

When $\mu_1 = \mu_2 = \mu_0$, we can write as $n_i = \sqrt{\frac{\varepsilon_i}{\varepsilon_0}}$. Then, we can write the reflected and transmitted amplitudes as

$$\begin{align}
E_t &= \frac{2n_1}{n_1 + n_2} E_i \\
E_r &= \frac{n_1 - n_2}{n_1 + n_2} E_i
\end{align}$$

We can also define the average power incident on the interface as $I_(in) = \langle \mathbf{S}_i \cdot \hat{\mathbf{n}} \rangle = \langle (\mathbf{E}_i \times \mathbf{H}_i) \cdot \hat{\mathbf{n}} \rangle$. We know that $\mathbf{E}_i \times \mathbf{H}_i$ is in the direction of $\hat{\mathbf{n}}$, so $I_{in} = \langle (\mathbf{E}_i \times (Y_1 \hat{\mathbf{k}} \times \mathbf{E}_i) \cdot \hat{\mathbf{z}}) \rangle = \frac{1}{2} Y_1 E_i^2$. We can further define $I_r = -\frac{1}{2} Y_1 E_t^2$ and $I_t = \frac{1}{2}Y_2 E_t^2$.

We can then compute $R = \frac{|I_r|}{I_{in}} = \frac{E_r^2}{E_i^2} = (\frac{Y_1 - Y_2}{Y_1 + Y_2})^2$ to see the fraction of power reflected and $I_t = \frac{I_t}{I_{in}} = \frac{Y_2 E_t^2}{Y_1 E_i^2} = \frac{4 Y_1 Y_2}{(Y_1 + Y_2)^2}$. Note that mathematically, $R + T = 1$. That is, all the power of the incident wave is either reflected or transmitted. Additionally, when $\mu_1 \approx \mu_2$, we can replace $Y$ with $n$.

### Section 10.2.3 - Oblique Incidence

Now, we assume that the wave is incident to the interface at some angle $\theta_i$.

**Definition**. The *interfacial plane* is the interface. The *plane of incidence* is the plane defined by the incident wave vector $\mathbf{k}_i$ and the normal vector of the interfacial plane $\mathbf{z}$

**Theorem**. Snell's Law. In the plane if incidence, the continuity of the electromagnetic field implies that for all times on the $z=0$ plane, the argument of the $\cos(\mathbf{k}_{i,r,t} \cdot \mathbf{r} - \omega t)$ must be equal. That is, in our example, for $\mathbf{r} = x \hat{\mathbf{x}} + y \hat{\mathbf{y}}$, we see that $\mathbf{k}_i \cdot \mathbf{r} = \mathbf{k}_t \cdot \mathbf{r} + \phi_r = \mathbf{k}_t \cdot \mathbf{r} + \phi_t$. Then, $\phi_r$ and $\phi_t$ must vanish, and the wave vectors must satisfy $k_{ix}x + k_{iy}y = k_{rx}x + k_{ry}y = k_{tx}x + k_{ty}y$. This implies that $k_{ix} = k_{rx} = k_{tx}$ and $k_{iy} = k_{ry} + k_{ty}$.

More generally, the requirement of continuity on the interface implies that the three wave vectors are coplanar and that components parallel to the interface must be equal, leading to $k_i \sin \theta_i = k_r \sin \theta_r = k_t \sin \theta_t$. Note that in this case, $k_i = k_r = \frac{\omega}{\nu}$ as they describe propagation in the same media, so $\theta_r = \theta_i$. As $n \propto \frac{1}{\nu}$, we see that $n \propto k$, so we can rewrite Snell's Law as $n_i \sin \theta_i = n_t \sin \theta_t$. This gives us the following wave vectors:

$$\begin{align}
\mathbf{k}_i &= k_i(\sin \theta_i \hat{\mathbf{x}} + \cos \theta_i \hat{\mathbf{z}}) \\
\mathbf{k}_r &= k_i(\sin \theta_i \hat{\mathbf{x}} - \cos \theta_i \hat{\mathbf{z}}) \\
\mathbf{k}_t &=(k_t \sin \theta_t \hat{\mathbf{x}} + k_t \cos \theta_t \hat{\mathbf{z}}) = (k_i \sin \theta_i \hat{\mathbf{x}} + k_t \cos \theta_t \hat{\mathbf{z}})
\end{align}$$

Additionally, if we write Snell's Law as $\sin \theta_t = \frac{n_i}{n_t} \sin\theta_i$, we c an see that it predicts the angle of refraction. Note that if $\frac{n_i}{n_t} \sin\theta_i \geq 1$, we see total internal reflection and there will be no transmitted waves.

#### Reflected and transmitted Fields for Oblique Incidence

Any incident oblique wave can be written as a superposition of two waves, one with transverse magnetic and electric fields respectively. A transverse electric (TE) wave has its electric field perpendicular to the plane of incidence. Respectively, a transverse magnetic (TM) wave has its magnetic field perpendicular to the plane of incidence.

Thus, if $\hat{\mathbf{k}}_i = \sin \theta_i \hat{\mathbf{x}} + \cos \theta_i \hat{\mathbf{z}}$, we can say that an incident wave with arbitrary polarization can be written as $\mathbf{E}(\mathbf{r}, t) = (E_{TE}(-\hat{\mathbf{y}}) + E_{TM}\hat{\mathbf{k}} \times (-\hat{\mathbf{y}})) \cos(\mathbf{k}_i \cdot \mathbf{r} - \omega t)$.

In the case of a transverse electric field, $\mathbf{E}$ is perpendicular to the plane of incidence. We know that $\mathbf{E}_r \perp \mathbf{k}_r$ and $\mathbf{E}_t \perp \mathbf{k}_r$. Knowing our definition of $\mathbf{r}$, we can say that $E_{rz} = \tan \theta_i E_{rx}$ and $E_{tz} = -\tan \theta_t E_{tx}$. Continuity of $\mathbf{D}^\perp$ requires that $\varepsilon_1 E_{rz} = \varepsilon_2 E_{tz}$, and continuity of $\mathbf{E}^\parallel$ requires that $E_{rx} = E_{tx}$. We can then see that $\varepsilon_1 \tan \theta_i = -\varepsilon_2 \tan \theta_t E_{tx}$, which we can substitute $E_{rx} = E_{tx}$ to see that $\varepsilon_1 \tan \theta_i = \varepsilon_2 \tan \theta_t$. However, this gives us an equation for $\tan \theta_t$ which contradicts with an equation that is not derived in the textbook. This implies that the $x$ and $z$ components of the electric field vanish.

All that is left is the $y$-direction, for which continuity requires that $E_i + E_r = E_t$. The continuity of the $x$-component of the magnetic fields thus requires that $[Y_1 (\hat{\mathbf{k}}_i \times E_i \hat{\mathbf{y}} + \hat{\mathbf{k}}_r \times E_r \hat{\mathbf{y}}) - Y_2 (\hat{\mathbf{k}}_t \times E_t \hat{\mathbf{y}})] \cdot \hat{\mathbf{x}} = 0$. We can use the scalar triple product identity to simplify this to $[Y_1 (\hat{\mathbf{k}}_i E_i + \hat{\mathbf{k}}_r E_r) - Y_2(\hat{\mathbf{k}}_t E_t)] \cdot \hat{\mathbf{z}} = 0$. This can be simplified to tell us that $Y_i (E_i - E_r) \cos(\theta_i) = Y_2 E_t \cos \theta_t$. These can be solved to find that $E_t = \frac{2Y_1 \cos \theta_i}{Y_1 \cos \theta_i + Y_2 \cos \theta_t} E_i$ and $E_r = \frac{Y_1 \cos \theta_i - Y_2 \cos \theta_t}{Y_1 \cos \theta_i + Y_2 \cos \theta_t}E_i$.

We can again calculate $R = \frac{|I_r|}{I_{in}} = \frac{E_r^2}{E_i^2} = (\frac{Y_1 \cos \theta_i - Y_2 \cos \theta_t}{Y_1 \cos \theta_i + Y_2 \cos \theta_t})^2$. Similarly, we see that $T = \frac{4Y_1 \cos(\theta_i) \cdot Y_2 \cos(\theta_t)}{(Y_1 \cos \theta_i + Y_2 \cos \theta_t)^2}$. Once again, $I_r + I_t = I_{in}$ and $R + T = 1$.

Now, consider the case of a transverse magnetic field. In this case, we know that $\mathbf{H_{i, r, t}} = H_{i, r, t}\hat{\mathbf{y}}$, and thus $\mathbf{E} = Z \mathbf{H} \times \hat{\mathbf{k}}$, where $Z = \sqrt{\frac{\mu}{\varepsilon}} = Y^{-1}$.

Thus, we can say that

$$\begin{align}
\mathbf{E}_i &= Z_1 H_i \hat{\mathbf{y}} \times \hat{\mathbf{k}}_i &= Z_1 H_i (\cos \theta_i \hat{\mathbf{x}} - \sin \theta_i \hat{\mathbf{z}}) \\
\mathbf{E}_r &= Z_1 H_r \hat{\mathbf{y}} \times \hat{\mathbf{k}}_r &= -Z_1 H_r (\cos \theta_i \hat{\mathbf{x}} + \sin \theta_i \hat{\mathbf{z}}) \\
\mathbf{E}_t &= Z_2 H_t \hat{\mathbf{y}} \times \hat{\mathbf{k}}_t &= Z_2 H_t (\cos \theta_t \hat{\mathbf{x}} - \sin \theta_t \hat{\mathbf{z}}) \\
\end{align}$$

Then, continuity of $\mathbf{H}^\parallel$ implies that $H_i + H_r = H_t$, and continuity of the electric fields implies that $Z_1 (H_i - H_r) \cos \theta_i = Z_2 H_t \cos \theta_t$.

From this, we can solve for $H_r$ and $H_t$ to see that

$$\begin{align}
H_r &= \frac{Z_1 \cos \theta_i - Z_2 \cos \theta_t}{Z_1 \cos \theta_i + Z_2 \cos \theta_t} H_i \\
H_t &= \frac{2Z_1 \cos \theta_i}{Z_1 \cos \theta_i + Z_2 \cos \theta_t} H_t
\end{align}$$

Alongside $E_i = Z_1 H_i$ and $H_t = Z_2 H_t$, we can see that

$$\begin{align}
E_r &= \frac{Z_2 \cos \theta_t - Z_1 \cos \theta_i}{Z_1 \cos \theta_i + Z_2 \cos \theta_t} H_i \\
E_t &= \frac{2Z_2 \cos \theta_i}{Z_1 \cos \theta_i + Z_2 \cos \theta_t} H_t
\end{align}$$

The relative signs of $E_r$ and $H_r$ was chosen to agree with their relationship for normal incidence.

Again, we can define $R$ and $T$ as

$$\begin{align}
R &= (\frac{Z_2 \cos \theta_t - Z_1 \cos \theta_i}{Z_1 \cos \theta_i + Z_2 \cos \theta_t})^2 \\
T &= \frac{4Z_1 Z_2 \cos \theta_i \cos \theta_t}{(Z_1 \cos \theta_i + Z_2 \cos \theta_t)^2}
\end{align}$$

Interestingly, if $Z_2 \cos \theta_t = Z_1 \cos \theta_i$ for a wave with any polarization, the reflection's transverse magnetic component vanishes. If $\mu_1 \approx \mu_2$, we see that this condition becomes $n_1 \cos \theta_t = n_2 \cos \theta_i$, which using Snell's law, becomes

$$\sqrt{1-(\frac{n_1}{n_2})^2 \sin^2 \theta_i} = \frac{n_2}{n_1} \cos \theta_i$$

**Definition**. This is satisfied when $\frac{n_2}{n_1} = \tan \theta_i$. This angle, for which there is no reflected TM wave, is *called Brewster's Angle.*

### Section 10.2.4 - Reflection from Conductors

We know that in a conductor, with current density $\sigma$, we can state that $\mathbf{J}_e = \sigma \mathbf{E}$. This then reintroduces the current term in Maxwell's equation, so that $\nabla \times \mathbf{H} = \sigma \mathbf{E} + \varepsilon \frac{\partial \mathbf{E}}{\partial t}$.

Then, if we curl the curls, we see that

$$\begin{align}
\nabla \times \nabla \times \mathbf{E} &= -\mu \frac{\partial}{\partial t}(\nabla \times \mathbf{H}) &= -\mu \frac{\partial}{\partial t}(\sigma \mathbf{E} + \varepsilon \frac{\partial \mathbf{E}}{\partial t}) \\
\nabla \times \nabla \times \mathbf{H} &= \sigma \nabla \times \mathbf{E} + \varepsilon \frac{\partial}{\partial t}(\nabla \times \mathbf{E}) &= -\mu\sigma \frac{\partial}{\partial t}\mathbf{H} + \varepsilon \frac{\partial}{\partial t}(-\mu \frac{\partial}{\partial t}\mathbf{H}) \\
\end{align}$$

Applying our identity for the curl of a curl and knowing the divergence of the electric and magnetic fields vanishes, we see that

$$\begin{align}
\nabla^2 \mathbf{E} &= -\mu \sigma \frac{\partial \mathbf{E}}{\partial t} - \mu \varepsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} \\
\nabla^2 \mathbf{H} &= -\mu \sigma \frac{\partial \mathbf{H}}{\partial t} - \mu \varepsilon \frac{\partial^2 \mathbf{H}}{\partial t^2} \\
\end{align}$$

We see that if $\sigma = 0$, we recover the equations for propagation in a linear material.

We can solve these equations manually, but that would make us sad. Instead, we assume solutions of the form $\mathbf{E} = E_0 \hat{\mathbf{x}} \cos(kz - \omega t) e^{-\kappa z}$.

Through calculation, we see that

$$\begin{align}
\nabla^2 \mathbf{E} &= -k^2 E_0 \hat{\mathbf{x}} \cos(kz - \omega t) e^{-\kappa z} + 2 k \kappa E_0 \hat{\mathbf{x}} \sin(kz - \omega t) e^{-\kappa z} + \kappa^2 E_0 \hat{\mathbf{x}} \cos(kz - \omega t) e^{-\kappa z} \\
\mu \sigma \frac{\partial \mathbf{E}}{\partial t} &= \mu \sigma \omega E_0 \hat{\mathbf{x}} \sin(kz - \omega t)^{-\kappa z} \\
\mu \sigma \frac{\partial^2 \mathbf{E}}{\partial^2 t} &= -\mu \sigma \omega^2 E_0 \hat{\mathbf{x}} \cos(kz - \omega t)^{-\kappa z}
\end{align}$$

We can substitute this into the wave equation. For the wave equation to hold true at all times, by matching terms of $\sin$ and $\cos$ we see that $-k^2 + \kappa^2 + \mu \varepsilon \omega^2 = 0$ and $\mu \sigma \varepsilon - 2k \kappa = 0$. We can solve the second for $\kappa$ to see that $\kappa = \frac{\mu \sigma \omega}{2k}$. This then allows us to solve the first equation for $k^2$, where we see

$$k^2 = \frac{\mu \varepsilon \omega^2}{2}(1+\sqrt{1+(\frac{\sigma}{\varepsilon \omega})^2})$$

This then lets us solve the first equation (again) for $\kappa^2$, where we see that

$$\kappa^2 = \frac{\mu \varepsilon \omega^2}{2}(\sqrt{1+(\frac{\sigma}{\varepsilon \omega})^2} - 1)$$

Our final equations them become

$$\begin{align}
\kappa = \omega \sqrt{\mu\varepsilon} \sqrt{\frac{\sqrt{1 + (\frac{\sigma}{\varepsilon \mu})^2} + 1}{2}} \\
\kappa = \omega \sqrt{\mu\varepsilon} \sqrt{\frac{\sqrt{1 + (\frac{\sigma}{\varepsilon \mu})^2} - 1}{2}} \\
\end{align}$$

Note that when $\sigma \ll \varepsilon \omega$, the wave number collapses to $k = \frac{\omega}{\nu}$, and we recover propagation in a vacuum. However, when $\sigma \gg \varepsilon \omega$, we see that $k = \kappa = \sqrt{\frac{\mu \omega \sigma}{2}}$. Here, the distance the wave propagates before decreasing by a factor of $\frac{1}{e}$ is known as the skin depth $d$, where $d = \frac{1}{\kappa} = \sqrt{\frac{2}{\mu \omega \sigma}}$. This is significantly less than the wavelength $\lambda = \frac{2\pi}{k}$. Note that in this limit, the electromagnetic wave is heavily damped.

The magnetic field is simpler to solve. We know that $\frac{\partial\mathbf{H}}{\partial t} = -\frac{1}{\mu}\nabla \times \mathbf{E} = \hat{\mathbf{y}} \frac{E_0 e^{-\kappa z}}{\mu}[k \sin(kz - \omega t) + \kappa \cos(kz - \omega t)]$

Integrating, we see that $\mathbf{H} = \hat{\mathbf{y}} = \frac{E_0 e^{-\kappa z}}{\mu \omega}[k \cos(kz - \omega t) - \kappa \sin(kz - \omega t)]$.

We can combine this to see $\mathbf{H} = \hat{\mathbf{y}} e^{-\kappa z} \frac{\sqrt{k^2 + \kappa^2}}{\mu \omega} \cos(kz - \omega t + \phi)$ where $\cos \phi = \frac{k}{\sqrt{k^2 + \kappa ^2}}$ and $\sim \phi = \frac{\kappa}{\sqrt{k^2 + \kappa^2}}$.

#### Reflection of EM waves Incident from an Insulator onto a Conductor

In material $1$ ($z < 0$), we know that

$$\begin{align}
\mathbf{E}_1 &= \hat{\mathbf{x}} E_i \cos (k_1 z - \omega t) + \hat{\mathbf{x}} E_r \cos (-k_1 z - \omega t + \phi_r) \\
\mathbf{H}_1 &= Y_1\hat{\mathbf{y}} E_i \cos (k_1 z - \omega t) - Y_1 \hat{\mathbf{y}} E_r \cos (-k_1 z - \omega t + \phi_r)
\end{align}$$

We know that in material $2$ ($x > 0$),

$$\begin{align}
\mathbf{E}_1 &= \hat{\mathbf{x}} E_t \cos (k_2 z - \omega t + \phi_t) e^{-\kappa z} \\
\mathbf{H}_1 &= \hat{\mathbf{y}} frac{\sqrt{k_2^2 + \kappa^2}}{\mu_2 \omega} \cos (k_2 z - \omega t + \phi + \phi_t) e^{-\kappa z}
\end{align}$$

Here, $\phi$ = $\tan^{-1} (\frac{\kappa}{k_2})$ os a phase shift intrinsic to the conductor.

The continuity of $\mathbf{E}^\parallel$ and $\mathbf{H}^\parallel$ gives us two equations. We can then substitute in $\omega t = 0$:

$$\begin{align}
E_i + E_r \cos \phi_r &= E_t \cos \phi_t \\
E_i - E_r \cos \phi_r &= \frac{\mu_1 v_1 \sqrt{k_2^2 + \kappa^2}}{\mu_2 \omega} E_t \cos(\phi_t + \phi) \\
\end{align}$$

Now, substitute $\omega t = \frac{\pi}{2}$:

$$\begin{align}
E_r \sin \phi_r &= E_t \sin \phi_t \\
-E_r \sin \phi_r &= \frac{\mu_1 v_1 \sqrt{k_2^2 + \kappa^2}}{\mu_2 \omega} E_t \sin(\phi_t + \phi) \\
\end{align}$$

We can then assume $\mu_1 \approx \mu_2$. This modifies the second equations, leaving us with

$$\begin{align}
E_i - E_r \cos \phi_r &= \frac{\sqrt{k_2^2 + \kappa^2}}{k_1} E_t \cos(\phi_t + \phi) \\
-E_r \sin \phi_r &= \frac{\sqrt{k_2^2 + \kappa^2}}{k_1} E_t \sin(\phi_t + \phi) \\
\end{align}$$

Now, apply the sine and cosine additive identities and the definitions for $\sin \phi$ and $\cos \phi$, alongside the definitions of $\sin \phi_t$ and $\cos \phi_t$.

$$\begin{align}
E_i - E_r \cos \phi_r &= E_t(\cos(\phi_t \frac{k_2}{k_1}) - \sin(\phi_t \frac{\kappa}{k_1})) \\
-E_r &= E_t (\sin(\phi_t \frac{k_2}{k_1}) + \cos(\phi_t \frac{\kappa}{k_2}))
\end{align}

Adding these equations lets us see that $\tan(\phi_t) = -\frac{\kappa}{k_1 + k_2}$. Applying the $\sigma \rightarrow 0$, we see $\phi_t \rightarrow 0$. Applying $\sigma \gg \varepsilon \omega$, we see that $\phi_t \rightarrow -\frac{\pi}{4}$.

Adding the first equations, we also wee that

$$E_t = \frac{2k_1 E_i}{\sqrt{(k_1 + k_2)^2 + \kappa^2}}$$

This also has the correct limits.

Furthermore, we can also obtain formulae for $\tan \phi_r = \frac{-2k_1 \kappa}{k_1^2 - k_2^2 - \kappa^2}$, and $E_r = \frac{\sqrt(k_1^2 - k_2^2 - \kappa^2)^2 + (2 k_1 \kappa)^2}{(k_1 + k_2)^2 + \kappa^2} E_i$. These collapse to the reflection at normal incidence values when $\sigma \rightarrow 0$. If $\sigma \gg \varepsilon \mu$, we see that $\kappa \approx k_2 \gg k_1$, as well as $\tan \phi_r \rightarrow 0$ and $\frac{E_r}{E_i} \rightarrow 1$ (complete reflection).

We can also compute energy currents. That is, $I_i = \frac{1}{2} Y_1 E_i^2 = \frac{1}{2} v_1 \varepsilon_1 E_i^2$, and $I_r = \frac{1}{2}v_1 \varepsilon_1 E_r^2$.

The transmitted wave is a bit more complicated. We see $I_t = \langle \mathbf{S}_t \cdot \hat{\mathbf{z}} \rangle = \frac{\sqrt{k_2^2 + \kappa^2}}{k_1} Y_1 E_t^2 \langle \cos(\omega t + \phi_t) \cos(\omega t + \phi_t + \phi) \rangle e^{-2\kappa z} = \frac{1}{2} Y_1 E_t^2 e^{-2\kappa z}$.

## Section 10.3 - Electrodynamic Interactions between Waves and Mattter

### Section 10.3.1 - Response Functions and Fourier Transforms

This section will cover the relations $\mathbf{D} = \varepsilon \mathbf{E}$, $\mathbf{B} = \mu \mathbf{H}$, and $\mathbf{J} = \sigma \mathbf{E}$. However, as the logic is the same for each, I will focus only on the equation for the electric flux density.

We know that the permeability of a material is not a constant, but instead can depend on the electric field at all previous times. We then define a response function $\varepsilon_R(t - t')$ such that

$$\mathbf{D}(t) = \int_{-\infty}^\infty \varepsilon_R(t - t') \mathbf{E}(t') dt'$$

**Definition**. For this to make physical sense, we say that $\varepsilon_R(\tau) = 0$ when $\tau < 0$. That is, the electric flux density is only impacted by the past electric field in the material.

A common response function is $\varepsilon_R(t - t') = \varepsilon \delta(t - t')$.

To make this worse, we know that the fields in a material are frequency-dependent. that is, $\mathbf{D}(\mathbf{r}, t) = \varepsilon_0 \mathbf{E}(\mathbf{r}, t)$ becomes $\mathbf{D}_\omega(\mathbf{r}, t) = \varepsilon(\omega) \mathbf{E}_\omega(\mathbf{r}, t)$.

**Definition**. Given some function $f(t)$, we can say that the *Fourier transform* of $f(t)$, represented by $\tilde{f}(\omega)$, is defined as

$$\tilde{f}(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i \omega t}$$

We then can define the *inverse Fourier transform* such that

$$f(t) = \frac{1}{2\pi} \int_{-\infty}{^\infty} \tilde{f}(\omega) e^{-i \omega t} d\omega$$

We also know that $\delta(x - x') = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{i(x-x')t}dt$. Then, we can write

$$\begin{align}
\mathbf{D}(t) &= \int_{-\infty}^{\infty} \varepsilon_R(t - t') \mathbf{E}(t') dt' \\
&= \int_{-\infty}^{\infty} (\frac{1}{2\pi}\int_{-\infty}^{\infty} \tilde{\varepsilon}(\omega)e^{-i \omega (t-t')} d\omega)(\frac{1}{2\pi}\int_{-\infty}^{\infty} \tilde{\mathbf{E}}(\omega')e^{-i \omega' t} d\omega') dt' \\
&= \int_{-\infty}^{\infty} (\frac{1}{2\pi}\int_{-\infty}^{\infty} \tilde{\varepsilon}(\omega)e^{-i \omega t}e^{i \omega t'} d\omega)(\frac{1}{2\pi}\int_{-\infty}^{\infty} \tilde{\mathbf{E}}(\omega')e^{-i \omega' t} d\omega') dt' \\
\end{align}$$

We know that $\delta(\omega - \omega') = \frac{1}{2\pi} \int_{-\infty}^{\infty}e^{i(\omega - \omega') t'}dt'$, which lets us rewrite $\mathbf{J}$ as

$$\mathbf{D}(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \tilde{\varepsilon}(\omega) \tilde{\mathbf{E}}(\omega) e^{-i \omega t} d\omega$$

**Theorem**. Convolution Theorem. By taking the Fourier transform of both sides, we see that $\tilde{\mathbf{D}} = \tilde{\varepsilon}(\omega) \tilde{\mathbf{E}}(\omega)$.

### Section 10.3.2 - Classical Models for Permittivity and Conductivity

Assuming we are in a material, we know that $\varepsilon = \varepsilon_0 (1 + \chi_e)$. If we move to a response function, we see that

$$\varepsilon_R(t - t') = \epsilon_0 \delta(t - t') + \epsilon_0 \chi_{eR}(t - t')$$

**Definition**. The $\epsilon_0 \chi_{eR}(t-t')$ function is the *susceptibility response function*.

As we are restricted to linear relations to the electric field, we can use the constructive equation for $\mathbf{D}$ to see that

$$\mathbf{D}(t) = \varepsilon_0 \mathbf{E}(t) + \varepsilon_0 \int_{-\infty}^{\infty}\chi_{eR}(t-t') \mathbf{E}(t') dt'$$

This specifically excludes materials in which the flux density depends on higher powers of the electric field. In the limit where the field is time-independent, this reduces to the original constructive equations. This implies that in the static (time-independent) limit,

$$\chi_e = \int_{-\infty}^{\infty} \chi_{eR}(t-t') dt$$

---

Consider an electron bound to its nucleus by a spring-like restoring force. We see that $F_{spring} = -Kx$ for some $K$ (uppercase, in contrast to mechanics), and damped by some force $F_{damping} = -m \gamma \dot{x}$, and driven by  some force $F_{field} = q_e E_0 e^{-i \omega t}$. Then, we see that

$$F = m \ddot{x} = -Kx - m\gamma \dot{x} + q E_{x0}
\exp(-i \omega t)$$

We assume a solution of the form $x(t) = x_0(\omega) \exp(-i \omega t)$, and see that

$$x_0(\omega) = \frac{\frac{q}{m}E_0}{\omega_0^2 - \omega^2 -i\omega\gamma}$$

Then, we can find that there exists a dipole moment $\tilde{p}(t) = qx(t) = \frac{\frac{q^2}{m}E_0}{\omega_0^2 - \omega^2 -i\omega\gamma}$, where the real part of the expression is the physical dipole moment.

If instead of being subject to an oscillatory force from a changing electric field, assume we have a delta function that imparts an impulse at $t=0$. then, we set $x(0) = 0$, and $\dot{x}(0) = \frac{qE\Delta t}{m}$. Our differential equation then becomes $\ddot{x} + \gamma \dot{x} + \omega_0^2 x=0$.

We can assume a solution of the form $x(t) = A e^{-\beta t} \cos(\omega t - \phi)$. Applying initial conditions, we see that $\phi = \frac{\pi}{2}$ and $A  = \frac{qE\delta t}{\omega m}$. Substituting into the differential equation, we see that $\beta = \frac{\gamma}{2}$ and $\omega = \omega_r = \sqrt{\omega_0^2 - (\frac{\gamma}{2})^2}$.

Thus, a harmonic oscillator with resonance frequency $\omega_0$, damping coefficient $\gamma$, and mass $m$, given initial momentum  $q E \delta t$, we will see a damped oscillation $x(t) = \frac{qE\Delta t}{m \omega_r} \exp(-\frac{\gamma}{2}t) \sin(\omega_r t)$, where $\omega_r$ is defined as above.

Now, adjust the initial momentum for the problem to be applied at $t = t_i$ to see that

$$x(t) = \frac{qE\Delta t}{m \omega_r} \exp(-\frac{\gamma}{2}(t-t_i)) \sin(\omega_r (t-t_i))$$

We can then apply a summation for an arbitrary time-dependent electric field.

$$x(t) = \frac{q}{m \omega_r} \sum_i E_i \Delta t_i \exp(-\frac{\gamma}{2}(t-t_i)) \sin(\omega_r (t-t_i))$$

We can then tweak this to find the Green function, which is the solution to

$$(\omega_0^2 + \gamma \frac{d}{dt} + \frac{d^2}{dt^2})G(t-t') = \delta(t-t')$$

The Green function then becomes

$$G(r-r') = \frac{1}{\omega_r}\exp(-\frac{\gamma}{2}(t-t'))\sin(\omega_r(t-t'))\Theta(t-t')$$

Then, for an arbitrary electric field $E_x(t)$, the solution to $(\omega_0^2 + \gamma \frac{d}{dt} + \frac{d^2}{dt^2})x(t) = E_x(t)$ can be writteen as

$$x(t) = \frac{q}{m} \int_{-\infty}^\infty G(t-t')E_x(t')dt'$$

We know that $p(t) = qx(t)$ represents the dipole moment. We can then see that

$$\mathbf{p}(t) = \frac{q^2}{m}\int_{-\infty}^\infty G(t-t')\mathbf{E}(t') dt'$$

We can substitute the inverse Fourier transform for the electric field to see that

$$\mathbf{p}(t) = \frac{q^2}{m} \int_{-\infty}^\infty G(t-t') \frac{1}{2\pi} \int_{-\infty}^\infty \tilde{\mathbf{E}}(\omega) e^{-i\omega t'} d\omega dt'$$

Applying the relation $\int_{-\infty}^{\infty} G(t-t')e^{-i\omega t'} dt' = -e^{i \omega t} \tilde{G}(\omega)$, we see that

$$\mathbf{p}(t) = -\frac{q^2}{m}\frac{1}{2\pi} \int_{-\infty}^{\infty}\tilde{\mathbf{E}}(\omega) \tilde{G}(\omega) e^{-i\omega t}$$

This then implies that $\tilde{\mathbf{p}}(\omega) = -\frac{q^2}{m}\tilde{G}(\omega)\mathbf{\tilde{E}}(\omega)$.

We can calculate that $\tilde{G}(\omega) = \frac{1}{\omega_0^2 - \omega^2 - i \gamma \omega}$. Then, if we have $N$ molecules per unit length, each with $f_i$ electrons with resonant frequency $\omega_i$ and damping parameter $\gamma_i$, we see that

$$\tilde{\mathbf{P}}(\omega) = \frac{Nq^2}{m}(\sum_i \frac{f_i}{\omega_i^2 - \omega^2 - i \omega \gamma_i})\tilde{\mathbf{E}}(\omega)$$

We can use this to then calculate the Fourier transform of the electric flux density, which tells us that

$$\tilde{\varepsilon}(\omega) = \epsilon + \frac{Nq^2}{m}(\sum_i \frac{f_i}{\omega_i^2 - \omega^2 - i \omega \gamma_i})$$

I've skipped the effects on optics, as well as the Drude response function, for brevity.

## Section 10.4 - Guided Waves and Transmission Lines

## Section 10.4.1 - Coaxial Cables

We know that for a coaxial cable with radii $R_1$ and $R_2$, given that the distance between wavelengths $R_2 - R_1$ is significantly less than some arbitrary length $\Delta z$, which is less than some length scale over which the electric field changes $\lambda$, the electric field is defined as $\mathbf{E}(s) = \frac{Q'}{2\pi s \varepsilon} \hat{\mathbf{s}}$. We can then see the voltage between the two insulators is simply

$$\Delta V = V(R_1) - V(R_2) = \int_{R_1}^{R_2} \mathbf{E}(\mathbf{r}) \cdot d\hat{\mathbf{s}} = \frac{Q'}{2\pi\varepsilon} \ln \frac{R_2}{R_1}$$

Then, we know that capacitance is $C = Q / \Delta V$, so capacitance per unit length becomes

$$C' = \frac{Q'}{\delta V} = \frac{2\pi \varepsilon}{\ln(R_2/R_1)}$$

Similarly, we know that the magnetic field is given by Ampere's law as $\mathbf{H} = \frac{I}{2 \pi s}$, as we place the Ampere's loop has radius $s$ around the inner conductor. Then, we see the flux is

$$\Phi = \frac{\Delta z \mu I}{2 \pi s} \int_{R_1}^{R_2} \frac{ds}{s} \ln \frac{R_2}{R_1}$$

This tells us that inductance per unit length, $L' = \Phi / I \Delta Z$ can be given by

$$L' = \frac{\mu}{2\pi}\ln\frac{R_2}{R_1}$$

Now, for some length $\Delta z$, we know that $\Delta Q = Q' \Delta z$, and then by definition,

$$\frac{\partial \Delta Q}{\partial t} = \Delta z \frac{\partial Q'(z, t)}{\partial t} = I(z, t) - I(z + \Delta z, t)$$

That is, the rate at which charge in a cylinder changes is equal to the current entering minus the current leaving. This then implies that

$$\frac{\partial Q'(z, t)}{\partial t} = \frac{I(z, t) - I(z + \Delta z, t)}{\delta z} = -\frac{\partial I(z, t)}{\partial z}$$

Since we know that $Q' = C' V$ (as $C' = Q' / V$), we can take the time derivative to see that

$$\frac{\partial Q'(z,t)}{\partial t} = C' \frac{\partial V(z, t)}{\partial t} = - \frac{\partial I(z,t)}{\partial z}$$

Now, consider a cylindrical loop (a rectangle revolved around the center, excluding the conductor). Faraday's law tells us that $\mathbf{E} \cdot d\mathbf{l} = -\frac{d\Phi}{dt}$, where $\Phi = L' \Delta Z I$ is the flux through the loop. As the electric field is radial and conservative, we know that

$$V(z + \Delta z, t) - V(z, t) = -L' \Delta z \frac{dI(z, t)}{dt}$$

We can take the limit to see that

$$\frac{\partial V(z, t)}{\partial z} = -L' \frac{\partial I(z, t)}{\partial t}$$

This gives is the two telegrapher's equations:

$$\begin{align}
\frac{\partial I(z, t)}{\partial z} &= -C' \frac{\partial V(z, t)}{\partial t} \\
\frac{\partial V(z, t)}{\partial z} &= -L' \frac{\partial I(z, t)}{\partial t}
\end{align}$$

We can then take the derivative of the first with respect to $t$ and the derivative of the second with respect to $z$, we see that

$$\begin{align}
\frac{\partial^2 I(z, t)}{\partial z^2} &= -C' \frac{\partial}{\partial z}(\frac{\partial V(z, t)}{\partial t}) \\
\frac{\partial}{\partial t}(\frac{\partial V(z, t)}{\partial z}) &= -L' \frac{\partial^2 I(z, t)}{\partial t^2}
\end{align}$$

This tells us that

$$\frac{\partial^2 I(z, t)}{\partial z^2} = -C'(-L' \frac{\partial^2 I(z, t)}{\partial t^2}) = C'L' \frac{\partial^2 I(z, t)}{\partial t^2}$$

We can instead take the derivative of the first equation with respect to $z$ and the derivative of the second with respect to $t$ to see that

$$\frac{\partial^2 V(z, t)}{\partial z^2} = L'C' \frac{\partial^2 V{z, t}}{\partial t^2}$$

These are wave equations with velocity $\nu = \frac{1}{\sqrt{L'C'}}$. In the case of light, $\nu = \frac{1}{\sqrt{\mu \epsilon}}$.

We presume solutions of the form $V(z, t) = V_0 \cos(kz - \omega t + \phi_V)$ and $I(z, t) = I_0 \cos(kz - \omega t + \phi_I)$, with a shared velocity. Applying the telegrapher's equations, we see that $\phi_I = \phi_V$ and $\frac{V_0}{I_0} = -\sqrt{\frac{L'}{C'}} = -Z$.

We have a formula for $C'$ and $L'$, so we can write $Z$ as

$$Z = \frac{1}{2\pi}\sqrt{\frac{\mu}{\epsilon}} \ln \frac{R_2}{R_1}$$

Often, modern coaxial cables have $\ln \frac{R_2}{R_1} \approx 1$, and the permittivity of free space is $\sqrt{\frac{\mu_0}{\epsilon_0}} = 377 \Omega$. Then, the impedance of a coaxial cable is often of order $Z \approx \frac{377 \Omega}{2\pi \sqrt{\varepsilon_r}} \approx 60 \Omega$.

**Definition**. The inverse of impedance is called the admittance.

## Section 10.4.2 - Parallel Conductor Transmission Lines

Consider a two-wire transmission line, with distance $d$ between the lines. Then, the electric field between the lines becomes

$$\mathbf{E} = \frac{-Q'}{2\pi \varepsilon_0} \frac{\hat{\mathbf{x}}}{x} + \frac{Q'}{2\pi \varepsilon_0} \frac{-\hat{\mathbf{x}}}{d - x}$$

Then, integrating from $x = a$ to $x = d - a$ (where $a$ is the radius of each conductor), we see that

$$\Delta V = \frac{Q'}{2\pi \varepsilon_0} (\int_a^{d-a} \frac{dx}{x} + \int_a^{d-a} \frac{dx}{d-x}) = \frac{Q'}{\pi \varepsilon_0} \ln(\frac{d}{a}-1)$$

Note that the integrals diverge if $a = 0$. We can then see that

$$C' = \frac{\pi \varepsilon_0}{\ln(\frac{d}{a}-1)}$$

We can also see that the magnetic field is given by

$$\mathbf{H} = \frac{I}{2\pi} \frac{\hat{\mathbf{y}}}{x} + \frac{I}{2\pi} \frac{\hat{\mathbf{y}}}{d-x}$$

This then lets us calculate flux as $\Phi_B = \mu_0 \Delta z \frac{I}{\pi} \ln{(\frac{d}{a} - 1)}$, which means unit inductance becomes

$$L' = \frac{\mu_0}{\pi} \ln(\frac{d}{a} - 1)$$

Again, the continuity equation tells us that $\frac{\partial Q'}{\partial t} = -\frac{\partial I}{\partial z}$, and the capacitance relation lets us derive that

$$\frac{\partial I}{\partial z} = -C' \frac{\partial V}{\partial t }$$

Then, we can use the back EMF to see that

$$\frac{\partial V}{\partial z} = -L' \frac{\partial I}{\partial t}$$

This lets us once again calculate wave equations for $V$ and $I$, with $\nu = c$

## Section 10.4.3 - Transmission Lines with Dissipation

Especially at high frequencies, we see that the dielectric functions become complex leading to a leakage current between insulators. We thus modify our telegrapher's equations to see that

$$\begin{align}
\frac{\partial I}{\partial z} &= -C' \frac{\partial V}{\partial t} - G'V \\
\frac{\partial V}{\partial z} &= -L' \frac{\partial I}{\partial t} - R'I
\end{align}$$

Here, the $R'$ is the resistance per unit length.

The wave equation for voltage then becomes

$$\frac{\partial^2 V}{\partial z^2} = L' C' \frac{\partial^2 V}{\partial t^2} + (L'G' + R'C') \frac{\partial V}{\partial t} + R'G'V'$$

We now assume a solution of the form $V(z, t) = V_0 \cos (kz - \omega t) e^{-\kappa z}$.

Applying the wave equation, we see that for this solution to work, $\kappa^2 - k^2 = -\omega^2 L' C' + R' G'$ and $2 k \kappa = (L' G' + R' C') \omega$.

From this, we can solve for $k$ and $\kappa$ by setting $b = \omega^2 L' C' - R' G'$ and $c = (L' G' + R' C') \omega$ so that $k = \frac{1}{\sqrt{2}} \sqrt{b + \sqrt{b^2 + c^2}}$ and $\kappa = \frac{c}{2k}$.

We can then solve for $\omega = \omega(k)$, which ends up being a very sad equation.

The Heaviside condition is the condition in which we change the parameters so that the parameters $\frac{G'}{C'} = \omega_C$ and $\frac{R'}{L'} = \omega_L$ are equal. Then, we see $\omega^2 = k^2 v_0^2$.
