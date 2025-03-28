# Chapter 5 - Free Energy and Chemical Thermodynamics

## Section 5.1 - Free Energy as Availible Work

**Definition**. *Enthalpy* $H$ is the energy of a system plus the energy needed to make room for it, $H = U + PV$ (as $\Delta V = V$).

**Definition**. Assuming an environment at constant temperature, the *Helmholtz Free Energy* $F$ is the energy needed to create the system minus the energy that can be gotten for free due to the environment's temperature, and is calculated as $F = U - TS$. That is, this is the energy that must be provided as work if the system is being created out of nothing, or the energy gained from annihilating the system (as entropy must be dissipated into the environment).

**Definition**. In an environment with constant pressure and temperature, we define the *Gibbs Free Energy* $G$ as the energy needed to create the system or can be gained from the system as $G = U - TS + PV$.

**Definition**. The values $U$, $H$, $F$, and $G$ are known as the *thermodynamic potentials*.

Notably, $\Delta F = \Delta U - \Delta(TS)$. At constant temperature, this becomes $\Delta F = \Delta U - T \Delta S = Q + W - T \Delta S$. If no new entropy is created, we see that $Q = T \Delta S$. Then, $\Delta F = W$. If new entropy is created, $T \Delta S > Q$, so then $\Delta F \leq W$.

We can also see that $\Delta G = \Delta U - \Delta (TS) + \Delta(PV)$. At constant pressure and temperature, this becomes $\Delta G = Q + W - T \Delta S + P \Delta V$. We see that $Q - T \Delta S$ is always zero or negative. Thus, with $W = W_{Compression} + W_{Other} = -P \Delta V + W_{Other}$, we see that $\Delta G \leq W_{Other}$.

We can also use this to calculate the voltage of an electrolytic cell, by dividing the Gibbs Free Energy by Avogadro's number times the number of electrons displaced in the Reduction-Oxidation reaction, such that $\Delta V = \frac{\Delta G}{e \cdot N_A}$.

We also know that $dU = T dS - P dV + \mu dN$. We can also calculate that $dH = dU + P dV + V dP = T dS - P dV + \mu dN + P dV + V dP = T dS + V dP + \mu dN$.

Similarly, $dF = dU - T dS - S dT = -S dT - P dV + \mu dN$. Holding $V, N$ constant, we see $dF = - S dT \Rightarrow S = -(\frac{\partial F}{\partial T})_{V, N}$. We also see that $P = -(\frac{\partial F}{\partial T})_{T, N}$ and $\mu = (\frac{\partial F}{\partial N})_{T, V}$.

We can apply the logic to $dG = -S dT + V dP + \mu dN$. Holding constants tell us that $S = -(\frac{\partial G}{\partial T})_{P,N}$, $V = (\frac{\partial G}{\partial P})_{T, N}$, and $\mu = (\frac{\partial G}{\partial N})_{T,P}$.

## Section 5.2 - Free Energy as a Force toward Equilibrium

Consider a system in which the environment acts as an energy reservoir. Then, the total entropy $S_{total}$ can be written as $S_{total} = S + S_R$, where $S$ is the entropy of the system and $S_R$ the entropy of the reservoir. Then, we can see that $dS_{total} = dS + dS_R$. We can then see that the thermodynamic identity tells us that

$$dS = \frac{1}{T}dU + \frac{P}{T}dV - \frac{\mu}{T} dN$$

Now, let us assume that the reservoir has a fixed volume $V$ and particle count $N$. Then, knowing that $dU_R = -dU$ and $T_R = T$, we see that

$$dS_{total} = dS + \frac{1}{T_R} dU_R = -\frac{1}{T}(dU - T dS) = -\frac{1}{T}dF$$

Thus, under fixed $T$, $V$, and $N$, an increase in entropy of the universe is the same as a decrease in Helmholtz free energy. So, instead of maximizing entropy, we can minimize Helmholtz free energy.

Similarly, we can instead assume the reservoir has fixed pressure $P$ and particle count $N$, rather than fixed volume $V$. Thus, with $dU_R = -dU$ and $dV_R$,

$$dS_{total} = dS + \frac{1}{T_R} dU_R + \frac{P}{T}dV_R = dS - \frac{1}{T} dU - \frac{P}{T} dV = -\frac{1}{T}(dU - T dS + P dV) = -\frac{1}{T} dG$$

Then, with only a variable volume, we see that the Gibbs free energy tends to decrease.

To summarize,

- At constant $U$ and $V$, $S$ tends to increase
- At constant $T$ and $V$, $F$ tends to decrease
- At constant $T$ and $P$, $G$ tends to decrease

Note that all thermodynamic potentials are extensive quantities.

---

We know that $(\frac{\partial G}{\partial N})_{T, P} = \mu$. We can see then that $G = N \mu$, given a fixed temperature and pressure. We also know that $(\frac{\partial F}{\partial N})_{T, V} = \mu$, so at a fixed temperature and volume, $F = N \mu$.

We can then see that

$$\frac{\partial \mu}{\partial P} = \frac{\partial}{\partial P}[\frac{G}{N}] = \frac{1}{N} \frac{\partial G}{\partial P} = \frac{V}{N}$$

Applying the ideal gas law, $V = \frac{NkT}{P}$, so

$$\frac{\partial mu}{\partial P} = \frac{V}{N} = \frac{NkT}{P} \frac{1}{N} = \frac{kT}{P}$$

We can integrate both sides to see that $\mu = \mu(T, P) = \mu^\circ(T) + kT \ln \frac{P}{P^\circ}$. Here, $P^\circ$ is atmospheric pressure and $\mu^\circ$ is the chemical potential at atmospheric pressure.

## Phase Transformations of Pure Substances

**Definition**. A *phase transformation* is a discontinuous change in the properties of a substance as its environment is only changed infinitesimally.

**Definition**. A *phase diagram* illustrates the phase against temperature and pressure.

**Definition**. At the *triple point*, all three phases coexist.

**Definition**. At the *critical point*, there is no longer any discontinuous change between the liquid and gas phases.

**Definition**. The *liquid crystal* phase is a phase in which molecules move randomly as in a liquid but remain oriented parallel to each other.

**Definition**. A *superfluid* phase has zero viscosity and high thermal conductivity.

**Definition**. A *Type-I Superconductor*, such as tin, mercury, or lead, exists only when the temperature and external magnetic field are sufficiently low.

**Definition**. A *ferromagnet*, such as Iron, has magnetized phases pointing either up or down depending on the direction of the applied field. When the applied field is $0$, both phases may coexist.

**Definition**. At the *Curie temperature*, magnetization in the material disappears entirely.

Consider Diamonds and Graphite. At STP, the Gibbs free energy of a mole of diamond is $2.9 kJ$ greater than the Gibbs free energy of a mole of graphite. We know that the stable phase is the one with the lower Gibbs free energy, so at STP, graphite is preferred.

However, we know that $(\frac{\partial G}{\partial P})_{T,N} = V$. As diamond has a smaller volume than graphite, at high pressures, diamond will have a smaller Gibbs free energy than graphite.

Similarly, $(\frac{\partial G}{\partial T})_{P,N} = -S$. Then, at higher temperatures, as graphite has more entropy, it will have a larger free energy.

**Definition**. The *Clausius-Clapeyron Relation* tells us that at phase boundaries, $G_1 = G_2$. That is, $d G_1 = dG_2$. We can then substitute in the thermodynamic identity to see that

$$-S_1 dT + V_1 dP = -S_2 dT + V_2 dP$$

This assumes that $N$ is fixed. Then, we can find $dP/dT$ as

$$\frac{dP}{dT} = \frac{S_2 - S_1}{V_2 - V_1}$$

We can then see that $S_2 - S_1 = L/T$, where $L$ is the total latent heat for converting from phase $1$ to $2$. Then, $\frac{dP}{dT} = \frac{L}{T \Delta V}$.
