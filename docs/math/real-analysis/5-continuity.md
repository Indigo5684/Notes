# Chapter 5 - Continuiy

## Section 5.1 - Continuous Functions

**Definition**. Let $A \subseteq \mathbb{R}$, and $f: A \rightarrow \mathbb{R}$. Then, if $a \in A$, $f$ is *continuous at $a$* if, given any $\epsilon > 0$, there exists some $\delta > 0$ such that for all $x \in A$,

$$
|x - a| < \delta \Rightarrow |f(x) - f(a)| < \epsilon
$$

Note that if $a$ is an *isolateed point* of $A$, that is, not a cluster point, then $a$ is automatically continuous.

If $a$ is a cluster point of $A$, then this definition collapses to the definition of $\lim_{x \rightarrow a} f(x) = f(a)$.

Note that a function cannot be continuous at a point outside of its domain, even if the limit exists.

**Definition**. $f$ is continuous on $A$ if it is continuous at every point $a \in A$.

**Theorem**. $f$ is continuous if and only if for every sequence $(x_n)$ in $A$ that converges to $a$, the sequence $(f(x_n))$ converges to $f(a)$.

---

**Definition**. Let $(S, d_S)$ and $(T, d_T)$ be metric spaces. A function $f: S \rightarrow T$ is continuous at a point $a \in S$ if given any $\epsilon > 0$, there exists some $\delta > 0$ such thaat for all $x \in S$,

$$
d_S(x, a) < \delta \Rightarrow d_T(f(x),  f(a)) < \epsilon
$$

**Theorem**. A function $f: S \rightarrow T$ is continuous at a point $a \in A$ if and only if given some neighborhood $V(f(a)) \in B$, there xists some $U(a) \in A$ such that $f(U) \subseteq V$.

## Section 5.2 - Combinations of continuous Functions.

**Theorem**. Let $f, g: A \rightarrow \mathbb{R}$ be continuous at $a \in A$. Then, 

- $f + g$ and $fg$ are continuous at $a$
- If $g(x) \neq 0$ for all $x \in A$, then $\frac{f}{g}$ is continuous at $a$.

As a consequence, every polynomial, rational, and basic trigonometric function are continuous on its domains.

**Theorem**. Lett $A, B \subseteq \mathbb{R}$, such that $f: A \rightarrow B$ and $g: B \rightarrow \mathbb{R}$. Then, if $c$ is a cluster point of $A$ such that $\lim_{x \rightarrow c} f(x) = L \in B$ and $g$ is continuous at $L$, then

$$
\lim_{x \rightarrow c} g(f(x)) = g(L) = g(\lim_{x \rightarrow c} f(x))
$$

**Collary**. let $A, B \subseteq  \mathbb{R}$, with $f: A \rightarrow B$ and $g: B \rightarrow \mathbb{R}$. If $f$ is continuous at $a \in A$ and $g$ is continuous at $f(a) \in B$, then $g(f(x))$ is continuous at $a$.

## Section 5.3 - continuous functions on Intervals

**Theorem**. Let $S, T$ be metric spaces with $A \subseteq S$ and $f: A \rightarrow T$. If $A$ is a compact subset of $S$, then $f(A)$ is a compact subset of $T$.

**Collary**. Let $f: A \rightarrow \mathbb{R}$ be a continuous function, with $A$ being a compact subset of metric space $S$. Then, $f(A)$ is closed and bounded. Moreover, there exists a $p, q \in A$ such that $f(p)$ and $f(q)$ are the supremum and infimum of $f(A)$.

**Collary**. Maximum-Minimum Theorem. If $I = [a, b]$ is a closed and bounded interval and $f: I \rightarrow \mathbb{R}$ is continuous on $I$, then $f$ has an absolute minumum and maximum on $I$.

---

**Theorem**. Let $S, T$ be metric spaces and $A \subseteq S$. Then, if $f: A \rightarrow T$ is continuous on $A$, and $A$ is a connected subset of $S$, then $f(A)$ is a connected subset of $T$.

**Collary**. Suppose that $I$ is an interval. Let $f: I \rightarrow \mathbb{R}$ be continuous on $I$. Then, $f(I)$ is an intterval.

**Theorem**. (Bolzano's) Invermediate Value Theorem. Suppose $f: [a, b] \rightarrow \mathbb{R}$ is continuous on $[a, b]$ with $a \neq b$. Then, given some $k$ such that $f(a) < k < f(b)$, there exists some $c \in (a, b)$ such that $k = f(c)$.

---

**Definition**. Let $A \subseteq R$. Then, a function $f: A \rightarrow \mathbb{R}$ is *uniformly continuous* if given any $\epsilon > 0$, there exists some $\delta > 0$ depending only on $\epsilon$ such that for any $x, y \in A$,

$$
|x - y| < \delta \Rightarrow |f(x) - f(y)| < \epsilon
$$

Note that if $f$ is uniformly continuous, it must be continuous on $A$.

**Theorem**. Let $I = [a, b]$ be a closed and bounded interval. If $f: I \rightarrow \mathbb{R}$ is continuous on $I$, then $f$ is uniformly continuous.

**Remark**. If $S, T$ are metric spaces, $K$ is a compact subset of $S$, and $f: K \rightarrow T$ is continuous on $K$, then $f$ is uniformly continuous.

**Theorem**. Suppose $A \subseteq \mathbb{R}$ and $f: A \rightaarrow \mathbb{R}$ is uniformly continuous. Then, if $(x_n)$ is a Cauchy sequence in $A$, $(f(x_n))$ is a Cauchy sequence in $\mathbb{R}$.

**Remark**. Suppose $S, T$ are metric spaces and $f: S \rightaarrow T$ is uniformly continuous. Then, if $(x_n)$ is a Cauchy sequence in $S$, $(f(x_n))$ is a Cauchy sequence in $T$.