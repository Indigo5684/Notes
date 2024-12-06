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

**Theorem**. The union of an arbitrary collection of open sets is open.

**Theorem**. The intersection of a finite collection of open sets is open.

**Theorem**. The union of finitely many closed sets is closed.

**Theorem**. The intersection of infinitely many closed sets is closed.

**Theorem**. A subset of a metric space is closed if and only if it contains all of its cluster points.

---

**Definition**. A *sequence* $(x_n)$ in a metric space $(S, d)$ converges to a point $x \in S$ if given any $\epsilon > 0$, there exists a $K \in \mathbb{N}$ such that given $n \in \mathbb{N}$,

$$
n \geq K \Rightarrow d(x_n, x) \leq \epsilon
$$

**Theorem**. Let $(x_n)$ be a sequence in metric space $(S, d)$. Then,

- $(x_n)$ converges to $x$ if and only if every $\epsilon$-neighborhood of $x$ contains all but finitely many terms of $(x_n)$.
- If $(x_n) \rightarrow x$ and $(x_n) \rightarrow x'$, then $x = x'$.
- If $(x_n)$ converges, then $(x_n)$ is bound.

**Definition**. A sequence $(x_n)$ in metric space $(S, d)$ is a *Cauchy sequence* if for every $\epsilon > 0$, there exists some $H \in \mathbb{N}$ such that for any $m, n \in \mathbb{N}$,

$$
m, n \geq H \Rightarrow d(x_n, x_m) < \epsilon
$$

**Definition**. A metric space in which every Cauchy sequence converges is said to be *complete*.

**Remark**. $\mathbb{R}$ is complete, but $\mathbb{Q}$ is not.

---

**Definition**. Let $A$ be a subset of metric space $(S, d)$. Then, an *open cover* of $A$ is some collection of subsets $\mathcal{G} = \{G_\alpha\}_{\alpha \in I}$, such that $G_\alpha \subseteq S$ and $A \subseteq \cup_{\alpha \in I} G_\alpha$. That is, $A$ is contained within the union of all open subsets in $\mathcal{G}$.

**Definition**. If $\mathcal{G}' \subseteq \mathcal{G}$ is an open cover of $A$, then $\mathcal{G}'$ is a *subcover* of $\mathcal{G}$.

**Definition**. Given $K$ is a subset of metric space $(S, d)$, K is *compact* if every cover of $K$ contains a finite subcover.

**Theorem**. If $K$ is a compact subset of a metric space, then $K$ is closed and bounded.

**Theorem**. Heine-Borel Theorem. In $\mathbb{R}$, the convese is true. That is, if $K \subseteq \mathbb{R}$ is closed and bounded, then it is compact.

**Theorem**. If $K$ is a compact subset of a metric space, then every infinite subset of $K$ has a cluster point.

**Corollary**. Bolzano-Weirstrass Theorem. Every bounded infinite subset of $\mathbb{R}$ has a cluster point in $\mathbb{R}$.

---

**Definition**. Let $(S, d)$ be a metric space, and $A_1, A_2 \in S$ be subsets. Then, $A_1, A_2$ are said to be *separated* if there exist disjoint open subsets $U_1, U_2$ such that $A_1 \subseteq U_1$ and $A_2 \subseteq U_2$.

**Definition**. A subset $C$ of metric space $(S, d)$ is said to be *connected* if it is not the union of nonempty separated subsets.

**Theorem**. A subset of $\mathbb{R}$ is connected if and only if it is an interval.
