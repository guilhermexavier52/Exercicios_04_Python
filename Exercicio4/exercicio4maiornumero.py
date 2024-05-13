#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#sistema para ver entre tres valores qual e o maior

print("Digite  3 valores para ver qual é o maior \n")

numero01 = float(input("Digite o primeiro valor\n"))

numero02 = float(input("Digite o segundo valor\n"))

numero03 = float(input("Digite o terceiro valor\n"))

if numero01 >= numero02 and numero01 >= numero03:
         numeromaior = numero01
elif numero02 >= numero01 and numero02 >= numero03:
    numeromaior = numero02  
else:
    numeromaior = numero03
    
print("O maior valor entre todos é: ", numeromaior)                 