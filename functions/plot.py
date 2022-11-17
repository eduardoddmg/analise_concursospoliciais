import pandas
from functions.format import *
import matplotlib.pyplot as plt

def classificacao(df):
   result = []
   for row in df.index:
      if df['taf'][row] == 'SIM' and df['medico'][row] == 'SIM' and df['odonto'][row] == 'SIM' and df['psico'][row] == 'SIM' and df['is'][row] == 'SIM':
         result.append('SIM')
      else:
         result.append('NÃO')
   df["classificado"] = result
   return df

def addColumn(df, fase, name):
   result = []
   cod_fase = fase["cod"].values
   cod_df = df["cod"].values
   for i in cod_df:
      if i in cod_fase:
         result.append("SIM")
      else: 
         result.append("NÃO")
   df[name] = result
   df.to_csv('./csv/aprovados.csv')
   return df
   

def generate_csv(name, cols):
   path = './files/'+name+'.txt'
   final = './files_tratados/'+name+'.txt'
   csv = './csv/'+name+'.csv'
   prepare_file(path, final, cols)
   df = pandas.read_csv(final)
   df.to_csv(csv)
   return pandas.read_csv(final)

def sort(df):
   return df.sort_values(by=['classificado', 'nf','nf', 'notas p2', 'acertos p2', 'acertos p1'], ascending=False)

def plot_graphic(lista):
   result = []
   for i in lista:
      result.append(len(i))
   ts = pandas.Series(result, index=['prova obj', 'taf', 'invest_social'])
   print(ts.plot())
   plt.show()
def plot_table(lista, aprovados):
   names = ['prova objetiva', 'taf', 'medico', 'invest_social']
   df = pandas.DataFrame({'name': names, 'candidatos': lista })
   df["percent"] = 100*df["candidatos"]/aprovados
   print(df)