#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#Escreva um programa que peça ao usuário para digitar um número e verifique se é positivo, negativo ou zero.

print("Digite um numero para ver se ele é maior, meor ou igual a zero\n")

numero = float(input("Digite um numero: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")