# Chapter 17 - Polynomial Rings

## Section 17.1 - Polynomial Rings

Throughout this chapter, we will assume that $R$ is a commutative ring with identity.

**Definition**. Any expression of the form

$$
f(x) = \sum_{i=0}^n a_i x^i = a_0 + a_1x + a_2x^2 + \ldots + a_n x^n
$$

where $a_i \in R$ and $a_n \neq 0$ is called a *polynomial over $R$* with *indeterminate* $x$. The elements $a_0, a_1, \ldots, a_n$ are the *coefficients* of $f$. The coefficient $a_n$ is the *leading coefficient*.

**Definition**. A polynomial is known as *monic* if the leading coefficient is equal to $1$.

**Definition**. The *degree* of $f$ is the largest nonnegative number such that $a_n \neq 0$, written as $\deg f(x) = n$. If no such mumber exists, that is, $f(x) = 0$, we say the degree of $f$ is $-\infty%.

**Definition**. We denote the set of all polynomials with coefficients in $R$ as $R[x]$.

Two polynomials are equal if and only if their corresponding coefficients are equal. When combined with standard addition and multiplication, $R[x]$ forms a ring.

**Theorem**. If $R$ is commutative and has identity, so does $R[x]$.

**Definition**. The *ring of polynomials with $n$ indeterminates and coefficients in $R$* is defined as $R[x_1][x_2][\ldots][x_n] = R[x_1, x_2, \ldots, x_n]$.

**Definition**. The *evaluation homomorphism* is the homomorphism $\varphi: R[x] \rightarrow R$ defined as $\varphi(p(x)) = p(\alpha)$ for some $\alpha \in R$.

## Section 17.2 - The Division Algorithm

**Theorem**. Given $f(x), g(x) \in F[x]$, where $F$ is a field and $g(x) \neq 0$, there exist unique polynomials $q(x), r(x) \in F[x]$ such that

$$
f(x) = g(x)q(x) + r(x)
$$

where either $\deg r(x) < \deg g(x)$ or $r(x)$ is the zero polynomial.

**Corollary**. Let $F$ be a field. Then, an element $\alpha \in F$ is a zero of $p(x) \ in F[x]$ if and only if $(x-\alpha)$ is a factor of $p(x)$.

**Corollary**. Let $F$ be a field. Then, a nonzero polynomial $p(x) \in F[x]$ with degree $n$ can have at most $n$ distinct zeros in $F$.

**Definition**. A monic polynomial $d(x)$ is the *greatest common divisor* of polynomials $p(x), q(x) \in F[x]$ if $d(x)$ evenly divides both $p(x)$ and $q(x)$. We write $\gcd(p(x), q(x)) = d(x)$. This polynomial is unique.

**Definition**. Two polynomials are *relatively prime* if their greatest common divisor is $1$.

## Section 17.3 Irreducible Polynomials

**Definition** A nonconstant polynomial $f(x) \ in F[x]$ is *irreducible* over a field $F$ if it cannot be expressed as the product of two non-identity polynomials $g(x)$ and $h(x)$ in $F[x]$, with the degree of both polynomials strictly less than the  degree of $f(x)$.

**Lemma**. Let $p(x) \in \mathbb{Q}[x]$. Then, with $r, s \in \mathbb{Z}, a(x) \in \mathbb{N}[x]$, we can write $p(x) = \frac{r}{s} a(x)$.

**Lemma**. Gauss's Lemma. Let $p(x) \in \mathbb{Z}[x]$ be monic such that $p(x)$ factors into two polynomials $\alpha(x), \beta{x} \in \mathbb{Q}[x]$, with the degrees of both strictly less than the degree of $p(x)$. Then, there exists two polynomials $a(x), b(x) \in \mathbb{Z}[x]$ such that $p(x) = a(x)b(x)$, and $\deg \alpha(x) = \deg a(x)$ and $\deg \beta(x) = \deg b(x)$.

**Corollary**. Let $p(x) \in \mathbb{Z}[x]$ be monic with constant term $a_0$. Then, if $p(x)$ has a zero in $\mathbb{Q}$, then it also has a zero $\alpha$ in $\mathbb[Z]$. Furthermore, $\alpha$ divides $a_0$.

**Theorem**. Eisenstein's Criterion. Let $p$ be prime, and suppose that

$$
f(x) = a_n x^n + \ldots + a_0 \in \mathbb{Z}[x]
$$

Then, if $p | a_i$ for $0 \leq i < n$, but $p \nmid a_n$ and $p^2 \nmid a_0$, then $f(x)$ is irreducible over $\mathbb{Q}[x]$.

**Theorem**. If $F$ is a field, then every ideal in $F[x]$ is a principal ideal.

**Theorem**. Let $F$ be a field, and suppose $p(x) \in F[x]$. Then, the ideal $<p(x)>$ is maximal if and only if $p(x)$ is irreducible.
