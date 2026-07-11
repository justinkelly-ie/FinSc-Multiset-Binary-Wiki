# The Boole-Möbius Transform — Sir Galahad's Deduction

This module implements Norman Wildberger's **Sir Galahad puzzle** (Lecture 279)
using the Boole-Möbius transform over an `OnTruthTable` ongoing sequence. It
demonstrates how the pointwise truth-table method resolves propositional
deductions mechanically, without clever identity manipulation.

```idris
module Finite_Science.Boole_mobius_transform

import QuickCheck
import Data.List
import Data.Nat
import Math.Singleton.Sing
import Math.BoxInt
import Math.Multiset
import Math.OnSeq.OnMSet
import Math.Singleton.Bit
import Math.Vexel.Byte
import Singleton.MobiusTransform

%default total
```

## 1. The Puzzle

Sir Galahad comes to a fork with three roads: **G**rail, **M**arble, **S**tone.
Two knights guard two roads and make declarations. Since they are liars, every
statement must be negated. We encode three Boolean variables:

| Variable | Meaning |
|----------|---------|
| `g` | The marble road leads to the Grail |
| `m` | The stone road does not lead to the Grail |
| `s` | The marble road will lead you astray |

After translating the liars' declarations into Boole algebra and applying Boole
reduction, the three premises become:

| Premise | Boole polynumber |
|---------|-----------------|
| X | `g * s` |
| Y | `g` |
| Z | `g + m + g*m` |

The conjunction of all three premises is the pointwise product `X * Y * Z`
across the truth table.

## 2. The OnTruthTable Approach

Rather than symbolically multiplying three polynomials, we:
1. Represent each premise as a **truth table vector** of length $2^3 = 8$.
2. **Multiply pointwise** (component-wise AND in B₂).
3. Check which conclusion column is implied by the product column.

The 8-row ordering follows binary encoding: row `i` has
`g = bit₀(i)`, `m = bit₁(i)`, `s = bit₂(i)`.

```idris
||| Pointwise product (* in B₂) of two truth-table vectors.
export
pointwiseMul : Byte Nat -> Byte Nat -> Byte Nat
pointwiseMul = mulByte

||| True iff the deduction is valid.
||| In the B₂ lattice: p * (1 + c) = min(p, ¬c).
||| Its inverse (1 + p*(1+c)) = p ⇒ c as a Boole polynumber.
||| Folding by * gives min over all rows of (inverse of min(p, ¬c)).
||| This equals 1 iff max(min(p, ¬c)) = 0 — the remainder vanishes.
export
implies : Byte Nat -> Byte Nat -> Bool
implies product conclusion =
  let terms = map (\i =>
                let p = lookupWeight i product
                    c = lookupWeight i conclusion
                in addBVal One (mulBVal p (addBVal One c))) [0..7]
  in foldl mulBVal One terms == One
```

## 3. Encoding the Premises

```idris
||| Extract bit position k of a natural number as a BVal.
bitOf : Integer -> Integer -> BVal
bitOf 0 n = if n `mod` 2 == 0 then Zero else One
bitOf k n = bitOf (assert_smaller k (k - 1)) (n `div` 2)

||| Build a length-8 truth table from a 3-variable boolean function.
||| Row i: g = bit0(i), m = bit1(i), s = bit2(i).
truthTable3 : (BVal -> BVal -> BVal -> BVal) -> Byte Nat
truthTable3 f = map (\i =>
  let val = f (bitOf 0 (cast i)) (bitOf 1 (cast i)) (bitOf 2 (cast i))
  in if val == One then OneS i One else ZeroS) [0..7]

-- Premise X: g * s
export
premiseX : Byte Nat
premiseX = truthTable3 (\g, _, s => g * s)

-- Premise Y: g
export
premiseY : Byte Nat
premiseY = truthTable3 (\g, _, _ => g)

-- Premise Z: g + m + g*m  (= g OR m in Boole algebra)
export
premiseZ : Byte Nat
premiseZ = truthTable3 (\g, m, _ => g + m + g * m)

||| Conjunction of all three premises (pointwise product X * Y * Z).
export
conjPremises : Byte Nat
conjPremises = pointwiseMul (pointwiseMul premiseX premiseY) premiseZ
```

## 4. Candidate Conclusions

```idris
-- Conclusion G: g
export
concG : Byte Nat
concG = truthTable3 (\g, _, _ => g)

-- Conclusion M: m
export
concM : Byte Nat
concM = truthTable3 (\_, m, _ => m)

-- Conclusion S: s
export
concS : Byte Nat
concS = truthTable3 (\_, _, s => s)
```

## 5. The Deduction Property

Wildberger shows that among the three candidates, **only S is validly implied**:
Sir Galahad should take the **stone road**.

In the Algebra of Boole, negation of a truth value `v ∈ B₂` is written `1 + v`
(addBVal One v), and conjunction is multiplication (`mulBVal`). The deduction
"¬G ∧ ¬M ∧ S" becomes:

$$\text{result} = (1 + v_G) \cdot (1 + v_M) \cdot v_S = 1$$

```idris
||| Lift a Bool result into B₂ for use in Boole algebra expressions.
boolToBVal : Bool -> BVal
boolToBVal True  = One
boolToBVal False = Zero

||| Verify the Galahad deduction using only the Algebra of Boole.
||| ¬validG ∧ ¬validM ∧ validS = (1 + vG) * (1 + vM) * vS = 1.
export
prop_galadhadChoosesStone : Property
prop_galadhadChoosesStone =
  let vG = boolToBVal (implies conjPremises concG)
      vM = boolToBVal (implies conjPremises concM)
      vS = boolToBVal (implies conjPremises concS)
  in property (mulBVal (mulBVal vG (addBVal One vM)) vS == One)
```

## 6. OnTruthTable: Self-Inverse Verification

The Boole-Möbius transform $T$ is self-inverse: $T^2 = I$. We verify this
over the premise conjunction by wrapping it in a constant `OnTruthTable`
(an ongoing sequence that always returns the same truth table), transforming
twice, and checking recovery:

```idris
||| Premise conjunction as a constant ongoing truth-table sequence.
galadhadOnSeq : OnTruthTable
galadhadOnSeq = constant 0 conjPremises

||| The Boole-Möbius transform of the premise conjunction.
mobiusGalahad : OnTruthTable
mobiusGalahad = mobiusTransformOnSeq galadhadOnSeq

||| Verify that applying the transform twice recovers the original truth table.
export
prop_mobiusSelfInverseOnSeq : Property
prop_mobiusSelfInverseOnSeq =
  case getTerm (mobiusTransformOnSeq mobiusGalahad) 0 of
    Nothing   => property False
    Just recovered => property (recovered == conjPremises)
```
