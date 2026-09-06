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

public export
qc : (Arbitrary a, Show a, Testable prop) => (a -> prop) -> QCRes
qc f = quickCheck (MkFn f)

public export
qc2 : (Arbitrary a, Show a, Arbitrary b, Show b, Testable prop) => (a -> b -> prop) -> QCRes
qc2 f = quickCheck (MkFn (\x => MkFn (f x)))
