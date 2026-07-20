# idris2-Logic-Wiki

**The living, executable mathematical documentation for [idris2-Logic](https://github.com/justinkelly-ie/Idris2-Logic) library.**

[![Idris2](https://img.shields.io/badge/Idris2-Logic-blue.svg)](https://github.com/idris-lang/Idris2)
[![Wiki](https://img.shields.io/badge/Wiki-Living_Docs-red.svg)]()
[![Tests](https://img.shields.io/badge/QuickCheck-5_passing-green.svg)]()

---

## Overview

Welcome to the **Idris2 Logic Wiki**. This repository contains the executable documentation, theoretical foundations, and compile-time proofs for Norman Wildberger's *Algebra of Boole* and the restricted logic type hierarchy (`Sing`/`Sing1`) in the Finite-Science model.

Like the parent science wiki, this library is **executable**. Every chapter is written in **Literate Idris 2 (`.md`)** combining Markdown explanations with functional code blocks. When built, the package compiles and runs QuickCheck property-testing suites to verify that logical deductions, boundary inequalities, and algebraic invariants remain mathematically intact.

---

## The 4-Row Logical and Probability Table

This wiki documents the first four layers of the Global Finite Science Table, tracing the progression from binary logic to polyhedral probability bounds:

### [1. Logic Repetition & Bit Vexels](Library/Wiki/Bit_vexel.md)
*   **[Bit Vexels & Operators](Library/Wiki/Bit_vexel.md)** — Guide to constructing digital logic circuits using multiset-based logic algebra.
*   **[Logic Repetition](Library/Wiki/Logic_Repetition.md)** — Modulo-2 digital logic wires using `BF2` coefficients.
*   **[Logic Explainer](Library/Wiki/Logic_Explainer.md)** — Core type definitions of `Sing`, `Sing1`, and dependently typed `DepVexel` registers.

### [2. Lifted Polynumbers & Positional Arithmetic](Library/Wiki/Logic_Lifted.md)
*   **[Logic Lifted Polynumbers](Library/Wiki/Logic_Lifted.md)** — Transition from logic gates to continuous arithmetic circuits by lifting coefficients to `BoxInt`.

### [3. Functional Probability & Hehner Normalization](Library/Wiki/Functional_Probability.md)
*   **[Functional Probability](Library/Wiki/Functional_Probability.md)** — Exact rational probability vectors using cross-multiplication over variable sum denominators ($\sum w$).

### [4. Probability Bounds & Polyhedral Squeezing](Library/Wiki/Boole_Last_Challenge.md)
*   **[George Boole's Last Challenge Problem](Library/Wiki/Boole_Last_Challenge.md)** — Applying the Boole-Möbius transform and polyhedral boundary inequalities to resolve George Boole's 1854 union probability challenge.

---

## Algebraic Transformation & Sequences

*   **[Boole-Möbius Transform (Sir Galahad)](Library/Wiki/Boole_mobius_transform.md)** — Resolving Sir Galahad's three-premises liar puzzle via component-wise truth tables and verification of the self-inverse property.
*   **[On-Sequences & Clips](Library/Wiki/On_Sequence.md)** — Finitist foundations representing ongoing sequences and consecutive observation windows.

---

## How to Compile & Verify

To build the executable and run all property tests in real time:

### Using the Fedora Toolbox environment:
```bash
# 1. Compile the wiki executable:
toolbox run -c fedora-toolbox-44 pack build idris2-Logic-Wiki.ipkg

# 2. Execute the verification proofs:
toolbox run -c fedora-toolbox-44 ./build/exec/boolewiki
```

This will run all 5 QuickCheck properties and automatically write the results to:
*   [Verification Matrix](Library/Wiki/Verification_Matrix.md)

---

&copy; Justin Kelly. All rights reserved.
