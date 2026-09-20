# Boole Functions

This chapter formalizes Norman Wildberger's definition of Boolean functions as mappings $B_2^n \to B_2$, represented as truth tables and linked with polynomials via the Boole-Möbius transform.

```idris
module Wiki.Boole_Function

import QuickCheck
import Data.List
import Math.Singleton.Sing
import Math.BoxInt
import Math.Multiset
import Math.Singleton.Bit
import Logic.BooleFunction
import Logic.BoolePolynumber
import Logic.MobiusTransform

%default total
```

## 1. Mathematical Representation
Under Norman Wildberger's **Algebra of Boole**, a Boolean function is a map from the Byfield space $B_2^n$ to $B_2$. Since there are $2^n$ distinct inputs, the function is represented by a dense list/vector of $2^n$ output values in $B_2$:

1. **Evaluation**: For any input binary tuple $x \in B_2^n$, the output is looked up at the corresponding binary index of the truth table.
2. **Boole-Möbius Isomorphism**: The Boole evaluation theorem asserts an isomorphism between Boolean functions and multilinear Boole polynumbers of degree at most 1:
   $$\text{BooleFunction} \longleftrightarrow \text{BoolePolynumber}$$
   The mapping is defined by the self-inverse Boole-Möbius transform matrix.

## 2. Properties and Verification
We verify evaluation correctness and the polynomial isomorphism via property-based tests:

```idris
||| Verify that evaluating a BooleFunction yields the correct truth table value.
export
prop_evalCorrect : Property
prop_evalCorrect = forAll {a = List Bool} {prop = Bool} arbitrary (MkFn (\bools =>
  let tableBool = take 4 (bools ++ replicate 4 False)
      vals = map (\b => if b then One else Zero) tableBool
      func = MkBooleFunction 2 vals
      in0 = [the Bit Zero, the Bit Zero]
      in1 = [the Bit Zero, One]
      in2 = [One, the Bit Zero]
      in3 = [One, One]
  in (evaluate func in0 == fromMaybe Zero (lookupIndex 0 vals)) &&
     (evaluate func in1 == fromMaybe Zero (lookupIndex 1 vals)) &&
     (evaluate func in2 == fromMaybe Zero (lookupIndex 2 vals)) &&
     (evaluate func in3 == fromMaybe Zero (lookupIndex 3 vals))))

||| Verify the isomorphism between BooleFunction and BoolePolynumber.
export
prop_polynumberIsomorphism : Property
prop_polynumberIsomorphism = forAll {a = List Bool} {prop = Bool} arbitrary (MkFn (\bools =>
  let tableBool = take 4 (bools ++ replicate 4 False)
      vals = map (\b => if b then One else Zero) tableBool
      func = MkBooleFunction 2 vals
  in truthTable (fromPolynumber 2 (toPolynumber func)) == vals))
```
