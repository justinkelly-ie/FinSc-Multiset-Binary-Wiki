module Main

import QuickCheck
import Logic_Explainer
import Logic_Repetition
import Bit_vexel
import Boole_Function
import Boole_mobius_transform
import Engine_Verification
import Information_As_Probability
import Cross_Entropy_And_Compression
import Hehner_Normalization

import System.File
import Data.String
import Math.Singleton.Bit
import Math.BoxInt
import Math.Multiset
import Math.Singleton.Sing

%default covering

boolToBit : Bool -> Bit
boolToBit True = One
boolToBit False = Zero

bitToString : Bit -> String
bitToString x = if isOne x then "1" else "0"

markdownTable : List (String, String, QCRes) -> String
markdownTable results =
  let header = "| Test | Description | Status | Details |\n|------|-------------|--------|---------|\n"
      rows = concat $ map formatRow results
  in header ++ rows
  where
    formatRow : (String, String, QCRes) -> String
    formatRow (name, desc, res) =
      let statusStr = case pass res of
                        Nothing => "❓ Unknown"
                        Just True => "✅ PASS"
                        Just False => "❌ FAIL"
      in "| " ++ name ++ " | " ++ statusStr ++ " | " ++ trim (msg res) ++ " |\n"

partial
main : IO ()
main = do
  putStrLn "Starting Idris2-Boole-Wiki QuickCheck Suite...\n"
  
  putStrLn "Running Test 1: Boole Function Evaluation Correctness"
  let resBF1 = quickCheck Boole_Function.prop_evalCorrect
  
  putStrLn "Running Test 2: Boole Function & Polynumber Isomorphism"
  let resBF2 = quickCheck Boole_Function.prop_polynumberIsomorphism
  
  putStrLn "Running Test 3: Sir Galahad's Deduction (Stone Road)"
  let resBF3 = quickCheck Boole_mobius_transform.prop_galadhadChoosesStone
  
  putStrLn "Running Test 4: Boole-Möbius Transform Self-Inverse on Sequence"
  let resBF4 = quickCheck Boole_mobius_transform.prop_mobiusSelfInverseOnSeq

  putStrLn "Running Test 5: Hehner Surprisal (1/4 Prob = 2 Bits)"
  let resInf1 = quickCheck Information_As_Probability.prop_studentQuarterSurprisal

  putStrLn "Running Test 6: Non-Negative Surprisal"
  let resInf2 = quickCheck Information_As_Probability.prop_studentSurprisalNonNegative

  putStrLn "Running Test 7: KL-Divergence Zero Loss (D_KL = 0)"
  let resCE1 = quickCheck Cross_Entropy_And_Compression.prop_studentKLZeroLoss

  putStrLn "Running Test 8: Hutter Curriculum Compression Ratio (4:1)"
  let resCE2 = quickCheck Cross_Entropy_And_Compression.prop_studentCompressionRatio

  putStrLn "Running Test 9: Hehner Normalization Operator (↕E = E / ∑E)"
  let resHN1 = quickCheck Hehner_Normalization.prop_studentNormalizeOperator

  putStrLn "Running Test 10: Normalized Distribution Bit Surprisal"
  let resHN2 = quickCheck Hehner_Normalization.prop_studentNormalizedSurprisal

  let tableStr = markdownTable [
        ("Boole Function Eval", "Verifies that evaluating a BooleFunction yields the correct truth table value.", resBF1),
        ("Polynumber Isomorphism", "Verifies the algebraic isomorphism between BooleFunction and BoolePolynumber via Möbius transform.", resBF2),
        ("Sir Galahad's Deduction", "Verifies that Sir Galahad's logical premises imply he must choose the stone road.", resBF3),
        ("Möbius Self-Inverse", "Verifies that the Boole-Möbius transform is self-inverse when mapped over an ongoing sequence.", resBF4),
        ("Hehner Surprisal (1/4)", "Verifies that a 1/4 probability outcome has exact surprisal of 2 bits under p = 2^-I.", resInf1),
        ("Surprisal Non-Negativity", "Verifies that self-information bits remain non-negative over multiset fractions.", resInf2),
        ("KL Zero Loss (D_KL = 0)", "Verifies zero KL divergence loss for exact discrete multiset cross-multiplication.", resCE1),
        ("Hutter Compression (4:1)", "Verifies 4:1 description length compression of multiset representations over 64-bit float vectors.", resCE2),
        ("Hehner Normalization ↕E", "Verifies that Hehner's ↕E operator scales raw multiset weights into exact probability fractions.", resHN1),
        ("Normalized Surprisal", "Verifies exact bit surprisal calculation over normalized multiset distributions.", resHN2)
      ]
  
  let preamble = unlines [
        "# Algebra of Boole & Singleton Verification Matrix",
        "",
        "This matrix tracks the automated testing suite for the Algebra of Boole, Singleton representation, Information Theory, and Möbius Transform modules.",
        "",
        "### Core Concepts",
        "* **Boolean Ring**: Every logical value is modeled as mod-2 addition (XOR) and multiplication (AND), allowing self-inverse subtraction and exact algebraic reduction.",
        "* **Möbius Transform**: Maps truth-table evaluations to unique polynumber coefficients, replacing SAT solving with direct comparison.",
        "* **Hehner Information Paradigm**: Defines probability in terms of memory bits (p = 2^-I), turning surprisal into exact integer bit counts.",
        "* **Cross-Entropy & Hutter Compression**: Proves exact zero KL-divergence loss (D_KL = 0) and 4:1 Kolmogorov description length savings over continuous floating-point models.",
        "",
        "---",
        ""
      ]
  
  putStrLn "\n--- Test Results ---"
  putStrLn tableStr
  Right () <- writeFile "Library/Wiki/Verification_Matrix.md" (preamble ++ tableStr)
    | Left err => putStrLn "Failed to write Verification_Matrix.md file."
  putStrLn "\n--- Engine Verification ---"
  Engine_Verification.main

  putStrLn "\nTests complete. Results written to Library/Wiki/Verification_Matrix.md!"
