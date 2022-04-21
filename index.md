---
title: Asymptotic Stability for Humans
author: 
- "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@minesparis.psl.eu), MINES Paris, PSL University"
date: "Wed, 20 Apr 2022 12:47:09 +0200"
---

```{=html}
<style>
details h1, details h2, details h3{
  display: inline;
}
</style>
```

```{=html}
<style>
details summary {
  cursor: pointer;
  list-style: '🔒 ';
}

details[open] summary {
  cursor: pointer;
  list-style: '🔓 ';
}

summary::-webkit-details-marker {
  display: none
}




details[open] summary ~ * {
  animation: sweep .5s ease-in-out;
}
@keyframes sweep {
  0%    {opacity: 0}
  100%  {opacity: 1}
}
</style>
```



# Introduction

Asymptotic stability is a cornerstone of control theory and engineering.
There is little doubt in my opinion that if only one notion among stability,
attractivity and asymptotic stability, should be taught to control engineers,
it should be asymptotic stability. 
Therefore, asymptotic stability, not attractivity nor stability, 
should be the only focus of time and complexity-bound control engineering lectures.
As heartbreaking as this conclusion can be, most experienced lecturers know that 
chosing means eliminating ("choisir, c'est renoncer"[^1]). 

[^1]: > L’erreur de ma vie fut dès lors de ne continuer longtemps aucune étude, 
> pour n’avoir su prendre mon parti de renoncer à beaucoup d’autres. 
> --- N'importe quoi s’achetait trop cher à ce prix-là, 
> et les raisonnements ne pouvaient venir à bout de ma détresse. 
> Entrer dans un marché de délices, en ne disposant (grâce à Qui ?) 
> que d’une somme trop minime ; en disposer ! 
> **Choisir, c'était renoncer pour toujours, pour jamais, à tout le reste** --- 
> et la quantité nombreuse de ce reste demeurait préférable à n'importe quelle unité. 
>
> *André Gide, Les nourritures terrestres*

However, the classic approach introduces asymptotic stability as a 
strengthening of the concept of stability,
with a composite definition that required stability and attractivity.
It has several didactic drawbacks:

  - It requires to understand the concept of stability, which is arguably hard
    (at the very least much harder than attractivity).
    Using it as a foundation to define asymptotic stability makes automatically
    asymptotic stability at least equally as hard.

  - Using a composite definition for asymptotic stability makes it a derived
    concept, which appears as a second-class citizen of control theory 
    instead of the first-class citizen that it should be.

  - This definition fails to address in simple terms what are in my opinion
    the shortcoming of the concept of attractivity and why it needs to be strengthened:
    a catastrophic failure to ensure a common speed of convergence, 
    even for arbitrary close initial states.

In this document we follow a different path: we introduce attractivity, expose
it shortcomings, then introduce a definition of asymptotic stability as an
independent concept which is

  - an obvious strenghtening of attractivity (and clearly solves its issues),

  - of reasonable complexity (harder than attractivity, but simpler than stability),

  - equivalent to the classic definition.

To the best of my knowledge, my definition is original,
but I have not performed an extensive research on this subject. Suffice to
say that I have never been exposed to it in my earlier studes;
if the concept is not new (I seriously doubt it is) at the very least it is
not in my opinion popular enough given its didactic potential.

🚧 **TODO:** 🚧 explain document meant for lecturers, not students.
Relate this to its organisation (relatively standalone, level of
details, videos, extra work to adapt, not "off-the-shelf" use, etc.).

# Definitions & Notations

### Vector Field {.definition} 
An **(time-invariant) vector field** is a $\mathbb{R}^n$-valued function $f$ 
whose domain $\mathrm{dom} \, f$ is an open subset $U$ of $\mathbb{R}^n$ 
(for some natural number $n$):
$$
f: U \subset \mathbb{R}^n \to \mathbb{R}^n,
\qquad \partial U \cap U= \varnothing. 
$$



### Dynamical System {.definition}
A vector field defines a unique **(time-invariant) dynamical system** denoted 
$\dot{x} = f(x)$. Any element of the domain of definition of $f$ is
a **(valid) state** of the dynamical system.

### Initial-Value Problem {.definition}
An vector field $f$ and a valid state $x_0$ define a unique
**initial-value problem (IVP)** denoted
$\dot{x} = f(x)$, $x(0) = x_0$.

### Solution & Flow {.definition}
A **(forward) solution** of the IVP $\dot{x} = f(x)$, $x(0) = x_0$ is 
an absolutely continuous and $\mathbb{R}^n$-valued function $x$ defined on 
$\left[0, \tau\right[$ for some $\tau \in \left]0, +\infty\right]$
such that
$$
x(t) = x_0 + \int_0^t f(x(s)) \, ds, \qquad 0 \leq t < \tau.
$$
When we wish to emphasize the role of the initial state $x_0$, we denote
the solution $x(t, x_0)$ and then call the application $x$ the **flow** 
of the dynamical system. 
We also consider solutions associated
with a set $X_0 \subset \mathrm{dom} \, f$ of initial states: 
we denote $x(t, X_0)$ the image of $X_0$ by the flow at time $t$:
$$
x(t, X_0) := \{x(t, x_0) \; | \; x_0 \in X_0\}.
$$ 

### Maximal Solutions {.definition}
A solution of the IVP $\dot{x} = f(x)$, $x(0) = x_0$ is **maximal**
if no other solution is a strict extension of it.



### Well-Posed System {.definition}
A dynamical system $\dot{x} = f(x)$ is **well-posed** if for any initial state 
the corresponding IVP has a unique maximal solution $x$ which 
**depends continuously on the initial state**: if $x(t, x_0)$ is defined on $[0, \tau]$, 
then for $x_0'$ close enough to $x_0$, 
$x(t, x'_0)$ is also defined on $[0, \tau]$ and
$$
\lim_{x_0' \to x_0} \left[\max_{t \in [0, \tau]} \|x(t, x'_0) - x(t, x_0)\|\right] = 0.
$$



# Attractivity


### Equilibrium {.definition}
An **equilibrium** $x_*$ of a dynamical system $\dot{x} = f(x)$ is a state such
that $x: t \in \left[0, +\infty\right[ \to x_*$ is a solution of 
$\dot{x} = f(x)$, $x(0) = x_*$.

Equivalently, a state $x_*$ is an equilibrium if and only if $f(x_*) = 0$.

### Attractivity {.definition}
An equilibrium $x_*$ of a well-posed system $\dot{x} = f(x)$ is **(globally) attractive**
if for any $x_0$ in the domain of definition of $f$, the solution $x(t, x_0)$ 
(exists for any $t\geq 0$ and) tends to $x_*$ as $t$ tends to $+\infty$.
$$
\forall \, x_0 \in \mathrm{dom} \, f, \;
\lim_{t \to +\infty} x(t, x_0) = x_*.
$$

### Example 1 -- Attractivity {.example}
The time-invariant system
\begin{equation}
\dot{x}^1 = -2x^1+x^2, \; \dot{x}^2 = -2x^2+x^1, \qquad x = (x^1, x^2) \label{LTI}
\end{equation}
has a single equilibrium $x_* = (0, 0)$. The auxiliary variables 
$y^1:= x^1+x^2$ and $y^2:=x^1 - x^2$ satisfy the decoupled differential equations
$\dot{y}^1 = -y^1$ and $\dot{y}^2 = -3 y^2$,
the solution associated to an initial state $x_0 = (x_0^1, x_0^2)$ is
$$
y^1(t) = (x_0^1 + x_0^2)e^{-t}, \;
y^2(t) = (x_0^1 - x_0^2)e^{-3t}
$$
and thus
\begin{equation}
\left[
  \begin{array}{c}
  x^1 \\
  x^2
  \end{array}
\right](t)
= 1/2 \left[
  \begin{array}{c}
  x_0^1 + x_0^2 \\
  x_0^1 + x_0^2
  \end{array}
\right]e^{-t}
+  1/2 \left[
  \begin{array}{c}
  x_0^1 - x_0^2 \\
  x_0^2 - x_0^1
  \end{array}
\right]e^{-3t}.
\label{LTI-solutions}
\end{equation}
It is therefore clear that for every initial state $x_0$, we have
$$
\lim_{t \to +\infty} x(t, x_0) = x_*. 
$$
Hence, the equilibrium is attractive.

```{=html}
<video controls style="width:100%;">
  <source src="videos/attractivity.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> 
```

# Limitations



# Asymptotic Stability

### Hausdorff Distance {.definition}
The **Hausdorff distance** between two sets $A$ and $B$ of $\mathbb{R}^n$ is
defined as
$$ 
d_H(A, B) := \max \left\{ \sup_{a \in A} d(a, B), \sup_{b \in B} d(A, b) \right\}.
$$
(see e.g. @Kur66, p. 214). 
A time-dependent set $A(t)$ tends to a set $B$ when $t$ tends to $+\infty$, 
noted
$$
\lim_{t \to +\infty} A(t) = B,
$$
whenever $\lim_{t \to +\infty} d_H(A(t), B) = 0.$




When $B$ is a singleton $\{b_*\}$, we have 
$$
\sup_{a \in A} d(a, B) = \sup_{a \in A} d(a, b_*) \geq \inf_{a \in A} d(a, b_*) 
= d(A, b_*)
= \sup_{b \in B} d(A, b), 
$$
thus
$$
d_H(A, \{b_*\}) = \sup_{a \in A} d(a, b_*).
$$

```{=html}
<video controls style="width:100%;">
  <source src="videos/hausdorff.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> 
```


### Asymptotic Stability {.definition}
An equilibrium $x_*$ of a well-posed system $\dot{x} = f(x)$ is **(globally)
asymptotically stable** if for any state $x_0$ there is a (small enough) 
closed ball of states of positive radius $r$ centered at $x_0$ 
$$
\bar{B}(x_0, r) := \{x \in \mathbb{R}^n \; | \; d(x, x_0) \leq r\}
$$ 
whose image by the flow at time $t$ (exists for every $t\geq 0$ and) 
tends to $\{x_*\}$ as $t$ tends to $+\infty$.
$$
\forall \, x_0 \in \mathrm{dom} \, f, \;
\exists \, r > 0, \; 
\lim_{t \to +\infty} x(t, \bar{B}(x_0, r)) = \{x_*\}.
$$

### Compactness

A set $A$ of $\mathbb{R}^n$ is **compactly included** in a set $B$ of $\mathbb{R}^n$,
noted $A \Subset B$, if $A$ is bounded and its closure 
$\bar{A} := \{x \in \mathbb{R}^n \; | \; d(x, A)=0\}$
is included in $B$.


### Proposition. Asymptotic Stability {.proposition}
An equilibrium $x_*$ of a well-posed system $\dot{x} = f(x)$ is (globally)
asymptotically stable if and only if the image of any set of states 
compactly included in $\mathrm{dom} \, f$ by the flow at time $t$
(exists for every $t\geq 0$ and) tends to $\{x_*\}$ as $t$ tends to $+\infty$.
$$
\forall \, X_0 \Subset \mathrm{dom} \, f, \;
\lim_{t \to +\infty} x(t, X_0) = \{x_*\}.
$$

```{=html}
<details>
  <summary>
    <h3>Proof</h3>
  </summary>
```

Since a closed ball of states is compactly included in $\mathrm{dom} \, f$,
the above criteria clearly implies asymptotic stability.

Conversly, let $X_0$ be a set compactly included in $\mathrm{dom} \, f$.
For every $x_0 \in \bar{X}_0,$ there is a positive radius $r(x_0)$ such that
$$
\lim_{t \to +\infty} x(t, \bar{B}(x_0, r(x_0))) = \{x_*\}.
$$
The collection of all open balls 
$B(x_0, r(x_0))$, when $x_0 \in \bar{X}_0$
is an open cover of the compact set $\bar{X}_0$, thus there is a finite
sub-collection $B_1$, $B_2$, $\dots$, $B_p$ such that 
$$
\bar{X}_0 \subset B_1 \cup B_2 \cup \dots \cup B_p.
$$
Since for any $k=1,\dots, p$, we have 
$\lim_{t \to +\infty} x(t, B_k) = \{x_*\}$, we have
$$
\lim_{t \to +\infty} d_H(B_k, \{x_*\}) \to 0.
$$
Since $X_0 \subset \bar{X}_0 \subset B_1 \cup B_2 \cup \dots \cup B_p$,
$$
d_H(X_0, \{x_*\}) \leq d_H(\bar{X}_0, \{x_*\})
\leq \max_{k=1...p} d_H(B_k, \{x_*\})
$$
and thus
$$
\lim_{t \to +\infty} d_H(X_0, \{x_*\}) \to 0.
$$

```{=html}
</details>
```

### Examples

The origin is an asymptotically stable equilibrium of the system
$$
\dot{x}^1 = -2x^1+x^2, \; \dot{x}^2 = -2x^2+x^1, \qquad x = (x^1, x^2)
$$
Indeed, the closed-form solution \eqref{LTI-solutions} yields
$$
\|x(t, x_0)\| \leq 2 \|x_0\| e^{-t}.
$$
A set $X_0$ is compactly included in $\mathbb{R}^n$ if and only if it
is a bounded subset of $\mathbb{R}^n$. For any such set,
$$
d_H(x(t, X_0), 0\}) \leq 2 \sup_{x_0 \in X_0} \|x_0\| e^{-t}.
$$
Hence $x(t, X_0) \to \{0\}$ when $t \to +\infty$:
the origin is asymptotically stable.


```{=html}
<video controls style="width:100%;">
  <source src="videos/asymptotic-stability.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> 
```

```{=html}
<video controls style="width:100%;">
  <source src="videos/vinograd.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> 
```

# Stability & Legacy Definitions, Equivalence

### Stability {.definition}
🚧 TODO 🚧 

--------------------------------------------------------------------------------

### Proposition. A. + S. $\Leftrightarrow$ A.S. {.proposition}
Attractivity + Stability $\Leftrightarrow$ Asymptotic Stability
🚧 TODO 🚧 

### {.proof}
🚧 TODO 🚧 


### Lemma. A.S. $\Rightarrow$ A.

```{=html}
<details>
  <summary>
    <h3>Proof</h3>
  </summary>
```

Obvious (by design).

```{=html}
</details>
```

### Lemma. Asymptotic Stability implies Stability.

```{=html}
<details>
  <summary>
    <h3>Proof</h3>
  </summary>
```

Let's assume that the system is asymptotically stable.
Let $r_1 > 0$ such that the closed ball $B_1$ of radius $r_1$ centered at $x_e$ 
is included in $\mathrm{dom} \, f$.
$$
B_1 := \{x \in \mathbb{R}^n \; | \; \|x - x_e\| \leq r_1 \} \subset \mathrm{dom} \, f.
$$ 

It is bounded, its closure is included in $\mathrm{dom} \, f$ and it is also 
a neighbourhood of $x_e$. Since the the system is asymptotically stable,
$x(t, B_1)$ is defined for any $t\geq 0$
and there is a $\tau \geq 0$ such that for any $t \geq \tau$, 
the image of $B_1$ by $x(t, \cdot)$ is included in itself
$$
t\geq \tau \, \Rightarrow \, x(t, B_1) \subset B_1.
$$

Additionally, the system is well-posed, hence there is a $r_2 > 0$ 
such that for any $x_0$ in the closed ball $B_2$ of radius $r_2$ 
centered at $x_e$ is included in $\mathrm{dom} \, f$ and any $t \in [0, \tau]$,
we have $\|x(x_0, t) - x(x_e, t) \| \leq r_1.$
Since $x_e$ is an equilibrium, $x(t, x_e) = x_e$, thus
$\|x(x_0, t) - x_e \| \leq r_1.$ Equivalently, 
$$
0\leq t \leq \tau \, \Rightarrow \, x(t, B_2) \subset B_1.
$$

Note that since $x(0, B_2) = B_2$, this inclusion yields $B_2 \subset B_1$.
Thus, for any $t \geq 0$, either $t\in [0, \tau]$
and $x(t, B_2) \subset B_1$, or $t\geq \tau$ and 
since $B_2 \subset B_1$, we have $x(t, B_2) \subset x(t, B_1) \subset B_1$.

To summarize our findings: we have established that for any $r_1 > 0$ 
such that $B_1 \subset \mathrm{dom} \, f$
there is a $r_2 > 0$ such that
$$
t\geq 0 \, \Rightarrow x(t, B_2) \subset B_1.
$$ 
Therefore that the system is stable.

```{=html}
</details>
```

### Lemma. A. + S. $\Rightarrow$ A.S.



```{=html}
<details>
  <summary>
    <h3>Proof</h3>
  </summary>
```
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

```{=html}
</details>
```

# References