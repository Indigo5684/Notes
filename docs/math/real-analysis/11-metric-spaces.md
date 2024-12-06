# Chapter 11 - Metric Spaces

## Section 11.4 - Netric Spaces

**Definition**. A *metric* on set $S$ is a function $d: S \otimes S \rightarrow \mathbb{R}$ that satifies the following properties for all $x, y, z \in S$,

- $d(x, y) \geq 0$
- $d(x, y) = 0 \; \text{ if and only if } x = y$
- $d(x, y) = d(y, x)$
- $d(x, y) \leq d(x, z) + d(z, y)$

**Definition**. A *metric space* $(S, d)$ is a set $S$, with elements called *points*, together with a metric $d$.

**Definition**. With metric space $(S, d)$, if $A \subset S$, then $(A, d)$ is a *subspace* of $(S, d)$.

**Definition**. The *discrete metric* is provided by

$$
d(x, y) = \begin{cases}
  0 \; \text{ if } x = y \\
  1 \; \text{ if } x \neq y
\end{cases}
$$

---

**Definition**. Let $(S, d)$ be a metric space. Then, for each $\epsilon > 0$, the *$\epsilon$-neighborhood* or *$\epsilon$-ball* of a point $a \in S$ is the set

$$
V_\epsilon(a) = {x \in S | d(a, x) < \epsilon}
$$

**Definition**. Let $(S, d)$ be a metric space. Then, a subset $G \subseteq S$ is *open* if for each $x \in G$, there exists some $\epsilon > 0$ so that $V_\epsilon(x) \subseteq G$.

**Definition**. Let $(S, d)$ be a metric space. Then, a subset $G \subseteq S$ is *closed* if its complement $C(G) = S - G = S \ F$ is closed.

**Definition**. Let $(S, d)$ be a metric space. A point $c \in S$ is a *cluster point$ of a set $A \subseteq S$ if every $\epsilon$-neighborhood of $c$ contains some point $a \in A$ such that $a \neq c$.

**Theorem**. Every $\epsilon$-neighborhood of a point is an open set.