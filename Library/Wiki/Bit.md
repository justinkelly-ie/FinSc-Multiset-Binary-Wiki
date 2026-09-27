# ⬛ Bit — The Bified B₂ Field

> **The two-element field {0, 1} represented directly as multisets.**
>
> A `Bit` is a `Sing` (singleton multiset containing exactly one element)
> where that element is restricted to the two canonical B₂ multiset values:
> `0 = []` (the empty multiset) and `1 = [[]]` (the multiset containing one empty multiset).

```idris
module Wiki.Bit

import Stage0.Singleton.Bit
```

---

## Foundations: Bification of B₂

Wildberger's **bification** principle encodes arithmetic in the von Neumann ordinal
tradition, where every number *is* a set of smaller numbers:

| B₂ value | Multiset notation | Sing notation |
| :--- | :--- | :--- |
| **0** | `[]` — the empty multiset | `Zero = MkSing ZeroM` |
| **1** | `[[]]` — the multiset containing one empty multiset | `One = MkSing (AddM ZeroM 1 ZeroM)` |

A `Bit` wraps one of these inside a `Sing` — a singleton multiset `{ m }`.
`Bit` is a type alias, not a wrapper:

```
Bit = Sing (Multiset BoxInt (Multiset BoxInt Void))
```

---

## The Two Canonical Values

```idris
-- Inspect the two canonical Bit values
showBits : List String
showBits = [show Zero, show One]
-- Result: ["0", "1"]
```

```idris
-- Distinguish values with predicates
checkZero : Bool
checkZero = isZero Zero   -- True

checkOne : Bool
checkOne = isOne One      -- True

notConfused : Bool
notConfused = isOne Zero  -- False
```

---

## B₂ Field Arithmetic

The two-element field **B₂ = {0, 1}** has characteristic 2.
Every operation closes within `{ Zero, One }`.

### Addition — XOR (mod 2)

| `x` | `y` | `x + y` |
| :--- | :--- | :--- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

```idris
-- Addition examples
ex_add_00 : Bit
ex_add_00 = Zero + Zero   -- Zero

ex_add_01 : Bit
ex_add_01 = Zero + One    -- One

ex_add_10 : Bit
ex_add_10 = One + Zero    -- One

ex_add_11 : Bit
ex_add_11 = One + One     -- Zero (self-annihilation)
```

Key consequences of addition in B₂:

- **Identity**: `x + Zero = x`
- **Self-annihilation**: `x + x = Zero` — every element is its own additive inverse
- **Commutativity**: `x + y = y + x`

### Multiplication — AND

| `x` | `y` | `x * y` |
| :--- | :--- | :--- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

```idris
-- Multiplication examples
ex_mul_00 : Bit
ex_mul_00 = Zero * Zero   -- Zero

ex_mul_11 : Bit
ex_mul_11 = One * One     -- One

ex_mul_01 : Bit
ex_mul_01 = One * Zero    -- Zero (annihilation)

-- Bit is idempotent under multiplication: bit² = bit
ex_square_zero : Bit
ex_square_zero = Zero * Zero   -- Zero

ex_square_one : Bit
ex_square_one = One * One      -- One
```

> **Bit² = Bit.** Every element of B₂ is idempotent under multiplication:
> `x * x = x`. This is the defining property that distinguishes the two-element
> field from ordinary integer arithmetic, where squaring is not the identity.

Key consequences of multiplication in B₂:

- **Idempotence**: `x * x = x` — bit squared equals bit
- **Identity**: `x * One = x`
- **Annihilation**: `x * Zero = Zero`
- **Commutativity**: `x * y = y * x`

### Negation and Subtraction

In the Algebra of Boole, negation is defined as the complement (adding 1): `negate x = 1 + x`.
Consequently, negation toggles the value:
- `negate Zero = One`
- `negate One  = Zero`

Subtraction is defined via the complement: `x - y = x + (1 + y)`.

```idris
-- Negation is complement
ex_neg : Bit
ex_neg = negate One   -- Zero

-- Subtraction is addition of complement
ex_sub : Bit
ex_sub = One - One    -- One (same as One + Zero)
```

### fromInteger — mod-2 embedding

```idris
-- Even integers map to Zero, odd to One
ex_fromInt0 : Bit
ex_fromInt0 = fromInteger 0   -- Zero

ex_fromInt1 : Bit
ex_fromInt1 = fromInteger 1   -- One

ex_fromInt2 : Bit
ex_fromInt2 = fromInteger 2   -- Zero  (2 mod 2 = 0)

ex_fromInt3 : Bit
ex_fromInt3 = fromInteger 3   -- One   (3 mod 2 = 1)
```

---

## Conversions

```idris
-- Bit <-> Nat
ex_bitToNat : Nat
ex_bitToNat = bitToNat One    -- S Z

ex_natToBit : Bit
ex_natToBit = natToBit 7      -- One  (7 mod 2 = 1)

-- Bit -> Integer
ex_integer : Integer
ex_integer = bitToInteger Zero  -- 0

-- normalize is idempotent
ex_norm : Bit
ex_norm = normalize (normalize One)  -- One
```

---

## Embedding into Sing

Since `Bit` is a type alias for `Sing BoxInt (Multiset BoxInt Void)`,
the `toSing` and `fromSing` functions from `Math.Singleton.Sing` apply
directly — add `import Stage0.Singleton.Sing` if you need them:

- `fromSing Zero` returns `ZeroM` — the empty multiset `[]`
- `fromSing One` returns `AddM ZeroM 1 ZeroM` — the multiset `[[]]`
- `toSing (fromSing x) = x` for all `x : Bit`

---

## Architecture Position

```
Row 0  Multiset c a           — general weighted multiset
         ↓
Row 1  Sing c a               — singleton: exactly one Multiset element
         ↓
Row 1  Bit                    — Sing restricted to { [], [[]] }
                                the bified B₂ = {0, 1}
         ↓
       Vexel / Byte           — lists of Bits forming state vectors
         ↓
       Circuit / BoolePolynumber  — polynomial logic over Bit coefficients
```

`Bit` is the **base layer of the logic stack**. Bytes, Vexels, and
Circuit evaluations are all built on top of `Bit` as their coefficient type.

---

## QuickCheck Properties

The following field axioms are machine-verified in
`tests/definitions/bit/Main.idr` against 100 randomly generated `Bit` values:

| Property | Statement |
| :--- | :--- |
| `prop_zeroNeOne` | `Zero ≠ One` |
| `prop_zeroIsEmptyMultiset` | `fromSing Zero = ZeroM` |
| `prop_oneIsUnitMultiset` | `fromSing One = AddM ZeroM 1 ZeroM` |
| `prop_addCommutative` | `x + y = y + x` |
| `prop_addIdentity` | `x + Zero = x` |
| `prop_addSelfAnnihilates` | `x + x = Zero` |
| `prop_mulCommutative` | `x * y = y * x` |
| `prop_mulIdentity` | `x * One = x` |
| `prop_mulZeroAnnihilates` | `x * Zero = Zero` |
| `prop_mulIdempotent` | `x * x = x` |
| `prop_distributive` | `x * (y + z) = (x * y) + (x * z)` |
| `prop_negInvolutive` | `negate (negate x) = x` |
| `prop_subIsComplementAdd` | `x - y = x + 1 + y` |
| `prop_natRoundTrip` | `natToBit (bitToNat x) = x` |
| `prop_fromIntegerMod2` | `fromInteger 2 = Zero`, `fromInteger 3 = One` |
| `prop_singEmbedding` | `toSing (fromSing x) = x` |
