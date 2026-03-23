import os
import pandas as pd
import matplotlib.pyplot as plt

# -------- director base del script --------
base_dir = os.path.dirname(os.path.abspath(__file__))  # directori on està aquest script
csv_file = os.path.join(base_dir, "Registre_d'explotacions_ramaderes_20260322.csv")          # fitxer CSV al mateix directori

# -------- llegir CSV --------
# Assumeix que el CSV té dues columnes: 'Categoria' i 'Valor'
df = pd.read_csv(csv_file)
columna_id_granja = "Codi REGA"  # Substitueix pel nom de la columna amb l'identificador únic
dataset_unic = df.drop_duplicates(subset=[columna_id_granja])

# 3. Comptem els valors d'una altra columna, per exemple "Columna1", només amb una entrada per granja
columna_a_comptar = "Tipus explotació"  # Substitueix pel nom de la columna que vulguis comptar
conteig = dataset_unic[columna_a_comptar].value_counts().reset_index()
conteig.columns = ['Valor', 'Nombre']  # Renombrem les columnes

nou_fitxer = os.path.join(base_dir, "dataset_resultat_2.csv")

# 5. Guardem el resultat
conteig.to_csv(nou_fitxer, index=False)

# -------- crear pie chart --------
plt.figure(figsize=(8,8))
plt.pie(
    conteig['Nombre'], 
    labels=None, 
    autopct='%1.1f%%',       # percentatge dins de cada sector
    startangle=90,           # rotació inicial
    colors=plt.cm.tab20.colors,  # paleta de colors
    pctdistance=1.1,  # Distància dels percentatges al centre
    )

plt.title("Tipus d'explotació ramadera a Catalunya")
plt.legend(conteig['Valor'],loc='upper left')
plt.tight_layout()


output_path = os.path.join(base_dir, "piechart.png")
plt.savefig(output_path, dpi=300)
print(f"La imatge s'ha guardat com a '{output_path}'")

plt.show()
