import pandas as pd
from func import *
import numpy as np

def printar(lista):
	for i in lista:
		print(i)

def read(file):
	f = open(file, 'r')
	return format(f.read())

def format(array):
	array = array.replace('\n', ' ')
	array = array.split(' /')
	for i in range(0, len(array)):
		array[i] = array[i].split(', ')
		array[i][0] = array[i][0].replace(' ', '')
	return array

def reFormart(aprovados):
	cod = parseSeparate(aprovados, 0, False)
	nome = parseSeparate(aprovados, 1, False)
	nota_p1 = parseSeparate(aprovados, 2, True)
	acertos_p1 = parseSeparate(aprovados, 3, True)
	nota_p2 = parseSeparate(aprovados, 4, True)
	acertos_p2 = parseSeparate(aprovados, 5, True)
	nota_final = parseSeparate(aprovados, 6, True)
	return [cod, nome, nota_p1, acertos_p1, nota_p2, acertos_p2, nota_final]

def parseSeparate(array, index, number):
	new_arr = []
	for i in array:
		if (i[index].find(' ') == 0):
			i[index] = i[index].replace(' ', '', 1)
		if (i[index].find(' ') == len(i[index])-1):
			i[index] = i[index][:-1]
		if (not number):
			new_arr.append(i[index])
		else:
			new_arr.append(float(i[index]))
	return new_arr

def filter(arr, string):
	arr = np.array(arr)
	filter_arr = arr == string
	return arr[filter_arr]

def changeBool(arr):
	for i in range(0, len(arr)):
		if arr[i] == True:
			arr[i] = "APTO"
		else:
			arr[i] = "INAPTO"
	return arr

def init():
	print("hello world")

	aprovados = read('aprovados.txt')
	taf_aprovados = read('./files/taf.txt')
	medico_aprovados = read('./files/medico.txt')
	odonto_aprovados = read('./files/odonto.txt')
	psico_aprovados = read('./files/psico.txt')
	invest_social_aprovados = read('./files/is.txt')

	cod_aprovados = parseSeparate(aprovados, 0, False)
	cod_taf = parseSeparate(taf_aprovados, 0, False)
	cod_medico = parseSeparate(medico_aprovados, 0, False)
	cod_odonto = parseSeparate(odonto_aprovados, 0, False)
	cod_psico = parseSeparate(psico_aprovados, 0, False)
	cod_invest_social = parseSeparate(invest_social_aprovados, 0, False)

	aprovadosToPlot = reFormart(aprovados)

	taf = codUnion(cod_aprovados, cod_taf)
	medico = codUnion(cod_aprovados, cod_medico)
	odonto = codUnion(cod_aprovados, cod_odonto)
	psico = codUnion(cod_aprovados, cod_psico)
	invest_social = codUnion(cod_aprovados, cod_invest_social)
	tox = [False]*len(aprovados)

	classificados = classificadosId(aprovados, [taf, medico, odonto, invest_social, psico])

	taf = changeBool(taf)
	medico = changeBool(medico)
	odonto = changeBool(odonto)
	psico = changeBool(psico)
	invest_social = changeBool(invest_social)
	tox = changeBool(tox)

	classificados_aptos = filter(classificados, "YES")
	classificados_inaptos = filter(classificados, "NO")

	qtd_aprovados = [len(cod_aprovados), len(cod_taf), len(cod_medico), len(cod_odonto), len(cod_psico), len(cod_invest_social)]

	# ## setup pandas
	plot(aprovadosToPlot, [taf, medico, odonto, invest_social, psico, tox], classificados)
	plot_graphic(qtd_aprovados)
	plot_bar([len(classificados_aptos), len(classificados_inaptos)])
init()