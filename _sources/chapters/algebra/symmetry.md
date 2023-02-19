# Symmetry

Forever fused by Newton, the allience of higher mathematics and modern physics have irreversably altered our relationship with the universe. The ultimate goal of both theories, mathematics and physics, is to develop logical and consistent abstract model of the properties of the systems that make up the world. Among the most profound achievements in this endeavor has been the construction of groups and group theory. This feat is a direct consequence of the following truth:

<div style="text-align:center;">
<b>groups</b> are a <b>formal language</b> for describing <b>symmetries</b>.</div>
<br>

Much like how ***derivatives*** provide a formal mathematical object to portray the structure of infinitesmal change, ***groups*** are a formal mathematical structure that extend our ability to understand and leverage symmetries.

Before going forward, our first goal is to motivate the study of groups by revisiting notions of sets, relations, mathematical structure, operations on sets, operators on sets, equivalence relations, and symmetry. This is followed by some basic results proved from the axioms of group theory, cosets, isomorphisms, and group actions.

## Set Theory

Sets are not merely defined as a collection of elements. Sets are defined by their elements and by the mathematical structure that glues elements together in any meaningful sense (ordering, summation, multiplication, orientation, etc.)

````{prf:definition} Set
:label: set

The *set* $S$ is the collection of all objects $s_1, s_2, \ldots$ that individually share the property of *existence* in $S$, denoted by, 

$$
s_1, s_2, \ldots \in S.
$$
````

Elements may be any kind of mathematical objects, including numbers, lists of numbers, mappings (functions) between sets of numbers, and even other sets.

### Relations

Relations and operations mathematically characterize the various kinds of structures that could exist between mathematical objects.
Relation can also describe a connection between two elements of different sets. Operations provide a way to discuss and view arbitrary elements by combining or manipulating other elements of a set. Together, these concepts form the foundation of many branches of mathematics and are used to define mathematical objects such as groups, vector spaces, and fields.

### Mathematical Structure

### Operations on Sets

### Operators

### Equivalence Relations

### Symmetry

The understanding that some properties of systems are preserved under certain "symmetries" stands out as fundamental.

In the context of physical systems, <a href="https://en.wikipedia.org/wiki/Noether%27s_theorem">Noether's theorem</a> was appreciated by Einstein as a piece of "penetrating mathematical thinking" because it revealed a deep connection between symmetry, conservation laws, and the fundamental laws of physics. At a high level, Noether's theorem states that for every  symmetry in a physical system, there exists a corresponding conservation law. In other words, if a physical system behaves the same way before and after a particular transformation (such as a rotation, translation, or time reversal), then there must be a corresponding conserved quantity (such as energy, momentum, or angular momentum) in that system. Einstein recognized the importance of Noether's theorem because it showed that the conservation laws that underpin so much of physics were not arbitrary or ad hoc, but were instead a consequence of deep mathematical symmetries that underlie the behavior of physical systems. Moreover, Noether's theorem also showed that the laws of physics were not dependent on the specific coordinate system or frame of reference used to describe them. This insight was particularly important in the development of Einstein's theory of relativity, which, in the spirit of Noether's work, to show that the laws of physics must be the same for all observers moving at constant speeds relative to each other.

In the context of polynomial systems, Évariste Galois used the concept of symmetry to prove that there is no general formula for solving polynomial equations of degree five or higher (known as the quintic or higher degree equations) using only the operations of addition, subtraction, multiplication, division, and extraction of roots. Galois showed that if a general formula existed for solving the quintic equation, then by a group of permutations of its roots, known as its Galois group, he showed that the quintic equation could not be solved using radicals alone. Galois the first example of a class of equations that )and it helped to pave the way for the development of new techniques for studying equations with higher degrees, such as elliptic functions and algebraic geometry.



## Group Theory
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. U

### Cosets & Normal Subgroups
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. U

### Homomorphisms & Isomorphism Theorems

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. U

### Group Actions

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. U


## Citations

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

```{bibliography}
```

## Learn more

This is just a simple starter to get you started.
You can learn a lot more at [jupyterbook.org](https://jupyterbook.org).
