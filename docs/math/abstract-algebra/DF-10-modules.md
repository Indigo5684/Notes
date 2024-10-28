# Dummit & Foote Chapter 10 - Modules

## Section 10.1 - Basic Definitions and Examples

**Definition**. Let $R$ be a ring. A *left $R$-module* or a *left module over $R$* is a nonempty set $M$ together with

1. A binary operation $+$ on $M$ under which $M$ is an abelian group
2. An action $\cross$ of $R$ on $M$, that is, a map or function $R \cross M \leftarrow M$, denoted $rm$, that for all $r, s \in R, m, n \in M$ satisfies
    - $(r + s)m = rm + sm$
    - $(rs)m = r(sm)$
    - $r(m + n) = rm + rn$
    - If $R$ has identity $1$, then $1m = m$

**Theorem**. If $R$ is commutative, any left-module is also a *right-module*.

**Remark**. Modules over a field $F$ and vector spaces over $F$ are identical.

**Definition** An *R-submodule* is a subset$N \subseteq M$ which is closed under the action taken forall $r \in R$. That is, given $r \in R, n \in N$, tthen $rn \in N$. Every module has at least two submodules: itself and the trivial (empty) submodule.

**Remark**. If $F$ is a field, submodules are equivilent to subspaces.

---

**Example**. Let $F$ be a field and $F[x]$ a polynomial ring. Then, let $V$ be a vector space of $F$, and $T$ be a linear transformaion from $V$ to itself. That is, $V: T \leftarrow T$. We know that $V$ is an $F$-module. We will want to show that $V$ can be written as an $F[x]$-module for some choice of $T$. That is, we want an action $F[x] \cross V \rightarrow V$.

Now, for a given linear transformation $T$, consider some polynomial $p(x) = a_n x^n + \ldots + a_0$ and some $v \in V$. We define $p(x) \cross v$ by$

$$
p(x) \cross v = a_n T^n(v) + a_{n-1} T^{n-1}(v) + \ldots + a_0 v
$$

with $T^n$ being defined as applying $T$ a total of $n$ times.

---

**Proposition**. Let $R$ be a ring and $M$ an $R$-module. Then, a subset $N$ of $M$ is a submodule of $M$ if and only if

1. $N \neq \emptyset$
2. For all $r \in R$, $x, y \in N$, then $rx - y \in N$

**Definition**. Let $R$ be a commutative ring with identity. An $R$-algebra is a ring $A$ together with a ring homomorphism $f: R \rightarrow A$ such that $\varphi(1_R) = 1_A$. Thus, the subring $f(R) \subseteq A$ is contained in the center of $A$.

**Recall**. The center of a ring $A$ is the subring $A'$ such that for all $x, y \in R'$, then $xy = yx$. In other words, it is the commutative subring of $A$.

**Definition**. Given two $R$-algebras $A, B$, an *$R$-algebra homomorphhism$ is a ring homomorphism $\varphi: A \rightarrow B$ that maps $1_A \rightarrow 1_B$ such that $\varphi(ra) = r\varphi(a)$.

## Section 10.2 - Quotient Modules and Module Homomorphisms

**Definition**. Let $R$ be a ring and $M, N$ be $R$-modules. then a ring homomorphhism $\varphi: M \rightarrow N$ is an *$R$-module homomorphism* if for all $r \in R$, $\varphi(rx) = r\varphi(x)$.

**Theorem**. An $R$-module homomorphism is an *isomorphism* if it is 1-1 and onto, and said modules are *isomorphic*.

**Definition**. Let $M, N$ be $R$-modules. The set $\Hom_R(M, N)$ is the set of all homomorphisms from $M$ to $N$.

**Promposition**. Let $M$, $N$, and $L$ be $R$-modules. Then,

1. A function $\varphi: M \rightarrow N$ is an $R$-module homomorphism if and only if $\varphi(rx + y) = r\varphi(x) + \varphi(y)$ for all $x, y \in M$ and $r \in R$.
2. Let $\varphi, \psi \in \Hom_R(M, N)$. Then, define $\varphi + \psi$ as

$$
(\varphi + \psi)(m) = \varphi(m) + \psi(m)
$$

Then, $\varphi + \psi \in \Hom_R(M, N)$. Additionally, if $R$ is commutative, with $(r\varphi)(m) = r(\varphi(m))$, then $r\varphi \in \Hom_R(M,N)$
3. If $\varphi \in \Hom_R(L, M)$ and $\psi \in \Hom_R(M, N)$, then $\psi \circ \varphi \in \Hom_R(L, N)$
4. $\Hom_R(M, M)$ is a ring with identity. With $R$ being commutative, $\Hom_R(M, M)$ is an $R$-algebra.

**Proposition**. Let $R$ be a ring, $M$ an $R$-module, and $N \subseteq M$ an $R$-submodule. then, $M/N$ can be made into an $R$-module by defining addition. With $r \in R$ and $x + N \in M/N$,

$$
r(x + N) = (rx) + N
$$

That is,

$$
r \overline{x} = \overline{rx}
$$

**Definition**. Let $A, B$ be submodules  of the $R$-module $M$. Then, the *sum* of $A$ and $B$ is defined as

$$
A + B = {a + b | a \in A, b \in B}
$$

This is the smallest submodule that contains both $A$ and $B$.

**Theorem**. First Isomorphism Theorem. Let $M, N$ be $R$-modules, and $\varphi: M \rightarrow N$ be an $R$-module homomorphhiism. Then, $\ker \varphi$ is a submodule of $M$, and $M / \ker \varphi \cong \varphi(M)$.

**Theorem**. Second Isomorphism Theorem. Let $A, B$ be submodules of the $R$-module $M$. Then, $(A + B)/B \cong A/(A \cap B)$.

**Theorem**. Third Isomorphism Theorem. Let $M$ be an $R$-module, and $A \subseteq B$ be submodules of $M$. Then, $\frac{M/A}{B/A} \cong M/B$.

**Theorem**. Lattice Isomorphism Theorem. Let $N$ be a submodule of the $R$-module $M$. Then, there is a bijection between submoudles of $M$ containing $N$ and submodules of $M/N$. This is given by $A \leftrightarrow A/N$, for $A \supseteq N$.

## Section 10.3 - Generation of Modules, Direct Sums, and Free Modules

**Definition**. Let $M$ be an $R$-module and $N_1, \ldots, N_n$ be submodules of $M$.

1. The *sum* of $N_1, \ldots, N_n$ is the set of all finite sums of elements from the sets $N_i$. That is, $N_1, \ldots, N_n := \{a_1 + a_2 + \ldots + a_n | a_i \in N_i\}$
2. For a ny subset $A$ of $M$, let $RA = \{r_1 a_1 + r_2 a_2 + \ldots + r_m a_m | r_i \in R, a_i \in A\}$. If $N$ is a submodule of $M$ such that $N = RA$, then $A$ is called the *generating set* for $N$.
3. A submodule $N$ of $M$ is *finitely generaated* if there is some finite subset $A$ of $M$ such that $N = RA$. That is, $N$ is generated by some finite subset.
4. A submodule of $M$ (up to equality) is $cyclic$ if there exists some element $a \in M$ such that $N = Ra = \{ra | r \in R\}$.

**Definition**. Let $M_1, \ldots, M_k$ be a collection of $R$-modules. Then, the *drirect product* is defined as

$$
M_1 \otimes \ldots M_k = (m_1, \ldots, m_k), m_i \in M_i
$$

This direct product is in itself an $R$-module.

**Proposition**. Let $N_1, \ldots, N_n$ be submodules of the $R$-module $M$. Then, the following are equivalent:

1. The map $\pi: N_1 \otimes \ldots \otimes N_k \leftarrow N_1 + \ldots + N_k$ defined by $\pi(a_1, \ldots, a_n) = a_1 + \ldots + a_n$ is an isomorphism
2. $N_j \cup (N+1 + \ldots + N_{j-1} + N{j+1} + \ldots + N_n) = 0 $ for all $j \in \{1, 2, \ldots, k\}$
3. Every $x \in N_1 + \ldots + N_n$ can be written uniquely in the form $a_1 + \ldots + a_n$, with $a_i \in N_i$

**Definition**. An $R$-module $F$ is said to be *free* on the subset $A$ of $F$ if for every nonzero $x \in F$, there exists nonzero elements $r_1, \ldots, r_n$ of $R$ and unique $a_1, \ldots, a_n$ such that $x = r_1 a_1 + \ldots + r_n a_n$ for some $n \in \mathbb{Z}^+$. That is, $A$ is a *basis* or *set of free generators* of $F$.

**Theorem**. For any set $A$, there is a free $R$-module $F(A)$ on $A$ such that $F(A)$ satisfies the universal property: if $M$ is any $R$-module, and $\varphi: A \rightarrow M$ is a map of sets, there eixts a unique $R$-module homomorphism: $\Phi: F(A) \rightarrow M$ such that $\Phi(a) = \varphi(a)$ for all $a \in A$.

**Collary**. If $F_1$ and $F_2$ are free modules on $A$, then there is a unique isomorphism between $F_1$ and $F_2$, which is the identity map on A.

**Collary**. If $F$ is a free $R$-module with basis $A$, then $F \cong F(A)$.

**Definition** For a free module $F$ with basis $A$, if $R$ is commutative, tthen the *rank* of $F$ is the cardinality of $A$.

## Section 10.4 - Tensor Products of Modules

Skipped

## Section 10.5 - Exact Sequences - Projective, Injective, and Flat Modules

Skipped