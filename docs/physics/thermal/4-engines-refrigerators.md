# Chapter 4 - Engines and Refrigerators

## Section 4.1 - Heat Engines

**Definition**. A *heat engine* is any machine that absorbs heat and converts part of it into work. We model heat engines as accepting heat from a *hot reservoir* with temperature $T_h$ and rejecting heat to a *cold reservoir* with temperature $T_c$, as well as outputting work.

**Definition**. A *reservoir* is any object so large that its temperature does not change as it accepts or rejects heat

For a a heat engine, we will denote $Q_h$ and $Q_c$ to represent the heat absorbed from the hot reservoir and heat rejected to the cold reservoir. Then, the net work done by the engine is $W$. In this model, all signs are positive.

**Definition**. The *efficiency* $e$ is the benefit/cost ratio. Fora  heat engine, we see that $e = \frac{W}{Q_h}$. As conservation of energy applies, we know that $Q_h = W + Q_c$, so that $W = Q_h - Q_c$. Then, we can write $e = \frac{W}{Q_h} = \frac{Q_h - Q_c}{Q_h} = 1 - \frac{Q_c}{Q_h}$. We then see that efficiency is always in the range $[0, 1]$.

By the second law of thermodynamics, $S_h \geq S_c$. We know that $S = \frac{Q}{T}$ for a reservoir, so $\frac{Q_h}{T_h} \geq \frac{Q_c}{T_c}$, which can be rewritten as $\frac{T_c}{T_h} \geq \frac{Q_c}{Q_h}$. Then, substituting into the equation for efficiency, $e \geq 1 - \frac{T_c}{T_h}$. Note that actual efficiency will be less than this limit as entropy will be produced within the engine as well.

Let us now revisit a classic: the Carnot cycle. This cycle consists of isothermal expansion of a gas at temperature $T_h$, adiabatic expansion of the gas from $T = T_h$ to $T = T_c$, isothermal compression at $T = T_c$, and adiabatic compression from $T = T_c$ to $T = T_h$. By applying the formula of the ideal gas, we see this cycle reaches the maximum efficiency of $e = 1 - \frac{T_c}{T_h}$. However, this engine is not very practical.
