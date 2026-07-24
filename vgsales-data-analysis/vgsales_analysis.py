"""
=============================================================================
PROJETO: Análise Exploratória de Dados (EDA) - Vendas Globais de Video Games
Autor: Victor Oliveira
Ferramentas: Python, Pandas, Matplotlib, Seaborn
=============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo dos gráficos
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

def carregar_e_limpar_dados(caminho_csv):
    """
    Carrega o dataset e realiza a limpeza de valores nulos e tratamento de tipos.
    """
    print("1. Carregando dados...")
    df = pd.read_csv(caminho_csv)
    print(f"   Dimensão original: {df.shape[0]} linhas e {df.shape[1]} colunas.")
    
    # Tratamento de nulos
    df_clean = df.dropna(subset=['Year', 'Publisher']).copy()
    df_clean['Year'] = df_clean['Year'].astype(int)
    
    print(f"   Dimensão após limpeza: {df_clean.shape[0]} linhas.")
    return df_clean

def gerar_insights(df):
    """
    Gera resumos estatísticos e respostas para perguntas de negócio.
    """
    print("\n2. Principais Insights de Negócio:")
    
    # Top 5 Jogos mais vendidos no mundo
    top5_jogos = df[['Name', 'Platform', 'Year', 'Genre', 'Global_Sales']].head(5)
    print("\n--- Top 5 Jogos Mais Vendidos (Global - em milhões de unidades) ---")
    print(top5_jogos.to_string(index=False))
    
    # Vendas totais por região
    vendas_na = df['NA_Sales'].sum()
    vendas_eu = df['EU_Sales'].sum()
    vendas_jp = df['JP_Sales'].sum()
    vendas_outros = df['Other_Sales'].sum()
    vendas_global = df['Global_Sales'].sum()
    
    print("\n--- Distribuição de Vendas Globais por Região ---")
    print(f"América do Norte (NA): {vendas_na:.2f}M ({vendas_na/vendas_global*100:.1f}%)")
    print(f"Europa (EU): {vendas_eu:.2f}M ({vendas_eu/vendas_global*100:.1f}%)")
    print(f"Japão (JP): {vendas_jp:.2f}M ({vendas_jp/vendas_global*100:.1f}%)")
    print(f"Outras Regiões: {vendas_outros:.2f}M ({vendas_outros/vendas_global*100:.1f}%)")
    print(f"Total Acumulado: {vendas_global:.2f}M")
    
    # Top 5 Consoles/Plataformas
    top_plataformas = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(5)
    print("\n--- Top 5 Consoles mais Vendidos na História ---")
    for plat, vendas in top_plataformas.items():
        print(f" - {plat}: {vendas:.2f} milhões de cópias")
        
    # Gêneros mais populares no Japão vs América do Norte
    print("\n--- Preferências Regionais de Gênero ---")
    top_genero_na = df.groupby('Genre')['NA_Sales'].sum().idxmax()
    top_genero_jp = df.groupby('Genre')['JP_Sales'].sum().idxmax()
    print(f" Gênero mais vendido na América do Norte: {top_genero_na}")
    print(f" Gênero mais vendido no Japão: {top_genero_jp}")

if __name__ == "__main__":
    # Caminho do dataset no Google Drive ou local
    caminho = "g:/Meu Drive/Cursos/Tecnologia e Dados/ALURA/Python para Data Science/Datasets/VGSales/vgsales.csv"
    try:
        dados = carregar_e_limpar_dados(caminho)
        gerar_insights(dados)
    except Exception as e:
        print(f"Aviso: Não foi possível localizar o arquivo CSV no caminho direto: {e}")
