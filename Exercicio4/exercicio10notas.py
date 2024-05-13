#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#Sistema para ver a media entre duas notas

print("Digite duas notas para calcular a media aritimética: ")

nota1 = float(input("Digite a nota da 1ª avaliação: "))
nota2 = float(input("Digite a nota da 2ª avaliação: "))

media = (nota1 + nota2) / 2

if media >= 6:
    situacao = "aprovado"
else:
    situacao = "reprovado"

print("A média do aluno é:", media)
print("O aluno está", situacao + ".")