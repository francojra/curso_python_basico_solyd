
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

while i < 7 and i == 7: # Não ocorrerá nada porque o i não começa igual a 7
  print('Eu paro quando i for igual a 7:', i)
  i = i + 1
  
### Iteração de números

i = 0

i = i + 10 # O valor será 10
print(i)
i = i + 10 # O valor será 20
print(i)
i = i + 20 # O valor será 40
print(i)

### Contador para a lista de frutas

frutas = ['abacaxi', 'laranja', 'melão', 'abacate', 'melancia']

contador = 0 

for fruta in frutas:
  contador += 1 # O mesmo que contador = contador + 1
  
print(contador)

print(len(frutas))  

### Break: usado para sair da estrutura de repetição

numero = 0

while True:
  print(numero)
  if numero == 25:
    break # Começa do zero somando de um em um e para no valor 25
  numero += 1
print('Saiu do While')

'''
EXERCÍCIO: faça um programa que leia a quantidade de pessoas que serão convidadas 
para uma festa. Após isso, o programa irá perguntar o nome de todas essas pessoas
e colocar numa lista de convidados, imprimindo todos os nomes da lista.
'''

convidados = ['Letícia', 'Rafaela', 'Pedro', 'Daniel', 'Melissa', 'Cassy']

contador = 0

for convidado in convidados:
  contador +=1

print(contador)
print(len(convidados))

for convidado in convidados:
  print(convidado)

# Tuplas, dicionários e conjuntos ---------------------------------------------------------------------------------------------------------------

### Listas (list)

### As listas são mutáveis, elas podem ter itens removidos, substituídos ou adicionados.
### As listas são ordenadas (cada item tem uma posição) e podem aparesentar diferentes 
### tipos de elementos. Usa-se colchetes.

minha_lista = ['Guilherme', 'Maria']

### Tuplas (tuple)

### As tuplas não são mutáveis, não pode ter seus elementos modificados. Não existe
### os métodos append, remove, etc. Sempre a mesma quantidade de itens. Usa-se parêteses.

minha_tupla = ('Guilherme', 'Maria')

### Dicionários (dict)

### Os dicionários apresentam chaves e valores, assim como um dicionário que apresenta
### cada uma de suas palavras com seus respectivos significados. Usa-se as chaves
### para criar os dicionários.

### Os itens dos dicionários não são ordenados.

### Nesse caso abaixo a chave é o 'nome' e o valor 'Guilherme'.

meu_dicionario = {'nome': 'Guilherme', 'idade': 27}

### Conjuntos (set)

### Os conjuntos funcionam como listas, entretanto, são formados com o uso de chaves.
### Diferente da lista, no conjunto não pode haver itens repetidos. E também, os itens
### não são ordenados como ocorre nas listas.
### Os conjuntos podem ser dinâmicas, podem ser adicionados mais itens, podem
### haver itens removidos, etc. Apenas as tuplas não são mutáveis.

meu_conjunto = {'Maria', 'Barbara', 'Samanta'}

### Verificando as estruturas de dados

type(minha_lista)
type(minha_tupla)
type(meu_dicionario)
type(meu_conjunto)

minha_tupla[0]
minha_lista[1]
meu_conjunto[2] # Como os itens não são ordenados, não é possível dizer a posição do elemento
meu_dicionario[1]
meu_dicionario['nome'] # Forma correta de verificar os itens de um dicionário

for i in minha_lista:
  print(i)

for i in minha_tupla:
  print(i)

for i in meu_conjunto:
  print(i)

for i in meu_dicionario:
  print(i)

minha_tupla[2] = 'Talia'
minha_tupla[0] = 'Valeria'

meu_dicionario['altura'] = 1.80 # Em dicionário não usa a posição dos itens
print(meu_dicionario)
meu_dicionario['nome'] = 'Alessandra'
print(meu_dicionario)
meu_dicionario['endereco'] = 'Av João das Neves'
print(meu_dicionario)

meu_conjunto.add('Leia')
print(meu_conjunto)

if 'Gui' in minha_tupla:
  print('Gui está na minha tupla.')
  
if 'Maria' in minha_tupla:
  print('Maria está na minha tupla.')  
  
if 'Guilherme' in meu_dicionario:
  print('Guilherme está no meu dicionário')

if 'Alessandra' in meu_dicionario: # É necessário informar se é chave ou valor
  print('Alessandra está no meu dicionário')
  
if 'Alessandra' in meu_dicionario.values(): 
  print('Alessandra está no meu dicionário')  
  
if 'idade' in meu_dicionario.keys(): 
  print('idade está no meu dicionário')  

if 'Samanta' in meu_conjunto:
  print('Samanta está no meu conjunto')
  
print(len(meu_dicionario))  
print(len(meu_conjunto))
print(len(minha_tupla))

for valores in meu_dicionario.values():
  print(valores)
  
for chaves in meu_dicionario.keys():
  print(chaves)  
  
meu_dicionario1 = meu_dicionario.copy()  
print(meu_dicionario1)

### Um diferença importante entre o conjunto e a lista é que para procurar um determinado
### item dentro de uma lista, por ela ser ordenada, o processo será mais demorado, pois
### teria que passar posição por posição para procurar o item. Já em um conjunto, por não
### ser ordenado, ele procurará diretamente pelo nome do item.

### Tanto os conjuntos como os dicionários permitem uma busca instantênea dos itens.

meu_conjunto.remove('Leia')
print(meu_conjunto)

### Formas de começar com listas vazias

lista = list([])
print(lista)
tupla = tuple(())
print(tupla)
dicionario = dict({})
print(dicionario)
conjunto = set({})
print(conjunto)

con = set({'svn', 'fn', 'fokev'})
print(con)
print(type(con))

for i in con:
  print(i)
  
### Múltiplos valores: listas, tuplas e conjuntos na mesma estrutura de dados

tuplas = ((5, 6), (6, 4, 9), (4, 9), 23, (3,8), ({'Vanessa', 'Higor'}))
print(tuplas)
type(tuplas) # O símbolo mais externo representa uma tupla

for i in tuplas:
  print(i)
  
exemplo = [(5, 6), (6, 4, 9), (4, 9), 23, (3,8), ({'Vanessa', 'Higor'})]
print(exemplo)
type(exemplo) # O símbolo mais externo representa uma lista

# Métodos e funções -----------------------------------------------------------------------------------------------------------------------------

### As funções costumam ser seguidas de parênteses, elas apresentam diversos argumentos
### que são utilizados para dar mais informações sobre a execução da função e os parâmetros
### dentro das funções são preenchidos pelo programador, de acordo com o que ele quer verificar
### da função.

### Podemos usar uma função dentro de outra:

print('Olá Mundo!')
print(len('Olá Mundo!'))

### Criando nossas funções com def

def soma(numero1, numero2):
  resposta = numero1 + numero2
  return resposta

retorno = soma(78, 45)
print(retorno)
