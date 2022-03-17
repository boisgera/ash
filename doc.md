% Asymptotic Stability for Humans
% Sébastien Boisgérault, MINES ParisTech, PSL University
% Wed 16 Mar 2022 19:39 GMT+1

## Motivation, Intro, references, didactic choices

TODO:

  - "classic" definitions, what is hard, what is (the most) important, 
    why we can/shall do better. Explain & advocate.

### System, IVP, maximal solutions, etc. {.definition}
🚧 TODO 🚧 

### Well-Posed System {.definition}
🚧 TODO 🚧 

(in the sequel, we assume that all systems are well-posed)

### Equilibrium {.definition}
🚧 TODO 🚧

### Attractivity {.definition}
🚧 TODO 🚧

### Attractivity {.definition}
🚧 TODO 🚧 

### Asymptotic Stability {.definition}
🚧 TODO 🚧 

🚧 TODO 🚧  Variants ? Global, with compact sets, etc. ? Yes: extension defs then 
reformulation with compactly included sets.

## Stability & Legacy Definitions

### Definition. Stability {.definition}
🚧 TODO 🚧 

--------------------------------------------------------------------------------

### Proposition. A. + S. $\Leftrightarrow$ A.S. {.proposition}
Attractivity + Stability $\Leftrightarrow$ Asymptotic Stability
🚧 TODO 🚧 

### {.proof}
🚧 TODO 🚧 


### Lemma. A.S. $\Rightarrow$ A.

### Proof. {.proof}
Obvious (by design).

### Lemma. A.S. $\Rightarrow$ S.

### Proof. {.proof}
Let $r_1 > 0$ be a radius such that the closed ball 
$$
B_1 := \{x \in \mathbb{R}^n \; | \; \|x - x_e\| \leq r_1 \}
$$ 
is included in $\mathrm{dom} \, f$.
Since is the system is asymptotically stable, there is a $\tau \geq 0$
such that for any $t \geq \tau$, we have $x(t, B) \subset B.$

Since the system is well-posed, there is a radius $r_2 > 0$ 
-- that we can select smaller or equal to $r_1$ -- such that for any
$x_0$ in the closed ball $B_2$ of radius $r_2$ centered on $x_e$ 
and any $t \in [0, \tau]$,
$$
\|x(x_0, t) - x_e\|  = \|x(x_0, t) - x(x_e, t) \| \leq r_1,
$$
which means that for any $t \in [0, \tau]$, $x(t, B_2) \subset B_1$.

Consequently, for any $t \in \left[0, \right[ = [0, \tau] \cup \left[\tau , +\infty\right[$,
we have $x(t, B_2) \subset B_1$ and the system is stable.

### Lemma. A. + S. $\Rightarrow$ A.S.

### Proof {.proof}
ℹ️ We prove directly the stronger version of A.S.

Let $X_0$ be a bounded set whose closure is included in $\mathrm{dom} \, f$.
We assume that additionally $X_0$ is closed (otherwise we substitute the closure
of $X_0$ to $X_0$).

Let $r_1 > 0$ and $B_1$ be the closed ball of radius $r_1$ centered on $x_e$.
Since the system is stable, there is a radius $r_2 > 0$ such that
for any $t \geq 0$, $x(t, B_2) \subset B_1$. Let $r_3 := r_2/2$ and 
$B_3$ be the ball of radius $r_3$ centered on $x_e$. 

Let $x_0 \in X_0$ ; since $x_e$ is attractive,
there is a $\tau \geq 0$ such that for any $t\geq \tau,$ $x(t, x_0) \in B_3$.
Since the system is well-posed, there is a radius $r_4 > 0$ such that for 
any $t \in [0, \tau],$ and any $x_1$ in the ball of radius $r_4$ centered on
$x_0$, $\|x(t, x_1) - x(t, x_0)\| \leq r_3$. Consequently,
$\|x(\tau, x_1) - x(\tau, x_0)\| \leq r_3$ and thus
$$
\begin{split}
\|x(\tau, x_1) - x(\tau, x_e)\| 
&\leq 
\|x(\tau, x_1) - x(\tau, x_0)\| +
\|x(\tau, x_0) - x(\tau, x_e)\| \\
&\leq r_3 + r_3 \\ 
&= r_2
\end{split}
$$
and thus $x(\tau, x_1) \in B_2$. 
Since $x(t, B_2) \subset B_1$ for any $t \geq \tau$, 
for any such $t$ we have 
$$
x(t, x_1) = x( t-\tau, x(\tau, x_1)) \in B_1.
$$

At this stage, we have proven that for any $r_1 > 0$ and any $x_0 \in X_0,$ there
is a $\tau(x_0) > 0$ and a $r_4(x_0)>0$ such that 
$$
\|x_1 - x_0\| \leq r_4(x_0) \; \wedge \; t\geq \tau(x_0)
\; \Rightarrow \;
\|x(t, x_1) - x_e\| \leq r_1.
$$
The collection of open balls centered on $x_0$ and of radius $r_0(x_0)$,
indexed by $x_0 \in X_0$ is an open cover of the closed set $X_0$, thus
there is a finite collection $x_0^1, \, x_0^2, \dots, \, x_0^m$ of points
of $X_0$ such that the open balls centered on $x_0^k$ with radius $r_4(x_0^k)$
cover $X_0$. Consequently, for any $x_0 \in X_0$, there is a $k \in \{1, \dots, m\}$
such that $\|x_0 - x_0^k\| \leq r_4(x_0^k)$ and thus $\|x(t, x_0) - x_e\| \leq r_1$
when $t \geq \tau(x_0^k)$. Consequently, for any $x_0 \in X_0$, if
$$
t\geq \tau := \max_{i=1,\dots,m} \tau(x_0^k),
$$
then $\|x(t, x_0) - x_e\| \leq r_1$. Thus, the equilbrium is asymptotically
stable.


## Examples


## Sandbox

Math  test: $a=1$

$$
\int_0^1 f(x)\, dx
$$