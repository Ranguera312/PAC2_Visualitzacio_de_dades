import os
import pandas as pd
import matplotlib.pyplot as plt
import ptitprince as pt
import seaborn as sns

# -----------------------------
# Ruta relativa al CSV
# -----------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "API_SP.DYN.LE00.IN_DS2_en_csv_v2_128.csv")

# -----------------------------
# Llegir CSV del World Bank
# -----------------------------
df = pd.read_csv(file_path, skiprows=4)

# -----------------------------
# Columnes que són anys
# -----------------------------
year_cols = [c for c in df.columns if c.isdigit()]

# -----------------------------
# Convertir format ample -> llarg
# -----------------------------
df_long = df.melt(
    id_vars=["Country Name", "Country Code"],
    value_vars=year_cols,
    var_name="Year",
    value_name="LifeExp"
)

# -----------------------------
# Convertir Year a int
# -----------------------------
df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")
df_long = df_long.dropna(subset=["Year"])
df_long["Year"] = df_long["Year"].astype(int)

# -----------------------------
# Assignar continent manualment
# -----------------------------
continent_map = {
  # EurAsia
    "France": "EurAsia",
    "Germany": "EurAsia",
    "Spain": "EurAsia",
    "Italy": "EurAsia",
    "United Kingdom": "EurAsia",
    "Sweden": "EurAsia",
    "China": "EurAsia",
    "India": "EurAsia",
    "Japan": "EurAsia",
    "South Korea": "EurAsia",
    # Amèrica
    "United States": "America",
    "Canada": "America",
    "Mexico": "America",
    "Brazil": "America",
    "Argentina": "America",
    "Chile": "America",
    "Cuba": "America",
    "Equador": "America",
    "Venezuela": "America",
    
    # Àfrica i Oceania
    "Nigeria": "Africa_Oceania",
    "Egypt": "Africa_Oceania",
    "South Africa": "Africa_Oceania",
    "Australia": "Africa_Oceania",
    "New Zealand": "Africa_Oceania",
    "Morocco": "Africa_Oceania",
    "Congo": "Africa_Oceania",
    "Zimbawe": "Africa_Oceania"
}

df_long["Continent"] = df_long["Country Name"].map(continent_map)
df_long = df_long.dropna(subset=["Continent"])

# -----------------------------
# Seleccionar any 2007
# -----------------------------
df_2007 = df_long[df_long["Year"] == 2007]

# -----------------------------
# Configuració de la figura
# -----------------------------
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# -----------------------------
# Raincloud amb ptitprince
# -----------------------------
pt.RainCloud(
    x="Continent",
    y="LifeExp",
    data=df_2007,
    palette="Set2",
    width_viol=0.6,
    bw=0.2,
    orient="h",
    alpha=0.7
)

plt.title("Esperança de vida per continent (2007)")
plt.ylabel("Continent")
plt.xlabel("Life expectancy")
plt.tight_layout()

# -----------------------------
# Guardar figura
# -----------------------------
output_path = os.path.join(base_dir, "Raincloud.png")
plt.savefig(output_path, dpi=300)
plt.show()