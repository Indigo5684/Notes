# Chapter 14 - Collision Theory

## Section 14.1  - The Scattering Angle and Impact Parameter

**Definition**. The angle between incoming and outgoing velocities is the *scattering angle* $\theta$. Note that $\theta = 0$ corresponds to no scattering and $\theta = \pi$ is a maximal value for $\theta$.

**Definition**. The impact parameter $b$ is the perpendicular distance from the projectile's incoming path to a parallel axis through the center of the target. $b = 0$ implies a head-on collision. Note that $\theta = \theta(b)$.

## Section 14.2 - The Collision Cross Section

**Definition**. Consider multiple targets. Then, the *target density* $n_{tar}$ is the number of targets per unit area as viewed from the incident direction.

If $A$ is the total area of the target assembly, the total number of targets becomes $n_{tar}A$.

**Definition**. The *cross sectional area* or *cross-section* is defined as $\sigma = \pi R^2$, where $R$ is the radius of one target as seen from the front.

Now, the total area of all targets is $n_{tar}A\sigma$. Then, we can see the probability of a hit is simply the area of all targets divided by area, or  $n_{tar} \sigma$. Naturally, if we send a test beam with $N_{inc}$ particles, we expect some fraction $N_{sc}$ to be scattered. Then,

$$N_{sc} = N_{inc} n_{tar} \sigma$$

If we then let $R_{inc} = N_{inc} / \Delta t$ for some time $\Delta t$, we find the rate of incoming particles per unit time. We can do the same to $N_{sc}$ to see that

$$R_{sc} = R_{inc} n_{tar} \sigma$$

**Definition**. Typical nuclear dimensions are about $10^{-14} \text{m}$, so the cross-sections are measured in units of $10^{-28} \text{m}^2$. This unit is known as $1 \text{barn}$.

## Section 14.3 - Generalizations of the Cross Section

Consider an incident sphere with radius $R_1$ and a target sphere of radius $R_2$. Then, we only care for $b \leq R_1 + R_2$. We know that $A = \pi(R_1 + R_2)^2$. Then, $\sigma = A = \pi(R_1 + R_2)^2$ (as any interaction in the area results in a collision). So, $N_{sc} = N_{inc} n_{tar} \sigma$

Now, consider an example in which the particle may be captured or absorbed as well. Then, we can repeat the previous logic to see that $N_{cap} = N_{inc} n_{tar} \sigma$. If a target can both deflect and capture particles, we see both $N_{cap}$ and $N_{sc}$, where $\sigma_{cap} + \sigma_{sc} = \sigma_{tot}$.

**Definition**. $\sigma_{cap}$ and $\sigma_{sc}$ are the *capture cross section* and *scattering cross section* respectively. Additionally, we can define the *ionization cross section* $\sigma_{ion}$ as the effective area of the target atom for an ionizing electron, and the *fission cross section* $\sigma_{ris}$ as the effective area of a $U^235$ nucleus for fission by neutron bombardment.

**Definition**. A collision is said to be *elastic* if the internal motion of the target is left unchanged. Otherwise, the collision is *elastic*.

**Definition**. The *ground state* of an atom is its lowest possible energy level. If an incident electron scatters elastically, it will leave the target in its ground state. Otherwise, *atomic excitation* will be seen.

Note that we can differentiate the types of collisions as $\sigma_{sc} = \sigma_{el} + \sigma_{inel}$. Then, the total cross section $\sigma_{tot} = \sigma_{sc} + \sigma_{cap} + \sigma_{ion}$, which is the total cross section for any interaction with the target particle.

## Section 14.4 - The Differential Scattering Cross Section

**Definition**. For a cylinder on a circle with radius $r$, with an arc length of $s$, we define the angle $\delta \theta = s/r$, which comes from the definition of radians.

**Definition**. For a cone on a sphere with radius $r$ and area $A$, we define the solid angle $\delta \Omega = A / r^2$, with units called *steradians* (abbreviated as sr), and ranges from $0$ to $4\pi$ (due to the maximum surface area of a sphere). Note this works for any shape of cone (eg. cones with non-rectangular bases).

We will work in modified spherical polar coordinates, with the target on the origin and $z = \rho$. For a cone in the range $\theta$ to $\theta + d\theta$ and $\phi$ to $\phi + d\phi$, that is, cones with a rectangular base, we see that based on $A = r^2 \sin \theta d\theta + d\phi$,

$$d\Omega = \sin \theta d\theta d\phi$$

We now define

$$N_{sc} (\text{into } d\Omega) = N_{inc} n_{tar} d\sigma (\text{into } d\Omega)$$

**Definition**. Here, $d\simga = \frac{d\sigma}{d\Omega} d\Omega$, where we define the *differential scattering cross section* as $d\sigma / d\Omega$. This lets us say

$$N_{sc} (\text{into } d\Omega) = N_{inc} n_{tar} \frac{d\sigma}{d\Omega} d\Omega$$

We then see that

$$\omega = \int \frac{d\sigma}{d\Omega}(\theta, \phi) d\Omega = \int_0^\pi \sin \theta \int_0^{2\pi} \frac{d\sigma}{d\Omega}(\theta, \phi) d\phi d\theta$$

## Section 14.5 - Calculating the Differential Cross Section

Consider the case of axial symmetry, that is, the differential cross section is independent of $\phi$. Then, we  can see that for $\theta = \theta(b)$, we can consider particles approaching in the range $b$ to $b + db$. The annulus created by  this has a cross-sectional area of $d\sigma = 2\pi b db$.

We then see that the particles emerge between angles $\theta$ and $\theta + d\theta$ with solid angle $d\Omega = 2\pi \sin \theta d\theta$

We can thus compute the differential cross section as

$$\frac{d\sigma}{d\Omega} = \frac{b}{\sin \theta} |\frac{db}{d\theta}|$$

## Section 14.6 - Rutherford Scattering

Consider scattering electrons of off nuclei. Then, we know that

$$F = \frac{kqQ}{r^2} = \frac{\gamma}{r^2}$$

The rest of this section is complicated.

## Section 14.7 - Cross Sections in Various Frames

Skipped

## Section 14.8 - Relation of the CM and Lab Scattering Angles

Skipped
