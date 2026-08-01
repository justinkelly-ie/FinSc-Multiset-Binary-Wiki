# idris2-Boole-Wiki

**The living, executable documentation for [idris2-Boole](https://github.com/justinkelly-ie/Idris2-Boole) library.**

[![Idris2](https://img.shields.io/badge/Idris2-Boole-blue.svg)](https://github.com/idris-lang/Idris2)
[![Wiki](https://img.shields.io/badge/Wiki-Living_Docs-red.svg)]()
[![Tests](https://img.shields.io/badge/QuickCheck-4_passing-green.svg)]()

---

## Overview

Welcome to the **Idris2 Boole Wiki**. This repository contains the executable documentation, theoretical foundations, and compile-time proofs for Norman Wildberger's *Algebra of Boole* and the restricted logic type hierarchy (`Sing`/`Sing1`) in the Finite-Science model.

Like the parent science wiki, this library is **executable**. Every chapter is written in **Literate Idris 2 (`.md`)** combining Markdown explanations with functional code blocks. When built, the package compiles and runs QuickCheck property-testing suites to verify that logical deductions, boundary inequalities, and algebraic invariants remain mathematically intact.

---

## The Logic Layer (Row 1)

This wiki documents the first layer of the Global Finite Science Table, tracing the structures and evaluations of Boolean logic:

### [1. Logic Repetition & Bit Vexels](Library/Wiki/Bit_vexel.md)
*   **[Bit Vexels & Operators](Library/Wiki/Bit_vexel.md)** — Guide to constructing digital logic circuits using multiset-based logic algebra.
*   **[Logic Repetition](Library/Wiki/Logic_Repetition.md)** — Modulo-2 digital logic wires using `BF2` coefficients.
*   **[Logic Explainer](Library/Wiki/Logic_Explainer.md)** — Core type definitions of `Sing`, `Sing1`, and dependently typed `DepVexel` registers.

---

## Algebraic Transformation & Sequences

*   **[Boole-Möbius Transform (Sir Galahad)](Library/Wiki/Boole_mobius_transform.md)** — Resolving Sir Galahad's three-premises liar puzzle via component-wise truth tables and verification of the self-inverse property.
*   **[On-Sequences & Clips](Library/Wiki/On_Sequence.md)** — Finitist foundations representing ongoing sequences and consecutive observation windows.

---

## How to Compile & Verify

To build the executable and run all property tests in real time:

### Using the Fedora Toolbox environment:
```bash
# Compile and execute the verification proofs:
toolbox run -c fedora-toolbox-44 pack run idris2-Boole-Wiki.ipkg
```

This will run all QuickCheck properties and automatically write the results to:
*   [Verification Matrix](Library/Wiki/Verification_Matrix.md)

---

&copy; Justin Kelly. All rights reserved.
