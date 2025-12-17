import os
import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# ======================================================
# CONFIGURAÇÃO
# ======================================================

BASE_PATH = "data/processed"

# ======================================================
# LOAD DOS DADOS PROCESSADOS
# ======================================================

df = pd.read_csv(f"{BASE_PATH}/enem_base.csv")
filters = pd.read_csv(f"{BASE_PATH}/enem_filters.csv")

faixas_etarias = sorted(filters["faixa_etaria"].dropna().unique().tolist())
faixas_etarias.append("todos os candidatos")

cor_raca = sorted(filters["cor_raca"].dropna().unique().tolist())
cor_raca.append("todos os candidatos")

# ======================================================
# FUNÇÃO AUXILIAR PARA FILTRO
# ======================================================

def filtrar_df(valor, coluna):
    if valor == "todos os candidatos":
        return df
    return df[df[coluna] == valor]

# ======================================================
# APP
# ======================================================

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
server = app.server

# ======================================================
# LAYOUT
# ======================================================

app.layout = dbc.Container(
    fluid=True,
    children=[

        html.H1("EDA – ENEM 2020"),
        html.H4("Perfil socioeconômico e presença no exame"),

        dcc.Markdown(
            """
**Fonte dos dados:**  
https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

Os dados exibidos aqui foram **pré-processados** para garantir melhor desempenho da aplicação.
"""
        ),

        html.Hr(),

        # ==================================================
        # COR / RAÇA x FAIXA ETÁRIA
        # ==================================================

        html.H5("Cor/Raça × Faixa Etária"),

        dcc.Dropdown(
            id="filtro_faixa_01",
            options=faixas_etarias,
            value="todos os candidatos",
            clearable=False
        ),

        dcc.Graph(id="grafico_01"),

        html.Hr(),

        # ==================================================
        # SEXO x COR / RAÇA
        # ==================================================

        html.H5("Sexo × Cor/Raça"),

        dcc.Dropdown(
            id="filtro_cor_02",
            options=cor_raca,
            value="todos os candidatos",
            clearable=False
        ),

        dcc.Graph(id="grafico_02"),

        html.Hr(),

        # ==================================================
        # SITUAÇÃO DE ENSINO x COR / RAÇA
        # ==================================================

        html.H5("Situação de Ensino × Cor/Raça"),

        dcc.Dropdown(
            id="filtro_cor_03",
            options=cor_raca,
            value="todos os candidatos",
            clearable=False
        ),

        dcc.Graph(id="grafico_03"),

        html.Hr(),

        # ==================================================
        # PRESENÇA NO EXAME
        # ==================================================

        html.H5("Presença no Exame × Faixa Etária"),

        dcc.Dropdown(
            id="filtro_faixa_04",
            options=faixas_etarias,
            value="todos os candidatos",
            clearable=False
        ),

        dcc.Graph(id="grafico_04"),

    ]
)

# ======================================================
# CALLBACKS
# ======================================================

@app.callback(
    Output("grafico_01", "figure"),
    Input("filtro_faixa_01", "value")
)
def grafico_cor_faixa(valor):
    dff = filtrar_df(valor, "faixa_etaria")

    fig = px.histogram(
        dff,
        x="cor_raca",
        y="quantidade",
        color="faixa_etaria",
        barmode="group"
    )
    return fig


@app.callback(
    Output("grafico_02", "figure"),
    Input("filtro_cor_02", "value")
)
def grafico_sexo_cor(valor):
    dff = filtrar_df(valor, "cor_raca")

    fig = px.histogram(
        dff,
        x="sexo",
        y="quantidade",
        color="cor_raca",
        barmode="group"
    )
    return fig


@app.callback(
    Output("grafico_03", "figure"),
    Input("filtro_cor_03", "value")
)
def grafico_situacao_cor(valor):
    dff = filtrar_df(valor, "cor_raca")

    fig = px.histogram(
        dff,
        x="situacao_ensino",
        y="quantidade",
        color="cor_raca",
        barmode="group"
    )
    return fig


@app.callback(
    Output("grafico_04", "figure"),
    Input("filtro_faixa_04", "value")
)
def grafico_presenca(valor):
    dff = filtrar_df(valor, "faixa_etaria")

    fig = px.histogram(
        dff,
        x="faixa_etaria",
        y="quantidade",
        color="presenca",
        barmode="group"
    )
    return fig


# ======================================================
# RUN
# ======================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8050)),
        debug=False
    )
