import pandas as pd

BASE_PATH = "data/processed/"

# =========================
# DADOS
# =========================
df = pd.read_csv(f"{BASE_PATH}enem_base.csv")
df_grouped = pd.read_csv(f"{BASE_PATH}enem_grouped.csv")

# =========================
# FILTROS
# =========================
faixa_etaria = pd.read_csv(
    f"{BASE_PATH}filtro_faixa_etaria.csv"
)["faixa_etaria"].tolist()

cor_raca = pd.read_csv(
    f"{BASE_PATH}filtro_cor_raca.csv"
)["cor_raca"].tolist()

presenca = pd.read_csv(
    f"{BASE_PATH}filtro_presenca.csv"
)["presenca"].tolist()

# Opção padrão
faixa_etaria.append("todos os candidatos")
cor_raca.append("todos os candidatos")
presenca.append("todos os candidatos")
