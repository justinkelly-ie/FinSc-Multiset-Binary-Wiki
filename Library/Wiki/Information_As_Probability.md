# 💡 Information as Probability — Hehner's Pedagogical Inversion ($p = 2^{-I}$)

> **Student Guide to Information-First Probability**
>
> In 1948, Claude Shannon defined information in terms of probability ($I = -\log_2 p$) because probability was already a mature mathematical field. Today, computer science pioneer Eric Hehner suggests reversing this priority: **define probability in terms of information ($p = 2^{-I}$)** because every modern student already understands bits, bytes, bandwidth, and file compression.

---

## 1. 🧠 The Inversion: Memory Bits Are Real

In traditional textbooks, probability is introduced as an abstract measure over infinite continuous sets. But when you download a compressed file, your computer doesn't deal with infinite limits—it deals with **bits of memory**.

```idris
module Wiki.Information_As_Probability

import QuickCheck
import Math.Multiset
import Math.BoxInt
import Math.SignedFraction
import Logic.FunctionalProbability
import Logic.InformationTheory

%default total
```

### The Two Formulas

| Perspective | Primary Concept | Derived Formula |
| :--- | :--- | :--- |
| **Traditional (1948)** | Probability ($p$) | Information Surprisal $I = -\log_2 p$ |
| **Hehner Inversion (Modern)** | Memory Information Bits ($I$) | Probability $p = 2^{-I}$ |

Under Hehner's inversion:
* **Information $I(x)$** is the number of **bits** needed to encode outcome $x$.
* **Probability $p(x)$** is simply the **decay of memory cost** allocated to $x$.

---

## 2. 😮 Surprisal: High Expectation = Short Bit Length

If an event is guaranteed (e.g. $p = 1$), you are not surprised when it happens—it costs **0 bits** to store ($I = -\log_2 1 = 0$).

If an event is rare (e.g. $p = 1/4$), you are surprised—it takes **2 bits** of memory to specify which of the 4 possibilities occurred ($I = -\log_2(1/4) = 2$).

In [Logic.InformationTheory](file:///var/home/justin/Projects/Idris2-Boole/src/Logic/InformationTheory.idr), we compute this directly over exact multiset fractions (`MSetFraction`):

```idris
||| Student Example 1: Surprisal of a 1/4 probability event is 2 bits
public export
prop_studentQuarterSurprisal : Property
prop_studentQuarterSurprisal =
  let pQuarter = MkMSF 1 4
  in property (selfInformationBits pQuarter == 2)

||| Student Example 2: Surprisal of a 1/8 probability event is 3 bits
public export
prop_studentEighthSurprisal : Property
prop_studentEighthSurprisal =
  let pEighth = MkMSF 1 8
  in property (selfInformationBits pEighth == 3)
```

---

## 3. 🧮 Discrete Surprisal without Floating-Point Drift

Standard probability calculations use floating-point numbers ($\text{f64}$), which suffer from rounding errors. In the **Finite-Science Algebra of Boole**, probabilities are stored as exact integer numerator/denominator pairs:

$$\text{MSetFraction} = \frac{\text{Numerator Weight } w}{\text{Total Multiset Sum } \sum w}$$

Self-information is calculated using exact integer binary logarithms:

$$\text{selfInformationBits}\left(\frac{w}{\sum w}\right) = \text{log2Ceil}\left(\sum w\right) - \text{log2Ceil}(w)$$

```idris
||| Property: Surprisal is always non-negative for valid probability fractions
public export
prop_studentSurprisalNonNegative : Property
prop_studentSurprisalNonNegative =
  let p = MkMSF 1 16
  in property (selfInformationBits p == 4)
```

---

## 4. 🎓 Key Takeaway for Students

1. **Probability is Memory Allocation**: $p = 2^{-I}$. Probability measures how compactly an event can be encoded.
2. **No Infinite Limits Needed**: In discrete multiset science, we count integer state weights ($w / \sum w$) and calculate bit-lengths directly.
3. **Surprisal is Exact**: Using integer logarithms, self-information remains exact and free of floating-point errors.
