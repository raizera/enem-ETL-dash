# 📊 ENEM 2020 – Análise Exploratória de Dados com Dash

Este projeto realiza uma **Análise Exploratória de Dados (EDA)** dos microdados do **ENEM 2020**, com foco no **perfil socioeconômico e cultural dos candidatos** e na **ausência (eliminação)** no exame. A aplicação foi desenvolvida em **Python**, utilizando **Pandas**, **Plotly** e **Dash**, com arquitetura otimizada para performance por meio do pré-processamento dos dados.

---

## 🎯 Objetivo do Projeto

* Explorar características socioeconômicas dos participantes do ENEM 2020
* Analisar relações entre **faixa etária**, **sexo**, **cor/raça**, **tipo de escola** e **presença no exame**
* Identificar padrões associados à **ausência dos candidatos**
* Disponibilizar os resultados em um **dashboard interativo**

---

## 🧱 Arquitetura do Projeto

O projeto foi estruturado em **três etapas principais**, separando dados brutos, processamento e visualização:

```
enem-dash/
│
├── app.py                 # Aplicação Dash
├── data/
│   ├── raw/               # ❌ Microdados brutos (IGNORADO pelo Git)
│   │   └── MICRODADOS_ENEM_2020.csv
│   │
│   ├── processed/         # ✅ Dados processados (leves)
│   │   ├── enem_base.csv
│   │   └── enem_filters.csv
│   │
│   └── build_data.py      # Script de pré-processamento
│
├── venv/                  # Ambiente virtual (IGNORADO)
├── .gitignore
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

* **Python 3.10+**
* **Pandas** – processamento e agregação dos dados
* **Plotly Express / Graph Objects** – visualizações interativas
* **Dash** – criação do dashboard web
* **Dash Bootstrap Components** – layout e estilização

---

## 🔄 Pipeline de Dados

### 1️⃣ Dados brutos

* Fonte oficial: INEP – Microdados do ENEM 2020
* Arquivo grande (~GB), **não versionado**

### 2️⃣ Pré-processamento (`build_data.py`)

Responsável por:

* Selecionar colunas relevantes
* Renomear variáveis para nomes semânticos
* Mapear códigos numéricos para categorias textuais
* Remover dados ausentes
* Gerar **CSVs agregados e leves**

Arquivos gerados:

* `enem_base.csv` → base principal usada pelo Dash
* `enem_filters.csv` → listas de valores únicos para filtros (dropdowns)

### 3️⃣ Visualização (`app.py`)

* Carrega apenas CSVs processados
* Cria gráficos interativos (histogramas, heatmaps, scatter, polar)
* Aplica filtros dinâmicos via callbacks

👉 **Resultado**: aplicação rápida, leve e pronta para deploy

---

## ▶️ Como Executar o Projeto

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Gerar os dados processados

> ⚠️ É necessário ter o microdados em `data/raw/`

```bash
python data/build_data.py
```

### 4️⃣ Executar a aplicação

```bash
python app.py
```

Acesse no navegador:

```
http://localhost:8050
```

---

## 📊 Principais Visualizações

* Cor/Raça × Faixa Etária
* Sexo × Cor/Raça
* Tipo de Escola × Cor/Raça
* Faixa Etária × Presença no Exame
* Heatmaps de densidade (faixa etária × residentes)
* Gráficos polares e distribuições

Todos os gráficos permitem:

* Filtro por faixa etária
* Zoom e seleção interativa
* Exportação como imagem

---

## 🧠 Contexto Acadêmico

Este projeto está alinhado a estudos na área de **Educação em Ciências** e **Análise de Dados Educacionais**, podendo ser utilizado como:

* Base empírica para artigos científicos
* Apoio à tomada de decisão educacional
* Exemplo de uso de **ferramentas computacionais e IA** na análise educacional

---

## 📌 Boas Práticas Adotadas

* Separação entre dados brutos e processados
* Uso de `.gitignore` para arquivos grandes
* Código modular e legível
* Otimização de performance para dashboards

---

## 📄 Licença e Dados

* Código: uso acadêmico e educacional
* Dados: INEP – uso conforme termos oficiais

🔗 Fonte dos dados: [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

---

## ✍️ Autor

**Rai Garcia Torres**
Projeto desenvolvido para fins acadêmicos e exploratórios.

---

🚀 *Sugestões, melhorias e extensões são bem-vindas!*
