import os
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from itertools import combinations

base_dir = os.path.dirname(os.path.abspath(__file__))  # directori on està el script
file_path = os.path.join(base_dir, "facebook/414.circles")


circles = {}

# -------- llegir fitxer --------

with open(file_path, "r") as f:
    for line in f:
        parts = line.strip().split()
        name = parts[0]
        nodes = set(parts[1:])
        circles[name] = nodes

names = list(circles.keys())

# -------- buscar 3 cercles amb intersecció --------

selected = None

for a, b, c in combinations(names, 3):

    A = circles[a]
    B = circles[b]
    C = circles[c]

    if len(A & B) > 0 or len(A & C) > 0 or len(B & C) > 0:
        selected = (a, b, c)
        break

if selected is None:
    raise Exception("No hi ha cercles amb intersecció")

a, b, c = selected

A = circles[a]
B = circles[b]
C = circles[c]

print("Using:", a, b, c)

# -------- crear diagrama de Venn --------

plt.figure(figsize=(6,6))

venn3(
    subsets=(A, B, C),
    set_labels=(a, b, c)
)

plt.title("Cercles de Facebook de l'usuari 414")
output_path = os.path.join(base_dir, "VennDiagram.png")
plt.savefig(output_path, dpi=300)
plt.show()