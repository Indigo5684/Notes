# Chapter 3 - Sequences and Series

## Section 3.1 - Sequences and their Limits

**Definition**. A *sequence in $\mathbb{R}$* is a function $X: \mathbb{N} \rightarrow \mathbb{R}$, typically notated as $X$ or $(x_n)$, with $x_n$ being referred to as the *terms* of the sequence. The set ${x_n | n \in \mathbb{N}}$ is the *range* of this sequence.

**Definition**. The sequence is *bounded* if its range is a bounded subset of $\mathbb{R}$.

**Example**. The *constant sequence* $C = (c) = (c, c, c, \ldots)$.

**Example**. The *harmonic sequence* $\frac{1}{n} = (1, \frac{1}{2}, \frac{1}{3}, \ldots)$

**Example**. The *geometric sequence*, given base $a \in \mathbb{R}$ and ratio $r \in \mathbb{R}$

$$
(x_n) = (a, ar,  ar^2, ar^3, \ldots)
$$

**Example**. The *arithmatic sequence*, given base $a \in \mathbb{R}$ and distance $d \in \mathbb{R}$,

$$
(x_n) = (a, a + d, a + 2d, a + 3d, \ldots)
$$

**Example**. Decimal expansions are bounded sequences.

---

**Definition**. A sequence $X = (x_n)$ is said to *converge* to a number $x \in \mathbb{R}$ if when given any $\epsilon > 0$, there exists some $K \in \mathbb{N}$ such that for every $n \in \mathbb{N}$ with $n \geq K$,

$$
\abs{x_n - x} < \epsilon
$$

If this is the case, we say that $X$ converges to  $x$, and $x$ is a *limit* of X. This can be written as

$$
\lim X = x \text{ or } \text \lim(x_n) = x \text{ or }  x_n \rightarrow x
$$

**Definition**. If a sequence does not have a limit, it is *divergent*.

**Theorem**. A sequence can have at most one limit. That is, if a limit exists, it is unique.

**Theorem**. If a limit is convergent, then it is bounded.

## Section 3.2 - Limit Theorems

**Theorem**. Suppose there exists some $X$ such that $(x_n) \rightarrow x$ and $Y$ such that $(y_n) \rightarrow y$. Then,

1. $x_n + y_n \rightarrow x + y$
2. $x_n \cdot y_n \rightarrow xy$
3. If $x_n \neq 0$ for all $n$, then $\frac{1}{x_n} \rightarrow \frac{1}{x}$

**Theorem**. Suppose $(x_n)$ aand $(y_n)$ are convergent sequences and $N \in \mathbb{N}$. Then,

1. If $x_n \leq y_n$ for all $n \geq N$, then $\lim(x_n) \leq \lim(y_n)$
2. If $x_n \leq a$ for all $n \geq N$, then $\lim(x_n) \leq a$
3. If $x_n \geq a$ for all $n \geq N$, then $\lim(x_n) \geq a$

**Theorem**. Squeeze Theorem. Suppose $(x_n), (y_n), (z_n)$ are all sequences of real numbers, and $\lim(x_n) = \lim(z_n) = a$. Then, if for some $N in \mathbb{N}$,

$$
\text{If } x_n \leq y_n \leq z_n, \text{ then } \lim(y_n) = a
$$

**Theorem**. Suppose $(x_n)$ is a sequence if real numbers. Then,

1. If $x_n \rightarrow x$, then $\abs{x_n} \rightarrow \abs{x}$
2. If $\abs{x_n} \rightarrow 0$, then $x_n \rightarrow 0$
3. $x_n \rightarrow x$ if and only if $\abs{x_n - n} \rightarrow 0$

**Theorem**. Suppose $(x_n)$ is a sequence if real numbers, with each $x_n \geq 0$. Then, given some $k \in \mathbb{N}$, if $x_n \rightarrow x$, then $\sqrt[k]{x_n} \rightarrow \sqrt[k]{x}$.

## Section 3.3 - Monotonic Sequences

**Definition**. A sequence $(x_n)$ is *monotonically increasing* if $x_{n+1} \geq x_n$ for all $n \in \mathbb{N}$.

**Definition**. A sequence $(x_n)$ is *monotonically decreasing* if $x_{n+1} \leq x_n$ for all $n \in \mathbb{N}$.

**Definition**. A sequence is *monotonic* if it is either monotonically increasing or decreasing.

**Theorem**. A monotonic sequence is converging if and only if it is bound.

## Section 3.4 - Subsequences

**Definition**. Let $X = (x_n)$ be a sequence in $\mathbb{R}$. Then, the sequence

$$
X_{n_k} = (x_{n_1}, x_{n_2}, \ldots)
$$

is a *subsequence* of $X$,

**Theorem**. If a sequence converges to $x$, then every subsequence also converges to $x$.

**Theorem**. Every sequence of real numbers $(x_n)$ contains a monotonic subsequence $(x_{n_k})$.

**Collary**. Bolzano-Weierstrass Theorem. Every bounded sequence of real numbers has a convergent subsequence.

## Section 3.5 - The Cauchy Criterion

**Definition**. A sequence $(x_n)$ is said to be a *Cauchy sequence* such that for any given $\epsilon$, there exists a natural number $H$ such that all natural numbers $m, n \geq H$, then

$$
\abs{x_m - x_n} \leq \epsilon
$$

**Theorem**. If $(x_n)$ is a Cauchy sequence, then $(x_n)$ is convergent.

## Section 3.7 - Series

**Definition**. Let $(x_n)$ be a sequence in $\mathbb{R}$. Then, the *infinite series genearted by $X$* is the sequence $S = (s_n)$ with terms

$$
s_1 = x_1; \; s_{n+1} = s_n + x_{n+1}
$$

In other words, $s_n = \sum_{i=1}^n x_i$. We denote this series as $\sum x_n$.

**Definition**. If this series is convergent to some number $s$, we say that $s$ is the *sum* of the series.

---

For natural numbers $n > m$, note that

$$
s_n - s_m = \sum_{i=m + 1}^n x_i
$$

In particular, $s_n - s_{n - 1} = x^n$. Thus, the Cauchy criteria takes the form

**Theorem**. Cauchy Criteria for Series. The series $\sum x_n$ converges if and only if, for a given $\epsilon$, there exists some natural number $H$ such that when $m > n > H$,

$$
\abs{s_m - s_n} = \abs{\sum_{i = m + 1}^n x_i} < \epsilon
$$

**Collary**. $n$-th Term Test. If $\sum x_n$ converges, then $x_n \rightarrow 0$.

**Collary**. Absolute Convergence Test. If $\sum \abs{x_n}$ converges, then $\sum x_n$ converges.

---

**Theorem**. A series with non-negative terms converges if and only if its sequence of partial sums is bounded.

---

**Theorem**. $e = \lim_{n \rightarrow \infty} (1+\frac{1}{n})^n = \sum_{n=0}^\infty \frac{1}{n!}$
