# idris2-Boole-Wiki

**The living, executable documentation for [idris2-Boole](https://github.com/justinkelly-ie/Idris2-Boole) library.**

[![Idris2](https://img.shields.io/badge/Idris2-Boole-blue.svg)](https://github.com/idris-lang/Idris2)
[![Wiki](https://img.shields.io/badge/Wiki-Living_Docs-red.svg)]()
[![Tests](https://img.shields.io/badge/QuickCheck-16_passing-green.svg)]()

---

## Overview

Welcome to the **Idris2 Boole Wiki**. This repository contains the executable documentation, theoretical foundations, and compile-time proofs for Norman Wildberger's *Algebra of Boole*, Eric Hehner's *Functional Probability*, and Marcus Hutter's *Compression-as-Intelligence* framework in the Finite-Science model.

Like the parent science wiki, this library is **executable**. Every chapter is written in **Literate Idris 2 (`.md`)** combining Markdown explanations with functional code blocks. When built, the package compiles and runs QuickCheck property-testing suites to verify that logical deductions, probability normalizations, cross-entropy bounds, and algebraic invariants remain mathematically intact.

---

## 🔀 Progression: From Boole Multisets to Probability Multisets

A fundamental insight of the Finite-Science Table is that **Probability is not an abstract measure space—it is the direct normalization of Boolean model counts**.

```
  Step 1a: Boolean Logic ──► Step 1b: Model Counting ──► Step 2: Normalization ──► Step 3: Information
 ┌──────────────────────┐   ┌──────────────────────┐   ┌─────────────────────┐    ┌─────────────────────┐
 │ Binary Wires         │   │ State Frequencies    │   │ Rational Prob       │    │ Surprisal Bits      │
 │ Bit ∈ {0, 1}         │   │ Vexel BoxInt state   │   │ ↕E = w_i / ∑w       │    │ I(x) = -log2(p)     │
 │ Denominator = 1      │   │ Total Mass = ∑w      │   │ MSetFraction        │    │ Hutter Compression  │
 └──────────────────────┘   └──────────────────────┘   └─────────────────────┘    └─────────────────────┘
```

### Step 1a: Deterministic Boolean Logic (Row 1)
Logical propositions begin as deterministic binary wires (`Bit` $\in \{0, 1\}$) under mod-2 addition (XOR) and multiplication (AND). A truth table assigns exact $0$ or $1$ evaluations to individual variable assignments.

### Step 1b: Combinatorial Model Counting & State Accumulation (Row 2)
Before jumping to probabilities, we count how many micro-states in a truth table or observation window satisfy a given proposition. 
* Binary states aggregate into **Integer Multiset Counts** (`Vexel BoxInt state`).
* Each element weight $w_i \in \mathbb{Z}_{\ge 0}$ represents the **raw frequency count** of state $x_i$ occurring.
* *Example*: In an 8-outcome sample space, 3 outcomes yield `Heads` ($w_{\text{heads}} = 3$) and 5 yield `Tails` ($w_{\text{tails}} = 5$). Total universe mass $\sum w = 8$.

### Step 2: Hehner Normalization Operator ($\updownarrow E = E / \sum E$) (Row 3)
Probability is introduced simply by normalizing the raw model count $w_i$ against the total universe mass $\sum w$. Applying Eric Hehner's normalization operator:

$$\updownarrow E = \frac{E}{\sum E}$$

scales unnormalized multiset weights into exact rational probability fractions ($w_i / \sum w$) stored in `MSetFraction`, eliminating floating-point rounding errors and precision loss.

### Step 3: Hehner Information Paradigm ($p = 2^{-I}$) (Row 4)
Instead of defining information in terms of probability ($I = -\log_2 p$), Hehner reverses the paradigm to define probability in terms of memory bits ($p = 2^{-I}$). High-probability multiset states require short bit lengths; rare states require long bit lengths.

### Step 4: Zero KL-Divergence Loss ($D_{\text{KL}} = 0$) & Hutter Compression
Because probability fractions ($w / \sum w$) operate via exact integer cross-multiplication ($a \cdot d > c \cdot b$), model divergence vanishes ($D_{\text{KL}}(P \parallel Q_{\text{mset}}) = 0$), achieving Marcus Hutter's Minimum Description Length (MDL) compression ($4:1$ Kolmogorov savings over 64-bit continuous float vectors).

---

## 📚 Living Wiki Chapters

### The Algebra of Boole (Row 1 & 2)
*   **[Bit Vexels & Operators](Library/Wiki/Bit_vexel.md)** — Guide to constructing digital logic circuits using multiset-based logic algebra.
*   **[Logic Repetition](Library/Wiki/Logic_Repetition.md)** — Modulo-2 digital logic wires using `Bit` multiset coefficients.
*   **[Logic Explainer](Library/Wiki/Logic_Explainer.md)** — Core type definitions of `Sing`, `Sing1`, and dependently typed `DepVexel` registers.
*   **[Lifted Polynumbers](Library/Wiki/Lifted_Polynumbers.md)** — Mapping Boolean logic fields into integer polynomial plane.
*   **[Singleton Lifted Polynumbers](Library/Wiki/Logic_Lifted.md)** — Positional arithmetic carriage with division-by-zero protection.

### Information Theory & Functional Probability (Row 3 & 4)
*   **[📊 Functional Probability](Library/Wiki/Functional_Probability.md)** — Calculational Hehner conditional probability, stateProbability, and divisionless comparisons.
*   **[💡 Information as Probability ($p = 2^{-I}$)](Library/Wiki/Information_As_Probability.md)** — Student guide to Hehner's pedagogical inversion, surprisal bits, and exact integer logarithms.
*   **[↕️ Hehner's Normalization Operator ($\updownarrow E$)](Library/Wiki/Hehner_Normalization.md)** — Student guide to $\updownarrow E = E / \sum E$ distribution summation and multiset normalization.
*   **[∧/∨ Hehner's Calculational Quantifiers ($\forall, \exists$)](Library/Wiki/Hehner_Quantifiers.md)** — Replacing $\forall$ with $\land$ (`minWeight`) and $\exists$ with $\lor$ (`maxWeight`).
*   **[🗜️ Cross-Entropy & Hutter Compression](Library/Wiki/Cross_Entropy_And_Compression.md)** — Explains Cross-Entropy $H(P, Q)$, zero KL loss ($D_{\text{KL}} = 0$), and Hutter's Compression-as-Intelligence metric.
*   **[🎓 George Boole's Last Challenge Problem](Library/Wiki/Boole_Last_Challenge.md)** — Computing exact polyhedral bounds $[7/10, 10/10]$ on Boole's 1854 3-event union problem.
*   **[🛡️ Probability Bounds (Hailperin)](Library/Wiki/Probability_Bounds.md)** — Bounded min/max interval representation over incomplete probability fields.

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

This will run all 16 QuickCheck property-testing suites and automatically write the results to:
*   [Verification Matrix](Library/Wiki/Verification_Matrix.md)

---

&copy; Justin Kelly. All rights reserved.
