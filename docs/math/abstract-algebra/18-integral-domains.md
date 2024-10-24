# Chapter 18 - Integral Domains

## Section 18.1 - Fields of Fractions

**Definition**. Given an integral domain $D$, we can construct a field $F$ containing $D$ by stating that any $p/q \in F$, annd that any two elements $a/b = c/d$ if and only if $ad = bc$. We can consider this akin o a set of ordered pairs

$$
S = \{(a, b) : a, b \in D \text{ and } b \neq 0 \}
$$

**Lemma**. 18.1: The relation $(a, b) ~ (c, d) \text{ if } ad = bc$ is an equivalence relation.

**Lemma**. 18.2: The operations of addition and multiplication on $F$ are well-defined.

**Lemma**. 18.3: The set of equivalence classes of $S, F$ under $~$ form a field.

**Theorem**. 18.4: Let $D$ be an integral domain. Then, $D$ can be embedded in a field of fractions $F_D$ where any element in $F_D$ can be expressed as the quotient of two elements in $D$.

Additionally, $F_D$ is unique. That is, given field $E$ such that $E \supset D$, there exists a map $\psi: F_D \rightarrow D$ giving an isomorphism such that $\psi(a) = a$ for all $a \in D$.

**Collary**. 18.6: Let $F$ be a field of charactaristic $0$. Then, $F$ contains a subfield isomorphic to $\mathbb{Q}$.

**Collary**. 18.6: Let $F$ be a field of charactaristic $p$. Then, $F$ contains a subfield isomorphic to $\mathbb{Z}_p$.

## Section 18.2 - Factorization in Integral Domains

**Definition**. Let $R$ be a commutative ring with identity, and $a, b \in R$. We say that $a$ *divideds* $b$, that is, $a | b$, if there exists some $c \in R$ such that $b = ac$.

**Definition**. A *unit* element is any element that has a multiplicative inverse.

**Definition**. Two elements $a, b \in R$ are said to be *associates* if there exists some unit $u \in R$ such that $a = ub$.

**Definition**. Let $D$ be an integral domain. A nonzero element $p \in D$ is said to be *irreducible* if when given $p = ab$, either $a$ or $b$ is a unit.

**Definition**. Let $D$ be an integral domain. A nonzero element $p$ is *prime* if when given $p = ab$, either $p | a$ or $p | b$.

**Definition**. Given integral domain $D$, we say that $D$ is a *Unique Factorization Domain (UFD)* if it satisfies the following criteria:

1. Given $a \in D, a \neq 0$, and $a$ is not a unit, $a$ can be written as a product of irreducible elements in $D$.
2. Let $a = p_1 \ldots p_r = q_1 \ldots q_s$, where $p_i$ and $q_i$ are all irreducible. Then, $r = s$, and there exists some fuction $\pi \in S_r$ such that $p_i$ and $q_{\pi(j)}$ are associates for $j = 1, \ldots, r$.

**Definition**. A ring $R$ is a *principal ideal domain (PID)* if every ideal of $R$ is principal.

**Lemma**. 18.11: Let $D$ be an integral domain and $a, b \in D$. Then,

1. $a | b$ if and only if $\langle b \rangle \subseteq \langle a \rangle$
2. $a$ and $b$ are associates if and only if $\langle b \rangle = \langle a \rangle$
3. $a$ is a unit in $D$ if and only if $\langle a \rangle = D$.

**Theorem**. 18.12: Let $D$ be a PID, and let $\langle p \rangle$ be a nonzero ideal in $D$. Thus, $\langle p \rangle$ is a maximal ideal if and only if $p$ is irreducible.

**Collary**. 18.13: Let $D$ be a PID. For any $p \in D$, if $p$ is irreducible, then $p$ is prime.

**Lemma**. 18.14: Let $D$ be a PID. Let $I_1 \subseteq I_2 \subseteq \ldots$. Then, there exists some integer $N$ such that $I_n = I_N$ for all $n > N$. That is, any chain of ideals converges.

**Definition**. Any commutative ring that satisfies the above condition (the *ascending chain condition*), even if it's not a PID, is called a *Noetherien ring*.

**Theorem**. 18.15: Every PID is a UFD. Note that the converse is not true.

**Collary** 18.16: Let $F$ be a field. Then, $F[x]$ is a UFD.

---

**Definition**. Any integral domain $D$ is a *euclidian domain* with a *euclidian function* $nu: D \\ \{0\} \rightarrow \mathbb{N}$ that satisfies the following:

1. Given $a, b \neq 0$, then $\nu(a) \leq \nu(ab)$.
2. Given, $a, b \in D$ and $b \neq 0$, there exists some $q, r \in D$ such that $a = bq + r$ and either $r = 0$ or $\nu(r) < \nu(b)$.

**Example**. Absolute value on $\mathbb{Z}$ is a Euclidian validation.

**Example**. Degree on $F[x]$ is a Euclidian validation.

**Example**. $\nu(a + bi) = a^2 + b^2$ is a Euclidian validation over $\mathbb{Z}[i]$.

**Theorem**. 18.21: Every Euclidian domain is a PID.

**Collary**. Every Euclidian domain is a UFD.

---

**Definition**. Given a polynomial $p(x) \in D$, with $D$ bein an integer domain, we say that the *content* of $p(x)$ is the greatest common divisor of its coefficients. Additionally, if the content is $1$, we say that $p(x)$ is *primitive*.

**Theorem**. 18.24: Let $D$ be a UFD, and $f(x), g(x) \in D[x]$ be primitive. Then, $f(x)g(x)$ is primitive.

**Lemma**. 18.25: Given $D$ is a UFD, and $p(x), q(x) \in D[x]$, the content of $p(x)q(x)$ is equal to the product of the contents of the individual polynomials

**Lemma**. 18.26: Let $D$ be a UFD and $F = F_D$ be its field of fractions. Given $p(x) \in D[x]$, and $p(x) = f(x)g(x)$ with $f(x), g(x) \in F_D$, we can say that $p(x) = f_1(x)g_1(x)$ with $f_1(x), g_1(x) \in D$. Additionally, $\deg f_1(x) = \deg f(x)$ and $\deg g_1(x) = \deg g(x)$.

As a direct consequence, we see the following.

**Collary**. Let $D$ be a UFD, and $F = F_D$. Then, a primitive polynomial $p(x) \in D[x]$ is irreducible in $D[x]$ if and only if it is irreducible in $F[x]$.

**Collary**. Let $D$ be a UDF, and $F = F_D$. Then, if a monic polynomial $p(x) \ in D[x]$ can be written as $p(x) = f(x)g(x)$ with $f(x), g(x) \in F_D[x]$, then $p(x)$ can be written as $p(x) = f_1(x)g_1(x)$, where $f_1(x), g_1(x) \in D[x]$.

**Theorem**. If $D$ is as UFD, then $D[x]$ is a UFD.

**Collary**. This theorem has several collaries:

1. Given a field $F$, since $F$ is a PID, it is also a UFD. Thus, $F[x]$ is a UFD.
2. The ring of polynomials over integers, $\mathbb{Z}[x]$ is a UFD.
3. Given $D$ is a UFD, $D[x]$ is a UFD. Thus, $D[x_1, x_2]$ is a UFD, and by induction, $D[x_1, \ldots, x_n]$ is a UFD.
