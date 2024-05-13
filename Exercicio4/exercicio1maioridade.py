#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#sistema para ver se é maior de idade

print("Olá bem vindo ao sistema")

nome = input("Por favor digite seu nome:\n ")
idade = int(input("Por favor digite a sua idade:\n "))

if idade < 18:
    print("Desculpe",nome, "você não pode acessar o site, Você é menor de idade")
else:
    print(nome, "Bem vindo ao site você é maior de idade ")    