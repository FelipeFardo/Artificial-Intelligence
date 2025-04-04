import streamlit as st
import pandas as pd

# Carregar Dados e colocar no Cache do Streamlit

@st.cache_data
def load_data():
  return pd.read_csv('./datasets/clustering_laptops.csv')

df = load_data()

# Sidebar para Filtro
st.sidebar.header('Filtros')

# Selecionar modelos

model = st.sidebar.selectbox('Selecionar Modelo', df['model'].unique())

# Filtar modelo
df_laptops_model = df[df['model']== model]

# Filtrar cluster do model escolhido
df_laptops_finale = df[df['cluster'] == df_laptops_model.iloc[0]['cluster']]

# Visualizar modelos

st.write('Recomendações de Modelos')
st.table(df_laptops_finale)