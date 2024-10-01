# Chapter 16 - Rings
## Section 16.1 - Rings

**Definition**. A nonempty set $S$ is a *ring* if, with two binary operations called addition and multipllication, the following are satisfied:

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

## Section 16.2 - Integral Domains and Fields

**Definition**. If $R$ is a commutative ring and $r \in R$, then $r$ is said to be a *zero divisor* if there is some nonzero $s \in R$ such that $rs = 0$.

**Definition**. A commutative ring with no zero divisors is called an *integral domain*.

**Example**. Consider the set $\mathbb{Z}[i] = \{m + ni | m, n \in \mathbb{Z}\}$. This ring is called the *Gaussian integers*. Prove that the Gaussian integers are not a field, and are an integral domain.

**Example**. Proposition 16.15: Cancellation law. Let $D$ be a commutative ring with identity. Then, $D$ is an integral domain if and only if for every nonzero $a \in R$, $ab = ac$ implies $b = c$.

**Theorem**. 16.16: Every finite integral domain is a field.

**Definition**. For any non-negative integer $n \in \mathbb{N}$ and $r \in R$, we say that $nr = r + ... + r \text{(n times)}$.

**Definition**. The *charactaristic* of a ring is the leat possible $n \in \mathbb{N}$ such that $nr = 0$ for all $r \in R$.

**Example**. For every prime number $p$, $\mathbb{N}_p$ is a field of charactaristic $p$.

**Lemma**. 16.18: Given $R$ is a ring with identity, the charactaristic of $1$ is the charactartistic of the field.

**Theorem**. 16.19: The charactaristic of an integral domain is prime or zero.

## Section 16.3 - Ring Homomorphisms and Ideals

**Definition** Given rins $R$ and $S$, and a mapping $\phi: R \leftarrow S$, we say that $\phi$ is a *ring homomorphism* if the following are satisfied for all elements of $R$:

$$
\begin{align}
    \phi(a + b) &= \phi(a) + \phi(b) \\
    \phi(ab) &= \phi(a) \phi(b)
\end{align}
$$

**Definition**. If $\phi$ is one-to-one and onto, it is an *isomorphism*.

**Definition**. For any ring homomorphism $\phi$, the *kernel* of $\phi$ is the set

$$
\ker \phi = \{ r \in R | \phi(r) = 0 \}
$$

**Definition**. Proposition 16.22: Let $\phi: R \leftarrow S$ be a ring homomorphism. Then,

1. If $R$ is a commutative ring, then $\phi(R) \subset S$ is a commutative ring.
2. $\phi(0_R) = 0_S$
3. Let $1_R$ and $1_S$ be the identities in $R$ and $S$. If $\phi$ is onto, then $\phi(1_R) = 1_S$
4. If $R$ is a field an $\phi(R) \neq \{0\}$, then $\phi(R) \subset S$ is a field.

**Definition**. A subring $I \subset R$ is asn *ideal* of $R$ if, when given $a \in I, r \in R$, then $ar$ and $ra$ are both in $I$. That is, $rI \subset I$ and $Ir \subset I$.

**Definition**. Given a commutative ring $R$ with identity, and $r \in R$, the set

$$
<a> = (r)R = \{ ar : r \in R \}
$$

is an ideal in $R$. Specifically, $<a>$ is a *principal ideal*.

**Example**. Theorem 16.25. Every ideal in $\mathbb{Z}$ is a principal ideal.

**Examplee**. With $\phi: R \leftarrow S$, $\ker \phi$ is an ideal of $R$.

**Remark**. 16.28: We are working with *two-sided ideals*. If rings are not commutative, we may deal with *left ideals* and *right ideals*.

**Theorem**. 16.29: Let  $I$ be an ideal of $R$. Then, the factor/quotient ring $R/I$ is a ring with multiplication defined by

$$
(r + I)(s + I) = rs + I
$$

**Theorem**. 16.30: Let $I$ be an ideal of $R$. Then, the map $\phi: R \leftarrow R/I$ defined by $\phi(r) = r + I$ is a ring homomorphism of $R$ onto $R/I$ with $\ker \phi = I$.

**Theorem**. 16.31, *First Isomorphism Theorem*. Let $\psi: R \leftarrow S$. Then, $\ker \psi$ is an ideal of $R$. Consider the isomorphism $\phi: R \leftarrow R/\ker \psi$. There exists an isomorphism $\eta: R / \ker \psi \leftarrow \psi(R)$ such that $\psi = \eta \phi$.

**Theorem**. 16.32, *Second Isomorphism Theorem*. Let $I$ be a subring of $R$ and $J$ be an ideal of $R$. Then, $I \union J$ is an ideal of $I$ and

$$
I/I \union J \congruent (I + J) / J
$$

**Theorem**. 16.33, *Third Isomorphism Theorem*. Let $R$ be a ring and $I, J$ be ideals of J. If $J \subsetneq I$, then

$$
R/I \\congruent \frac{R/J}{I/J}
$$

**Theorem**. 16.34, *Correspondence Theorem*. Let $I$ be an ideal of $R$. Then, $S \mapsto S/I$ is a one-to-one correspeondence between the set of subrings $S$ containing $I$ (that is, $I \in S$) and the set of subrings of $R/I$. Furthermore, the ideals of $R$ containing $I$ correspond to the ideals of $R/I$.