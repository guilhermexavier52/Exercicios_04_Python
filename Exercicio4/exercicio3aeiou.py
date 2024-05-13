#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#sistema para ver a quntidade de vogais


def contar_vogais(frase):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

print("Digite uma frase para fazer a contagem de vogais\n")

frase = input("Digite uma frase: ")
total_vogais = contar_vogais(frase)
print("Total de vogais na frase:", total_vogais)