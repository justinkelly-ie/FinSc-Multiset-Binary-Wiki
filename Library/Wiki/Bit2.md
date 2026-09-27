# ⬛ Bit2 — The Bified B₂ Field over DepMultiset

> **The two-element bi-field {0, 1} represented as a dependently typed multiset of size 1.**
>
> A `Bit2` is a `DepMultiset` of size 1 whose single element is itself a `Multiset`,
> restricted to the two canonical B₂ values:
> `0 = []` (the empty multiset) and `1 = [[]]` (the multiset containing one empty multiset).
>
> `Bit2` differs from `Bit` in that the element and its type-level index are
> tracked by `DepMultiset` rather than `Sing`.

```idris
module Wiki.Bit2

import Stage0.Singleton.Bit2
```

---

## Foundations: Bification of B₂ via DepMultiset

Both `Bit` and `Bit2` represent the same two B₂ values. The difference is
the **carrier structure**:

| | `Bit` | `Bit2` |
| :--- | :--- | :--- |
| Carrier | `Sing (Multiset BoxInt (Multiset BoxInt Void))` | `DepMultiset BoxInt (Multiset BoxInt (Multiset BoxInt Void)) idx` |
| Index tracked | no (runtime only) | yes (type-level `Multiset`) |
| Constructor style | `MkSing m` | `DepAddM m 1 DepEmptyM` |

Because the two `Bit2` values carry **different type-level indices**, they cannot
share a single type alias. The runtime `Bit2` data type wraps both and erases
the index:

```
ZeroIdx : Multiset BoxInt (Multiset BoxInt (Multiset BoxInt Void))
ZeroIdx = AddM ZeroM 1 ZeroM                        -- one entry: ZeroM with count 1

OneIdx  : Multiset BoxInt (Multiset BoxInt (Multiset BoxInt Void))
OneIdx  = AddM (AddM ZeroM 1 ZeroM) 1 ZeroM         -- one entry: [[]] with count 1

Zero2 : DepMultiset BoxInt (Multiset BoxInt (Multiset BoxInt Void)) ZeroIdx
Zero2 = DepAddM ZeroM 1 DepEmptyM                   -- element = []

One2  : DepMultiset BoxInt (Multiset BoxInt (Multiset BoxInt Void)) OneIdx
One2  = DepAddM (AddM ZeroM 1 ZeroM) 1 DepEmptyM   -- element = [[]]
```

The runtime `Bit2` sum type:

```
data Bit2 : Type where
  Bit2Zero : DepMultiset BoxInt (Multiset BoxInt (Multiset BoxInt Void)) ZeroIdx -> Bit2
  Bit2One  : DepMultiset BoxInt (Multiset BoxInt (Multiset BoxInt Void)) OneIdx  -> Bit2
```

---

## The Two Canonical Values

```idris
-- Inspect the two canonical Bit2 values
showBit2s : List String
showBit2s = [show b2Zero, show b2One]
-- Result: ["0", "1"]
```

```idris
-- Distinguish values with predicates
checkB2Zero : Bool
checkB2Zero = isB2Zero b2Zero   -- True

checkB2One : Bool
checkB2One = isB2One b2One      -- True

notConfused : Bool
notConfused = isB2One b2Zero    -- False
```

---

## B₂ Field Arithmetic

The two-element field **B₂ = {0, 1}** has characteristic 2.
Every operation closes within `{ b2Zero, b2One }`.

### Addition — XOR (mod 2)

| `x` | `y` | `x + y` |
| :--- | :--- | :--- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

```idris
-- Addition examples
ex_add_00 : Bit2
ex_add_00 = b2Zero + b2Zero   -- b2Zero

ex_add_01 : Bit2
ex_add_01 = b2Zero + b2One    -- b2One

ex_add_10 : Bit2
ex_add_10 = b2One + b2Zero    -- b2One

ex_add_11 : Bit2
ex_add_11 = b2One + b2One     -- b2Zero (self-annihilation)
```

Key consequences of addition in B₂:

- **Identity**: `x + b2Zero = x`
- **Self-annihilation**: `x + x = b2Zero` — every element is its own additive inverse
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
ex_mul_00 : Bit2
ex_mul_00 = b2Zero * b2Zero   -- b2Zero

ex_mul_11 : Bit2
ex_mul_11 = b2One * b2One     -- b2One

ex_mul_01 : Bit2
ex_mul_01 = b2One * b2Zero    -- b2Zero (annihilation)

-- Bit2 is idempotent under multiplication: bit² = bit
ex_square_zero : Bit2
ex_square_zero = b2Zero * b2Zero   -- b2Zero

ex_square_one : Bit2
ex_square_one = b2One * b2One      -- b2One
```

> **Bit2² = Bit2.** Every element of B₂ is idempotent under multiplication:
> `x * x = x`. This holds for `Bit2` exactly as it does for `Bit`.

Key consequences of multiplication in B₂:

- **Idempotence**: `x * x = x` — bit squared equals bit
- **Identity**: `x * b2One = x`
- **Annihilation**: `x * b2Zero = b2Zero`
- **Commutativity**: `x * y = y * x`

### Negation and Subtraction

In the Algebra of Boole, negation is defined as the complement (adding 1): `negate x = 1 + x`.
Consequently, negation toggles the value:
- `negate b2Zero = b2One`
- `negate b2One  = b2Zero`

Subtraction is defined via the complement: `x - y = x + (1 + y)`.

```idris
-- Negation is complement
ex_neg : Bit2
ex_neg = negate b2One   -- b2Zero

-- Subtraction is addition of complement
ex_sub : Bit2
ex_sub = b2One - b2One  -- b2One (same as b2One + b2Zero)
```

### fromInteger — mod-2 embedding

```idris
-- Even integers map to b2Zero, odd to b2One
ex_fromInt0 : Bit2
ex_fromInt0 = fromInteger 0   -- b2Zero

ex_fromInt1 : Bit2
ex_fromInt1 = fromInteger 1   -- b2One

ex_fromInt2 : Bit2
ex_fromInt2 = fromInteger 2   -- b2Zero  (2 mod 2 = 0)

ex_fromInt3 : Bit2
ex_fromInt3 = fromInteger 3   -- b2One   (3 mod 2 = 1)
```

---

## Conversions

```idris
-- Bit2 <-> Nat
ex_bit2ToNat : Nat
ex_bit2ToNat = bit2ToNat b2One    -- S Z

ex_natToBit2 : Bit2
ex_natToBit2 = natToBit2 7        -- b2One  (7 mod 2 = 1)

-- Bit2 -> Integer
ex_integer : Integer
ex_integer = bit2ToInteger b2Zero  -- 0

-- normalize is idempotent
ex_norm : Bit2
ex_norm = normalizeBit2 (normalizeBit2 b2One)  -- b2One
```

---

## Recovering the DepMultiset: freezeBit2

Since `Bit2` wraps a `DepMultiset`, `freezeBit2` recovers the runtime `Multiset`
that the `DepMultiset` tracks at the type level:

```idris
-- freezeBit2 b2Zero = ZeroM              (the empty multiset [])
-- freezeBit2 b2One  = AddM ZeroM 1 ZeroM (the multiset [[]])
```

This is the analogue of `fromSing` in `Bit`. Add
`import Stage0.DepMultiset` if you need `freezeDep` directly.

---

## Bit vs Bit2 — Comparison

| Aspect | `Bit` (`Sing`) | `Bit2` (`DepMultiset`) |
| :--- | :--- | :--- |
| Zero constructor | `MkSing ZeroM` | `DepAddM ZeroM 1 DepEmptyM` |
| One constructor | `MkSing (AddM ZeroM 1 ZeroM)` | `DepAddM (AddM ZeroM 1 ZeroM) 1 DepEmptyM` |
| Type-level index | none | `ZeroIdx` / `OneIdx` |
| Runtime type | type alias | `data Bit2` sum type |
| Extraction | `fromSing` | `freezeBit2` / `freezeDep` |
| B₂ arithmetic | identical | identical |
| Linear instances | identical | identical |

---

## Architecture Position

```
Row 0  Multiset c a               — general weighted multiset
         ↓
Row 0  DepMultiset c a contents   — Multiset with type-level index
         ↓
Row 1  DepMultiset of size 1      — Zero2 / One2 (index-tracked singletons)
         ↓
Row 1  Bit2                       — runtime B₂ = {0, 1} over DepMultiset
                                    same field as Bit, different carrier
```

`Bit2` sits at the same logical level as `Bit` in the algebra stack.
The `DepMultiset` carrier makes the type-level index explicit, which
can be useful when proofs need to inspect which B₂ value is present
without runtime pattern-matching.

---

## QuickCheck Properties

The same field axioms hold for `Bit2` as for `Bit`:

| Property | Statement |
| :--- | :--- |
| `prop_b2zeroNeb2One` | `b2Zero ≠ b2One` |
| `prop_addCommutative` | `x + y = y + x` |
| `prop_addIdentity` | `x + b2Zero = x` |
| `prop_addSelfAnnihilates` | `x + x = b2Zero` |
| `prop_mulCommutative` | `x * y = y * x` |
| `prop_mulIdentity` | `x * b2One = x` |
| `prop_mulZeroAnnihilates` | `x * b2Zero = b2Zero` |
| `prop_mulIdempotent` | `x * x = x` |
| `prop_distributive` | `x * (y + z) = (x * y) + (x * z)` |
| `prop_negInvolutive` | `negate (negate x) = x` |
| `prop_subIsComplementAdd` | `x - y = x + 1 + y` |
| `prop_natRoundTrip` | `natToBit2 (bit2ToNat x) = x` |
| `prop_fromIntegerMod2` | `fromInteger 2 = b2Zero`, `fromInteger 3 = b2One` |
