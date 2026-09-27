# 🎛️ Singleton Explainer

> **Architectural Overview of Singleton Multisets in Logical Layers**
>
> An explanation of the restricted multiset implementations (`Sing`/`Sing1`) and their dependently typed counterparts (`DepVexel`/`DepMultiset`) that formalize the logical layers of the Finite Science Table.

---

## 🎛️ Types and Verification Test

The Singleton type system uses two principal primitives to represent coordinates with size bounds, now complemented by dependently typed index-tracked variants:
*   `Sing c a`: Bounded to a size of at most 1 (either empty `ZeroS` or containing one item `OneS`).
*   `Sing1 c a`: Bounded to a size of exactly 1 (always containing one item `MkSing1`).
*   `DepVexel c a xs`: A dependently typed list of singletons tracking coordinate elements in the type signature `xs : List a`.

```idris
module Wiki.Logic_Explainer

import Stage0.Singleton.Sing
import Stage0.Vexel.Vexel
import Stage0.Vexel.DepVexel
import Stage0.Singleton.Bit
import Stage0.DepMultiset
import Stage0.BoxInt
import Stage0.Multiset

-- A dependently typed singleton of length exactly 1
0 DepSing1 : (a : Type) -> (token : Sing a) -> Type
DepSing1 a (MkSing x) = DepVexel a [x]

-- A dependently typed singleton of length at most 1 (xs is empty or a singleton)
0 DepSing : (a : Type) -> (xs : Vexel Bit a) -> Type
DepSing a xs = DepVexel a (vexelToMSet xs)
```

### Verification Test: Compile-Time Bounds Enforcer

We verify that the type system strictly prevents building values that exceed the designated singleton boundaries, ensuring division-by-zero protection.

```idris
-- Verification property: Sing1 cannot be empty (compilation failure if empty)
public export
prop_sing1NonEmpty : Sing1 a -> Bool
prop_sing1NonEmpty (MkSing coord) = True

-- Verification property: DepSing1 contains exactly one element
public export
prop_depSing1HasOne : {token : Sing a} -> DepSing1 a token -> Nat
prop_depSing1HasOne _ = 1
```

---

## 🎨 Singleton

```
  SINGLETON REGISTER (Sing c a)            Topological Base Anchor (Sing1 c a)
  ┌─────────────────────────────────┐      ┌─────────────────────────────────┐
  │  Sing/DepVexel c a xs: size ≤ 1 │      │  Sing1/DepVexel c a xs: size 1  │
  │                                 │      │                                 │
  │  [ ZeroS / [] ] or [ OneS / [x] ]      │         [ MkSing1 / [x] ]       │
  │     (Empty)          (Active)   │      │           (Unit Base)           │
  └────────┬────────────────────────┘      └────────────────┬────────────────┘
           │                                                │
           └───────────────────────┬────────────────────────┘
                                   ▼
                      (Cross-Multiplication & Collapse)
```

---

## 📊 Step-by-Step Pipeline Table

| Step | Component | Role / Purpose | Type / Representation |
| :--- | :--- | :--- | :--- |
| **1** | **Input State (Vexel)** | Bounded active wire states/switches. | `Sing c a` / `DepVexel c a xs` |
| **2** | **Denominator Anchor** | Prevents division-by-zero and locks the scale. | `Sing1 c a` / `DepVexel c a [base]` |
| **3** | **Symmetric Bilinear Form** | Dictates the local routing and collision pathways. | `SBFMset Maxel` / `DepMaxel` |
| **4** | **Output State (Vexel)** | The resolved singleton output state. | `Sing c a` / `DepVexel c a ys` |

---

## 🔄 Row Relation & Progression: Row 1 → Row 2 → Row 3

1.  **Row 1 (Singleton Logic)**: Bounded wire states are represented via `Sing Bit state` (using `Math.Singleton.Bit`). Collisions trigger modulo-2 annihilation.
2.  **Row 2 (Positional Arithmetic)**: We lift the weights to `Sing BoxInt state` or `DepVexel BoxInt state xs`. Instead of annihilating, collisions trigger carries to higher positional registers.
3.  **Row 3 (Rational Scales)**: The fixed denominator is lifted. The numerator and denominator generalise to arbitrary multisets (`MSetFraction` / `DepMultiset`), representing prime factors and exact rational probabilities.
