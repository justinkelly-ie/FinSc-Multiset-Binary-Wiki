# Probability Bounds (Hailperin)

## Dependent Type Formalization
Hailperin probability bounds replace exact probabilities with bounded min/max intervals, structurally encoded as pairs of Multisets.

```idris
module Formal.Hailperin

-- Bounded interval structurally guaranteed to be valid (Min <= Max)
record HailperinBound where
  constructor MkBound
  minVal : Integer
  maxVal : Integer
  prf    : minVal <= maxVal

total
hailperinCoOp : HailperinBound -> HailperinBound -> HailperinBound
-- Co-operations for calculating logical intersections of bounded probabilities
```
