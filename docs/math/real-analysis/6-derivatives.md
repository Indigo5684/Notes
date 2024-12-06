# Chapter 6 - Derivatives

## Section 6.1 - The Derivative

**Definition**. Let $I \subseteq \mathbb{R}$ be an interval $f: I \rightarrow \mathbb{R}$ a function, and $c \in I$. Then, the *derivative of $f$ at $c$* is

$$
f'(c) = \lim_{x \rightarrow c} \frac{f(x)-f(c)}{x-c}
$$

provided that the limit exists. Thus, we obtain $f'(x)$, or the *derivative of $f$*, with a domain of all points $c \in I$ where the limit exists.

**Theorem**. If $f: I \rightarrow \mathbb{R}$ is differentiable at point $c$, it is continuous at point $c$.

**Theorem**. Let $f, g: I \rightarrow \mathbb{R}$ be differentiable at $c \in I$. Then,

- $(f+g)'(c) = f'(c) + g'(c)$
- $(fg)'(c) = f'(c)g(c) + f(c)g'(c)$
- $(\frac{f}{g})'(c) = \frac{f'(c)g(c) - f(c)g'(c)}{(g(c))^2}$

**Theorem**. Let $f: I \rightarrow \mathbb{R}$ and $g: J \rightarrow \mathbb{R}$, with $f(I) \subseteq J$. Then, if $f$ is differentiable at $c \in I$ and $g$ is differentiable att $f(c) \in J$, then $f \circ g$ is differentiable at $c$, and

$$
(g \circ f)'(c) = g'(f(c))f'(c)
$$

**Theorem**. Suppose $f: I \rightarrow \mathbb{R}$ is a one-to-one function on some interval $I$. Then, with $J = f(I)$ and $f^{-1}: J \rightarrow \mathbb{R}$, for all $x \in I$,

$$
f^{-1}(f(x)) = x
$$

**Lemma**. $f$ is continuous on some interval $I$ if and only if it is monotonic on said interval.

**Theorem**. Suppose $f: I \rightarrow \mathbb{R}$ is a one-to-one function on some interval $I$. Then, with $J = f(I)$ and $f^{-1}: J \rightarrow \mathbb{R}$, if $f$ is continuous on $I$ and $I$ is an interval, then $f(I)$ is an interval, and $f^{-1}$ is continuous on $J$.

**Theorem**. Suppose $f: I \rightarrow \mathbb{R}$ is differentiable at some $c \in I$. Then, with $J = f(I)$ and $f^{-1}: J \rightarrow \mathbb{R}$, if $f$ is differentiable at $c$ and $f'(c) \neq 0$, then $f^{-1}$ is differentiable at $d = f(c)$, and

$$
(f^{-1})(d) = \frac{1}{f'(c)}
$$

---

**Definition**. Let $I \subseteq \mathbb{R}$ be an interval and let $f: I \rightarrow \mathbb{R}$. Then, $f$ has a *relative maximum* (or *local maximum*) at some point $c \in I$ if there exists some $\delta$-neighborhood $V_\delta(c)$ such that for all $x \in V_\delta(C) \cup I$, then $f(x) \leq f(c)$. *Relative minima* are defined similarly.

**Theorem**. Let $I$ be an interval and $f: I \rightarrow \mathbb{R}$. Then, if $f$ has a relative extremum at an *interior point* $c \in I$, and if $f'(c)$ exists, then $f'(c) = 0$.

**Corollary**. Suppose $f: [a, b] \rightarrow \mathbb{R}$ and $g: [a, b] \rightarrow \mathbb{R}$ are both continuous on $[a, b]$ and differentiable on $(a, b)$ with $a \neq b$. Then,

- Rolle's Theorem. If $f(a) = f(b)$, then there exists at least one point $c \in (a, b)$ with $f'(c) = 0$.
- If $f(a) = g(a)$ and $f(b) = g(b)$, then there exists aat least one point $c \in (a, b)$ such that $f'(c) = g'(c)$.

**Theorem**. Mean Value Theorem. Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$, with $a \neq b$. Then, there exists at least one $c \in (a, b)$ with

$$
f(b) - f(a) = f'(c)(b - a)
$$

**Theorem**. Suppose $f: I \rightarrow \mathbb{R}$ is differentiable on I. Then,

- If $f'(x) > 0$ for all $x \in $I, then $f$ is strictly increasing on $I$.
- If $f'(x) = 0$ for all $x \in $I, then $f$ is constant on $I$.
- If $f'(x) <> 0$ for all $x \in $I, then $f$ is strictly decreasing on $I$.

**Theorem**. Cauchy Mean Value Theorem. Let $f, g$ be continuous on $[a, b]$ and differentiable on $(a, b)$. If $g'(x) \neq 0$ for all $x \in (a, b)$, and $a \neq b$, then there exists  at least one point $c \in (a, b)$ such that

$$
\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(c)}{g'(c)}
$$
