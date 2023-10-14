
# Curso Python Básico ----------------------------------------------------------------------------------------------------------------------
# Autora do script: Jeanne Franco ----------------------------------------------------------------------------------------------------------
# Data: 09/10/23 ---------------------------------------------------------------------------------------------------------------------------
# Referência: Curso Solyd ------------------------------------------------------------------------------------------------------------------

# Introdução ao Python -------------------------------------------------------------------------------

### Linguagem surgiu em 1989, é de alto nível e orientada a objetos. É uma das principais
### linguagens do mundo, de script e interpretada. Apresenta elementos funcionais com
### tipagem (tipos de variáveis) dinâmica e forte (inferida). Apresenta uma comunidade 
### rica com muitas bibliotecas. O Python é usado para análise de dados, produção de sites,
### jogos, segurança da informação, matemática, etc. É possível produzir com poucas linhas
### de comando.

### O Python é usado por grandes empresas nacionais e internacionais como Google, YouTube,
### Nasa, Linux, IBM, Apple, Rede Globo, Microsoft, etc.

# Comandos básicos ---------------------------------------------------------------------------------------------

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

# Entrada e saíde de dados: print() -----------------------------------------------------------------------------------------------

print("Aqui está um texto.") # Imprime um texto ou string
g = 'g'
g
print('Helo World! \n Vamos aprender Python!') # Barra invertida + n pula uma linha
print('Helo World! \t Vamos aprender Python!') # Tab permite aidionar parágrafo

# Variáveis -----------------------------------------------------------------------------------------------------

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

# Criando formulários -----------------------------------------------------------------------------------------------------

name = input('Escreva seu nome aqui: ')
age = input('Escreva sua idade aqui: ')
print(name, 'tem', age, 'anos')
print(type(name), type(age)) # Imprime todos como string

# Operações matemáticas ------------------------------------------------------------------------------------------------------------

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

# Operadores lógicos e estruturas de decisões - IF/ELSE -----------------------------------------------------------------------------------------

# Dados booleanos: true ou false

var_verdade = True
var_falso = False

print(type(var_verdade), type(var_falso)) # Verificar o tipo de variável

if var_verdade == True: # Um '=' é para atribuição de variáveis, dois '=' é para comparação
  print('var_verdade é verdadeiro.') # Código com identação

1 == 1 # Resposta é True
1 == 2 # Resposta é False
'abacaxi' == 'uva' # Resposta é False
5 > 9 # Resposta é False
2 < 7 # Resposta é True
2 <= 5 # Resposta é True
2 >= 5 # Resposta é False

# Símbolos usados na comparação: ==, !=, <, >, <=, >= 

2 == 2 and 3 == 3 # Resposta é True
2 == 2 and 5 == 3 # Resposta é False
2 == 2 or 5 == 3 # Resposta é True

num = 5
if num == 5: 
    print('O valor é igual a 5.')

if 3 > 2:
  print('Três é maior do que dois.')

if 3 > 7:
  print('Três é maior do que dois.') # Nenhuma informação é gerada

a = 2
b = 20

if a > b:
    print('O a é maior do que b.')
else:
    print('O a não é maior do que b.')
    
a = 50
b = 20
c = 'abacaxi'
d = 'abacate'

if a > b and c == d: # No and as duas comparações devem estar corretas
    print('Ambos requisitos estão corretos.')
else:
    print('Apenas um (ou nenhum) dos requisitos está correto.')

print('Combos promocionais: \n 1 = Big cheddar\n 2 = Big Tasty\n 3 = Big bacon')

opcao = input('Escreva o número do combo promocional:')

if opcao == '1':
    print('Big cheddar')
elif opcao == '2':
  print('Big Tasty')
elif opcao == '3':
  print('Big bacon')
else:
  print('Nenhuma opção selecionada')

# Uso do not no if e else

if not True: # Nega a afirmação True
  print('Aceita o if')
else:
  print('Aceita o else')
  
if True: 
  print('Aceita o if')
else:
  print('Aceita o else')
  
'''
EXERCÍCIO: faça um programa que pergunte a idade, peso e altura de uma pessoa.
Depois decida se ela está apta ou não para participar do exército. Para entrar
no exército, a pessoa precisa ter 18 anos ou mais, pesar mais ou igual a 60 kilos 
e ter mais ou igual a 1.70 de altura.
'''

idade = input('Qual a sua idade?')
peso = input('Qual o seu peso?')
altura = input('Qual a sua altura?')

if idade >= '18'and peso >= '60' and altura >= '1.70':
  print('Esta pessoa é apta para participar do exército.')
else:
  print('Esta pessoa não está apta para participar do exército.')
  
# Strings e listas ------------------------------------------------------------------------------------------------------------------------------

frase = 'Oi, tudo bem?'
print(frase)
print(type(frase)) # Frase é uma string
print(frase[0]) # Estrai a primeira letra (atributo) da frase
print(frase[4]) # Estrai a quinta letra (atributo) da frase
print(frase[3]) # Estrai a quarta letra (atributo) da frase, no caso é um espaço vazio
print(frase[2])
print(frase[12])

### As listas podem ser coleções de vários tipo de variáveis (inteiros, floats, strings...)
### Para criar listas, usa-se colchetes.

lista_nomes = ['Joao', 'Maria', 'Guilherme', 'Diego']
print(lista_nomes)
print(type(lista_nomes)) # Retorna 'list'
print(lista_nomes[0]) # Retorna o primeiro atributo da lista, no caso, Joao
print(lista_nomes[3])
print(lista_nomes[0:2]) # Imprime os itens 0 e 1 (até dois elementos)
print(lista_nomes[0:3:1]) # Do zero ao terceiro elemento, passando por cada 1

lista = ['Joao', 'Maria', 'Guilherme', 'Diego', 10, 7.6]
print(lista[5])
print(type(lista))
print(lista[1:6]) # Imprime o elemento 1 (Maria) até o sexto elemento da lista
print(lista[0:6:2])
print(lista[0:6:3])
print(lista[0:6:5])
print(lista[-1]) # Extrai o último elemento da lista (a lógica é de traz para frente)
print(lista[-6]) # Extrai o primeiro elemento da lista
print(lista[-5]) # Extrai o segundo elemento da lista
print(lista[::-1]) # Inclui todos os elementos de traz para frente

### Adicionar nomes na lista

lista.append('Karolina')
print(lista)
lista.append('Karen')
print(lista)
lista.remove(10)
print(lista)
lista.remove(7.6)
print(lista)
lista.clear() # Limpa toda a lista
print(lista)
lista = ['Joao', 'Maria', 'Guilherme', 'Diego', 'Karolina', 'Karen']
lista.reverse()
print(lista)
lista.insert(3, 'Gabrielle') # Insere o novo nome na terceira posição
print(lista)
lista[6] = 'Roberta' # Troca o nome da sexta posição por Roberta
print(lista)
lista.count('Diego') # Conta os nomes 'Diego'
lista.pop() # Retira o último elemento e diz qual o elemento
print(lista)
lista.pop() 
print(lista)

### Verificar quantidade de caracteres das strings e listas

print(len(frase))
print(len(lista_nomes))
print(len(lista))

### Passar tudo para minúscula ou maíscula

frase.lower()
frase.upper()

### Transformar strings em listas

frase_separada = frase.split(',') # Retorna os elementos separados por vírgula
print(frase_separada)
print(type(frase_separada)) # Passa a ser uma lista
print(frase_separada[1])

frase_separada1 = frase.split(' ') 
print(frase_separada1)
print(frase_separada1[2])

frase_nova = frase + ' ' + 'Como vai você?'
print(frase_nova)

# Estruturas de laço (WHILE e FOR) --------------------------------------------------------------------------------------------------------------

### Usando o for

frutas = ['abacaxi', 'laranja', 'melão', 'abacate', 'melancia']

for fruta in frutas:
  print(fruta)

numeros = range(6)
numeros

for numero in numeros:
  print(numero) # Irá imprimir 6 números
  
numeros1 = range(1, 30, 2)
numeros1

for numero in numeros1:
  print(numero) 

for item in range(0, 100, 1):
  print(item)

### O último vamor estipulado nunca aparecerá no print.

for i in range(3):
  print(frutas[i]) # Extrai os 3 primeiros itens da lista

for i in range(5):
  print(frutas[i]) # Extrai todos os itens da lista
  
for i in range(len(frutas)): # Caso não saiba o número total de itens da lista
  print(frutas[i])  

for i in range(len(frutas)):
  print(frutas[i])  
  frutas.append('Ok')

print(frutas) 

frutas = ['abacaxi', 'laranja', 'melão', 'abacate', 'melancia']

for i in range(len(frutas)):
  print(frutas[i])  
  frutas.insert(3, 'acerola') # Adiciona o nome na terceira posição e para cada item da lista

print(frutas)

### O for para strings

palavras = 'Meu nome é Jeanne'
palavras

for i in palavras:
  print(i)
  
### Usando o while

i = 2 # Número inicial é 2

while i < 10:
  print('i ainda é menor do que 10:', i)
  i = i + 1 # Isso impede o loop infinito, chega até o 10

print('Acabou o while', i)

while 2 < 10:
  print('Loop infinito:', i) # Loop infinito, 5 sempre será menor que 10
  
while i < 7 or i == 7:
  print('Eu paro quando i for igual a 7:', i)
  i = i + 1

