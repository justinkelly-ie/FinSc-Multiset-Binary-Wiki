# 💻 Singleton Lifted Polynumbers — [Algebra of Boole](https://github.com/justinkelly-ie/Idris2-Boole)

> **Row 2 Variant: Singleton-Based Lifted Polynumbers**
>
> An alternative formulation of the second layer of the Finite Science Table using 1-component Singleton coordinates. By transitioning weights from modulo-2 bi-field coefficients ($BF2$) to exact signed integers ($BoxInt$), the singleton structure lifts directly into Arithmetic Circuits while maintaining type-level division-by-zero protection.

---

## 🎛️ Types and Verification Test

At this positional layer, the states represent binary registers with integer weights.

### Type Definition

```idris
module Singleton_Lifted

import Math.Singleton.Sing
import Math.Vexel.Vexel
import Math.BoxInt
import Math.Vexel.DepVexel
import Math.Multiset
import Math.DepMaxel
import Math.Singleton.SingFraction

||| A positional arithmetic state numerator using BoxInt weights.
0 ArithmeticState : (state : Type) -> Type
ArithmeticState state = Sing BoxInt state

||| Denominator remains locked to TrivialBase for type safety.
0 ArithmeticDenom : Type
ArithmeticDenom = Sing1 BoxInt TrivialBase

||| A dependently typed arithmetic register state tracking coordinates at compile time.
0 DepArithmeticState : (state : Type) -> (xs : Vexel BoxInt state) -> Type
DepArithmeticState state xs = DepVexel BoxInt state (vexelToMSet xs)
```

### Verification Test: Positional Carriage

We verify the transition from Row 1 to Row 2 by checking that the binary wire singleton lifts into an integer singleton without losing information, allowing arithmetic addition to scale positions.

```idris
-- Verification property: lifting a full binary singleton maps it to weight 1
public export
prop_liftFullSingleton : Eq state => (s : state) ->
                         liftSingBitGateToBoxInt (OneS s One) = OneS s 1
```

---

## 🎨 Pipeline ASCII Art Graphic

```
 INPUT STATE                  TRANSFORMATION               ROUTING TEMPLATE             OUTPUT STATE
 (ArithmeticState)            (Boole Maxel)                (Positional SBF Maxel)        (ArithmeticState)
 [DepVexel BoxInt state xs]   [DepMaxel]                   [SBFMset Maxel]               [DepVexel BoxInt state ys]
 
 ┌───────────────┐            ┌───────────────┐            ┌──────────────────────┐     ┌───────────────┐
 │ Input Reg:    │            │ Shift Map:    │            │ Positional Scale:    │     │ Output Reg:   │
 │ [  2^i  ]     │            │ [a -> b] map  │            │ [2^0 -> 2^1 -> 2^n]  │     │ [  2^(i+1)  ] │
 └───────┬───────┘            └───────┬───────┘            └──────────┬───────────┘     └───────▲───────┘
         │                            │                               │                     │
         └─────────────┬──────────────┘                               │                     │
                       │ (Transitive composition)                     │                     │
                       ▼                                              │                     │
               ┌───────────────┐                                      │                     │
               │  Active Wire  ├──────────────────────────────────────┘                     │
               │  Junction     │  (Positional Carry-Over Scaling Zone)                      │
               └───────────────┘                                                            │
                       │                                                                    │
                       └─────────────────── Annihilation / Resolution ──────────────────────┘
```

---

## 📊 Step-by-Step Pipeline Table

| Step | Component | Role / Purpose | Type / Representation |
| :--- | :--- | :--- | :--- |
| **1** | **Input State** | Holds the input binary register states with integer coefficients. | `ArithmeticState state` / `DepVexel BoxInt state xs` |
| **2** | **Transformation** | The Boole-Möbius shift Maxel managing relational shift maps. | `Multiset BoxInt (SingRelation (LogicState state))` / `DepMaxel` |
| **3** | **Symmetric Bilinear Form** | Positional carry form mapping $2^0 \rightarrow 2^1 \rightarrow 2^n$. | `row2SBF = Multiset BoxInt (SingRelation (LogicState state))` / `DepMaxel` |
| **4** | **Output State** | The resolved output register state vector with carries resolved. | `ArithmeticState state` / `DepVexel BoxInt state ys` |

---

## 🔄 Row Relation & Progression: Row 2 → Row 3

*   **Row 2 (Positional Arithmetic)**: Evaluates register states over `BoxInt` (integers) with the scale bound to the unit constant ($1$ / `TrivialBase`).
*   **Transitioning to Row 3**: In Row 3 (Functional Probability), we lift the restriction of a fixed unit denominator. The denominator generalizes to the sum of all unnormalized state weights ($\sum w$), transforming absolute counts into exact rational probabilities ($w / \sum w$) and allowing the coordinate space to transition into normalized probability fields.
