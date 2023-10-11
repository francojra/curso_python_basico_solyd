
# Curso Python Básico ----------------------------------------------------------------------------------------------------------------------
# Autora do script: Jeanne Franco ----------------------------------------------------------------------------------------------------------
# Data: 09/10/23 ---------------------------------------------------------------------------------------------------------------------------
# Referência: Curso Solyd ------------------------------------------------------------------------------------------------------------------

# Introdução ao Python

### Linguagem surgiu em 1989, é de alto nível e orientada a objetos. É uma das principais
### linguagens do mundo, de script e interpretada. Apresenta elementos funcionais com
### tipagem (tipos de variáveis) dinâmica e forte (inferida). Apresenta uma comunidade 
### rica com muitas bibliotecas. O Python é usado para análise de dados, produção de sites,
### jogos, segurança da informação, matemática, etc. É possível produzir com poucas linhas
### de comando.

### O Python é usado por grandes empresas nacionais e internacionais como Google, YouTube,
### Nasa, Linux, IBM, Apple, Rede Globo, Microsoft, etc.

### Comandos básicos:

a = 2
b = 4
a + b
b - a
c = a * b
c
d = 1630
e = 145
print(d + 2)
d + e
print("Estou estudando Python.")
print("Estou estudando Python." + "Estou gostando muito do curso.")
50 / c
50 * a

### Entrada e saíde de dados: print()

print("Aqui está um texto.") # Imprime um texto ou string
g = 'g'
g
print('Helo World! \n Vamos aprender Python!') # Barra invertida + n pula uma linha
print('Helo World! \t Vamos aprender Python!') # Tab permite aidionar parágrafo

### Variáveis

nome = 'Jeanne' # Variável chamada 'nome' que contem o objeto 'Jeanne'
nome
idade = 33 # Não precisa de aspas para número
idade
type(nome) # Para saber o tipo de variável
type(idade)
estado_civil = 'solteira'
tipo_estado_civil = type(estado_civil)
tipo_estado_civil
peso = 70.2
peso
type(peso) # Número decimal em python é chamado de float
print(nome, 'tem', idade, 'anos,', 'é', estado_civil, 'e pesa', peso, 'quilos.')

### Fica mais fácil concatenar com vírgula, pois assim não precisa converter os
### números em strings. Quando tem apenas strings, podemos concatenar com o '+'.

str(idade) # Converte número inteiro em string
str(peso) # Converte float em string

### Criando formulários

name = input('Escreva seu nome aqui: ')
age = input('Escreva sua idade aqui: ')
print(name, 'tem', age, 'anos')
print(type(name), type(age)) # Imprime todos como string

### Operações matemáticas

num1 = 54
num2 = 65
num3 = 8
num4 = 0

resultado1 = num1 + num2 / num3 * 5
print(resultado1)
resultado2 = num1 * num2 / num3 * 5
print(resultado2)
resultado3 = num1 * num2 / num4 * 5 # Não existe divisão por número 0
print(resultado3)
resultado4 = num2 ^ num3 # Podemos usar também "**"
print(resultado4)

numero1 = input('Escreva o primeiro valor: ')
numero2 = input('Escreva o segundo valor: ')
resultado = int(numero1) - int(numero2)
print('O resultado é:', resultado)

'''
EXERCÍCIO: faça um fómulário que pergunte nome, idade, CPF,
endereço, altura e telefone. Depois imprima isso em um relatório
organizado.
'''

nome = input('Escreva seu nome: ')
idade = input('Escreva sua idade: ')
cpf = input('Escreva seu cpf: ')
endereco = input('Escreva seu endereço: ')
altura = input('Escreva sua altura: ')
telefone = input('Escreva seu telefone: ')

print('Seu nome é', nome, ', ela tem', idade, 'anos.', 'O CPF dela é',
cpf, ', ela mora na', endereco, '. Ela tem', altura, 'de altura', 
'e seu telefone é', telefone)
