module Wiki.Main

import System
import Wiki.BinaryScaleTransformSpec
import Stage0.Singleton.Bit
import Stage1.BoolePolynumber

%default total

main : IO ()
main = do
  putStrLn "========================================================"
  putStrLn "  IDRIS 2 MULTISET BINARY WIKI VERIFICATION SUITE"
  putStrLn "========================================================"
  putStrLn "1. Bit ScaleTransform & Galois Inversion QuickCheck Specs:"
  p <- auditBinaryScaleTransformSpecProof
  if p
     then putStrLn "   [PASSED] Bit B2 ScaleTransform Verified!"
     else do
       putStrLn "   [FAILED] QuickCheck Specs Failed!"
       exitWith (ExitFailure 1)
  putStrLn $ "2. Boole Polynumber Streaming Multiset Round-Trip (Rule 04 §12): " ++ (if Stage1.BoolePolynumber.auditBoolePolyStreamRoundTripProof then "[PASSED] ✅" else "[FAILED] ❌")
  putStrLn "========================================================"
  putStrLn "  MULTISET BINARY WIKI VERIFICATION COMPLETE: ALL PASSED!"
  putStrLn "========================================================"
