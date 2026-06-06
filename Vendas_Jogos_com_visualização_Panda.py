import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Guia Pandas - IFNMG", layout="wide")

st.title("Visualização de Dados com Pandas")
st.markdown("### Guia Completo: Exploração, Filtros e Qualidade de Dados")


# --- Carregamento ---
URL_SUJO = 'https://raw.githubusercontent.com/suzanasvm/visualizacao_de_dados/refs/heads/main/datasets/vendas_videogame_dados_sujos.csv'

@st.cache_data
def carregar_dados():
    return pd.read_csv(URL_SUJO)

df = carregar_dados()

# --- Parte 2: Exploração Detalhada ---
st.header("2. Comandos de Exploração Inicial")
col1, col2 = st.columns(2)
with col1:
    if st.button("Ver Formato (Shape)"):
        st.write(f"Linhas e Colunas: {df.shape}")
    if st.button("Ver Nome das Colunas"):
        st.write(df.columns.tolist())
with col2:
    if st.button("Resumo Estatístico (.describe())"):
        st.write(df.describe())
    if st.checkbox("Mostrar DataFrame Completo"):
        st.dataframe(df)

# --- Parte 3: Seleção e Filtros ---
st.header("3. Seleção, Filtros e Consultas")
coluna = st.selectbox("Selecione a coluna para filtrar", df.columns)
valor = st.text_input(f"Digite o texto/valor para filtrar em {coluna}")

if valor:
    df_filtrado = df[df[coluna].astype(str).str.contains(valor, case=False, na=False)]
    st.write(f"Resultado do filtro:", df_filtrado)

# --- Parte 4: Qualidade de Dados (Limpeza) ---
st.header("4. Qualidade de Dados")
tab1, tab2, tab3 = st.tabs(["Valores Ausentes", "Duplicados", "Limpeza Geral"])

with tab1:
    st.write("Contagem de nulos:", df.isnull().sum())
    if st.button("Preencher nulos com 0"):
        df = df.fillna(0)
        st.success("Nulos preenchidos com 0.")

with tab2:
    st.write(f"Total de duplicados: {df.duplicated().sum()}")
    if st.button("Remover Duplicados"):
        df = df.drop_duplicates()
        st.success("Duplicados removidos.")

# --- Parte 5: Agrupamentos e Agregações ---
st.header("5. Agrupamentos e Agregações")
col_agrupar = st.selectbox("Selecione coluna para agrupar (Grupo)", df.columns)
col_analise = st.selectbox("Selecione coluna para calcular (Valor)", df.columns)

metodo = st.radio("Escolha a operação:", ["Soma", "Média", "Contagem"])

if st.button("Calcular Agrupamento"):
    if metodo == "Soma":
        st.write(df.groupby(col_agrupar)[col_analise].sum())
    elif metodo == "Média":
        st.write(df.groupby(col_agrupar)[col_analise].mean())
    else:
        st.write(df.groupby(col_agrupar).size())

# Dica de Visualização
st.sidebar.success("Guia IFNMG carregado com sucesso!")