#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#Faça um programa que receba um número inteiro e retorne se é primo ou não.

def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

numero = int(input("Digite um número inteiro: "))

if eh_primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")