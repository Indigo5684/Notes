# Chapter 2 - The Second Law

## Section 2.1 - Two-State Systems

**Definition**. Given a system defined by a test statistic $XS$ and positive integer $N$, an ordered tuple with length $N$ and elements in the range of $X$ is known as a *microstate*. An unordered tuple with the same length $N$ and elements in the range of $X$ is known as a *macrostate*.

**Definition**. The *multiplicity* of a macrostate is the number of possible microstates that, when when written as an unordered tuple, produce said macrostate. In this work, we will define $\Omega(Macrostate) = Multiplicity$.

Note that if the test statistic $X$ is a uniform and discrete test statistic, the probability of generating a given macrostate $m$ can be written as $P(m) = \frac{\Omega(M)}{\sum_M \Omega M}$.

**Recall**. From Statistics, $C(n, k) = \binom{n}{k}$, or *$n$ choose $k$*, is the number of unordered pairs of length $k$ that can be generated from a list of $n$ distinct elements.

**Definition**. A *paramagnet* is a material whose molecular magnetic moments do not align unless in the presence of an external magnetic field.

**Definition**. A *ferromagnet* is a material whose molecular magnetic moments will be aligned in the presence of an external magnetic field and retain their alignment in its absence.

**Definition**. The individual magnetic particles in a material are referred to as *dipoles*, as each contains a unique magnetic vector.

**Definition**. In a *two-state paramagnet*, when exposed to a magnetic field, each dipole may only be parallel or antiparallel to the applied field. We denote $N = N_\uparrow + N_\downarrow$ to represent the number of dipoles pointing up or down.

Assuming the external magnetic field points up, we note that an up-dipole contains less energy than a down-dipole. The total energy of a system is determined by $N_\uparrow$ and $N_\downarrow$, so the macrostate of this system can be used to determine the total energy.

## Section 2.2 - The Einstein Model of a Solid

Consider a collection of microscopic systems that can each store any discrete amount of quantized energy. If each system is a harmonic oscillator, we know from [Quantum Mechanics](../../todo.md) that the potential energy is $\frac{1}{2}k_s x^2$, where $k_s$ is the spring constant. Then, the size of energy units is $hf$, where $h$ is Planck's constant ($h = 6.63 \times 10^{-34} \text{J} \vdot \text{s}$) and $f$ is the natural frequency of the oscillator ($f = \frac{1}{2\pi} \sqrt{k_s / m}$).

**Definition**. For a three-dimensional solid, each particle can oscillate in three dimensions. Thus, if there are $N$ oscillators, there are $N/3$ particles. A solid modeled as such is known as an *Einstein solid*.

Consider a system in which $N = 3$. Then, $\Omega(0) = 1$, $\Omega(1) = 3$, $\Omega(2) = 6$, $\Omega(3) = 10$, and so on. We can extend this to see that for an Einstein solid with $N$ oscillators, the multiplicity of the total energy $q$ is

$$\Omega(N, q) = \binom{q+N-1}{q} = \frac{(q+N-1)!}{q!(N-1)!}$$

## Section 2.3 - Interacting Systems

Consider a system containing two solids, $A$ and $B$, that can share energy back and forth.

**Definition**. Two solids are *weakly coupled* when the rate of energy transfer between the two solids is substantially less than the rate of energy transfer within the solids. That is, the total energy of each solid $U_A$ and $U_B$ only change slowly. Note that $U = U_A + U_B$ is fixed.

Consider a small system, in which $N_A = N_B = 3$, with a total energy of $q_{total} = q_A + q_B = 6$ (Note that the actual value of energy is $U = qhf$). There are seven possible macrostates of the system, each defined by $q_A \in {0, 1, \ldots, 6}$ (as $q_B = 6 - q_A$). We can find the multiplicity of the overall macrostate by multiplying the multiplicity of $q_A$ in solid $A$ with the multiplicity of $q_B$ in solid $B$.

**Theorem**. The *fundamental assumption of statistical mechanics* states that in an isolated system in thermal equilibrium, all microstates are equally probably. Note that this does not imply that macrostates are equally probably.

**Theorem**. The *second law of thermodynamics* states that the spontaneous flow of energy stops when a system is at the macrostate with the greatest multiplicity.

## Section 2.4 - Large Systems

**Definition**. When dealing with *large and small numbers*, it is important to note that a small number may be added to a large number without significantly changing it.

We can also define *very large numbers*, of which large or small numbers may be added or multiplied by each other and remain unchanged.

**Theorem**. Stirling's Approximation. For some large $N \in \mathbb{N}$, we can estimate $N! \approx N^N e^{-N} \sqrt{2\pi N}$. This comes from $N! \approx N^N$, with the additional correction terms $e^{-N}$ and $\sqrt{2\pi N}$. If we care about $\ln(N!)$, we can omit the last term to see $\ln (N!) \approx N \ln N - N$.

We can use this to simplify $\Omega(N, q) = \binom{q + N - 1}{q} = \frac{(q + N - 1)!}{q!(N-1)!} \approx \frac{(q+N)!}{q!N!}$. Take the logarithm to see that $\ln \Omega = \ln(\frac{(q+N)!}{q!N!}) = \ln((q+N)!) - \ln(q!) - \ln(N!)$. We can now apply the simplification to see that $\Omega \approx (q + N)\ln(q+N) - (q - N) - q\ln q + q - N \ln N + N = (q+N)\ln(q+N) - q\ln q - N\ln N$.

We can factor $\ln (q+N)$ to see that $\ln(q+N) = \ln q + \ln(1 + \frac{N}{q})$, and if $N \gg q$, we can use the Taylor series of $\ln(x)$ at $x_0 = 1$ to see that $\ln(q+N) \approx \ln q + \frac{N}{q}$ Thus, $\ln \Omega \approx N \frac{q}{N} + N + \frac{N^2}{q}$.

Note that $N^2/q$ becomes negligible. This, we can exponentiate to see that $\Omega \approx e^{N\ln(q/N)}e^N = (\frac{eq}{N})^N$.

Now, for a system of two large Einstein solids, we wish to know the width of the peak in the multiplicity function. We know that with $q = q_{total} = q_A + q_B$,

$$\Omega = \Omega(q_A) \Omega(q_B) = (\frac{eq_A}{N})^N (\frac{eq_B}{N})^N = (\frac{e}{N})^{2N}(q_A q_B)^N$$

The highest peak will be at $q = 2 q_A$, where $\Omega_max = (\frac{e}{N})^{2N} (\frac{q}{2})^{2N}$. If we instead let $q_A = \frac{q}{2} + x$ and $q_B = \frac{q}{2} - x$, we will see that $\Omega = (\frac{e}{N})^{2N}((\frac{q}{2})^2 - x^2)^N$. By taking the logarithm of the second factor and then applying simplifications, we can reduce this to $\Omega = \Omega_{max} e{-N (2x/q)^2}$. This function should be familiar, as it is a *Gaussian*.

Note that the multiplicity falls to $1/e$ of its maximum value when $N(\frac{2x}{q})^2 = 1$, or when $x = \frac{q}{2\sqrt{N}}$. This means that the approximate width of the peak is $q/\sqrt{N}$

**Definition**. The *thermodynamic limit* is when a system becomes infinitely large, so that measurable fluctuations away from the most likely microstate never occur.
