# ♾️ On-Sequences and Clips — [idris2-Multiset](https://github.com/justinkelly-ie/idris2-Multiset)

> **Finitist Foundation for Ongoing Sequences and Localized Observation Clips**
>
> In finitist mathematics, the concept of completed infinity is rejected. Infinite sequences are replaced by **on-sequences** (ongoing processes that can generate arbitrary terms but are never "completed") and **clips** (finite, localized, consecutive windows of observation).

---

## 🏛️ Theoretical Foundation: Finitist Sequences

This module implements the finitist approach to infinite sequences as described by Norman Wildberger in *Real Numbers and Limits* (Lectures 98, 100–102, and 114) and *Algebra of Boole* (Lecture 272). 

Instead of treating an infinite sequence as a static, completed set of infinite elements (which is computationally impossible and algebraically problematic), we define:
1. **On-sequence**: An explicit generator rule $P(n)_a^+$ that starts at a finite index $a$ and produces the $n$-th element on demand.
2. **Clip**: A finite consecutive sublist of a sequence. A clip is a lossy representation of a sequence (denoted $S \Rightarrow \text{Clip}$), signifying that we cannot reconstruct the full sequence or its generator from a finite snapshot.

---

## 💻 Idris 2 Data Structures

In [OnMSet.idr](file:///var/home/justin/Projects/idris2-Multiset/src/Math/OnSeq/OnMSet.idr), we represent these concepts as follows:

```text
||| An on-sequence (ongoing sequence) starting at a specific index.
||| Defined via a generator function mapping the term index to the value.
public export
record OnSeq a where
  constructor MkOnSeq
  start : Nat
  at    : Nat -> a

||| A finite consecutive subsequence (clip) extracted from a sequence.
public export
record Clip a where
  constructor MkClip
  startIdx : Nat
  elements : List a
```

---

## 🧮 Pointwise Multiset Operations (`OnMSet`)

By parameterizing `OnSeq` with the signed [Multiset](file:///var/home/justin/Projects/idris2-Multiset/src/Math/Multiset.idr) type, we obtain the **OnMSet** type:

```text
public export
0 OnMSet : (c : Type) -> (a : Type) -> Type
OnMSet c a = OnSeq (Multiset c a)
```

Pointwise arithmetic operations are mapped across these ongoing sequences. For example, adding two `OnMSet` structures combines them at each step, aligning their starting indices to $\max(s_1, s_2)$:

```text
public export
addOnMSet : OnMSet c a -> OnMSet c a -> OnMSet c a
addOnMSet = zipWith addMultiset
```

### Example: Pointwise Sum of Growing Multisets
Suppose we have two ongoing sequences of multisets where:
* $S_1(n)$ adds $n$ copies of coordinate `'A'` at step $n$, starting at index $1$.
* $S_2(n)$ adds $3$ copies of coordinate `'B'` at step $n$, starting at index $0$.

```text
let s1 = MkOnSeq 1 (\n => AddM 'A' (cast n) ZeroM)
let s2 = MkOnSeq 0 (\n => AddM 'B' 3 ZeroM)

-- Pointwise sum starts at max(1, 0) = 1
let sSum = addOnMSet s1 s2

-- Extracting a clip of length 3 starting at index 1:
-- sSum(1) = [( 'A', 1 ), ( 'B', 3 )]
-- sSum(2) = [( 'A', 2 ), ( 'B', 3 )]
-- sSum(3) = [( 'A', 3 ), ( 'B', 3 )]
let clip = getClip sSum 1 3
-- Result: Clip@1[[( 'A', 1 ), ( 'B', 3 )], [( 'A', 2 ), ( 'B', 3 )], [( 'A', 3 ), ( 'B', 3 )]]...
```

---

## 🎛️ Unbounded Logic Variables & On-Circuits

For row-specific details of ongoing sequences in Boolean logic (Row 1) and Arithmetic Circuits (Row 2), see:
*   [Digital Repetition (Row 1)](./Digital_Repetition.md#%EF%B8%8F-ongoing-sequences-unbounded-logic-variables-onbyte) — detailing [OnByte](file:///var/home/justin/Projects/Idris2-Boole/src/Logic/OnCircuit.idr#L47-L49) for growing coordinate vectors.
*   [Lifted Polynumbers (Row 2)](./Lifted_Polynumbers.md#%EF%B8%8F-ongoing-sequences-expanding-arithmetic-circuits-oncircuit) — detailing [OnCircuit](file:///var/home/justin/Projects/Idris2-Boole/src/Logic/OnCircuit.idr#L12-L14) for expanding logic gates.

---



## 🔄 Sequential Möbius Transform over Maxels

Transitioning between poset evaluations and polynomial coefficients is generalized to multisets using **Maxel Inversion**.

A partial order relation (poset) on a set of nodes is represented as a **Zeta Maxel** (a multiset of relation pixels $[i, j]$ representing $i \le j$ with count $1$). The **Möbius Maxel** is the inverse of the Zeta Maxel under Maxel multiplication, containing the Möbius coefficients $\mu(i, j)$ as counts.

For an ongoing sequence of growing posets, we define this transform **sequentially** (an "on-Maxel" transform). Because the Zeta relation represents an upper-triangular matrix with $1$s on the diagonal, we compute its inverse recursively using a total back-substitution algorithm with structural Nat fuel:

```text
||| Computes the Möbius Maxel from a Zeta Maxel for a finite set of sorted nodes.
||| Zeta relation has count 1 for i <= j.
||| Returns the Möbius Maxel containing pixels with their correct Mobius counts.
public export
mobiusFromZeta : (Eq a, Num c, Neg c, Eq c) 
               => List a 
               -> Maxel metric c a 
               -> Maxel metric c a
mobiusFromZeta nodes zeta =
  let fuel = length nodes
  in fromList (concatMap (\i => map (\j => (MkPixel i j, mu fuel i j)) nodes) nodes)
  where
    zetaVal : a -> a -> c
    zetaVal u v = lookupCount (MkPixel u v) zeta

    mu : Nat -> a -> a -> c
    mu Z _ _ = 0
    mu (S f) i j =
      if i == j
         then 1
         else if zetaVal i j == 0
                 then 0
                 else negate (sumOver i j nodes)
      where
        sumOver : a -> a -> List a -> c
        sumOver _ _ [] = 0
        sumOver u v (k :: rest) =
          if u == k
             then sumOver u v rest
             else let term = if zetaVal u k /= 0 then zetaVal u k * mu f k v else 0
                  in term + sumOver u v rest
```

### How to use the transform sequentially:
Given an ongoing sequence of Zeta Maxels representing expanding poset structures:
$$\text{Zeta}(n) \in \text{OnMaxel metric c a}$$
we can map `mobiusFromZeta` pointwise over the sequence to produce the corresponding sequence of Möbius Maxels:
$$\text{Mobius}(n) = \text{map (mobiusFromZeta nodes) Zeta}$$
This enables the exact, rational Boole-Möbius transform to run dynamically over expanding states in real time.
