import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(data=df, x='dia', y='venda', color='red')
  grafico.set(title='Preço da Gasolina', xlabel='Dias', ylabel='Vendas')
  plt.tight_layout()
  plt.show()
  plt.savefig('gasolina.png')