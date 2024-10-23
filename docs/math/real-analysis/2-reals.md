# Chapter 2

## Section 2.1 - The Algebraic and Order Properties of Real Numbers

**Proposition**. 2.1.1: $\mathbb{R}$ is a field, with zero element $0$ and identity $1$.

**Definition**. The rational numbers $\mathbb{Q}$ is the field of fractions of the natural numbers $\mathbb{N}$.

**Theorem**. 2.1.4: There does not exist a rational number $r$ such that $r^2 = 2$.

---

**Definition**. An *ordered field* is a field $F$ together with subset $F^+$ such that

1. $F+$ is closed under addition and multiplication
2. If $a \in F$, then exclusively $a \in F^+$, $a = 0$, or $-a \in F^+$.

**Theorem**. In any ordered field $F$, the following hold

1. $1 \in F^+$
2. $\mathbb{N} \subset F^+$
3. If $a \in F^+$, then $\frac{1}{a} \in F^+$

**Definition** The order relation $a > b$ and $b < a$ is defined by $a - b \in F^+$.

**Theorem**. If $a, b, c \in F$, then

1. One of $a > b$, $a = b$, or $a < b$ hold (trichotomy)
2. If $a > b$ and $b > c$, then $a > c$ (transitivity)
3. If $a > b$, then $-a < -b$
4. If $a > b$ and $c > 0$, then $ac > bc$
5. If $a > b$ and $c < 0$, then $ac < bc$
6. If $a > b > 0$, then $\frac{1}{b} > \frac{1}{a} > 0$

---

**Definition**. Let $S$ be a nonempty subset of ordered field $F$. Then, $S$ is *bounded above* if there exists some $u \in F$ such that $s \leq u$ for all $s \in S$. Then, said element $u$ is an *upper bound* of $S$.

**Definition**. Let $S$ be a nonempty subset of ordered field $F$. Then, $S$ is *bounded below* if there exists some $u \in F$ such that $s \geq u$ for all $s \in S$. Then, said element $u$ is a *lower bound* of $S$.

**Definition**. Let $S$ be a nonempty subset of ordered field $F$. Then, $S$ is *bounded* if it is bounded both above and below.

**Definition**. Given field $F$ and nonempty subset $S \subset F$, an element $u \in F$ is a *supremum* or *least upper bound* of $S$ if $u$ is an upper bound of $S$, and given any other upper bound $v$, then $u < v$

**Definition**. Given field $F$ and nonempty subset $S \subset F$, an element $u \in F$ is an *infimum* or *greatest lower bound* of $S$ if $u$ is a lower bound of $S$, and given any other lower bound $v$, then $u > v$

**Definition**. Given an ordered field $F$, the field has the *supremum/infimum property* if given any nonempty subset $S$, if $S$ is bounded above/below, $S$ has a supremum/infimum.

## Section 2.2 - Absolute Value and the Real Line

**Definition**. Absolute value is defined as normal (piecewise). Multiline function in LaTeX are hard.

**Theorem**. Given any $a, b \in \mathbb{R}$, we know that

1. $|a| > 0$ for $a \neq 0$
2. $|ab| = |a||b|$
3. $|a + b| \leq |a| + |b|$

**Collary**. Givem $a, b \in \mathbb{R}$, then $\abs{\abs{a} - \abs{b}} \leq \abs{a - b}$.

**Remark**. Every field has at least one absolute value function.

**Theorem**. In an ordered field $F$, for any $r > 0$, we know that

1. $\abs x = r$ if and only if $x = r$ or $x = -r$
2. $\abs x < r$ if and only if $-r < x < r$
3. $\abs x > r$ if either $x > r$ or $x < -r$
