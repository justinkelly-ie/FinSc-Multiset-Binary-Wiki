# Probability Bounds (Hailperin)

## Dependent Type Formalization
Hailperin probability bounds replace exact probabilities with bounded min/max intervals, structurally encoded as pairs of Multisets.

```idris
module Probability_Bounds

import Data.So

-- Bounded interval structurally guaranteed to be valid (Min <= Max)
public export
record HailperinBound where
  constructor MkBound
  minVal : Integer
  maxVal : Integer
  prf    : So (minVal <= maxVal)

public export
hailperinCoOp : HailperinBound -> HailperinBound -> HailperinBound
hailperinCoOp b1 b2 = b1
```
