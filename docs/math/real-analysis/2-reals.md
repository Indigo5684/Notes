# Chapter 2 - The Real Number Line

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
2. $\mathbb{N} \subseteq F^+$
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

**Definition**. Given field $F$ and nonempty subset $S \subseteq F$, an element $u \in F$ is a *supremum* or *least upper bound* of $S$ if $u$ is an upper bound of $S$, and given any other upper bound $v$, then $u < v$

**Definition**. Given field $F$ and nonempty subset $S \subseteq F$, an element $u \in F$ is an *infimum* or *greatest lower bound* of $S$ if $u$ is a lower bound of $S$, and given any other lower bound $v$, then $u > v$

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

1. $\abs{x = r}$ if and only if $x = r$ or $x = -r$
2. $\abs{x < r}$ if and only if $-r < x < r$
3. $\abs{x > r}$ if either $x > r$ or $x < -r$

---

**Definition**. The *standard distance function* or *metric* on the real numbers $\mathbb{R}$ given $a, b$ is $\abs{a - b}$.

**Theorem**. For any real numbers $a, b, c$,

1. $\abs{a - b} > 0$ if and only if $a \neq b$ and $\abs{a - b} = 0$ if and only if $a = b$
2. $\abs{a - b} = \abs{b - a}$
3. $\abs{a - c} \leq \abs{a - b} + \abs{b + c}$

**Definition** A set together with a function satisfying these three properties is known as a *metric space*.

**Definition** The $\epsilon$-neighborhood of $a \in \mathbb{R}$, denoted $V_\epsilon(a)$ is the set of all real numbers $x \in \mathbb{R}$ such that $\abs{x - a} < \epsilon$. That is,

$$
V_\epsilon(a) = (a - \epsilon, a + \epsilon)
$$

---

**Decimals**. Let $x \in \mathbb{R}$ such that $x > 0$. By the archimedian property, there exists some $b_0 \in \mathbb{N} \cup {0}$ such that $b_0 < x < b_0 + 1$. We can repeat this to see

$$
x = b_0 + \frac{b_1}{10} + \frac{b_2}{100} + \ldots + \frac{b_n}{100^n} + \ldots
$$

**Definition**. The *decimal expansion* of $x$ is denoted $b_0.b_1 b_2 b_3 \ldots$.

## Section 2.5 - Intervals

**Definition**. A subset $I$ is an *interval* if and only if, given $a, b \in I$, then $[a, b] \subseteq I$.

**Definition**. Intervals $I_1, I_2, \ldots, I_n, \ldots$ are *nested* if and only if $I_1 \subseteq I_2 \subseteq \ldots \subseteq I_n \subseteq \ldots$.

**Theorem**. Nested Intervals Property. If $I_n = [a_n, b_n]$ is a set of nested intervals that are closed and bound, then there exists some number $z \in \mathbb{R}$ such that $z \in I_n$ for all $n$.

**Theorem**. If $a < b$, then the interval $[a, b]$ is an uncountable set.

**Collary**. $\mathbb{R}$ is uncountable.
