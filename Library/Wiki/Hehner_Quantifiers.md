# ∧ and ∨ — Hehner's Calculational Quantifiers ($\forall$ and $\exists$)

> **Student Guide to Calculational Quantifiers**
>
> In traditional mathematics, quantifiers like *"for all"* ($\forall$) and *"there exists"* ($\exists$) are non-constructive words that require debate over infinite domains. In Eric Hehner's *From Boolean Algebra to Unified Algebra*, quantifiers are transformed into **automated calculational tools**:
> * **For All ($\forall$)** $\mapsto$ **Minimum Operator ($\land$)** / `minWeight`
> * **There Exists ($\exists$)** $\mapsto$ **Maximum Operator ($\lor$)** / `maxWeight`

---

## 1. 📐 Why Replace $\forall$ and $\exists$ with Minimum and Maximum?

```idris
module Hehner_Quantifiers

import QuickCheck
import Math.Multiset
import Math.Singleton.Sing
import Math.BoxInt
import Math.Vexel.Vexel
import Logic.FunctionalProbability

%default total
```

### The Unification Insight

Hehner notes that any expression introducing a dummy/local variable $x$ over a domain $S$ is simply an operator applied to a function:

* **Summation**: $+ \langle x : S \cdot f(x) \rangle \implies \text{Total Mass } \sum w$
* **For All ($\forall$)**: $\land \langle x : S \cdot f(x) \rangle \implies \text{Minimum value } \min_{x \in S} f(x)$
* **There Exists ($\exists$)**: $\lor \langle x : S \cdot f(x) \rangle \implies \text{Maximum value } \max_{x \in S} f(x)$

---

## 2. 🎛️ Multiset Weight Quantifiers (`minWeight` & `maxWeight`)

Given an unnormalized multiset space `v : Vexel BoxInt state`:

$$\forall(v) = \text{minWeight}(v) \qquad \text{and} \qquad \exists(v) = \text{maxWeight}(v)$$

```idris
||| Student Example 1: Verifying minWeight (∀) and maxWeight (∃) over an unnormalized multiset
public export
prop_studentMinMaxQuantifiers : Property
prop_studentMinMaxQuantifiers =
  let -- Vexel space with weights [Boy -> 3, Girl -> 5]
      vexelSpace : Vexel BoxInt Gender
      vexelSpace = AddM (MkSing Boy) 3 (AddM (MkSing Girl) 5 ZeroM)
      minW = minWeight vexelSpace
      maxW = maxWeight vexelSpace
  in property (minW == Just 3 && maxW == Just 5)
```

---

## 3. ⚙️ Function Calculational Quantifiers (`forAll` & `thereExists`)

Given an evaluation payload function $f : v \to \text{BoxInt}$ evaluated over domain $S : \text{List } v$:

$$\forall \langle x : S \cdot f(x) \rangle = \text{forAll } f \, S \qquad \text{and} \qquad \exists \langle x : S \cdot f(x) \rangle = \text{thereExists } f \, S$$

```idris
||| Student Example 2: Verifying forAll (min) and thereExists (max) over payload evaluations
public export
prop_studentFunctionQuantifiers : Property
prop_studentFunctionQuantifiers =
  let domain = [Boy, Girl]
      -- Payload function assigning Boy -> 10, Girl -> 20
      payload : Gender -> BoxInt
      payload Boy = 10
      payload Girl = 20
      minVal = forAll payload domain
      maxVal = thereExists payload domain
  in property (minVal == Just 10 && maxVal == Just 20)
```

---

## 4. 🎓 Summary of Hehner's Quantifier Matrix

| Classical Quantifier | Hehner Operator | Multiset Function | Meaning in Finite-Science |
| :--- | :--- | :--- | :--- |
| $\forall x \cdot P(x)$ | $\land \langle x : S \cdot f(x) \rangle$ | `minWeight` / `forAll` | Minimum weight / payload across domain |
| $\exists x \cdot P(x)$ | $\lor \langle x : S \cdot f(x) \rangle$ | `maxWeight` / `thereExists` | Maximum weight / payload across domain |
| $\sum_x P(x)$ | $+ \langle x : S \cdot f(x) \rangle$ | `totalMass` / `expectation` | Total sum / expected value $\mathbb{E}[f]$ |
