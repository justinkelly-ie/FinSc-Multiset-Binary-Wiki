# Rational Trigonometry (Wildberger)

## Dependent Type Formalization
Wildberger's Rational Trigonometry removes transcendentals (sin, cos, pi) and replaces them with exact integer Quadrance (squared distance) and Spread. 

```idris
module Formal.Wildberger

import Math.Chromogeometry

-- Dependent formulation of the Triple Quad formula
-- Ensures that the three quadrances of any triangle form a closed polynomial
total
tripleQuadTheorem : (q1, q2, q3 : BoxInt) -> 
  (q1 + q2 + q3) * (q1 + q2 + q3) = 2 * (q1*q1 + q2*q2 + q3*q3)
```
