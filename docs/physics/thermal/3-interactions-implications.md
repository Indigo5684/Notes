# Chapter 3 - Interactions and Implications

## Section 3.1 - Temperature

Consider two Einstein solids, $A$ and $B$, that are weakly coupled (that is, they can exchange energy, but the total amount of energy is fixed). If $N_A = 300$ and $N_B = 200$, with a total energy of $q = 100$, we can compute the multiplicity of each macrostate as well as its entropy. By calculation, we can see that the most likely macrostate is when $q_A = 60$. From the graph of $q_A$ vs $\Omega$, we see the expected spike. Then, by the definition of the maximum, we see that

$$\frac{\partial S_{total}}{\partial q_A} = 0\; \text{ and } \; \frac{\partial S_{total}}{\partial U_A} = 0$$

Note that the second equation is derived from the first, as $U_A$ is simply $q_A$ times a constant (as $q_A$ is the number of energy quanta), and $S = k \ln \Omega$. Furthermore, from $S_{total} = S_A + S_B$, we can differentiate with respect to $U_A$ to see that

$$\frac{\partial S_{total}}{\partial U_A} = \frac{\partial S_A}{\partial U_A} + \frac{\partial S_B}{\partial U_A} = 0$$

Here, we note that for the second term, $dU_A = -dU_B$. From this, we can see that at equilibrium,

$$\frac{\partial S_A}{\partial U_A} = \frac{\partial S_B}{\partial U_B}$$

Note that due Boltzmann's constant, these terms will have units of $1/\text{K}$.

**Definition**. The *temperature* of a system is defined as $T = (\frac{\partial S}{\partial U})^{-1}$, with the volume and number of particles held fixed. That is,

$$\frac{1}{T} = (\frac{\partial S}{\partial U})_{N,V}$$

For a practical example, consider an Einstein solid in which $q \gg N$. Here, we say that $U = q\epsilon$. Then, we know that

$$S = Nk[\ln(\frac{q}{N}) + 1] = Nk \ln U - Nk\ln(\frac{UN}{q}) + Nk = Nk \ln U - Nk \ln (\epsilon N) + Nk$$

Then, we can see that $T = (\frac{Nk}{U})^{-1}$, so then $U = NkT$, which given that $f = 2$ for an Einstein solid, allows us to recover the Equipartition theorem.

Now, consider a monatomic ideal gas. Then, $S = Nk \ln V + Nk \ln U^\frac{3}{2} + f(N)$. Then, $T = (\frac{\frac{3}{2}Nk}{U})^{-1}$, so $U = \frac{3}{2}NkT$.

## Section 3.2 - Entropy and Heat

If we differentiate $U(T)$ with respect to $T$ given a constant particle count and volume, by definition we obtain the heat capacity at constant volume. That is,

$$C_V = (\frac{\partial U}{\partial T})_{N, V}$$

For an Einstein solid with $q \gg N$, we see that $C_V = \frac{\partial}{\partial T}(NkT) = Nk$, and for a monatomic ideal gas, $C_V = \frac{\partial}{\partial T}(\frac{3}{2}NkT) = \frac{3}{2} Nk$.

Note that obtaining $C_V$ from this is difficult, and nobody wants to do it.

Even if entropy cannot be written mathematically due to the complexity of a system, it can still be measured. For a given system if a small amount of heat $Q$ is added while holding volume constant and applying no work, we see that $\frac{Q}{T} = \frac{dU}{T} = dS$. This is taken from the definition of temperature as given previously.

If the temperature remains constant while heat is added (such as during a phase change), then the previous equation can be applied when $Q$ and $dS$ are not infinitesimal, so that $dS = \frac{C_V dT}{T}$. From this, if we allow temperature to vary, we see that

$$\Delta S = S_f - S_i = \int_{T_i}^{T_f} \frac{C_V}{T} dT$$

Note that often, $C_V$ is constant over the temperature range of interest and can be taken out of the integral. For certain materials, especially at low temperatures, this may not hold true. Additionally, if we know $C_V$ all the way to absolute zero, we can find the total entropy. That is, $S = S_f - S(0) = S_f$, as theoretically, $S(0) = 0$.

**Theorem**. The Third Law of Thermodynamics. At zero temperature, a system should settle into its unique lowest-energy state. That is, $\Omega = 1$ and $S = 0$.

However, in many materials, $S(0) \neq 0$. This is often due to the fact that orientations of molecules may be changed with very little effect on overall energy.

**Definition**. *Residual entropy*, is the entropy at absolute zero. For compounds with multiple arrangements, it is equal to $k$ times the logarithm times the number of possible molecular arrangements. For compounds with multiple isotopes, at $T = 0$, the isotopes are often distributed randomly across lattice sites as the material is a solid (and thus the isotopes cannot flow between lattice sites). Additionally, some materials gain multiplicity due to the alignment of nuclear spins (and while these do align themselves eventually, most labs are not capable of getting that close to absolute zero).

Note that by convention, tabulated entropies include residual entropy due to molecular orientations but neglect mixing or spin entropy.

Note that to force the integral to converge at absolute zero, we force $\lim_{T \rightarrow 0} C_V = 0$.

Historically, $dS = Q/T$ was the original definition of entropy. This tells us nothing about what entropy is, but is sufficient enough for use in most purposes.

## Section 3.3 - Paramagnetism

Consider a two-state paramagnet, with $N$ spin-$1/2$ particles, in a constant magnetic field $\mathbf{B} = B\hat{\mathbf{z}}$. Then, with each particle acting as a dipole, and neglecting dipole-dipole interactions, we consider the two potential spin values, labeled here as up and down. Then, we can say the energy of any dipole is $\pm \mu B$ for the material's value of $\mu$. If we let a dipole oriented with the field have a negative energy, we can then write the total energy as

$$U = \mu B(N_\darr - N_\uparrow) = U = \mu B((N - N_\uparrow) - N_\uparrow) = \mu B(N - 2N_\uparrow)$$

This holds true as $N = N_\uparrow + N_\darr$. Additionally, this energy can be negative. In this material, we know there is no internal magnetic field, so $B = \mu(H + M)$ (we are not working with the symmetric case) simplifies so that

$$M = \mu(N_\uparrow - N_\darr) = -U/B$$

Now, we can also consider the multiplicity of the system $\Omega$ as $\Omega(N_\uparrow) = \binom{N}{N_\uparrow}$.

A notable consequence of this is if we plot $x = U$ vs $y = S$, the temperature is the reciprocal of the slope (as $1/T = \partial S / \partial U$). We can then normalize this by writing $x = U / \mu B$ (as $B$ is a constant external field) and $y = S / k$. The resulting graph will appear to be a semicircle. Notably, we can find negative temperatures when more than half the dipoles point up.

Analytically, Stirling's approximation tells us that

$$S = k[N \ln N - N_\uparrow \ln N_\uparrow - (N - N_\uparrow) \ln(N - N_\uparrow)]$$

We then see that

$$\frac{1}{T} = (\frac{\partial S}{\partial U})_{N, V} = \frac{\partial N_\uparrow}{\partial U} \frac{\partial S}{\partial N_\uparrow} = -\frac{1}{2\mu B} k \ln(\frac{N - U/\mu B}{N + U / \mu B})$$

We can then solve to see that

$$U = N \mu B \frac{1 - \exp(2 \mu B / kT)}{1 + \exp(2 \mu B / kT)} = -N \mu B \tanh(\frac{\mu B}{kT})$$

Then, we see that $M = N \mu \tanh(\frac{\mu B}{kT})$. Knowing that the heat capacity $C_B$ can be written as $C_B =  (\frac{\partial U}{\partial T})_{N, B}$, we see that

$$C_B = Nk \frac{(\mu B / kT)^2}{\cosh(\mu B / kT)}$$

Note that for an electronic two-state paramagnet, the value of $\mu$ is the Bohr magneton, where $\mu_B = \frac{eh}{4\pi m_e}$. As $x = \mu B / kT \ll 1$ in most cases, we can write $\tanh x \approx x$, so that $M \approx \frac{N \mu^2 B}{kT}$. The fact that $M \propto 1/T$ is known as *Curie's Law*, and holds in the high temperature limit for all paramagnets.

## Section 3.4 - Mechanical Equilibrium and Pressure

Consider two systems separated by a movable partition, in which energy and volume may be exchanged, but the total energy and volume is fixed. Then, at equilibrium, we see that $\frac{\partial S}{\partial U_A} = 0 = \frac{\partial S}{\partial V_A}$. Then, we know that $S = S_A + S_B$, so

$$0 = \frac{\partial S}{\partial V_A} = \frac{\partial S_A}{\partial V_A} + \frac{\partial S_B}{\partial V_A} = \frac{\partial S_A}{\partial V_A} - \frac{\partial S_B}{\partial V_B} \Rightarrow \frac{\partial S_A}{\partial V_A} = \frac{\partial S_B}{\partial V_B}$$

We can state this as $V = V_A + V_B$ being fixed forces $0 = \partial V_A + \partial V_B$ so then $\partial V_B = -\partial V_A$. Then, at equilibrium, $T(\partial S / \partial V)$ is the same for both systems. We then define pressure as $P = T (\frac{\partial S}{\partial V})_{U, N}$. For an ideal gas, with $\Omega = f(N) V^N U^{3N/2}$, we see that $P = \frac{NkT}{V}$ under this definition, which agrees with the ideal gas law.

Now, consider a two-step process. In the first step, energy is changed by $\Delta U$ while volume is fixed. Then, in step two, volume is changed by $\Delta V$ while energy is fixed. Then, $\Delta S = \Delta S_1 + \Delta S_2$. We can write this as $\Delta S = (\frac{\Delta S}{\Delta U})_V \Delta U + (\frac{\Delta S}{\Delta V})_U \Delta V$. As we take the limit, we see that

$$dS = (\frac{\partial S}{\partial U})_V dU + (\frac{\partial S}{\partial V})_U dV = \frac{1}{T} dU + \frac{P}{T} dV$$

**Theorem**. This gives us the *thermodynamic identity*, in which $dU = T dS - P dV$, which is true in any system.

We can then recall that $dU = Q + W$. Then if $W = -P dV$, we can say $Q = T dS$. However, this is only true if this is a quasistatic process, no other work is done, and many variables are held constant. Additionally, in a quasistatic process that is also adiabatic ($Q = 0$), we call the process *isentropic*. Then, $\Delta S = \frac{Q}{T}$.

For constant pressure processes, we can then write $(\Delta S)_P$ = \int_{T_i}^{T_f}\frac{C_P}{T} dT$.

Note that in non-quasistatic processes, $dS > \frac{Q}{T}$, as $W > -P dV$.

## Section 3.5 - Diffusive Equilibrium and Chemical Potential

Now consider two systems, $A$ and $B$, that can also exchange particles. Then, we see that $\partial S_A / \partial N_A = \partial S_B / \partial N_B$ at equilibrium. Then,

$$ -T \frac{\partial S_A}{\partial N_A} = -T \frac{\partial S_B}{\partial N_B}$$

We then define a chemical potential $\mu$ as

$$\mu = -T (\frac{\partial S}{\partial N})_{U, V}$$

Then, we can say that $\mu_A = \mu_B$ at equilibrium. Otherwise, the system with the lesser chemical potential will tend to gain particles, as it will gain more entropy than the other loses. This makes intuitive sense, as the system with more energy tends to have more particles.

Then, we know that

$$dS = (\frac{\partial S}{\partial U})_{N, V} dU + (\frac{\partial S}{\partial V})_{N, U} dV + (\frac{\partial S}{\partial N})_{U, V} dN$$

We can then say that $dS = \frac{1}{T} dU + \frac{P}{T} dV - \frac{\mu}{T} dN$, so that $dU = T dS - P dV + \mu dN$. Then, we tend to associate $\mu dN$ with chemical work.

Then, if we fix $U$ and $V$, the system only has chemical work, so that $0 = T dS + \mu dN$, which implies $\mu = -T (\frac{\partial S}{\partial N})_{U, V}$. Then, if we instead fix $S$ and $V$, we see that $dU = \mu dN$, which implies that $\mu = (\frac{\partial U}{\partial N})_{S, V}$. This tells us that $\mu$ has units of energy.

## Section 3.6 - Summary, A Look Ahead

**Definition**. In Classic Thermodynamics, we see that $dU = T dS - P dV + \mu dN$, where $\frac{1}{T} = (\frac{\partial S}{\partial U})_{V, N}$, $\frac{P}{T} = (\frac{\partial S}{\partial V})_{U, N}$, and $-\frac{\mu}{T} = \frac{\partial S}{\partial N}_{U, V}$.

Additionally, we can find info for systems such as paramagnets using statistical mechanics.
