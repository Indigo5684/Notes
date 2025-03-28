# Chapter 6 - Boltzmann Statistics

## Section 6.1 - The Boltzmann Factor

Consider some system coupled to a reservoir. Then, we can associate each microstate of the system with some energy level $E$.

**Definition**. We say an energy level is *degenerate* if it corresponds to more than one microstate.

Now, consider two microstates $s_1$ and $s_2$, with energies $E(s_1)$ and $E(s_2)$ and probabilities $\mathcal{P}(s_1)$ and $\mathcal{P}(s_2)$ respectively. While in an isolated system, the fundamental assumption of statistical mechanics tells us that each microstate is equally probable, this is not the case in a closed or open system.

We can now consider the reservoir when the system is in state $s_1$. There are multiple microstates the reservoir can be in under these constrains, so let us define $\Omega_R(s_1)$ as the multiplicity of the macrostate of the reservoir while the system is in state $s_1$.

This then lets us derive the relation

$$\frac{\mathcal{P}(s_2)}{\mathcal{P}(s_1)} = \frac{\Omega_R(s_2)}{\Omega_R(s_1)}$$

We can then see that as $S = k ln \Omega$, we can write $\Omega_R = \exp(S_R/k)$, allowing us to write

$$\frac{\mathcal{P}(s_2)}{\mathcal{P}(s_1)} = \frac{\exp(S_R(s_2)/k)}{\exp(S_R(s_1)/k)} = \exp((S_R(s_2) - S_R(s_1))/k)$$

If the system is small compared to the reservoir, such as if the system is an atom, we can write $S_R(s_2) - S_R(s_1) = dS_R$, and invoke the thermodynamic identity. We further can assume that $P dV_R$, while nonzero, is negligible compared to $dU_R$. Additionally, we assume $dN = 0$ for closed systems. Thus,

$$S_R(s_2) - S_R(s_1) = \frac{1}{T}(U_R(s_2) - U_R(s_1)) = -\frac{1}{T}(E(s_2) - E(s_1))$$

We can substitute this into the ratio of probabilities to see that

$$\frac{\mathcal{P}(s_2)}{\mathcal{P}(s_1)} = \frac{\exp(-E(s_2)/kT)}{\exp(-E(s_1)/kT)}$$

We can rearrange this.

$$\frac{\mathcal{P}(s_2)}{\exp(-E(s_2)/kT)} = \frac{\mathcal{P}(s_1)}{\exp(-E(s_1)/kT)}$$

However, for this to be true for all states, the expression must equal a constant, which we denote as $1/Z$. Thus,

$$\mathcal{P}(s) = \frac{1}{Z}e^{-E(s)/kT}$$

**Definition**. Here, $Z$ is the *partition function*. This is a constant that only depends on temperature, and equals the sum of all unweighted probabilities.
