module Main

import QuickCheck
import Finite_Science.Singleton_Explainer
import Finite_Science.Singleton_Lifted
import Finite_Science.Singleton_Repetition
import Finite_Science.Boole_Last_Challenge
import Finite_Science.Bit_vexel
import Finite_Science.Boole_Function
import Finite_Science.Boole_mobius_transform
import Finite_Science.IndivisibleHistory
import Code.Engine_Verification

import System.File
import Data.String
import Math.Singleton.Bit
import Math.BoxInt
import Math.Multiset
import Math.Singleton.Sing

%default covering

boolToBVal : Bool -> BVal
boolToBVal True = One
boolToBVal False = Zero

bvalToString : BVal -> String
bvalToString ZeroS = "0"
bvalToString (OneS () 1) = "1"
bvalToString _ = "?"

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
  putStrLn "Starting Idris2-Logic-Wiki QuickCheck Suite...\n"
  
  putStrLn "Running Test 1: George Boole's Last Challenge Bounds"
  let resBooleChallenge = quickCheck prop_booleChallengeBounds
  
  putStrLn "Running Test 2: Boole Function Evaluation Correctness"
  let resBF1 = quickCheck Finite_Science.Boole_Function.prop_evalCorrect
  
  putStrLn "Running Test 3: Boole Function & Polynumber Isomorphism"
  let resBF2 = quickCheck Finite_Science.Boole_Function.prop_polynumberIsomorphism
  
  putStrLn "Running Test 4: Sir Galahad's Deduction (Stone Road)"
  let resBF3 = quickCheck Finite_Science.Boole_mobius_transform.prop_galadhadChoosesStone
  
  putStrLn "Running Test 5: Boole-Möbius Transform Self-Inverse on Sequence"
  let resBF4 = quickCheck Finite_Science.Boole_mobius_transform.prop_mobiusSelfInverseOnSeq

  putStrLn "Running Test 6: Indivisible History Trajectory"
  let resIndivisibleHistory = quickCheck prop_indivisibleHistoryLength

  let tableStr = markdownTable [
        ("Boole's Last Challenge", "Verifies the Hailperin polyhedral bounds on George Boole's 1854 challenge evaluate exactly to [7/10, 10/10].", resBooleChallenge),
        ("Boole Function Eval", "Verifies that evaluating a BooleFunction yields the correct truth table value.", resBF1),
        ("Polynumber Isomorphism", "Verifies the algebraic isomorphism between BooleFunction and BoolePolynumber via Möbius transform.", resBF2),
        ("Sir Galahad's Deduction", "Verifies that Sir Galahad's logical premises imply he must choose the stone road.", resBF3),
        ("Möbius Self-Inverse", "Verifies that the Boole-Möbius transform is self-inverse when mapped over an ongoing sequence.", resBF4),
        ("Indivisible History Trajectory", "Verifies that the length and division event resets of an IndivisibleHistory are tracked correctly.", resIndivisibleHistory)
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
  Code.Engine_Verification.main

  putStrLn "\nTests complete. Results written to Library/Wiki/Verification_Matrix.md!"
