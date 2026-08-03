# ↕ Hehner's Normalization Operator ($\updownarrow E = E / \sum E$)

> **Student Guide to Distribution Normalization**
>
> In Hehner's *a Probability Theory*, a **distribution** is defined as an expression whose values are probabilities ($0 \le p_i \le 1$) and whose total sum over all states equals **1** ($\sum E = 1$). Most raw physical expressions $E$ (like multiset state counts) are unnormalized. Hehner introduces the **normalization operator $\updownarrow E$** (pronounced *"normalize E"*) to scale any non-negative expression into a valid probability distribution.

---

## 1. 📐 The Normalization Formula

Given an unnormalized non-negative expression $E$ whose total sum $\sum E$ is between $0$ and $\infty$:

$$\updownarrow E = \frac{E}{\sum E}$$

```idris
module Hehner_Normalization

import QuickCheck
import Math.Multiset
import Math.Singleton.Sing
import Math.BoxInt
import Math.Vexel.Vexel
import Math.SignedFraction
import Logic.FunctionalProbability
import Logic.InformationTheory

%default total
```

### Hehner's Example: $2^{-n-m}$ over Naturals

1. Consider the expression $E(n, m) = 2^{-n-m}$ where $n, m \in \mathbb{N} = \{0, 1, 2, \dots\}$.
2. The total sum over all assignments is:
   $$\sum_{n, m \in \mathbb{N}} 2^{-n-m} = \left(\sum_{n=0}^{\infty} 2^{-n}\right) \left(\sum_{m=0}^{\infty} 2^{-m}\right) = 2 \times 2 = 4$$
3. Since the sum is $4$, $2^{-n-m}$ is **not** a distribution.
4. Applying Hehner's normalization operator yields the valid distribution:
   $$\updownarrow(2^{-n-m}) = \frac{2^{-n-m}}{4}$$

---

## 2. 🎛️ Multiset Implementation in `Logic.FunctionalProbability`

In the **Finite-Science Algebra of Boole**, unnormalized distributions are stored as `MSetFractionVexel v` (multisets of state weights $w_i \in \mathbb{Z}$).

The $\updownarrow E$ operator is implemented by [normalizeFraction](file:///var/home/justin/Projects/Idris2-Boole/src/Logic/FunctionalProbability.idr#L78-L90) and [stateProbability](file:///var/home/justin/Projects/Idris2-Boole/src/Logic/FunctionalProbability.idr#L66-L75):

```idris
||| Student Example 1: Verifying Hehner's normalization operator on unnormalized multiset weights
public export
prop_studentNormalizeOperator : Property
prop_studentNormalizeOperator =
  let -- Unnormalized space with weights [Heads -> 3, Tails -> 5], total sum = 8
      vexelSpace = mkMSetFractionVexel (AddM (MkSing Boy) 3 (AddM (MkSing Girl) 5 ZeroM)) 8
      -- Normalizing extracts P(Boy) = 3/8 and P(Girl) = 5/8
      pBoy = stateProbability vexelSpace Boy
      pGirl = stateProbability vexelSpace Girl
  in property (pBoy == MkMSF 3 8 && pGirl == MkMSF 5 8)
```

---

## 3. 💡 Connecting Normalization to Information Surprisal

Once an expression is normalized ($\updownarrow E = E / \sum E$), we compute its exact Information Surprisal ($I = -\log_2 p$) using [Logic.InformationTheory](file:///var/home/justin/Projects/Idris2-Boole/src/Logic/InformationTheory.idr):

$$I(x) = -\log_2 \left(\updownarrow E(x)\right) = \log_2\left(\sum E\right) - \log_2(E(x))$$

```idris
||| Student Example 2: Computing bit surprisal of normalized distribution outcomes
public export
prop_studentNormalizedSurprisal : Property
prop_studentNormalizedSurprisal =
  let -- Normalized probability p = 1/4 (e.g. 2/8)
      p = MkMSF 2 8
      -- Surprisal I = log2(8) - log2(2) = 3 - 1 = 2 bits
  in property (selfInformationBits p == 2)
```

---

## 4. 🎓 Summary of Hehner's Normalization

1. **Unnormalized Expression $E$**: Raw weights or state counts ($E(x) \ge 0$).
2. **Sum $\sum E$**: Total mass of the universe space.
3. **Normalized Distribution $\updownarrow E = E / \sum E$**: Ensures total sum equals $1$ ($\sum \updownarrow E = 1$).
4. **Exact Rational Representation**: Stored as exact `MSetFraction` numerators and denominators, guaranteeing zero floating-point error.
