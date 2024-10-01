# Chapter 3 - Eletric and Magnetic Scalar Potentials

# Section 3.1 - Work and Energy in Electrostatics and Magnetostatics

The force on charge $q$ is given by $\vb{F}(\vb{r}) = q_e \vb{E}(\vb{r})$ or $\vb{F}(\vb{r}) = q_m \vb{H}(\vb{r})$. If this charge is moved $\dd{\vb{l}} = \dd x \vu{x} + \dd y \vu{y} + \dd z \vu{z}$, the change in internal energy (work) this produces can be written as

$$
\dd{U}= - \vb{F} \vdot \dd{\vb{l}}
$$

Rewriting this, $\vb{F} = -\grad{U}$, with $U$ as potential energy. Now, we can denote this change in internal energy in terms of $q$ as follows:

$$
\vb{E}(\vb{r}) = \frac{1}{q_e} \vb{F_e}(\vb{r}) = - \frac{1}{q_e} \grad{U_e(\vb{r})} = -\grad{V_e(\vb{r})}
$$

The units of electrostatic potential is Joule/Coublomb, also known as a Volt. Thus, the units of the electric field should be expressed in Volts/meter. Similarly,

$$
\vb{H}(\vb{r}) = \frac{1}{q_m} \vb{F_m}(\vb{r}) = - \frac{1}{q_m} \grad{U_m(\vb{r})} = -\grad{V_m(\vb{r})}
$$

The units of magnetostatic potential is Joule/Weber, also known as an Ampere. Thus, the units of the magnetic field can be written as Amperes/meter.

With this, we can calculate work. Moving a charge $q$ from $A$ to $B$, we see that

$$
\delta W = \int_A^B \vb{F} \vdot \dd{\vb{l}} = q_e \int_A^B \vb{E} \vdot \dd{\vb{l}} = -q_e \int_A^B \grad{\vb{V}} \vdot \dd{\vb{l}} = -q_e \delta V_e 
$$

Strictly speaking, this is a potential difference. To find the absolute potential, assume a point charge $Q$ at the origin, and a charge $q$. We take the work as $q$ moves from $\vb{r'} = \vb{\infty}$ to $\vb{r'} = \vb{r}$. Thus,

$$
W = -q_e \frac{Q_e}{4 \pi \epsilon_0} \int_{\infty}^0 \frac{\vu{r'}}{r'^2} \vdot (\vu{r'}) \dd{r'} = -q_e \frac{Q_e}{4 \pi \epsilon_0} [\frac{-1}{r'}]_{\infty}^{r'} = q_e \frac{Q_e}{4 \pi \epsilon_0} \frac{1}{r}
$$

$$
W = -q_m \frac{Q_m}{4 \pi \mu_0} \int_{\infty}^0 \frac{\vu{r'}}{r'^2} \vdot (\vu{r'}) \dd{r'} = -q_m \frac{Q_m}{4 \pi \mu_0} [\frac{-1}{r'}]_{\infty}^{r'} = q_m \frac{Q_m}{4 \pi \mu_0} \frac{1}{r}
$$

Letting the potential as $\vb{r} \leftarrow \infty$ equal $0$ be our reference and dividing out `q`, we find that the voltage for arrangement is the following:

$$
V_e(\vb{r}) = \frac{Q_e}{4 \pi \epsilon_0 r} \text{ and } V_m(\vb{r}) = \frac{Q_m}{4 \pi \mu_0 r}
$$

Now, if we let the stationary charge $Q$ be located at $\vb{r'}$, we see that

$$
V_e(\vb{r}) = \frac{Q_e}{4 \pi \epsilon_0 \abs{\vb{r} - \vb{r'}}} \text{ and } V_m(\vb{r}) = \frac{Q_m}{4 \pi \mu_0 \abs{\vb{r} - \vb{r'}}}
$$

If we allow multiple charges, this becomes

$$
V_e(\vb{r}) = \frac{1}{4\pi \epsilon_0} \sum_{i=1}^N \frac{Q_ei}{\abs{\vb{r}-\vb{r_i}}}
$$

Taking this to its natural limit,

$$
V_e(\vb{r}) = \frac{1}{4 \pi \epsilon_0} \int_{V'} \frac{\rho_e(\vb{r'})}{\abs{\vb{r}-\vb{r'}}} \dd{V'}
$$


$$
V_m(\vb{r}) = \frac{1}{4 \pi \mu_0} \int_{V'} \frac{\rho_m(\vb{r'})}{\abs{\vb{r}-\vb{r'}}} \dd{V'}
$$