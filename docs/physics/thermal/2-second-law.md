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

Consider a collection of microscopic systems that can each store any discrete amount of quantized energy. If each system is a harmonic oscillator, we know from [Quantum Mechanics](../../todo.md) that the potential energy is $\frac{1}{2}k_s x^2$, where $k_s$ is the spring constant. Then, the size of energy units is $hf$, where $h$ is Planck's constant ($h = 6.63 \times 10^{-34} \text{J} \cdot \text{s}$) and $f$ is the natural frequency of the oscillator ($f = \frac{1}{2\pi} \sqrt{k_s / m}$).

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

## Section 2.5 - The Ideal Gas

Assume we have a single atom of a monoatomic gas with kinetic energy $U$ in a container of volume $V$. By considering a container with volume $2V$, we can see that $\Omega_1 \propto V \cdot V_p$, where $V$ is the volume of ordinary space, and $V_p$ the  volume of momentum space.

**Definition**. *Momentum space* is the space of all possible momentum values with axis $p_x, p_y, p_z$.

We know that since $KE = U = \frac{1}{2}m(v_x^2 + v_y^2 + v_z^2) = \frac{1}{2} \frac{1}{m} (p_x^2 + p_y^2 + p_z^2)$, we can write $2mU = p_x^2 + p_y^2 + p_z^2$, which describes the surface of a sphere with radius $\sqrt{2mU}$. As such, we can say for a given total momentum $P$, the multiplicity of momentum space is equal to the surface area of the sphere. However, this does not aid us in counting the total number of microstates as area is infinite.

**Definition**. In Quantum Mechanics, the *Heisenberg Uncertainty Principle* states that $(\Delta x)(\Delta p_x) \approx h$. Under this criteria, the number of independent waveforms is thus fixed.

If the number of distinct position states is $L / (\Delta x)$, and number of distinct momentum states is $L_p / (\Delta p_x)$, then we know that the number of distinct sates is $\frac{L}{\Delta x} \frac{L_p}{\Delta x}$, which becomes $\frac{L L_p}{h}$ by the uncertainty principle. Thus, when cubed, we see that $\Omega_1 = \frac{V V_p}{h^3}$.

Note that this is not a rigorous proof, and we have not shown that there are no additional factors for $\Omega_1$, such as a multiplicative factor of $2$ to describe an additional dimension of freedom.

Now, consider a two-molecule system. As we only fix total kinetic energy, the momentum constraint thus becomes $p_{1x}^2 + \ldots + p_{2x}^2 + \ldots = 2mU$, assuming both molecules have the same mass. Then, we can write

$$\Omega_2 = \frac{V^2}{h^6} \times \text{area of momentum 6-dimensional sphere}$$

This only holds true, however, if the two molecules are somehow distinguishable. In reality, molecules are indistinguishable and swapping the two molecules will not yield a distinct state. Thus, we have over-counted by a factor of 2.

If we have $N$ indistinguishable molecules, we see that $\Omega_n = \frac{1}{N!} \frac{V^N}{h^{3N}} \times \text{area of momentum N-dimensional sphere}$. We can define this area as $\frac{2\pi^(N/2)}{(\frac{N}{2} - 1)!} r^(N-1)$, where $r$ is $\sqrt{2mU}$. This derivation is left as a textbook appendix. Thus, we see that

$$\Omega_N = \frac{1}{N!} \frac{V^N}{h^{3N}} \frac{2\pi^{\frac{3N}{2}}}{(\frac{3N}{2} - 1)!} (\sqrt{2mU})^{3N-1} \approx \frac{1}{N!} \frac{V^N}{h^{3N}} \frac{2\pi^{\frac{3N}{2}}}{(\frac{3N}{2})!} (\sqrt{2mU})^{3N}$$

We can write this as $\Omega(U, V, N) = f(N) V^N U^{\frac{3N}{2}}$ where $f(N)$ is some function of $N$.

Now, suppose we have two ideal gasses separated by a partition that allows energy (but not mass) transfer. Then, $\Omega = \Omega_1 \Omega_2$. If $N_1 = N_2 = N$, then $\Omega = (f(N))^2 (V_A V_B)^N (U_A U_B)^{3N/2}$. Following the last section, we see that the width of the peak of the probability distribution is $\frac{U_{total}}{\sqrt{\frac{3N}{2}}}$.

If the partition is thus moveable (where one gas expands and the other compresses), allows energy exchange, and disallows mass transfer, we see that the width of the peak in distribution is $\frac{V_{total}}{\sqrt{N}}$.

If we allow mass transfer, we see that while the analysis becomes difficult, we would expect a sharp peak, and that $\Omega$ is $\Omega(N_A, U_A)$.

## Section 2.6 - Entropy

We can rewrite the second law of thermodynamics as, given a system, the multiplicity of the current state tends to increase.

**Definition**. We define *Entropy* as $S \cong k \ln \Omega$, where $k$ is included due to historical reasons. This takes the very large number into an ordinary large number. While $\Omega$ is unitless, due to the factor of $k$, we see that $S$ has units of energy over temperature, or $J/K$ in the SI system.

Recall that in an Einstein solid with $N$ oscillators and $q$ energy units, we see that $\Omega = \binom{q + N - 1}{q}$. If we introduce the constraint $q \gg N$ and apply Stirling's approximation, we see that $\Omega \approx (eq/N)^N$, so that

$$S = k \ln \Omega = Nk(\ln \frac{q}{N} + 1)$$

Note that in this case, increasing either $q$ or $N$ increases the entropy of an Einstein solid.

A convenient property of entropy is that the composite entropy of a total system is additive. That is,

$$S = k \ln \Omega = k \ln(\Omega_A \Omega_B) = k \ln \Omega_A + k \ln \Omega_B = S_A + S_B$$

We can thus use this to rewrite the second law.

**Theorem**. The Second Law of Thermodynamics. Any large system in equilibrium will be found in the macrostate with the greatest entropy (with some small, unmeasurable fluctuations).

### Entropy of an Ideal Gas

We know that, for an ideal gas,

$$\Omega \approx \frac{1}{N!} \frac{V^N}{h^{3N}} \frac{2\pi^{\frac{3N}{2}}}{(\frac{3N}{2})!} (\sqrt{2mU})^{3N}$$

This is horrible, and nobody likes it. If we then apply Stirling's approximation and then discard some factors, we can see that

$$S = Nk [ \ln(\frac{V}{N}(\frac{4\pi m U}{3Nh^2})^{3/2}) + \frac{5}{2}]$$

This is known as the *Sackur-Tetrode Equation*.

A notable consequence of this is that if $N$ and $U$ are held fixed, $\Delta S = Nk \ln \frac{V_f}{V_i}$. This applies, for example, to quasistatic isothermal expansion work, in which heat is added to maintain constant pressure while undergoing expansion.

**Definition**. *Free expansion* of a gas is a gas expanding from a container into a vacuum. Note that as nothing external to the system is being moved, $W=0$, and as no heat is flowing, $Q=0$, so $\Delta U = Q + W = 0$.

**Definition**. Now, consider two gasses in containers of equal volume, in which $U_1 = U_2$ and $N_1 = N_2$. The, if $V_1 = V_2$, when the containers are combined, $\Delta S = Nk \ln 2$ for gas $A$ and gas $B$, so $\Delta S_{total} = \Delta S_A + \Delta S_B = 2 Nk \ln 2$. This is known as the *entropy of mixing*. Note that this only applies if the gasses are distinguishable, as otherwise $\Delta S = 0$.

Note that for distinguishable molecules, the $\Omega$ term lacks a factor of $1 / N!$, so then $S = Nk[\ln(V(\frac{4\pi m U}{3Nh^2})^{3/2}) + \frac{3}{2}]$. For this formula, dividing volume (and thus energy and number of molecules) by two results in the total entropy being larger than the sum of the partitions by a large factor. That is, by inserting a partition, the second law of thermodynamics can be violated. This is known as *Gibbs Paradox*.

### Reversible and Irreversible Processes

**Definition**. A process is said to be *irreversible* if it creates new entropy, as to reverse it would be to violate the second law of thermodynamics. Processes that do not generate new entropy (or only generate a negligible amount) are said to be *reversible*.

Notably, any reversible expansion is quasistatic, in which $W = -P \Delta V$. Note that a quasistatic process is only reversible if $Q = 0$.
