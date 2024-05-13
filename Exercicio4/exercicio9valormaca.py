#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#Sitema para ver o Valor maçã
print("Digite a quantidade de Maçãs")

quantidade_maca = int(input("Digite o número de maçãs compradas: "))

if quantidade_maca < 12:
    custo_total = quantidade_maca * 1.30
else:
    custo_total = quantidade_maca * 1.00

print("O custo total da compra é R$", round(custo_total, 2))