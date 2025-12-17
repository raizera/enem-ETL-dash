import pandas as pd
from pathlib import Path

# =====================================
# PATHS
# =====================================

RAW_PATH = Path("data/raw/MICRODADOS_ENEM_2020.csv")
OUT_PATH = Path("data/processed")

OUT_PATH.mkdir(parents=True, exist_ok=True)

# =====================================
# LOAD MICRODADOS
# =====================================

df = pd.read_csv(
    RAW_PATH,
    sep=";",
    encoding="ISO-8859-1",
    low_memory=False
)

# =====================================
# COLUNAS DE INTERESSE
# =====================================

cols = [
    "TP_FAIXA_ETARIA",
    "TP_SEXO",
    "TP_COR_RACA",
    "TP_ST_CONCLUSAO",
    "TP_ESCOLA",
    "TP_PRESENCA_CN"
]

df = df[cols].dropna()

# =====================================
# RENOMEAR
# =====================================

df = df.rename(columns={
    "TP_FAIXA_ETARIA": "faixa_etaria",
    "TP_SEXO": "sexo",
    "TP_COR_RACA": "cor_raca",
    "TP_ST_CONCLUSAO": "situacao_ensino",
    "TP_ESCOLA": "tipo_escola",
    "TP_PRESENCA_CN": "presenca"
})

# =====================================
# MAPEAR CÓDIGOS
# =====================================

df["sexo"] = df["sexo"].map({"F": "Feminino", "M": "Masculino"})

df["cor_raca"] = df["cor_raca"].map({
    0: "Não declarado",
    1: "Branca",
    2: "Preta",
    3: "Parda",
    4: "Amarela",
    5: "Indígena"
})

df["situacao_ensino"] = df["situacao_ensino"].map({
    1: "Concluiu",
    2: "Cursando",
    3: "Cursando",
    4: "Evasão"
})

df["presenca"] = df["presenca"].map({
    0: "Eliminado",
    1: "Presente",
    2: "Eliminado"
})

df["faixa_etaria"] = df["faixa_etaria"].map({
    1: "16", 2: "17", 3: "18", 4: "19", 5: "20",
    6: "21", 7: "22", 8: "23", 9: "24", 10: "25",
    11: "26-30", 12: "31-35", 13: "36-40",
    14: "41-45", 15: "46-50", 16: "51-55",
    17: "56-60", 18: "61-65", 19: "66-70", 20: ">70"
})

df = df.dropna()

# =====================================
# AGREGAÇÃO
# =====================================

df_base = (
    df
    .groupby(
        ["faixa_etaria", "sexo", "cor_raca", "situacao_ensino", "presenca"],
        as_index=False
    )
    .size()
    .rename(columns={"size": "quantidade"})
)

# =====================================
# SALVAR BASE PRINCIPAL
# =====================================

df_base.to_csv(OUT_PATH / "enem_base.csv", index=False)

# =====================================
# GERAR FILTERS (CORRETAMENTE!)
# =====================================

filters = {
    "faixa_etaria": sorted(df_base["faixa_etaria"].unique()),
    "cor_raca": sorted(df_base["cor_raca"].unique()),
}

filters_df = pd.concat(
    [pd.Series(v, name=k) for k, v in filters.items()],
    axis=1
)

filters_df.to_csv(OUT_PATH / "enem_filters.csv", index=False)

print("✅ Arquivos gerados com sucesso!")
