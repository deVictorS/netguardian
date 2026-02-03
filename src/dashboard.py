import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

DB_PATH = "../banco/netguardian.db"
URL = "https://www.blocklist.de/en/export.html"

def dashboard():
    conexao = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT tipo_ameaca, fonte_dados FROM ameacas", conexao)
    conexao.close

    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(16,7), subplot_kw = dict(aspect = "equal"))

    contagem_ameacas = df['tipo_ameaca'].value_counts()

    if len(contagem_ameacas) > 5:
        top_5 = contagem_ameacas.head(5)
        outros = pd.Series({'Outros' : contagem_ameacas.iloc[5:].sum()})
        contagem_ameacas = pd.concat([top_5, outros])

    ax.pie(contagem_ameacas, labels = contagem_ameacas.index, autopct = '%1.1f%%',
            startangle = 140, colors = sns.color_palette("viridis"))
    ax.set_title("Proporção por Tipo de Ameaça", fontsize = 14, fontweight = 'bold')

    plt.tight_layout()

    print(f"Total de registros analisados: {len(df)}")

    plt.show()

if __name__ == "__main__":
    dashboard()
    