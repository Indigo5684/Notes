# Chapter 4 - Engines and Refrigerators

## Section 4.1 - Heat Engines

**Definition**. A *heat engine* is any machine that absorbs heat and converts part of it into work. We model heat engines as accepting heat from a *hot reservoir* with temperature $T_h$ and rejecting heat to a *cold reservoir* with temperature $T_c$, as well as outputting work.

**Definition**. A *reservoir* is any object so large that its temperature does not change as it accepts or rejects heat

For a a heat engine, we will denote $Q_h$ and $Q_c$ to represent the heat absorbed from the hot reservoir and heat rejected to the cold reservoir. Then, the net work done by the engine is $W$. In this model, all signs are positive.

**Definition**. The *efficiency* $e$ is the benefit/cost ratio. Fora  heat engine, we see that $e = \frac{W}{Q_h}$. As $\Delta U = Q_h - Q_c - W$ and $U$ is a state variable (so $\Delta U = 0$ as this engines are cyclic), we know that $Q_h = W + Q_c$, so that $W = Q_h - Q_c$. Then, we can write $e = \frac{W}{Q_h} = \frac{Q_h - Q_c}{Q_h} = 1 - \frac{Q_c}{Q_h}$. We then see that efficiency is always in the range $[0, 1]$.

By the second law of thermodynamics, $S_h \geq S_c$. We know that $S = \frac{Q}{T}$ for a reservoir, so $\frac{Q_h}{T_h} \geq \frac{Q_c}{T_c}$, which can be rewritten as $\frac{T_c}{T_h} \geq \frac{Q_c}{Q_h}$. Then, substituting into the equation for efficiency, $e \geq 1 - \frac{T_c}{T_h}$. Note that actual efficiency will be less than this limit as entropy will be produced within the engine as well.

Let us now revisit a classic: the Carnot cycle. This cycle consists of isothermal expansion of a gas at temperature $T_h$, adiabatic expansion of the gas from $T = T_h$ to $T = T_c$, isothermal compression at $T = T_c$, and adiabatic compression from $T = T_c$ to $T = T_h$. By applying the formula of the ideal gas, we see this cycle reaches the maximum efficiency of $e = 1 - \frac{T_c}{T_h}$. However, this engine is not very practical.

## Section 4.2 - Refrigerators

**Definition**. A *refrigerator* is a heat engine operated in reverse.

**Definition**. The *coefficient of performance* is a fancy name for efficiency, in which

$$\text{COP} = \frac{Q_c}{W} = \frac{Q_c}{Q_h - Q_c} = \frac{1}{Q_h/Q_c - 1}$$

We can then apply the second law to see that

$$\text{COP} \leq \frac{1}{T_h/T_c - 1} = \frac{T_c}{T_h - T_c}$$ 

This textbook does not account for heat pumps.

## Section 4.3 - Real Heat Engines

An internal combustion engine is a classic example, in which the working substance is a gas.

**Definition**. An internal combustion engine follows an *Otto cycle*, in which gas is compressed adiabatically by a piston. Then, during ignition, the temperature and pressure are raised while volume is constant, followed by a power stroke in which the gas expands and does work. Lastly, the gas is vented as pressure is held constant and volume drops.

We can then show that $e = 1 - (\frac{V_2}{V_1})^{\gamma - 1}$, where $V_1 / V_2$ is the *compression ratio*. Unfortunately, if the compression ratio becomes too high, the gas will preignite spontaneously before compression is finished.

**Definition**. In a *diesel engine*, only air is compressed, before fuel is sprayed into the engine when air temperature is high enough for ignition. The efficiency then becomes a function of the *cutoff ratio*.

**Definition**. In a *steam engine*, a gas will follow the *Rankine cycle*, in which water is pumped to a high pressure, converted to a gas and expanded, sent through a turbine as it expands and pressure drops, and then condensed back to an initial volume. The efficiency then becomes a function of enthalpy ($H = U + PV$), where $e = \frac{H_4 - H_1}{H_3 - H_2} \approx 1 - \frac{H_4 - H_1}{H_3 - H_1}$.

For a steam engine, we see steam tables, and everybody becomes unhappy.

## Section 4.4 - Real Refrigerators

A refrigerator is normally the reverse of a Rankine cycle. Notably, refrigerants are used instead of water due to the lower freezing and boiling temperatures. However, many are CFCs. We then see that

$$\text{COP} = \frac{H_1 - H_4}{H_2 - H_3 - H_1 + H_4}$$

**Definition**. The *throttling* or *Joule-Thomson* process is used in refrigerators, and is complex. This class skips it for now.

I've also skipped the Liquefaction of Gasses and Towards Absolute Zero sections.
