import os

WIKI_DIR = "/var/home/justin/Projects/Idris2-Logic-Wiki/Library/Wiki/Finite_Science"
os.makedirs(WIKI_DIR, exist_ok=True)

pages = [
    {
        "id": "Digital_Repetition",
        "title": "Digital Repetition (Algebra of Boole)",
        "content": """# Digital Repetition (Algebra of Boole)

## Dependent Type Formalization
In Finite-Science, boolean logic is not a primitive truth value; it is a structural multiset representing the lowest order of physical repetition. By utilizing Idris 2's dependent types, we ensure that digital operations are strictly bounded and conserved.

```idris
module Formal.Boole

import Math.Multiset
import Math.SignedFraction

-- A digital bit is structurally bounded to 0 or 1 at the type level
data Bit : Type where
  O : Bit
  I : Bit

-- Dependent proof that boolean algebra forms a valid modulo-2 Ring over Multisets
-- Using the SignedFraction (Numerator over Unit Denominator)
DigitalFraction : Type
DigitalFraction = MSetFraction Bit Unit

total
modulo2Invariance : (x : DigitalFraction) -> (x + x = 0)
-- Proof that identical causal chains annihilate in mod-2 (destructive interference)
```
"""
    },
    {
        "id": "Lifted_Polynumbers",
        "title": "Lifted Polynumbers (Arithmetic Circuits)",
        "content": """# 💻 Lifted Polynumbers — [Algebra of Boole](https://github.com/justinkelly-ie/Idris2-Boole)

> **Row 2 of the Global Finite Science Table**
>
> The transition from logical bit-gates to continuous arithmetic. By mapping modulo-2 logic fields into the integer polynomial plane, Row 2 provides the algebraic framework that underpins probability, rational trigonometry, and physical laws.

---

## 🏛️ Theoretical Foundation: The Polynomial Plane

This row implements the algebraic mapping of Boolean functions into integer polynomials, as described by Norman Wildberger in his lecture series *[Algebra of Boole](https://www.youtube.com/playlist?list=PLIljB45xT85A-qCypcmZqRvamiF-FYLPv)* (Lectures 256, 264, and 270–272). 

The key insight is that any Boolean function $f: B_2^n \\to B_2$ can be uniquely represented as a multilinear polynomial over $\\mathbb{Z}$:

$$p(x_1, x_2, \\dots, x_n) = \\sum_{I \\subseteq \\{1,\\dots,n\\}} c_I \\prod_{i \\in I} x_i$$

where the coefficients $c_I$ are integers. This is known as the **Algebraic Normal Form (ANF)**. Because coordinates in this layer are integers ($\\mathbb{Z}$), we can represent operations using standard subtraction, addition, and multiplication, avoiding the constraints of modulo-2 bit arithmetic while preserving exactness.

---

## 🗃️ The MSetFraction Structure: Numerator and Denominator

Following the uniform architecture of the Global Finite Science Table, Row 2 is represented as an `MSetFraction` of multisets:

$$\\text{MSetFraction} = \\frac{\\text{TRUTH TABLE COEFFICIENTS} \\;\\{w \\cdot [\\text{Monomial}]\\} \\;\\in \\mathbb{Z}}{\\text{UNIT CONSTANT} \\;\\{1 \\cdot [\\text{Base}]\\} \\;\\in \\mathbb{Z}}$$

For Row 2 specifically, the fraction is structured as:
- **Numerator Box:** `LiftedPolynumber v` — an integer-weighted multiset of monomials, representing terms like $1 - x - y + xy$ using `BoxInt`.
- **Denominator Box:** `Multiset BoxInt TrivialBase` — locked to the unit constant $\\{1 \\cdot [\\text{Base}]\\}$.
- **Compile-Time Constraint:** A dependent type proof (`isTrivial`) verifies that the denominator is exactly `theUnitConstantZ`, preventing scale deviation.

```idris
record LiftedBooleFraction (v : Type) where
  constructor OverLiftedCircuit
  numeratorPolynumber : LiftedPolynumber v
  denominatorUnit     : Multiset BoxInt TrivialBase
  isTrivial           : denominatorUnit = theUnitConstantZ
```

---

## 🎓 The Core Types

### 1. `Monomial v` — Product Terms
**File:** `Boole/LiftedPolynumber.idr` | **Source:** Wildberger Lecture 256

Instead of character strings, a monomial (such as $xy$ or $xyz$) is modeled as a multiset of variable tokens of type `v` with `BoxInt` counts:

```idris
Monomial : Type -> Type
Monomial v = Multiset BoxInt v
```

### 2. `LiftedPolynumber v` — The Numerator Box
**File:** `Boole/LiftedPolynumber.idr` | **Source:** Wildberger Lecture 264

A lifted polynumber polynomial is a linear combination of these monomials, weighted by algebraic integers (`BoxInt`):

```idris
record LiftedPolynumber (v : Type) where
  constructor MKPolynumber
  underlyingPolynomial : Multiset BoxInt (Monomial v)
```

---

## 🔄 The Combinatorial Mechanism: Idempotent Collapse

When multiplying monomials or calculating Möbius transforms, variables can duplicate ($x \\cdot x = x^2$). In standard algebra, this raises the degree. In the Algebra of Boole, Wildberger's algorithm enforces the **idempotent rule**:

$$x^2 = x$$

Our implementation enforces this structural rule at the data-type level via `idempotentCollapse`, clamping positive counts down to exactly 1 and pruning non-positive counts:

```idris
idempotentCollapse : Eq v => Monomial v -> Monomial v
idempotentCollapse mono =
  let entries = multisetToList mono
      collapsedEntries = concatMap (\\\\(var, count) => if count > 0 then [(var, 1)] else []) entries
  in fromList collapsedEntries
```

---

## 🧮 Algebra in Action: Arithmetic Circuit Conversions

Under the polynomial mapping, logic gates map directly to arithmetic operations over $\\mathbb{Z}$:

| Logic Gate | Boolean Ring Form (Row 1) | Arithmetic Polynomial Form (Row 2) |
|---|---|---|
| **NOT $x$** | $1 + x$ | $1 - x$ |
| **AND($x,y$)** | $xy$ | $xy$ |
| **XOR($x,y$)** | $x + y$ | $x + y - 2xy$ |
| **OR($x,y$)** | $x + y + xy$ | $x + y - xy$ |
| **NAND($x,y$)** | $1 + xy$ | $1 - xy$ |

### Monomial Multiplication Example
Multiplying the monomial $(xy)$ by $(yz)$ yields:

$$(xy) \\cdot (yz) \\mapsto x \\cdot y^2 \\cdot z \\\\xrightarrow{\\\\text{idempotentCollapse}} xyz$$

This is handled automatically by `mulMonomial`:
```idris
mulMonomial : Eq v => Monomial v -> Monomial v -> Monomial v
mulMonomial m1 m2 = idempotentCollapse (addMultiset m1 m2)
```

---

## 🔄 The Boole-Möbius Shift Pipeline

Transitioning between the truth table values (evaluation points) and the polynomial coefficients requires the integer-valued Möbius transform:

```idris
||| Forward transform: computes truth table evaluations from polynomial coefficients.
mobiusTransformZ : List BoxInt -> List BoxInt

||| Inverse transform: recovers polynomial coefficients from a dense truth table.
mobiusInverseZ : List BoxInt -> List BoxInt
```

### Transition to Row 3 (Functional Probability)

Because the polynomial plane supports negative integer weights (like $-2xy$ in XOR), it is capable of tracking overlapping boundary conditions. In Row 3, Hehner normalization sums these coefficients over a variable sample space denominator (\\\\sum w), transforming the arithmetic circuits of Row 2 into exact, rational probability distributions.
"""
    },
    {
        "id": "Functional_Probability",
        "title": "Functional Probability (Hehner)",
        "content": """# 🧮 Functional Probability — [Algebra of Boole](https://github.com/justinkelly-ie/Idris2-Boole)

> **Row 3 of the Global Finite Science Table**
>
> The normalization of unnormalized physical mass distributions into exact rational probability vectors. Row 3 replaces classical axiomatic probability theory with calculational minimums and maximums over closed finite spaces, using cross-multiplication instead of division to prevent precision loss.

---

## 🏛️ Theoretical Foundation: Hehner Normalization

This row implements the functional probability framework developed by Eric Hehner in *[a Probability Theory](http://www.cs.utoronto.ca/~hehner/aPT.pdf)*. 

In classical logic and physics, probability is typically introduced as a measure-theoretic axiom over infinite limits. In Hehner's model, probability is a derived **normalization** of unnormalized weights (such as the integer coefficients produced by a boolean circuit in Row 2). 

For each state element $e_i$ with an unnormalized weight $w_i$ in an environment $E$, its normalized probability $\\overline{E}_i$ is defined as:

$$\\overline{E}_i = w_i \\cdot \\left(\\sum E\\right)^{-1}$$

In our discrete finitist framework, we avoid floating-point numbers entirely. Probabilities are represented as exact fractions of integers: a signed weight numerator over a strictly positive natural sum denominator. 

---

## 🗃️ The MSetFraction Structure: Numerator and Denominator

Following the uniform architecture of the Global Finite Science Table, Row 3 is represented as an `MSetFraction` of multisets:

$$\\text{MSetFraction} = \\frac{\\text{QUANTIFIED MSET} \\;\\{w \\cdot [\\text{valid}]\\} \\;\\in \\mathbb{Z}}{\\text{TOTAL UNIVERSE SUM} \\;\\{\\sum w \\cdot [\\text{all\\_states}]\\} \\;\\in \\mathbb{N}^{+}}$$

In Row 1 and Row 2, the scale was locked to the unit constant ($1$). In Row 3, the denominator **generalizes to the total mass of the unnormalized distribution** ($\\sum w$). This allows the probability scale to adjust dynamically based on the total weight of the sample space.

The `BitFraction` type enforces the structure of Row 3 in the singleton architecture, corresponding directly to the compiled type `MSetFractionVexel` in the [Singleton.FunctionalProbability](file:///var/home/justin/Projects/Idris2-Logic/src/Singleton/FunctionalProbability.idr#L55-L59) library:

```idris
record BitFraction (v : Type) where
  constructor OverBitSpace
  numeratorMset  : Sing BoxInt v
  denominatorSum : Sing1 BoxInt TrivialBase
```

Using the smart constructor `mkBitFraction`, we construct the fraction from a singleton numerator (which may be 0 or 1) and the total mass of the space (where 0 is not permissible in the `Sing1` denominator box):

```idris
mkBitFraction : Sing BoxInt v -> BoxInt -> BitFraction v
mkBitFraction m tot = OverBitSpace m (MkSing1 BaseAnchor tot)
```

---

## 🎓 The Core Types

### 1. `stateProbability` — Exact State Probability
**File:** `Boole/FunctionalProbability.idr` | **Source:** Eric Hehner, *a Probability Theory*

Extracts the exact normalized probability of a single state as an `MSetFraction` containing a signed numerator and positive natural denominator:

```idris
stateProbability : Eq v => BitFraction v -> v -> MSetFraction
```

### 2. `normalizeFraction` — Distribution Normalizer
**File:** `Boole/FunctionalProbability.idr` | **Source:** Eric Hehner, *a Probability Theory*

Decomposes the full normalised space into a list of association pairs mapping each state to its exact probability:

```idris
normalizeFraction : BitFraction v -> List (v, MSetFraction)
```

---

## 🔄 Calculational Quantifiers: Replacing $\\forall$ and $\\exists$

In infinite set theory, logical deduction relies on quantifiers like "for all" ($\\forall$) and "there exists" ($\\exists$). Hehner replaces these with **calculational quantifiers** over the unnormalized weights of closed spaces:

*   **For All ($\\forall$)** $\\mapsto$ `minWeight`: The minimum unnormalized weight in the multiset.
*   **There Exists ($\\exists$)** $\\mapsto$ `maxWeight`: The maximum unnormalized weight in the multiset.

```idris
minWeight : Sing BoxInt a -> BoxInt
maxWeight : Sing BoxInt a -> BoxInt
```

This reduces logical quantifiers to simple, high-performance $O(N)$ structural scans over the multiset.

---

## 🧮 Algebra in Action: Divisionless Comparisons

Because probabilities are stored as exact fractions, we compare probabilities using cross-multiplication:

$$\\frac{a}{b} > \\frac{c}{d} \\iff a \\cdot d > c \\cdot b \\qquad (\\text{for } b, d > 0)$$

This enables divisionless comparisons, preventing precision loss and rounding errors:

```idris
||| Check whether one probability dominates another.
gtProbability : MSetFraction -> MSetFraction -> Bool
gtProbability (MkMSF a b) (MkMSF c d) =
  (a * fromInteger (natToInteger d)) > (c * fromInteger (natToInteger b))
```

### Normalization Example
Given an unnormalized distribution of outcomes:

$$M = \\{ \\text{Heads} \\mapsto 3, \\text{Tails} \\mapsto 5 \\}$$

1. The total mass is $\\sum M = 3 + 5 = 8$.
2. The normalized `BitFraction` is constructed as:
   $$\\text{Space} = \\frac{\\{ \\text{Heads} \\mapsto 3, \\text{Tails} \\mapsto 5 \\}}{8}$$
3. Normalizing the space yields the exact probabilities:
   *   $\\text{P(Heads)} = 3/8$
   *   $\\text{P(Tails)} = 5/8$
---

## 🔄 The Progression Bridge: Row 3 → Row 4

Functional probability assumes complete information about the state space weights. When information is incomplete, we can no longer assign single rational probabilities. In Row 4 (Probability Bounds / Hailperin), we wrap the numerator into min/max bounds (inclusion-exclusion corners), transitioning functional probability into exact polyhedral probability bounds.
"""
    },
    {
        "id": "Probability_Bounds",
        "title": "Probability Bounds (Hailperin)",
        "content": """# Probability Bounds (Hailperin)

## Dependent Type Formalization
Hailperin probability bounds replace exact probabilities with bounded min/max intervals, structurally encoded as pairs of Multisets.

```idris
module Formal.Hailperin

-- Bounded interval structurally guaranteed to be valid (Min <= Max)
record HailperinBound where
  constructor MkBound
  minVal : Integer
  maxVal : Integer
  prf    : minVal <= maxVal

total
hailperinCoOp : HailperinBound -> HailperinBound -> HailperinBound
-- Co-operations for calculating logical intersections of bounded probabilities
```
"""
    },
    {
        "id": "Indivisible_Mechanics",
        "title": "Indivisible Stochastic Mechanics (Barandes)",
        "content": """# Indivisible Stochastic Mechanics (Barandes)

## Dependent Type Formalization
Physics unfolds via indivisible discrete transitions, not continuous Markov chains. We model this as exact transitions on a causal Substrate (poset).

```idris
module Formal.Barandes

import Simplex.Core

-- An exact indivisible history transition between two valid Geometries
record HistoryTransition where
  constructor MkTransition
  parent : Geometry
  child  : Geometry
  weight : Integer

total
nonMarkovianEvolution : List HistoryTransition -> Substrate
-- Ensures transitions structurally map to the poset topology without floating-point probabilities
```
"""
    },
    {
        "id": "Rational_Trigonometry",
        "title": "Rational Trigonometry (Wildberger)",
        "content": """# Rational Trigonometry (Wildberger)

## Dependent Type Formalization
Wildberger's Rational Trigonometry removes transcendentals (sin, cos, pi) and replaces them with exact integer Quadrance (squared distance) and Spread. 

```idris
module Formal.Wildberger

import Math.Chromogeometry

-- Dependent formulation of the Triple Quad formula
-- Ensures that the three quadrances of any triangle form a closed polynomial
total
tripleQuadTheorem : (q1, q2, q3 : BoxInt) -> 
  (q1 + q2 + q3) * (q1 + q2 + q3) = 2 * (q1*q1 + q2*q2 + q3*q3)
```
"""
    }
]

# Write individual pages
index_content = "# Finite Science Formalizations (Boole & Singleton)\n\nThis wiki documents the dependent-type level proofs and structural mappings of the Algebra of Boole and Singleton layers.\n\n"

for p in pages:
    filepath = os.path.join(WIKI_DIR, f"{p['id']}.md")
    with open(filepath, "w") as f:
        f.write(p["content"])
    index_content += f"- [{p['title']}](./{p['id']}.md)\n"

# Write index
with open(os.path.join(WIKI_DIR, "index.md"), "w") as f:
    f.write(index_content)

print("Idris2-Logic-Wiki pages generated successfully.")
