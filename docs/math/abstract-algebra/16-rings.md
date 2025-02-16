# Chapter 16 - Rings

## Section 16.1 - Rings

**Definition**. A nonempty set $S$ is a *ring* if, with two binary operations called addition and multiplication, the following are satisfied:

1. Addition is commutative. $a + b = b + a$ for $a, b \in R$
2. Addition is associative. $(a + b) + c = a + (b + c)$ for $a, b, c \in R$
3. There exists a zero-element $0_R$ in $R$ such that $a + 0 = a$ for all $a \in $
4. Every element $a$ has an additive inverse $-a \in R$ such that $a + (-a) = 0_R$
5. Multiplication is associative. That is, $a(bc) = (ab)c$ for $a, b, c \in R$
6. The Distributive Property holds. That is, $\forall a, b, c \in R,$

$$
a(b+c) = ab+bc \\
(a+b)c = ac + bc
$$

**Definition**. If there exists some element $1_R \in R$ such that $1a = a1 = a$ for all $a \in R$, we say that $R$ is a ring with *unity* or *identity*.

Note that some books impose the condition that $1 \neq 0$. If $1 = 0$, we can show the ring only has one element.

**Definition**. If $ab = ba$ for all $a, b \in R$, the ring is said to be a *commutative ring*.

**Definition**. If a ring $R$ is commutative, $R$ is an *integral domain* if and only if for every $a, b \in R$, $ab = 0$ implies that either $a = 0$ or $b = 0$.

**Definition**. An element $a \in R$ is called a *unit* if there exists some $a^{-1}$ such that $a a^{-1} = a^{-1} a = 1$.

**Definition**. A ring $R$ with identity is called a *division ring* if every nonzero element in $R$ is a unit.

**Definition**. A commutative division ring is called a *field*. That is, in a field, every element has an inverse.

**Definition**. A subset $S$ of ring $R$ is a *subring* if given any $r, s \in S$, then $rs \in S$ and $r - s \in S$.

## Section 16.2 - Integral Domains and Fields

**Definition**. If $R$ is a commutative ring and $r \in R$, then $r$ is said to be a *zero divisor* if there is some nonzero $s \in R$ such that $rs = 0$.

**Definition**. A commutative ring with no zero divisors is called an *integral domain*.

**Example**. Consider the set $\mathbb{Z}[i] = \{m + ni | m, n \in \mathbb{Z}\}$. This ring is called the *Gaussian integers*. Prove that the Gaussian integers are not a field, and are an integral domain.

**Example**. Proposition 16.15: Cancellation law. Let $D$ be a commutative ring with identity. Then, $D$ is an integral domain if and only if for every nonzero $a \in R$, $ab = ac$ implies $b = c$.

**Theorem**. 16.16: Every finite integral domain is a field.

**Definition**. For any non-negative integer $n \in \mathbb{N}$ and $r \in R$, we say that $nr = r + \ldots + r \text{(n times)}$.

**Definition**. The *characteristic* of a ring is the least possible $n \in \mathbb{N}$ such that $nr = 0$ for all $r \in R$.

**Example**. For every prime number $p$, $\mathbb{N}_p$ is a field of characteristic $p$.

**Lemma**. 16.18: Given $R$ is a ring with identity, the characteristic of $1$ is the characteristic of the field.

**Theorem**. 16.19: The characteristic of an integral domain is prime or zero.

## Section 16.3 - Ring Homomorphisms and Ideals

**Definition**. Given rings $R$ and $S$, and a mapping $\varphi: R \rightarrow S$, we say that $\varphi$ is a *ring homomorphism* if the following are satisfied for all elements of $R$:

$$
\begin{align}
    \varphi(a + b) &= \varphi(a) + \varphi(b) \\
    \varphi(ab) &= \varphi(a) \varphi(b)
\end{align}
$$

**Definition**. If $\varphi$ is one-to-one and onto, it is an *isomorphism*.

**Definition**. For any ring homomorphism $\varphi$, the *kernel* of $\varphi$ is the set

$$
\ker \varphi = \{ r \in R | \varphi(r) = 0 \}
$$

**Definition**. Proposition 16.22: Let $\varphi: R \rightarrow S$ be a ring homomorphism. Then,

1. If $R$ is a commutative ring, then $\varphi(R) \subseteq S$ is a commutative ring.
2. $\varphi(0_R) = 0_S$
3. Let $1_R$ and $1_S$ be the identities in $R$ and $S$. If $\varphi$ is onto, then $\varphi(1_R) = 1_S$
4. If $R$ is a field an $\varphi(R) \neq \{0\}$, then $\varphi(R) \subseteq S$ is a field.

**Definition**. A subring $I \subseteq R$ is asn *ideal* of $R$ if, when given $a \in I, r \in R$, then $ar$ and $ra$ are both in $I$. That is, $rI \subseteq I$ and $Ir \subseteq I$.

**Definition**. Given a commutative ring $R$ with identity, and $r \in R$, the set

$$
\langle a \rangle = (r)R = \{ ar : r \in R \}
$$

is an ideal in $R$. Specifically, $\langle a \rangle$ is a *principal ideal*.

**Example**. Theorem 16.25. Every ideal in $\mathbb{Z}$ is a principal ideal.

**Example**. With $\varphi: R \rightarrow S$, $\ker \varphi$ is an ideal of $R$.

**Remark**. 16.28: We are working with *two-sided ideals*. If rings are not commutative, we may deal with *left ideals* and *right ideals*.

**Theorem**. 16.29: Let  $I$ be an ideal of $R$. Then, the factor/quotient ring $R/I$ is a ring with multiplication defined by

$$
(r + I)(s + I) = rs + I
$$

**Theorem**. 16.30: Let $I$ be an ideal of $R$. Then, the map $\varphi: R \rightarrow R/I$ defined by $\varphi(r) = r + I$ is a ring homomorphism of $R$ onto $R/I$ with $\ker \varphi = I$.

**Theorem**. 16.31, *First Isomorphism Theorem*. Let $\psi: R \rightarrow S$. Then, $\ker \psi$ is an ideal of $R$. Consider the isomorphism $\varphi: R \rightarrow R/\ker \psi$. There exists an isomorphism $\eta: R / \ker \psi \rightarrow \psi(R)$ such that $\psi = \eta \varphi$.

**Theorem**. 16.32, *Second Isomorphism Theorem*. Let $I$ be a subring of $R$ and $J$ be an ideal of $R$. Then, $I \cap J$ is an ideal of $I$ and

$$
I/I \cap J \cong (I + J) / J
$$

**Theorem**. 16.33, *Third Isomorphism Theorem*. Let $R$ be a ring and $I, J$ be ideals of J. If $J \subsetneq I$, then

$$
R/I \cong \frac{R/J}{I/J}
$$

**Theorem**. 16.34, *Correspondence Theorem*. Let $I$ be an ideal of $R$. Then, $S \mapsto S/I$ is a one-to-one correspondence between the set of subrings $S$ containing $I$ (that is, $I \in S$) and the set of subrings of $R/I$. Furthermore, the ideals of $R$ containing $I$ correspond to the ideals of $R/I$.

## Section 16.4 - Maximal and Prime Ideals

**Definition**. Consider ring $R$ and proper ideal $M \subseteq R$. Then, $M$ is a *maximal ideal* of $R$ if the ideal $M$ is not a subset of any ideal except $R$ itself. That is, given any ideal $I$ properly containing $M$, $I = R$.

**Theorem**. 16.35: Given a commutative ring with identity $R$, $M$ is a maximal ideal if and only if $R/M$ is a field.

**Definition**. Consider ring $R$ and proper ideal $P \subseteq R$. Then, $P$ is a *prime ideal* if given $ab \in P$, either $a \in P$ or $b \in P$.

**Theorem**. 16.38: Let $R$ be a commutative ring with identity $1$. Then, $P \subseteq R$ is a prime ideal of $R$ if and only if $R/P$ is a field.

Let us assume that $P$ is an ideal in $R$ and $R/P$ is an integral domain. Take two elements $ab \in P$. Now, consider $a + P$ and $b + P$ in $R/P$ such that $(a+P)(b+P) = 0+P = P$. As $R/P$ is a field, either $a + P = 0 + P = P$ or $b + P = 0 + P = P$, meaning either $a \in P$ or $b \in P$. Thus, $P$ is as prime ideal.

Now, assume the opposite. Let $P$ be prime. Now, we want to show that $R/P$ is an integral domain.

Consider two elements $a + P$, $b + P$ in $R/P$. We know that

$$
(a + P)(b + P) = ab + P = 0 + P = P
$$

Thus, $ab \in P$. By symnetry, assume $a \notin P$. Thus, $b \in P$ by the definition of a prime ideal, so $b + P = 0 + P$, meaning $R/P$ is an integral domain.

**Theorem**. 16.40: In a commutative ring with identity, every maximal ideal is also a prime ideal.

## Section 16.5 - Applications to Computer Science

**Lemma**. Let $m, n \in \mathbb{B}$ be given. Then, for any $a, b \in \mathbb{Z}$, there exists some $x$ that satisfies

$$
\begin{align}
    x &\equiv a \pmod{m} \\
    x &\equiv b \pmod{n}
\end{align}
$$

**Theorem**. Chinese Remainder Theorem. Let $n_1, \ldots, n_k \in \mathbb{N}$ be given such that $\gcd(n_i, n_j) = 1$. Then, for any integers $a_1, \ldots, a_k$, the system

$$
\begin{align}
    x &\equiv a_1 \pmod{n_1} \\
    x &\equiv a_2 \pmod{n_2} \\
    \ldots
    x &\equiv a_k \pmod{n_k}
\end{align}
$$

has a solution. Additionally, all systems are congruent modulo $n_1 n_2 \ldots n_k$.
