#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#sistema para ver se é par ou impar


print("Ola vamos ver se o numero e par ou impar \n")

numero = int(input("Digite um número: "))


if numero % 2 == 0:
    print(f"O número digitado que é {numero} é par.")
else:
    print(f"O número digitado que é {numero} é ímpar.")