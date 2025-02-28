import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
def carregar_dados():
    file_path = "KOP.xlsx"
    df = pd.read_excel(file_path, sheet_name="Sheet0")
    return df

df = carregar_dados()

# Contagem de lojas ativas e inativas
status_counts = df["Status"].value_counts()

# Definir cores personalizadas
colors = {"Ativa": "green", "Inativa": "red"}

# Mostrar a planilha
tab1, tab2 = st.tabs(["Gráfico", "Dados"])
with tab2:
    st.write("### Dados da Planilha")
    st.dataframe(df)

# Criar gráfico de pizza
fig = px.pie(names=status_counts.index, values=status_counts.values, 
             title="Distribuição de Lojas Ativas e Inativas",
             color=status_counts.index, color_discrete_map=colors)

# Exibir no Streamlit
st.title("Dashboard de Lojas")
st.plotly_chart(fig)

