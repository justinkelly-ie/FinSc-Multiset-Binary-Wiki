import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.join(SCRIPT_DIR, "Library", "Wiki")

os.makedirs(WIKI_DIR, exist_ok=True)

pages = [
    {"id": "Digital_Repetition", "title": "Digital Repetition (Algebra of Boole)"},
    {"id": "Logic_Explainer", "title": "Singleton Explainer"},
    {"id": "Logic_Repetition", "title": "Singleton Repetition"},
    {"id": "Bit_vexel", "title": "Bit Vexels & Logical Operators"},
    {"id": "Boole_Function", "title": "Boole Functions"},
    {"id": "Boole_mobius_transform", "title": "The Boole-Möbius Transform — Sir Galahad's Deduction"},
]

index_content = "# Finite Science Formalizations (Boole & Logic)\n\nThis wiki documents the dependent-type level proofs and structural mappings of the Algebra of Boole and Logic layers.\n\n"

for p in pages:
    filepath = os.path.join(WIKI_DIR, f"{p['id']}.md")
    title = p["title"]
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line_str = line.strip()
                if line_str.startswith("# "):
                    raw_title = line_str[2:].strip()
                    title = raw_title.replace("[", "").replace("]", "")
                    break
    index_content += f"- [{title}](./{p['id']}.md)\n"

index_path = os.path.join(WIKI_DIR, "index.md")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Idris2-Boole-Wiki index updated successfully.")
