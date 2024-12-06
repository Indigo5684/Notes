# Chapter 12 - Modules over Principal Ideal Domains

## Section 12.1 The Basic Theory

**Definition**. The left $R$-module $M$ is said to be a *Noetherian* $R$-module if there are no infinitely increasing chains of submodules. That is, given

$$
M_1 \subseteq M_2 \subseteq \ldots
$$

there exists some $k \in \mathbb{N}$ such thaht given any $n \in \mathbb{N}$ with $n \geq k$, then $M_n = M_k$.

**Definition**. A ring $R$ is *Noetherian* if it is Noetherian when viewed as a left $R$-module over itself.

**Theorem**. Let $R$ be a ring and $M$ a left $R$-module. Then, the following are equivalent:

1. $M$ is Noetherian
2. Every nonempty set of submodules of $M$ contains a maximal element under inclusion
3. Every submodule of $M$ is finitely-generated

**Corollary**. If $R$ is a principal ideal domain (PID), then all nonempty set of ideals of $R$ has a maximal element. Additionally, $R$ is as Noetherian ring.

**Proposition**. Let $R$ be an integral doman, and $M$ be a free $R$-module of rank $n < \infty$. Then, given $S$ is subset $M$ with $|S| > n$, the elements of $S$ are $R$-linearly dependent.

**Definition**. Given $R$ an integral domain and $M$ an $R$-module,

$$
\Tor(M) = \{ x \in M | rx = 0 \text{ for any } r \neq 0 \}
$$

This is the *torsion submodule* of $M$. If $\Tor(M)$ is empty, then $M$ is *torsion-free*.

**Definition** Let $R$ be an integral domain and $M$ be an $R$-module. Then, given a submodule $N$,

$$
\Ann_R(N) = \{r \in R | rn = 0 \text{ for all } n \in N \}
$$

This ideal of $R$ is the *annihilator of $N$*. That is, $\Ann(N)$ is the set of elements of $R$ such that $(r)N = \{ 0 \}$.

Note that if $N$ is not a torsion submodule of $M$, then $\Ann(N) = (0)R$. Additionally, given $N, L$ are submodules of $M$ with $N \subseteq L$, then $\Ann(N) \subseteq \Ann(L)$.

Additionally, if $R$ is a PID, as $\Ann_R(N)$ is an ideal, $\Ann(N) = (n)R$ and $\Ann(L) = (l)R$ for some $n, l \in R$ such that $n | l$.

**Definition**. Given any integral domain $R$, the *rank* of an $R$-module $M$ is the maximum number of $R$-linearly independent elements of M.

**Corollary**. The rank of a free module is the number of generating elements.

**Theorem**. Let $R$ be a principal ideal domain, and $M$ be a free $R$-module of finite rank $m$, and $N$ be a submodule of $M$. Then,

1. $N$ is a free submodule with rank $n \leq m$.
2. There exiss a basis $y_1, y_2, \ldots, y_m$ of $M$ so that $r_1 y_1, r_2 y_2, \ldots, r_m y_n$ is a basis of $N$ for some $r_i \in R$ and $r_1 | r_2 | \ldots | r_n$

