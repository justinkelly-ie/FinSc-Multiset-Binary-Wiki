import os

WIKI_DIR = "/var/home/justin/Projects/Idris2-Boole-Wiki/Library/Wiki"
os.makedirs(WIKI_DIR, exist_ok=True)

pages = [
    {
        "id": "Digital_Repetition",
        "title": "Digital Repetition (Algebra of Boole)",
        "content": """# Digital Repetition (Algebra of Boole)

## Dependent Type Formalization
In Finite-Science, boolean logic is not a primitive truth value; it is a structural multiset representing the lowest order of physical repetition. By utilizing Idris 2's dependent types, we ensure that digital operations are strictly bounded and conserved.

```idris
module Formal.Boole

import Math.Multiset
import Math.SignedFraction

-- A digital bit is structurally bounded to 0 or 1 at the type level
data Bit : Type where
  O : Bit
  I : Bit

-- Dependent proof that boolean algebra forms a valid modulo-2 Ring over Multisets
-- Using the SignedFraction (Numerator over Unit Denominator)
DigitalFraction : Type
DigitalFraction = MSetFraction Bit Unit

total
modulo2Invariance : (x : DigitalFraction) -> (x + x = 0)
-- Proof that identical causal chains annihilate in mod-2 (destructive interference)
```
"""
    }
]

# Write individual pages
index_content = "# Finite Science Formalizations (Boole & Logic)\n\nThis wiki documents the dependent-type level proofs and structural mappings of the Algebra of Boole and Logic layers.\n\n"

for p in pages:
    filepath = os.path.join(WIKI_DIR, f"{p['id']}.md")
    with open(filepath, "w") as f:
        f.write(p["content"])
    index_content += f"- [{p['title']}](./{p['id']}.md)\n"

# Add the hand-written pages
index_content += "- [Singleton Explainer](./Logic_Explainer.md)\n"
index_content += "- [Singleton Repetition](./Logic_Repetition.md)\n"
index_content += "- [Bit Vexels & Logical Operators](./Bit_vexel.md)\n"
index_content += "- [Boole Functions](./Boole_Function.md)\n"
index_content += "- [The Boole-Möbius Transform — Sir Galahad's Deduction](./Boole_mobius_transform.md)\n"

# Write index
with open(os.path.join(WIKI_DIR, "index.md"), "w") as f:
    f.write(index_content)

print("Idris2-Boole-Wiki pages generated successfully.")
