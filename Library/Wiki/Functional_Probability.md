# 🧮 Functional Probability — [Algebra of Boole](https://github.com/justinkelly-ie/Idris2-Boole)

> **Row 3 of the Global Finite Science Table**
>
> The normalization of unnormalized physical mass distributions into exact rational probability vectors. Row 3 replaces classical axiomatic probability theory with calculational minimums and maximums over closed finite spaces, using cross-multiplication instead of division to prevent precision loss.

---

## 🏛️ Theoretical Foundation: Hehner Normalization

This row implements the functional probability framework developed by Eric Hehner in *[a Probability Theory](http://www.cs.utoronto.ca/~hehner/aPT.pdf)*. 

In classical logic and physics, probability is typically introduced as a measure-theoretic axiom over infinite limits. In Hehner's model, probability is a derived **normalization** of unnormalized weights (such as the integer coefficients produced by a boolean circuit in Row 2). 

For each state element $e_i$ with an unnormalized weight $w_i$ in an environment $E$, its normalized probability $\overline{E}_i$ is defined as:

$$\overline{E}_i = w_i \cdot \left(\sum E\right)^{-1}$$

In our discrete finitist framework, we avoid floating-point numbers entirely. Probabilities are represented as exact fractions of integers: a signed weight numerator over a strictly positive natural sum denominator. 

---

## 🗃️ The MSetFraction Structure: Numerator and Denominator

Following the uniform architecture of the Global Finite Science Table, Row 3 is represented as an `MSetFraction` of multisets:

$$\text{MSetFraction} = \frac{\text{QUANTIFIED MSET} \;\{w \cdot [\text{valid}]\} \;\in \mathbb{Z}}{\text{TOTAL UNIVERSE SUM} \;\{\sum w \cdot [\text{all\_states}]\} \;\in \mathbb{N}^{+}}$$

In Row 1 and Row 2, the scale was locked to the unit constant ($1$). In Row 3, the denominator **generalizes to the total mass of the unnormalized distribution** ($\sum w$). This allows the probability scale to adjust dynamically based on the total weight of the sample space.

The `BitFraction` type enforces the structure of Row 3 in the singleton architecture, corresponding directly to the compiled type `MSetFractionVexel` in the [Logic.FunctionalProbability](file:///var/home/justin/Projects/Idris2-Logic/src/Logic/FunctionalProbability.idr#L55-L59) library:

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

## 🔄 Calculational Quantifiers: Replacing $\forall$ and $\exists$

In infinite set theory, logical deduction relies on quantifiers like "for all" ($\forall$) and "there exists" ($\exists$). Hehner replaces these with **calculational quantifiers** over the unnormalized weights of closed spaces:

*   **For All ($\forall$)** $\mapsto$ `minWeight`: The minimum unnormalized weight in the multiset.
*   **There Exists ($\exists$)** $\mapsto$ `maxWeight`: The maximum unnormalized weight in the multiset.

```idris
minWeight : Sing BoxInt a -> BoxInt
maxWeight : Sing BoxInt a -> BoxInt
```

This reduces logical quantifiers to simple, high-performance $O(N)$ structural scans over the multiset.

---

## 🧮 Algebra in Action: Divisionless Comparisons

Because probabilities are stored as exact fractions, we compare probabilities using cross-multiplication:

$$\frac{a}{b} > \frac{c}{d} \iff a \cdot d > c \cdot b \qquad (\text{for } b, d > 0)$$

This enables divisionless comparisons, preventing precision loss and rounding errors:

```idris
||| Check whether one probability dominates another.
gtProbability : MSetFraction -> MSetFraction -> Bool
gtProbability (MkMSF a b) (MkMSF c d) =
  (a * fromInteger (natToInteger d)) > (c * fromInteger (natToInteger b))
```

### Normalization Example
Given an unnormalized distribution of outcomes:

$$M = \{ \text{Heads} \mapsto 3, \text{Tails} \mapsto 5 \}$$

1. The total mass is $\sum M = 3 + 5 = 8$.
2. The normalized `BitFraction` is constructed as:
   $$\text{Space} = \frac{\{ \text{Heads} \mapsto 3, \text{Tails} \mapsto 5 \}}{8}$$
3. Normalizing the space yields the exact probabilities:
   *   $\text{P(Heads)} = 3/8$
   *   $\text{P(Tails)} = 5/8$
---

## 🔄 The Progression Bridge: Row 3 → Row 4

Functional probability assumes complete information about the state space weights. When information is incomplete, we can no longer assign single rational probabilities. In Row 4 (Probability Bounds / Hailperin), we wrap the numerator into min/max bounds (inclusion-exclusion corners), transitioning functional probability into exact polyhedral probability bounds.
