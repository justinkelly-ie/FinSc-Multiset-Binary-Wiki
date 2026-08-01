module Main

import QuickCheck
import Logic_Explainer
import Logic_Repetition
import Bit_vexel
import Boole_Function
import Boole_mobius_transform
import Engine_Verification

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
      in "| " ++ name ++ " | " ++ desc ++ " | " ++ statusStr ++ " | " ++ trim (msg res) ++ " |\n"

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

  let tableStr = markdownTable [
        ("Boole Function Eval", "Verifies that evaluating a BooleFunction yields the correct truth table value.", resBF1),
        ("Polynumber Isomorphism", "Verifies the algebraic isomorphism between BooleFunction and BoolePolynumber via Möbius transform.", resBF2),
        ("Sir Galahad's Deduction", "Verifies that Sir Galahad's logical premises imply he must choose the stone road.", resBF3),
        ("Möbius Self-Inverse", "Verifies that the Boole-Möbius transform is self-inverse when mapped over an ongoing sequence.", resBF4)
      ]
  
  let preamble = unlines [
        "# Algebra of Boole & Singleton Verification Matrix",
        "",
        "This matrix tracks the automated testing suite for the Algebra of Boole, Singleton representation, and Möbius Transform modules.",
        "",
        "### Core Concepts",
        "* **Boolean Ring**: Every logical value is modeled as mod-2 addition (XOR) and multiplication (AND), allowing self-inverse subtraction and exact algebraic reduction.",
        "* **Möbius Transform**: Maps truth-table evaluations to unique polynumber coefficients, replacing SAT solving with direct comparison.",
        "* **Singleton Bounds**: Restricted multiset sizes (Sing/Sing1) guarantee division-by-zero protection at compile time.",
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
