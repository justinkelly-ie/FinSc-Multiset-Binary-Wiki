module Wiki.Generators

import public QuickCheck
import Math.BoxInt
import Math.Singleton.Bit

%default total

public export
Arbitrary Bit where
  arbitrary = map Math.Singleton.Bit.natToBit arbitrary

  coarbitrary b gen =
    if isOne b
       then coarbitrary (the Nat 1) gen
       else coarbitrary (the Nat 0) gen
