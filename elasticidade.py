# python version ??  tested with http://mathcs.holycross.edu/~kwalsh/python/
precoinicial = input("Digite o preco inicial: ")
precofinal = input("Gigite o preco final: ")
variavel1 = (precofinal-precoinicial)/(precoinicial)*100
demandainicial = input("Digite a quantidade inicial demandada: ")
demandafinal = input ("Digite a quantidade final demandada: ")
variavel2 = (demandafinal-demandainicial)/(demandainicial)*100
print variavel1
print variavel2
elas = (variavel2 / variavel1)
if elas == 1:
	print('A demanda do produto e unitaria e seu valor e: ', elas)
if elas > 1:
	print('A demanda e elestica e seu valor e: ', elas)
if elas <1:
	print('A demanda e inelestica e seu valor e: ', elas)
