precoinicial = input("Digite o preco inicial: ")
precofinal = input("Gigite o preco final: ")
variavel1 = (precofinal-precoinicial)/(precoinicial)*100
demandainicial = input("Digite a quantidade inicial demandada: ")
demandafinal = input ("Digite a quantidade final demandada: ")
variavel2 = (demandafinal-demandainicial)/(demandainicial)*100
print variavel1
print variavel2
resultado = abs(variavel2 / variavel1)



print('A eslasticidade final e de: ', resultado)
