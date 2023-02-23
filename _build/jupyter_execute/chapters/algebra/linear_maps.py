#!/usr/bin/env python
# coding: utf-8

# # Linear Maps
# 
# Linear algebra is the study of linear maps on finite-dimensional vector spaces. Vector spaces are defined in this chapter, and their basic properties are developed.
# 
# The central goal of linear algebra is to:
# 
# 1. describe the properties properties, and
# 2. provide a recipe to completely parameterize,
# 
# all linear maps between arbitrary finite-dimensional vector spaces. Vector spaces are a generalization of the description of a plane using two coordinates, as published by Descartes in 1637. Like groups, the theory of linear maps holds for an entire class of examples, where results are uncoupled from any particular cases. We start with the following axiomatic definition.
# 
# ```{prf:axiom} Linear Map
# :label: linear-map
# 
# We will find it useful to make the distinction that  any map $f: V \to W$ sending each element $v \in V$ to some element in the image $f(V) \subset W$, is called a **linear map** from $V$ to $W$ whenever the following two conditions hold,
# 
# - **Additivity**  
# \begin{equation*} f(a + b) = f(a) + f(b) \end{equation*}
# - **Homogeneity** 
# \begin{gather*} f(\lambda a) = \lambda f(a) \end{gather*}
# 
# for the image of $a, b \in V$ and any scalar multiple $\lambda a$ of $a$.
# ```
# 
# ---
# 
# ## Vector Spaces
# 
# On first introspection, it is natural, perhaps tempting, to glance over a handful of deep, subtle requirements that {prf:ref}`linear-map` imposes regarding the structure of $V$ and $W$.  Observe, it may not neccessarily be true that there even exists an obvious sum of two elements in $V$ or that,
# 
# $$
# a + b \in V
# $$
# 
# corresponds to precisely one element in $V$ (the existence of a well-defined summation structure in $V$).
# Moreover, for any given field $\mathbb{F}$, it may also not be neccessarily be true that there even exists an obvious definition of scalar multiplication that assigns precisely one element
# 
# $$
# \lambda a \in V
# $$
# 
# to each scalar-vector pair, $(\lambda, a) \in \mathbb{F} \times V$. In other words, if a map $f : V \to W$ is a linear mapping, then we are implicitly assuming that $V$ has a well-defined summation structure $+_V : V \times V \to V$ and scalar-multiplication structure $\cdot_V : \mathbb \times V \to V$ compatible with $f$. Likewise, by assuming the existence of a linear map $f: V \to W$, we also require the existence of a summation structure $+_W : W \times W \to W$ and a scalar multiplication structure $\cdot_W : \mathbb{F} \times W \to W$ so that $f$ may satisfy the additivity and homogeneity structure defined in {prf:ref}`linear-map`. Thus, if one wishes to build a solid theory of linear maps, we are motivated first to consider what types of *sets* linear maps can be well-defined over.
# Distilling fundamental properties of addition and scalar multiplication, we define vector spaces as follows,
# 
# ```{margin}
# Since elements of a vector space relate under some scalar multiplication structure, which itself depends on the choice of $\mathbb{F}$, the phrase "$V$ is a vector space over $\mathbb{F}$" indicates that $V$ is a vector space and, for the situation at hand, the choice of scalar field is $\mathbb{F}$.
# ```
# 
# ```{prf:axiom} Vector Space
# :label: vector-space
# 
# A **vector space** is a quadruple $(V, \mathbb{F}, +, \cdot)$ where $V$ is a set, $\mathbb{F}$ is an algebraic field of scalars, $+: V \times V \to V$ is an addition on $V$, and $\cdot: \mathbb{F} \times V \to V$ is a scalar multiplication on the cartesian product $\mathbb{F} \times V$, whose definitions satisfy the following properties
# 
# - **associativity:** the sum of three elements $v_1, v_2, v_3 \in V$ is invariant under association,
# \begin{gather*} v_1 + (v_2 + v_3) = (v_1 + v_2) + v_3 \end{gather*}
# 
# - **commutativity:** any two given elements $v, w \in V$ commute under addition,
# \begin{gather*} v + w = w + v  \end{gather*}
# 
# - **neutral element:** there exists some element that acts neutrally under addition,
# \begin{gather*} \exists 0 \in V, \forall v \in V, v + 0 = v \in V \end{gather*}
# 
# - **annihilator element:** there exists some element that gives the identity element,
# \begin{gather*} \forall v \in V, \exists w \in V, v + w = 0 \in V \end{gather*}
# 
# - **neutral scalar:** a neutral factor $1 \in \mathbb{F}$ is also a neutral scalar,
# \begin{gather*} (1) v = v \in V,  \end{gather*}
# 
# - **compatibile scalar multiples**: scalars associate compatibly between $\mathbb{F}$ and $V$,
# \begin{gather*} (a \cdot_\mathbb{F} b) \cdot_V v = a \cdot_V (b \cdot_V v) \end{gather*}
# 
# - **distributivity of addition over scalar multiplication**
# \begin{gather*} (a + b) v = (av) + (bv) \end{gather*}
# 
# - **distributivity of scalar multiplication over addition**
# \begin{gather*} a (v + w) = (av) + (aw) \end{gather*}
# 
# ```
# 
# With this definition, we can view linear maps as constituting a class of morphisms between two *vector spaces* with compatible summation and scalar multiplication structures over the same field $\mathbb{F}$.
# 
# In practice, the scalar field $\mathbb{F}$ will either be the scalar field $\mathbb{R}$ of real numbers or the scalar field $\mathbb{C}$ of complex numbers. For brevity, we will make the following two definitions,
# 
# ```{prf:definition} Real Vector Space, Complex Vector Space
# :label: real-complex-vector-space
# 
# A vector space over $\mathbb{R}$ is called a **real vector space**.
# 
# A vector space over $\mathbb{C}$ is called a **complex vector space**.
# ```
# 
# The following geometric language is defined for convenience of thinking. *Linear algebra* focuses on the ***algebraic*** structure of vector spaces; intuition depending greatly on geometric insight should be avoided when invoked at the expense algebraic insight.
# 
# ```{prf:definition} Vector, Point
# :label: vector-point
# 
# Elements of a vector space are called **vectors** or **points**.
# ```
# 
# ```{margin}
# Common geometric notions  like `angle`, `orientation`, and `distance` between points and vectors (unless we consider a vector space with an *inner product structure*)  do not have any obvious meaning in abstract vector spaces.
# 
# *Inner product spaces* will be a later topic of discussion.
# ```
# 
# The following operation is defined for convenience of thinking and proof-writing. It does not ordain a set with any additional structure beyond what is already defined by its parent operation.
# 
# There are many more examples of vector spaces than $\mathbb{F}^n$, which are described extensively in the literature.
# 
# ```{prf:example} $\mathbb{F}^S$
# :label: set-vector-space
# 
# If $S$ is any set, then $\mathbb{F}^S$ denotes the set of functions $\{ f : f : S \mathbb{R}^ightarrow \mathbb{F}\}$. For $f, g \in \mathbb{F}^S$, addition and scalar multiplication are defined by:
# - $(f+g)(x) = f(x) + g(x)$    for all $x \in S$.
# - $(\lambda \cdot f)(x) = \lambda \cdot f(x)$   for all $x \in S$.
# 
# It is easy to verify that $\mathbb{F}^S$ is a vector space.
# ```
# 
# The following theorems hold for all vector spaces.
# 
# ```{prf:theorem} Every vector space has a unique additive identity.
# :label: unique-additive-identity
# 
# Suppose $0$ and $0'$ are additive identities in $V$. Then $0 = 0'$.
# ```
# 
# ```{prf:proof}
# :class: dropdown
# 
# Suppose $0$ and $0'$ are neutral elements in a vector space $V$. Then
# 
# $$
# 0 = 0 + 0' = 0' + 0 = 0'
# $$
# 
# where the first equality holds because $0$ is invariant under adddition with a neutral element (assumed); the second equality holds by the commutative property of $V$ ({prf:ref}`vector-space`), and the final equality holds because $0'$ is invariant under adddition with a neutral element (assumed). 
# 
# This equality shows that any two neutral elements in $V$ are, in fact, equal. Every vector space has a unique additive identity.
# ```
# 
# ```{prf:theorem} Every element in a vector space has a unique additive inverse.
# :label: unique-additive-inverse
# 
# For any $u, v, w \in V$ where $u + v = 0$ and $u + w = 0$. Then $v = w$.
# ```
# 
# ```{prf:proof}
# :class: dropdown
# 
# Choose any $u, v, w \in V$ where $u + v = 0$ and $u + w = 0$. Then
# \begin{align*}
# v &= v + 0 \\
# &= v + (u + w) \\
# &= (v + u) + w \\
# &= (u + v) + w \\
# &= 0 + w \\
# &= w \\
# \end{align*}
# Hence, any two elements that are additive inverses of some $u \in V$ are, in fact, equal. Every element in a vector space has a unique additive inverse.
# ```
# 
# ```{prf:theorem} The Annihilating Scalar
# :label: annihilating-scalar
# 
# The additive identity in $V$ decomposes as $0 \cdot v = 0 \in V$ for every $v \in V$.
# ```
# 
# ```{prf:proof}
# :class: dropdown
# 
# Take any $v \in V$. Observe,
# 
# $$
# 0 \cdot v = (0 + 0) \cdot v = 0 \cdot v + 0 \cdot v.
# $$
# 
# Since every element in $V$ has an additive inverse, the additive inverse of $0 \cdot v$ can be added to both sides, resulting in the following sum, 
# 
# 
# $$
# \mathbf{0} = 0 \cdot v
# $$
# 
# Hence, $0 \cdot v = 0 \in V$ for every $v \in V$. 
# ```
# 
# ```{prf:theorem} Scaling the Additive Identity
# :label: a-zero-equals-zero
# 
# $a \cdot 0  = 0 \in V$ for every $a \in \mathbb{F}$.
# ```
# 
# ```{prf:proof}
# :class: dropdown
# 
# Take any $a \in \mathbb{F}$. Observe
# 
# $$
# a \cdot 0 = a \cdot (0 + 0) = a \cdot 0 + a \cdot 0.
# $$
# 
# Since every element in $V$ has an additive inverse, the additive inverse of $a \cdot 0$ can be added to both sides, resulting in the following sum,
# 
# 
# $$
# \mathbf{0} = a \cdot 0
# $$
# 
# Hence, $a \cdot 0  = 0 \in V$ for every $a \in \mathbb{F}$.
# ```
# 
# ```{prf:theorem} The number (-1) as a Scalar
# :label: minus-one-scalar
# 
# $(-1) \cdot v = -v$ for every $v \in V$.
# ```
# 
# ```{prf:proof}
# :class: dropdown
# 
# For any $v \in V$, we have 
# 
# \begin{align*}
# -v &= -v + \mathbf{0} \\
# &= -v + (0 \cdot v) \\
# &= -v + (1 + (-1)) \cdot v \\
# &= -v + (1 \cdot v + (-1) \cdot v) \\
# &= -v + (v + (-1) \cdot v) \\
# &= (-v + v) + (-1) \cdot v \\
# &= \mathbf{0} + (-1) \cdot v \\
# &= (-1) \cdot v
# \end{align*}
# 
# where the first equality holds from {prf:ref}`vector-space`, the second equality holds from {prf:ref}`annihilating-scalar`, the third equality holds by definition of field addition in $\mathbb{F}$, and the fourth and all remaining equalities hold from the repeated application of {prf:ref}`vector-space`.
# 
# Hence, $(-1) \cdot v = -v$ for every $v \in V$.
# ```
# 
# ### Subspaces
# 
# The concept of subspaces greatly increases the richness and utility of the subject.
# 
# ```{prf:definition} Subspace
# :label: subspace
# 
# A subset $U \subset V$ over $\mathbb{F}$ is called a subspace of $V$ if $U$ is also a vector space over $\mathbb{F}$; the notation $U < V$ is used to signify that the subset $U \subset V$ is, in fact, a subspace of $V$.
# ```
# 
# The next, very important, result gives an necessary and sufficient condition to check whether a subset of a vector space is, in fact, a subspace.
# 
# ```{prf:theorem} Necessary + sufficient conditions for a Subspace
# :label: subspace-condition
# 
# A subset $U < V$ if and only if $U$ satisfies the following:
# - **Additive Identity:** $0 \in U$;
# - **Closure Under Addition:** $u, w \in U \implies u + w \in U$;
# - **Closure Under Scalar Multiplication:** $u \in U \implies \lambda \cdot u \in U$ for every $\lambda \in \mathbb{F}$.
# ```
# 
# ```{prf:proof}
# :class: dropdown
# We will show both directions of the bidirectional implication,
# 
# $(\implies)$
# 
# If $U < V$, then the above conditions hold, as required from {prf:ref}`vector-space`.
# 
# $(\impliedby)$
# 
# To demonstrate the converse, consider any $u, v \in U \subset V$ and scalars $a, b \in \mathbb{F}$. Since $u, v$ are, inherently, elements of $V$, which is a vector space, the following statements are true for the operations of addition and scalar multiplication.
# - **Commutativity:** $u + v = v + u$ for all $u,v \in U$;
# - **Associativity:** $(u + v) + w = u + (v + w)$ and $a (bv) = (ab) v$
# - **Multiplicative Identity:** $1 \cdot v = v$ as expected for $1 \in \mathbf{F}$;
# - **Distributive Properties:** Addition and Scalar Multiplication satisfy the following two relations:
#   - $a (v + u) = av + au \text{ for all } a \in \mathbb{F} \text{ and } u, v \in U,$
#   - $(a + b) v = av + bv \text{ for all } a, b \in \mathbb{F} \text{ and } v \in U.$
# 
# Since all the properties of {prf:ref}`vector-space` hold for addition and scalar multiplication restricted to $U$, we have $U < V$, as required.
# ```
# 
# Given the previous result, it is easy to verify that each of the following are subspaces.
# 
# ```{prf:example} Examples of subspaces
# :label: subspace-examples
# 
# - The set of continuous real-vaued functions on the interval $[0, 1]$ is a subspace of all functions $\mathbb{R}^{[0,1]}$.
# - The set of differentiable real-valued functions on $\mathbb{R}^{}$ is a subspace of $\mathbb{R}^{\mathbb{R}^{}}$.
# - The set of differentiable real-valued functions $f$ on the interval $(0, 3)$ such that $f'(2)=b$ is a subspace of $\mathbb{R}^{(0, 3)}$ if and only if $b = 0$.
# - The set of all sequences of complex numbers with limit 0 is a subspace of $\mathbb{C}^{\infty}$.
# 
# - If $b \in \mathbb{F}$, then 
# 
# $$
# \{(x_1, x_2, x_3, x_4) \in \mathbb{F}^{4} : x_3 = 5x_4 + b\}
# $$
# 
# is a subspace of $\mathbb{F}^{4}$ if and only if $b=0.$
# 
# ```
# 
# ### Span & Linear Independence
# 
# ### Bases & Dimension
# 
# ## Vector Space of Linear Maps
# 
# Recall the above definition of a linear map,
# 
# Using the terminology later defined, could have made the more concise but nevertheless equivalent definition,
# 
# ```{prf:proposition} Linear Map
# :label: linear-comb-map
# 
# Consider any $f: V \to W$. Observe $f$ is a linear map if and only if linear combinations are preserved under $f$, i.e.
# 
# \begin{equation*}
# f(a_1 v_1 + \cdots + a_n v_n) = a_1 f(v_1) + \cdots + a_n f(v_n)
# \end{equation*}
# ```
# 
# ### Algebraic Operations
# 
# ## Fund. Thm. of Linear Maps
