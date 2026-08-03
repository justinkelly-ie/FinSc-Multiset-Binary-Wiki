# idris2-Boole-Wiki

**The living, executable documentation for [idris2-Boole](https://github.com/justinkelly-ie/Idris2-Boole) library.**

[![Idris2](https://img.shields.io/badge/Idris2-Boole-blue.svg)](https://github.com/idris-lang/Idris2)
[![Wiki](https://img.shields.io/badge/Wiki-Living_Docs-red.svg)]()
[![Tests](https://img.shields.io/badge/QuickCheck-10_passing-green.svg)]()

---

## Overview

Welcome to the **Idris2 Boole Wiki**. This repository contains the executable documentation, theoretical foundations, and compile-time proofs for Norman Wildberger's *Algebra of Boole*, Eric Hehner's *Functional Probability*, and Marcus Hutter's *Compression-as-Intelligence* framework in the Finite-Science model.

Like the parent science wiki, this library is **executable**. Every chapter is written in **Literate Idris 2 (`.md`)** combining Markdown explanations with functional code blocks. When built, the package compiles and runs QuickCheck property-testing suites to verify that logical deductions, probability normalizations, cross-entropy bounds, and algebraic invariants remain mathematically intact.

---

## 🔀 Progression: From Boole Multisets to Probability Multisets

A fundamental insight of the Finite-Science Table is that **Probability is not an independent measure space—it is an algebraic continuation of Boole polynomial multisets**.

```
    Boole Ring (Row 1/2)                     Probability Multisets (Row 3/4)
┌───────────────────────────┐               ┌─────────────────────────────────┐
│ Mod-2 / BoxInt Weights    │               │ Hehner Normalization ↕E = E/∑E  │
│ [Vexel BoxInt state]      │  ───────►     │ Exact Fraction: w / ∑w          │
│ Denominator = 1           │               │ Surprisal Bits: I = -log2(p)    │
└───────────────────────────┘               └─────────────────────────────────┘
```

### Step 1: Boole Polynomial Multisets (Row 1 & 2)
Logical wires start as binary values (`Bit` $\in \{0, 1\}$) under mod-2 addition (XOR) and multiplication (AND). In Row 2, binary states lift into integer-weighted multisets (`Vexel BoxInt state`) over 1-component Singleton coordinates. At this stage, the scale denominator is fixed to the unit constant ($1$ / `TrivialBase`).

### Step 2: Hehner Normalization Operator ($\updownarrow E = E / \sum E$)
In Row 3, the fixed unit denominator **generalizes to the total mass of the unnormalized distribution** ($\sum w$). Applying Eric Hehner's normalization operator:

$$\updownarrow E = \frac{E}{\sum E}$$

transforms raw multiset weights ($w_i \in \mathbb{Z}$) into exact rational probabilities ($w_i / \sum w$) stored in `MSetFraction`, eliminating floating-point drift and rounding errors.

### Step 3: Hehner Information Paradigm ($p = 2^{-I}$)
Instead of defining information in terms of probability ($I = -\log_2 p$), Hehner reverses the paradigm to define probability in terms of memory bits ($p = 2^{-I}$). High-probability multiset states require short bit lengths; rare states require long bit lengths.

### Step 4: Zero KL-Divergence Loss ($D_{\text{KL}} = 0$) & Hutter Compression
Because probability fractions ($w / \sum w$) operate via exact integer cross-multiplication ($a \cdot d > c \cdot b$), model divergence vanishes ($D_{\text{KL}}(P \parallel Q_{\text{mset}}) = 0$), achieving Marcus Hutter's Minimum Description Length (MDL) compression ($4:1$ Kolmogorov savings over 64-bit continuous float vectors).

---

## 📚 Living Wiki Chapters

### The Algebra of Boole (Row 1 & 2)
*   **[Bit Vexels & Operators](Library/Wiki/Bit_vexel.md)** — Guide to constructing digital logic circuits using multiset-based logic algebra.
*   **[Logic Repetition](Library/Wiki/Logic_Repetition.md)** — Modulo-2 digital logic wires using `Bit` multiset coefficients.
*   **[Logic Explainer](Library/Wiki/Logic_Explainer.md)** — Core type definitions of `Sing`, `Sing1`, and dependently typed `DepVexel` registers.

### Information Theory & Functional Probability (Row 3 & 4)
*   **[💡 Information as Probability ($p = 2^{-I}$)](Library/Wiki/Information_As_Probability.md)** — Student guide to Hehner's pedagogical inversion, surprisal bits, and exact integer logarithms.
*   **[🗜️ Cross-Entropy & Hutter Compression](Library/Wiki/Cross_Entropy_And_Compression.md)** — Explains Cross-Entropy $H(P, Q)$, zero KL loss ($D_{\text{KL}} = 0$), and Hutter's Compression-as-Intelligence metric.
*   **[↕️ Hehner's Normalization Operator ($\updownarrow E$)](Library/Wiki/Hehner_Normalization.md)** — Student guide to $\updownarrow E = E / \sum E$ distribution summation and multiset normalization.

### Algebraic Transformations & Sequences
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

This will run all 10 QuickCheck property-testing suites and automatically write the results to:
*   [Verification Matrix](Library/Wiki/Verification_Matrix.md)

---

&copy; Justin Kelly. All rights reserved.
