#!/usr/bin/env python
# coding: utf-8

# # Linear Maps
# 
# The central goal of linear algebra is to:
# 
# 1. illustrate, and
# 2. completely characterize,
# 
# all linear maps between arbitrary finite-dimensional vector spaces.
# 
# This section serves to help the reader begin to appreciate the above statement. To start, we will ponder the central object of study in linear algebra, linear maps. Like groups, linear maps are developed as an axiomatic theory, where results are guaranteed to hold for an entire class of mathematical objects (in contrast to one particular mathematical object). We start with the following axiomatic definition.
# 
# ```{prf:axiom} Linear Map
# :label: linear-map
# 
# The function $f: V \to W$ is said to **map linearly** from $V$ to $W$ when the following two properties are satisfied
# 
# 1. Additivity of $f$
# 
# $$
# f(a + b) = f(a) + f(b)
# $$
# 
# 2. Homogeneity of $f$
# 
# $$
# f(\lambda a) = \lambda f(a)
# $$
# 
# for any given two elements $a, b \in V$ and any given scalar $\lambda \in \mathbb{F}$.
# ```
# 
# ---
# 
# ## Vector Spaces
# 
# On initial introspection, it is natural, perhaps tempting, to glance over a subtle condition of Definition {eq}`linear-map`.  Linear maps constitute a class of group morphisms compatible only with vector spaces.
# 
# ```{prf:axiom} Vector Space
# :label: vector-space
# 
# A **vector space** is a quadruple $(V, \mathbb{F}, +, \cdot)$ where $V$ is a set, $\mathbb{F}$ is a field, $+: V \times V \to V$ is a composition law colloquially called "addition", and $\cdot: \mathbb{F} \times V \to V$ is a scalar multiplication, whose individual definitions come together to satisfy the following properties
# 
# 1. **associativity**
# sums remains equal under arbitrary association, i.e. 
# 
# 2. Given any $a$ belonging to $V$, we can find some neutral element $e_a$ within $V$ which leaves $a$ unchanged under addition, that is, $a$ can decompose as $a = e_a + a$,
# 
# 3. Given any element $a$ belonging to $V$, we can find some annihilator element $-a$ belonging to $V$, which combines with $a$ under addition to produce a neutral element $e_{a'}$ in $V$, i.e., $a + (-a) = e_{a'}$,
# ```
