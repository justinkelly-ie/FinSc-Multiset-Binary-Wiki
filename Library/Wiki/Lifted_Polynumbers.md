# 💻 Lifted Polynumbers — [Algebra of Boole](https://github.com/justinkelly-ie/FinSc-Boole)

> **Row 2 of the Global Finite Science Table**

The transition from logical bit-gates to continuous arithmetic. By mapping modulo-2 logic fields into the integer polynomial plane, Row 2 provides the algebraic framework that underpins probability, rational trigonometry, and physical laws.

---

## 🏛️ Theoretical Foundation: The Polynomial Plane

This row implements the algebraic mapping of Boolean functions into integer polynomials, as described by Norman Wildberger in his lecture series *[Algebra of Boole](https://www.youtube.com/playlist?list=PLIljB45xT85A-qCypcmZqRvamiF-FYLPv)* (Lectures 256, 264, and 270–272). 

The key insight is that any Boolean function $f: B_2^n \to B_2$ can be uniquely represented as a multilinear polynomial over $\mathbb{Z}$:

$$p(x_1, x_2, \dots, x_n) = \sum_{I \subseteq \{1,\dots,n\}} c_I \prod_{i \in I} x_i$$

where the coefficients $c_I$ are integers. This is known as the **Algebraic Normal Form (ANF)**. Because coordinates in this layer are integers ($\mathbb{Z}$), we can represent operations using standard subtraction, addition, and multiplication, avoiding the constraints of modulo-2 bit arithmetic while preserving exactness.

---

## 🗃️ The MSetFraction Structure: Numerator and Denominator

Following the uniform architecture of the Global Finite Science Table, Row 2 is represented as an `MSetFraction` of multisets:

$$\text{MSetFraction} = \frac{\text{TRUTH TABLE COEFFICIENTS} \;\{w \cdot [\text{Monomial}]\} \;\in \mathbb{Z}}{\text{UNIT CONSTANT} \;\{1 \cdot [\text{Base}]\} \;\in \mathbb{Z}}$$

For Row 2 specifically, the fraction is structured as:
- **Numerator Box:** `LiftedPolynumber v` — an integer-weighted multiset of monomials, representing terms like $1 - x - y + xy$ using `BoxInt`.
- **Denominator Box:** `Multiset BoxInt TrivialBase` — locked to the unit constant $\{1 \cdot [\text{Base}]\}$.
- **Compile-Time Constraint:** A dependent type proof (`isTrivial`) verifies that the denominator is exactly `theUnitConstantZ`, preventing scale deviation.

```idris
module Wiki.Lifted_Polynumbers

import Stage0.Multiset
import Stage0.BoxInt
import Stage0.Singleton.Sing
import Stage1.LiftedPolynumber

%default total
```

---

## 🎓 The Core Types

### 1. `Monomial v` — Product Terms
**File:** `Boole/LiftedPolynumber.idr` | **Source:** Wildberger Lecture 256

Instead of character strings, a monomial (such as $xy$ or $xyz$) is modeled as a multiset of variable tokens of type `v` with `BoxInt` counts:

```text
Monomial : Type -> Type
Monomial v = Multiset BoxInt v
```

### 2. `LiftedPolynumber v` — The Numerator Box
**File:** `Boole/LiftedPolynumber.idr` | **Source:** Wildberger Lecture 264

A lifted polynumber polynomial is a linear combination of these monomials, weighted by algebraic integers (`BoxInt`):

```text
record LiftedPolynumber (v : Type) where
  constructor MKPolynumber
  underlyingPolynomial : Multiset BoxInt (Monomial v)
```

---

## 🔄 The Combinatorial Mechanism: Idempotent Collapse

When multiplying monomials or calculating Möbius transforms, variables can duplicate ($x \cdot x = x^2$). In standard algebra, this raises the degree. In the Algebra of Boole, Wildberger's algorithm enforces the **idempotent rule**:

$$x^2 = x$$

Our implementation enforces this structural rule at the data-type level via `idempotentCollapse`, clamping positive counts down to exactly 1 and pruning non-positive counts:

```text
idempotentCollapse : Eq v => Monomial v -> Monomial v
idempotentCollapse mono =
  let entries = multisetToList mono
      collapsedEntries = concatMap (\(var, count) => if count > 0 then [(var, 1)] else []) entries
  in fromList collapsedEntries
```

---

## 🧮 Algebra in Action: Arithmetic Circuit Conversions

Under the polynomial mapping, logic gates map directly to arithmetic operations over $\mathbb{Z}$:

| Logic Gate | Boolean Ring Form (Row 1) | Arithmetic Polynomial Form (Row 2) |
|---|---|---|
| **NOT $x$** | $1 + x$ | $1 - x$ |
| **AND($x,y$)** | $xy$ | $xy$ |
| **XOR($x,y$)** | $x + y$ | $x + y - 2xy$ |
| **OR($x,y$)** | $x + y + xy$ | $x + y - xy$ |
| **NAND($x,y$)** | $1 + xy$ | $1 - xy$ |

### Monomial Multiplication Example
Multiplying the monomial $(xy)$ by $(yz)$ yields:

$$(xy) \cdot (yz) \mapsto x \cdot y^2 \cdot z \xrightarrow{\text{idempotentCollapse}} xyz$$

This is handled automatically by `mulMonomial`:
```text
mulMonomial : Eq v => Monomial v -> Monomial v -> Monomial v
mulMonomial m1 m2 = idempotentCollapse (addMultiset m1 m2)
```

---

## 🔄 The Boole-Möbius Shift Pipeline

Transitioning between the truth table values (evaluation points) and the polynomial coefficients requires the integer-valued Möbius transform:

```text
||| Forward transform: computes truth table evaluations from polynomial coefficients.
mobiusTransformZ : List BoxInt -> List BoxInt

||| Inverse transform: recovers polynomial coefficients from a dense truth table.
mobiusInverseZ : List BoxInt -> List BoxInt
```

### Transition to Row 3 (Functional Probability)

Because the polynomial plane supports negative integer weights (like $-2xy$ in XOR), it is capable of tracking overlapping boundary conditions. In Row 3, Hehner normalization sums these coefficients over a variable sample space denominator (\\sum w), transforming the arithmetic circuits of Row 2 into exact, rational probability distributions.
