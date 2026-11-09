module Wiki.Generators

import public QuickCheck
import Stage0.BoxInt
import Stage0.Bit

%default total

public export
Arbitrary Bit where
  arbitrary = map natToBit arbitrary

  coarbitrary b gen =
    if isOne b
       then coarbitrary (the Nat 1) gen
       else coarbitrary (the Nat 0) gen
