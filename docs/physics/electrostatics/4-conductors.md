# Chapter 4 - Conductors and Static Electric Fields

## Section 4.1 - Introduction

We will focus primarily on electric fields and charges. For the purposes for this section, we will assume insulators are perfect.

## Section 4.2 - Electrostatic Properties of a Conductor

In a metal or conductor, there are plentiful charges not bound to a particular atom and are thus free to move throughought the material.

We note that there is no electric fiend inside a conductor, as charges internal to the material would move under the force it generates until they find a configuration that eliminates the field. This may happen, but not in electrostatics.

Additionally, as the field is zero, it follows from Maxwell's equations that there is no charge inside a conductor. However, charge may be present at the surface. For sufficiently symnetric charges, this charge may be calculated.

Consider any two points internal to the conductor. The voltage between said points is defined as $\int_A^B \vb{E} \vdot \dd{\vb{l}}$. Since $\vb{E} = 0$ inside the conductor, the volage difference must be zero. Thus, any two points in or on the surface (TODO: Why on the surface?) of a conductor must be at the same potential.

The electric field at the surface of a conductor is perpendicular to its surface. Consider some displacement $\dd{\vb{l}}$. Now, $\vb{E} \vdot \dd{\vb{l}} = \vb{E}_s \vdot \dd{\vb{l}}_s + \vb{E}_p \vdot \dd{\vb{l}}_p = \dd{V_s} + \dd{V_p}$, in terms of parallel and perpendicular components. The paralell voltage difference is zero, so the electric field must be zero.

Consider the surface of a conductor with surface charge density $\sigma_e$. A cyliner with one end inside and one end outside said surface, with its axis normal to said surface, will be a Gaussian "pillbox", which will show that with V being the volume of the pillbox, $\int_V \div{\vb{E}} \dd{V} = \frac{Q_e}{\epsilon_0} = \frac{A\sigma_e}{\epsilon_0}$. Thus, $\sigma_e = \epsilon_0 E$.