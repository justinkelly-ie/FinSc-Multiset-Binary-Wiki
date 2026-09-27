module Wiki.Main

import System
import Wiki.BinaryScaleTransformSpec
import Stage0.Singleton.Bit

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
  putStrLn "========================================================"
  putStrLn "  MULTISET BINARY WIKI VERIFICATION COMPLETE: ALL PASSED!"
  putStrLn "========================================================"
