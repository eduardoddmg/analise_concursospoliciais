import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

plt.close("all")

def codUnion(cod1, cod2):
   fase = [False]*len(cod1)
   for i in cod2:
         if i in cod1:
            fase[cod1.index(i)] = True
   return fase

def classificadosId(lista_aprovados, fases):
   classificados = ["SIM"]*len(lista_aprovados)
   for i in range(0, len(fases[0])):
      for j in range(0,len(fases)):
         if fases[j][i] == False:
            classificados[i] = "NÃO"
   return classificados

def plot(lista_aprovados, fases, classificado):
   [cod, nome, nota_p1, acertos_p1, nota_p2, acertos_p2, nota_final] = [lista_aprovados[0], lista_aprovados[1], lista_aprovados[2], lista_aprovados[3], lista_aprovados[4], lista_aprovados[5], lista_aprovados[6]]
   df = pd.DataFrame({'Código': cod, 'Nome': nome, 'nota final': nota_final, 'notas p1': nota_p1, 'acertos p1': acertos_p1, 'notas p2': nota_p2, 'acertos p2': acertos_p2, 'taf': fases[0], 'medico': fases[1], 'odonto': fases[2], 'psico': fases[3], 'invest_social': fases[4], 'toxico': fases[5], 'classificado': classificado })
   df.index = np.arange(1, len(df) + 1)   
   df = df.sort_values(by=['classificado', 'nota final', 'notas p2', 'acertos p2', 'acertos p1'], ascending=False, ignore_index=True)
   print(df)
   df.to_csv("aprovados.csv")
   print('Finalizou a exportação')

def plot_graphic(lista):
   ts = pd.Series(lista, index=["prova objetiva", "taf", "medico", "odonto", "psico", "is"])
   ts = ts.plot(xlabel="etapas do concurso", ylabel="quantidade de candidato")
   plt.show()

def plot_bar(lista):
   series = pd.DataFrame({'situação': ["apto", "inapto"], 'values':lista })
   series.plot.bar(x='situação', y='values', rot=0)
   plt.show()