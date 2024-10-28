# Chapter 4 - Limits

## Secrion 4.1 - Limits of Functions

**Definition**. Let $A \subseteq \mathbb{R}$. Then, a point $c \in \mathbb{R}$ is a *cluster point* of $A$ if for every $\delta > 0$, the $\delta$-neighborhood of $c$ contains a point $a \in A$ such thhat $a \neq c$. That is, there exists some $a$ such that $0 < |a - c| < \delta$.

**Theorem**. A real number $c$ is a cluster point for a set $A$ if and only if there exists a sequence $(a_n)$ in $A\\ \{c\}$ such that $a_n \rightarrow c$

**Collary**. A real number $c$ is a cluster point of a set $A$ if and only if every $\delta$-neighborhood conttains infinitely many points of $A$.

**Definition**. The set of every cluster point of $A$ is called the *derived set* of $A$, and denoted $A'$.

**Collary**. A set $A$ is closed if and only if $A' \subseteq A$.

**Remark**. If $A'$ is the derived set of $A$, then $A'' \subseteq A'$.

**Remark**. Intervals involving infinity and square brackets for the constant are closed.

---

**Definition**. Suppose $f: A \rightarrow \mathbb{R}$ is a function with domain $A \subseteq \mathbb{R}$, and let $c \in A$ be a cluster point of $A$. then, a real number $L$ is a *limit of $f$ at $c$* if goven any $\epsilon > 0$, there exists some $\delta > 0$ such that

$$
0 < |x-c| < \delta \Rightarrrow |f(x) - L| < \epsilon
$$

**Therorem**. For a given function and cluster point, there can be at most one limit at said point.

**Theorem**. Let $A \subseteq \mathbb{R}$ and $f: A \rightarrow \mathbb{R}$. Then, to show that $lim_{x \rightarrow c} f(x) = L$, it suffices to show that for every sequence $(a_n)$ in $A\\ \{c\}$, the sequence $(f(a_n))$ converges tto $L$.

---

**Definition**. The *extended real numbers aree $\hat{\mathbb{R}} = \mathbb{R} \cup \{ \inftyy, -\infty \}$ are a totally-ordered set witth supremum and infimum. Note that this set is no longer a field.

**Definition**. At any point $c$, the limitt of $f$ at $c$ is infinite if given some $\alpha$,  there exists some $V_\delta(c)$ such that forr all $x \in V_\epsilon(c)$, then $f(x) \in V_\alpha(\infty)$.

**Definition**. The limit of a function at infinity is defined if for a given $\epsilon$, there ixists some $\alpha$ so that there exists some $V_\delta(c)$ such that for all $x \in A$,

$$
x > \alpha \Rightarrow |f(x) - L| < \epsilon
$$
