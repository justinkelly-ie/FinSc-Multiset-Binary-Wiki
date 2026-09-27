# 🔌 Bit Vexels & Logical Operators

Welcome to the **Finite Science Logic Layer (Row 1)**. This guide provides a step-by-step walkthrough for new users to construct, evaluate, and compose digital logic circuits using Wildberger's multiset-based singleton algebra in Idris 2.

In this framework, logic circuits are not represented by traditional syntax trees (ASTs). Instead, they are represented natively as **multisets** of coordinates and weights, enabling logic, arithmetic, and geometry to share a single unified representation.

---

## 🧭 Step-by-Step Circuit Guide

Here is how to build and evaluate a complete logic circuit from scratch.

### Step 1: Define Your Circuit Coordinates
Every logic wire or register pin is represented as a coordinate type. For example, let's define a simple 3-pin system:

```idris
module Wiki.Bit_vexel

import Stage0.Singleton.Sing
import Stage0.Vexel.Vexel
import Stage0.Multiset
import Stage0.Pixel
import Stage0.IntPolynumber
import Stage0.Vexel.DepVexel
import Stage0.Singleton.Bit
import Stage0.BoxInt
import Stage0.Vexel.Transformation
import Stage0.Singleton.SBFMset
import Stage1.Circuit
import Stage1.BoolePolynumber
import Stage0.Vexel.Byte
import Stage0.Singleton.SingFraction

vexelToMSetRuntime : Vexel Bit a -> List (a, Bit)
vexelToMSetRuntime ZeroM = []
vexelToMSetRuntime (AddM (MkSing x) w xs) = (x, w) :: vexelToMSetRuntime xs

-- Define the pins of our logic gate
data Pin = InA | InB | OutPin

Eq Pin where
  InA == InA = True
  InB == InB = True
  OutPin == OutPin = True
  _ == _ = False
```

---

### Step 2: Create the Input State (Vexel)
A **Vexel** represents the state vector of our pins. In Row 1, a `Byte` is defined as a list of Singletons:

```idris
-- A Byte representing InA = 1 and InB = 0, along with the constant high bias anchor
myInputState : Byte (LogicState Pin)
myInputState = AddM (MkSing (ConstState BaseAnchor)) One (AddM (MkSing (VarState InA)) One ZeroM)

```

---

### Step 3: Define the Gate Operator (Transform / Maxel)
A **Maxel** represents a transformation matrix or relational operator. In logic, we define this as a `TransformationMSet`, which is a multiset of directed relation links between pins:

```idris
-- Create a NOT gate from InA to OutPin
-- Internally: notGate = (1 -> OutPin) + (InA -> OutPin)
notGateOperator : TransformationMSet Pin
notGateOperator = notGate (VarState InA) (VarState OutPin)
```

---

### Step 4: Apply the Transform (Gate Execution)
Applying the transform to our input state propagates the signals and performs modulo-2 parity collapse:

```idris
-- Propagates InA through the NOT gate to OutPin
myOutputState : Byte (LogicState Pin)
myOutputState = applyTransformationVexel myInputState notGateOperator
-- Result: Since InA was active (1), 1 + 1 annihilates to 0. OutPin remains inactive.
```

---

### Step 5: Evaluate the Parity (Symmetric Bilinear Form / SBF)
A **Symmetric Bilinear Form** measures the overlap (dot product) of our state. We can construct a 1D parity metric template to query active states:

```idris
-- A metric template tracking the OutPin wire activity
outPinMetric : Multiset Bit (Pixel Blue (LogicState Pin))
outPinMetric = AddM (MkPixel (VarState OutPin) (VarState OutPin)) One ZeroM

-- Evaluate the activity level Q(v) of the output vector
outActivity : Bit
outActivity = evalSBFMset outPinMetric (fromList (vexelToMSetRuntime myOutputState))
```

---

### Step 6: Construct an Algebraic Polynomial Circuit
For complex composite circuits, we bypass manual relational networks and use **Polynomial Circuits** (`Circuit`), where gates evaluate as pure ring arithmetic:

```idris
-- NOT gate: 1 + x
notCircuit : Circuit
notCircuit = 1 + Var 0

-- XOR gate: x + y
xorCircuit : Circuit
xorCircuit = Var 0 + Var 1
```

To lift this Boolean logic circuit (Row 1) upward to the positional arithmetic circuit (Row 2), we use the Boole-Möbius bridge:

```idris
-- Lift the logic circuit into an integer-valued arithmetic carrier
liftedArithmetic : IntPolynumber
liftedArithmetic = liftCircuit xorCircuit
```

---

## 🛠️ The Multiset Architecture of Row 1

This table explains how the general multiset structures are specialized to form the digital logic layer:

| Structure | Type Definition | Role in Logic Layer | Multiset Property |
| :--- | :--- | :--- | :--- |
| **Sing** | `Sing Bit a` | Single active node state. | A multiset restricted to at most one element. |
| **Sing1** | `Sing1 Bit a` | Unit divisor for fractions. | A multiset restricted to exactly one element. |
| **Bit** | `Bit a x weight` | Dependent singleton bit. | Statically tracks coordinate and weight. |
| **Bit1** | `Bit1 a x` | Dependent active unit bit. | Bounded strictly to weight `One`. |
| **Vexel** | `Byte state` | State vector (register). | A collection of singletons representing active wires. |
| **Maxel** | `TransformationMSet` | Logical operator (relation matrix). | A multiset of directed wire-to-wire signals. |
| **SBF** | `row1SBF` | Parity junction metric. | A symmetric tensor template driving XOR collisions. |
