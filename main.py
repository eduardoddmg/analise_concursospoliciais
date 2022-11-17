from functions.plot import *

dictionary = {
	"aprovados": "cod,nome,notas p1,acertos p1,notas p2,acertos p2,nf\n",
	"rest": "cod, nome\n"
}

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
aprovados = sort(aprovados)
aprovados.to_csv('aprovados.csv')
plot_graphic([aprovados, taf, invest_social])
plot_table([len(aprovados), len(taf), len(medico), len(invest_social)], len(aprovados))