import pandas

dictionary = {
	"aprovados": "cod,nome,notas p1,acertos p1,notas p2,acertos p2,nf\n",
	"rest": "cod, nome\n"
}

# formatar txt
def prepare_file(path, final, cols):
	f = open(path)
	text = f.read()
	f.close()

	text = text.replace('\n', ' ').replace(', ', ',').replace(' / ', '\n').replace('\n ', '\n')
	text = cols+text

	f = open(final, 'w')
	f.write(text)

def classificacao(aprovados):
	result = []
	for row in aprovados.index:
		if aprovados['taf'][row] == 'SIM' and aprovados['medico'][row] == 'SIM' and aprovados['odonto'][row] == 'SIM' and aprovados['psico'][row] == 'SIM' and aprovados['is'][row] == 'SIM':
			result.append('SIM')
		else:
			result.append('NÃO')
	aprovados["classificado"] = result
	return aprovados

def addColumn(aprovados, fase, name):
	result = []
	cod_fase = fase["cod"].values
	cod_aprovados = aprovados["cod"].values
	for i in cod_aprovados:
		if i in cod_fase:
			result.append("SIM")
		else: 
			result.append("NÃO")
	aprovados[name] = result
	aprovados.to_csv('./csv/aprovados.csv')
	return aprovados
	

def generate_csv(name, cols):
	path = './files/'+name+'.txt'
	final = './files_tratados/'+name+'.txt'
	csv = './csv/'+name+'.csv'
	prepare_file(path, final, cols)
	df = pandas.read_csv(final)
	df.to_csv(csv)
	return pandas.read_csv(final)

aprovados = generate_csv('aprovados', dictionary["aprovados"])
taf = generate_csv('taf', dictionary["rest"])
medico = generate_csv('medico', dictionary["rest"])
odonto = generate_csv('odonto', dictionary["rest"])
psico = generate_csv('psico', dictionary["rest"])
invest_social = generate_csv('is', dictionary["rest"])

aprovados = addColumn(aprovados, taf, 'taf')
aprovados = addColumn(aprovados, medico, 'medico')
aprovados = addColumn(aprovados, odonto, 'odonto')
aprovados = addColumn(aprovados, psico, 'psico')
aprovados = addColumn(aprovados, invest_social, 'is')

aprovados = classificacao(aprovados)
aprovados = aprovados.sort_values(by=['classificado', 'nf','nf', 'notas p2', 'acertos p2', 'acertos p1'], ascending=False)
print(aprovados)
aprovados.to_csv('aprovados.csv')