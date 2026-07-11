# 🎛️ Singleton Repetition — [Algebra of Boole](https://github.com/justinkelly-ie/Idris2-Boole)

> **Row 1 Variant: Singleton-Based Digital Repetition**
>
> An alternative formulation of the foundational logic layer using 1-component Singleton coordinates. This mirrors the node-based wire states directly at the type level, establishing type-level division-by-zero protection.

---

## 🎛️ Types and Verification Test

This variant utilizes restricted singleton types `Sing` and `Sing1` to guarantee at compile-time that registers contain at most one element, and denominators are non-zero.

### Type Definition

```idris
module Singleton_Repetition

import Math.Singleton.Sing
import Math.Vexel.Vexel
import Math.Vexel.DepVexel
import Math.BoxInt
import Math.Multiset
import Math.Singleton.SingFraction
import Math.Vexel.Byte
```

### Verification Test: Modulo-2 Annihilation

Under modulo-2 addition (`addVexels`), identical active singleton bits in the Vexel must undergo parity collapse and annihilate each other.

```idris
-- Verification property: adding two identical active singletons annihilates them
public export
prop_modulo2Collapse : Eq state => (s : state) -> (w : BVal) ->
                       addVexels [OneS s w] [OneS s w] = []
```

---

## Pipeline 

```
 INPUT STATE                  TRANSFORMATION               ROUTING TEMPLATE             OUTPUT STATE
 (Byte)                       (Boole Maxel)                (Parity SBF Maxel)           (Byte)
 [DepByte state xs]           [DepMaxel]                   [SBFMset Maxel]              [DepByte state ys]
 
 ┌───────────────┐            ┌───────────────┐            ┌──────────────────────┐     ┌───────────────┐
 │ Input Vexel:  │            │ Logic Maxel:  │            │ Parity Junction:     │     │ Output Vexel: │
 │ [  [[]]  ]    │            │ [a -> b] map  │            │ [ [[]], [[]] ≡ [] ]  │     │ [   []   ]    │
 └───────┬───────┘            └───────┬───────┘            └──────────┬───────────┘     └───────▲───────┘
         │                            │                               │                     │
         └─────────────┬──────────────┘                               │                     │
                       │ (Transitive composition)                     │                     │
                       ▼                                              │                     │
               ┌───────────────┐                                      │                     │
               │  Active Wire  ├──────────────────────────────────────┘                     │
               │  Junction     │  (Modulo-2 Parity Collision Zone)                          │
               └───────────────┘                                                            │
                       │                                                                    │
                       └─────────────────── Annihilation / Resolution ──────────────────────┘
```

---

## 📊 Step-by-Step Pipeline Table

| Step | Component | Role / Purpose | Type / Representation |
| :--- | :--- | :--- | :--- |
| **1** | **Input State** | Holds the active wire signals as singletons. | `Byte state` / `DepByte state xs` |
| **2** | **Transformation** | The Boole Maxel mapping inputs to outputs via logic gates. | `TransformationMSet state = Multiset BF2 (SingRelation (LogicState state))` / `DepMaxel` |
| **3** | **Symmetric Bilinear Form** | Enforces the 1x1 parity junction constraint. | `row1SBF = Multiset BF2 (Pixel Blue Coord1D)` / `DepMaxel` |
| **4** | **Output State** | The resolved output wire state vector. | `Byte state` / `DepByte state ys` |

---

## 🔄 Row Relation & Progression: Row 1 → Row 2

*   **Row 1 (Singleton Logic)**: Maps logical coordinates using `BF2` coefficients (which wrap `Sing Integer ()`). Collisions force duplicate wire states to collapse back into `[]` (Logical XOR/Inversion).
*   **Transitioning to Row 2**: When we transition to Row 2, the coefficients are promoted from `BF2` to `BoxInt` (integers), and the denominator unit expands from `Sing1 BF2 TrivialBase` to `Sing1 BoxInt TrivialBase`. This enables weights to accumulate, turning binary wire signals into positional place values and binary carry registers (Arithmetic Circuits).
