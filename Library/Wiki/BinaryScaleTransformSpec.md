# Multiset Binary ScaleTransform & B₂ Field Verification

```idris
module Wiki.BinaryScaleTransformSpec

import Math.BoxInt
import Core.ScaleTransform
import Math.Singleton.Bit
import Wiki.Generators
import public QuickCheck

%default total
```

## ScaleTransform & InvertibleScaleTransform Instances

```idris
public export
ScaleTransform Bit Nat where
  scaleTransform b = if isOne b then 1 else 0

public export
InvertibleScaleTransform Bit Nat where
  invertScaleTransform Z = Zero
  invertScaleTransform (S _) = One
```

## QuickCheck Verification Properties

```idris
public export
prop_bitScaleTransformBounded : Bit -> Bool
prop_bitScaleTransformBounded b =
  let z : Nat = scaleTransform b
  in z <= 1

public export
prop_bitInvertScaleAdjunction : Bit -> Bool
prop_bitInvertScaleAdjunction b =
  let z : Nat = scaleTransform b
      b' : Bit = invertScaleTransform z
  in b' == b

public export
prop_bitObservablePreserved : Bit -> Bool
prop_bitObservablePreserved b =
  let z : Nat = scaleTransform b
  in z == Math.Singleton.Bit.bitToNat b

public export
auditBinaryScaleTransformSpecProof : IO Bool
auditBinaryScaleTransformSpecProof = do
  let r1 = qc prop_bitScaleTransformBounded
  let r2 = qc prop_bitInvertScaleAdjunction
  let r3 = qc prop_bitObservablePreserved
  pure (r1.pass == Just True && r2.pass == Just True && r3.pass == Just True)
```
