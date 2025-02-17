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
