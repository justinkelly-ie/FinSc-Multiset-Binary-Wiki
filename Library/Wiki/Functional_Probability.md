# 🧮 Functional Probability — [Algebra of Boole](https://github.com/justinkelly-ie/FinSc-Boole)

> **Row 3 / Row 4 of the Global Finite Science Table**

The normalization of unnormalized physical mass distributions into exact rational probability vectors. Replaces classical axiomatic probability theory with calculational minimums and maximums over closed finite spaces, using cross-multiplication instead of division to prevent precision loss.

```idris
module Wiki.Functional_Probability

import QuickCheck
import Stage0.Multiset
import Stage0.BoxInt
import Stage0.SignedFraction
import Stage1.FunctionalProbability

%default covering

||| Verified Hehner conditional probability: P(Both Girls | At Least One Girl)
public export
prop_atLeastOneGirlProb : Property
prop_atLeastOneGirlProb =
  property (probBothGirlsGivenAtLeastOne == MkMSF 1 1)

||| Verified Hehner conditional probability: P(Both Girls | Older Child Girl)
public export
prop_olderGirlProb : Property
prop_olderGirlProb =
  property (probBothGirlsGivenOlderGirl == MkMSF 1 1)

||| Verified Bertrand's Box Paradox: P(Other Side Red | Observed Red)
public export
prop_bertrandBoxProb : Property
prop_bertrandBoxProb =
  property (probOtherSideRed == MkMSF 2 2)
```

---

## 🏛️ Theoretical Foundation: Hehner Normalization

This row implements the functional probability framework developed by Eric Hehner in *[a Probability Theory](http://www.cs.utoronto.ca/~hehner/aPT.pdf)*. 

In classical logic and physics, probability is typically introduced as a measure-theoretic axiom over infinite limits. In Hehner's model, probability is a derived **normalization** of unnormalized weights (such as the integer coefficients produced by a boolean circuit in Row 2). 

For each state element $e_i$ with an unnormalized weight $w_i$ in an environment $E$, its normalized probability $\overline{E}_i$ is defined as:

$$\overline{E}_i = w_i \cdot \left(\sum E\right)^{-1}$$

In our discrete finitist framework, we avoid floating-point numbers entirely. Probabilities are represented as exact fractions of integers: a signed weight numerator over a strictly positive natural sum denominator. 

---

## 🗃️ The MSetFraction Structure: Numerator and Denominator

Following the uniform architecture of the Global Finite Science Table, Row 3/4 is represented as an `MSetFraction` of multisets:

$$\text{MSetFraction} = \frac{\text{QUANTIFIED MSET} \;\{w \cdot [\text{valid}]\} \;\in \mathbb{Z}}{\text{TOTAL UNIVERSE SUM} \;\{\sum w \cdot [\text{all\_states}]\} \;\in \mathbb{N}^{+}}$$

In Row 1 and Row 2, the scale was locked to the unit constant ($1$). In Row 3/4, the denominator **generalizes to the total mass of the unnormalized distribution** ($\sum w$). This allows the probability scale to adjust dynamically based on the total weight of the sample space.

---

## 🎓 The Core Functions

### 1. `stateProbability` — Exact State Probability
**File:** `Logic/FunctionalProbability.idr` | **Source:** Eric Hehner, *a Probability Theory*

Extracts the exact normalized probability of a single state as an `MSetFraction` containing a signed numerator and positive natural denominator:

```idris
||| Verified stateProbability extraction on normalized vexel space
public export
prop_stateProbabilityExtraction : Property
prop_stateProbabilityExtraction =
  property (stateProbability atLeastOneGirl (Girl, Girl) == MkMSF 1 1)
```

### 2. `normalizeFraction` — Distribution Normalizer
**File:** `Logic/FunctionalProbability.idr` | **Source:** Eric Hehner, *a Probability Theory*

Decomposes the full normalised space into a list of association pairs mapping each state to its exact probability:

```idris
||| Verified normalizeFraction distribution decomposition
public export
prop_normalizeFractionDecomposition : Property
prop_normalizeFractionDecomposition =
  property (normalizeFraction atLeastOneGirl == [((Girl, Girl), MkMSF 1 1)])
```

---

## 🔄 Calculational Quantifiers: Replacing $\forall$ and $\exists$

In infinite set theory, logical deduction relies on quantifiers like "for all" ($\forall$) and "there exists" ($\exists$). Hehner replaces these with **calculational quantifiers** over the unnormalized weights of closed spaces:

*   **For All ($\forall$)** $\mapsto$ `minWeight`: The minimum unnormalized weight in the multiset.
*   **There Exists ($\exists$)** $\mapsto$ `maxWeight`: The maximum unnormalized weight in the multiset.

---

## 🧮 Algebra in Action: Divisionless Comparisons

Because probabilities are stored as exact fractions, we compare probabilities using cross-multiplication:

$$\frac{a}{b} > \frac{c}{d} \iff a \cdot d > c \cdot b \qquad (\text{for } b, d > 0)$$

This enables divisionless comparisons, preventing precision loss and rounding errors:

```idris
||| Verified divisionless probability comparison: 2/3 > 1/2
public export
prop_gtProbabilityComparison : Property
prop_gtProbabilityComparison =
  property (gtProbability (MkMSF 2 3) (MkMSF 1 2) == True)
```

### Normalization Example
Given an unnormalized distribution of outcomes:

$$M = \{ \text{Heads} \mapsto 3, \text{Tails} \mapsto 5 \}$$

1. The total mass is $\sum M = 3 + 5 = 8$.
2. Normalizing the space yields the exact probabilities:
   *   $\text{P(Heads)} = 3/8$
   *   $\text{P(Tails)} = 5/8$

---

## 🔄 The Progression Bridge: Row 3 → Row 4

Functional probability assumes complete information about the state space weights. When information is incomplete, we can no longer assign single rational probabilities. In Row 4 (Probability Bounds / Hailperin), we wrap the numerator into min/max bounds (inclusion-exclusion corners), transitioning functional probability into exact polyhedral probability bounds.
