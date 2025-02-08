# Chapter 4 - Limits

## Section 4.1 - Limits of Functions

**Definition**. Let $A \subseteq \mathbb{R}$. Then, a point $c \in \mathbb{R}$ is a *cluster point* of $A$ if for every $\delta > 0$, the $\delta$-neighborhood of $c$ contains a point $a \in A$ such that $a \neq c$. That is, there exists some $a$ such that $0 < |a - c| < \delta$.

**Theorem**. A real number $c$ is a cluster point for a set $A$ if and only if there exists a sequence $(a_n)$ in $A\\ \{c\}$ such that $a_n \rightarrow c$

**Corollary**. A real number $c$ is a cluster point of a set $A$ if and only if every $\delta$-neighborhood contains infinitely many points of $A$.

**Definition**. The set of every cluster point of $A$ is called the *derived set* of $A$, and denoted $A'$.

**Corollary**. A set $A$ is closed if and only if $A' \subseteq A$.

**Remark**. If $A'$ is the derived set of $A$, then $A'' \subseteq A'$.

**Remark**. Intervals involving infinity and square brackets for the constant are closed.

---

**Definition**. Suppose $f: A \rightarrow \mathbb{R}$ is a function with domain $A \subseteq \mathbb{R}$, and let $c \in A$ be a cluster point of $A$. then, a real number $L$ is a *limit of $f$ at $c$* if given any $\varepsilon > 0$, there exists some $\delta > 0$ such that

$$
0 < |x-c| < \delta \Rightarrow |f(x) - L| < \varepsilon
$$

**Theorem**. For a given function and cluster point, there can be at most one limit at said point.

**Theorem**. Let $A \subseteq \mathbb{R}$ and $f: A \rightarrow \mathbb{R}$. Then, to show that $lim_{x \rightarrow c} f(x) = L$, it suffices to show that for every sequence $(a_n)$ in $A\\ \{c\}$, the sequence $(f(a_n))$ converges tto $L$.

---

**Definition**. The *extended real numbers* are $\hat{\mathbb{R}} = \mathbb{R} \cup \{ \infty, -\infty \}$ are a totally-ordered set with supremum and infimum. Note that this set is no longer a field.

**Definition**. At any point $c$, the limit of $f$ at $c$ is infinite if given some $\alpha$,  there exists some $V_\delta(c)$ such that for all $x \in V_\varepsilon(c)$, then $f(x) \in V_\alpha(\infty)$.

**Definition**. The limit of a function at infinity is defined if for a given $\varepsilon$, there exists some $\alpha$ so that there exists some $V_\delta(c)$ such that for all $x \in A$,

$$
x > \alpha \Rightarrow |f(x) - L| < \varepsilon
$$

## Section 4.2 - Limit Theorems

**Definition**. Let $A \subseteq \mathbb{R}$ and $c \in \mathbb{R}$ be a cluster point of $A$. Then, a function $f: A \rightarrow \mathbb{R}$ is *bounded on a neighborhood of $c$* if there exists some $\delta$-neighborhood $V_\delta(c)$ of $c$ and some constant $M > 0$ such that for all $x \in A \cap V_\delta(c)$, then $|f(x)| \leq M$.

**Theorem**. If $A \subseteq \mathbb{R}$ and $f: A \rightarrow \mathbb{R}$ has a finite limit at $c \in \mathbb{R}$, then $f$ is bounded on some neighborhood of $c$.

**Theorem**. With $A \subseteq \mathbb{R}$, and $f, g: A \rightarrow \mathbb{R}$, with $c \in \mathbb{R}$ a cluster point of $A$, then if $\lim_{x \rightarrow c} f(x) = L$ and $\lim_{x \rightarrow c} g(x) = M$, then:

$$\lim_{x \rightarrow c} (f(x) + g(x)) = L + M$$

$$\lim_{x \rightarrow c} (f(x)g(x)) = LM$$

Additionally, if $g(x) \neq 0$ for all $x \in A$, and $M \neq 0$, then

$$
\lim_{x \rightarrow c} \frac{f(x)}{g(x)} = \frac{L}{M}
$$

**Corollary**. If $p, q \in \mathbb{R}[x]$, and $q(c) \neq 0$ for some $c \in \mathbb{R}$, then

$$
\lim_{x \rightarrow c} p(x) = p(c)
$$

$$
\lim_{x \rightarrow c} \frac{p(x)}{q(x)} = \frac{p(c)}{q(c)}
$$

**Theorem**. Squeeze Theorem. Let $A \subseteq \mathbb{R}$. Then, if $f, g, h: A \rightarrow \mathbb{R}$ and with $c \in \mathbb{R}$ being a cluster point of $A$, then if both

$$
\lim_{x \rightarrow c} f(x) = \lim_{x \rightarrow c} h(x) = L
$$

$$
f(x) \leq g(x) \leq h(x) \; \text{ for all } x \in A, x \neq c
$$

Then, $\lim_{x \rightarrow c} g(x) = L$.
