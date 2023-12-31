
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

### Pode ser necessário converter as strings acima em int ou float,
### e abaixo não coloca os valores em formato de string (entre aspas).

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
  contador += 1

print(contador)
print(len(convidados))

for convidado in convidados:
  print(convidado)
  
### Outra forma de resolver:

num_convidados = input('Coloque o número de convidados: ')
lista_convidados = []

i = 1 # Começa com convidado nº 1
while i <= int(num_convidados):
  nome_convidado = input('Escreva o nome do convidado nº' + str(i) + ': ')
  lista_convidados.append(nome_convidado)
  i += 1

print(lista_convidados)

for convidado in lista_convidados:
  print(convidado)
  
print('Haverá ' + str(len(lista_convidados)) + ' convidados para a festa.')

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
type(retorno)

retorno1 = soma(34.7, 20.8)
print(retorno1)
type(retorno1)

def imprime_oi():
  print('Oi!')

imprime_oi()  

def tem_7_letras(palavra):
  if len(palavra) == 7:
    return True
  else:
    return False

tem_7_letras('panela')

def tem_5_letras(palavra):
  if len(palavra) == 5:
    return print('A palavra tem 5 letras')
  else:
    return print('A palavra não tem 5 letras')

tem_5_letras('livro')
tem_5_letras('ambiente')

def soma_10(num1, num2, num3):
  if num1 + num2 + num3 == 10:
    return print('Os três valores somam 10')
  else:
    return print('Os três valores não somam 10')
  
soma_10(5, 2, 3)
soma_10(4, 23, 8)

'''
EXERCÍCIO: escreva uma função que recebe um objeto de coleção (lista, tupla, conjunto) e 
retorna o valor do maior número dentro da coleção. E outra função que retorna o menor
valor da coleção.
'''

def maior_numero(num1, num2, num3, num4, num5, num6):
  resultado = max(num1, num2, num3, num4, num5, num6)
  return resultado

maior_numero(9, 4, 6, 3, 7, 5)

def menor_numero(num1, num2, num3, num4, num5, num6):
  resultado = min(num1, num2, num3, num4, num5, num6)
  return resultado

menor_numero(9, 4, 6, 3, 7, 5)

### Outras formas de resolver

def maior(colecao):
  maior_item = colecao[0]
  for item in colecao:
    if item > maior_item:
      maior_item = item
  return maior_item
    
maior([6, 3, 8, 2, 67, 34, 0, 23, 9])

col = list([])
type(col)

def maior_valor(col):
  resultado = max(col)
  return resultado

maior_valor(col=[3, 6, 2, 67, 8, 43])
maior_valor(col=[45, 2, 3, 1])

def menor_valor(col):
  resultado = min(col)
  return resultado

menor_valor(col=[3, 6, 2, 67, 8, 43])
menor_valor(col=[45, 2, 3, 1])

### Adicionar novos objetos a listas

def adicionar_item(nome_lista):
  res = nome_lista.append('Novo item')
  return res
  
convidados = ['Patrícia', 'Izabel', 'Kelly']
print(convidados)
adicionar_item(convidados)  
print(convidados)
  
def segunda_posicao(lista_de_nomes):
  res = lista_de_nomes[1]
  return res

lista_nomes = ['Gabriel', 'Kelita', 'Amélie', 'Pedro']
print(lista_nomes)

segunda_posicao(lista_nomes)

lista_nomes1 = ['Daniel', 'Fernanda', 'Sergio', 'Felipe']
print(lista_nomes1)

segunda_posicao(lista_nomes1)

# Argumentos de linha de comando ----------------------------------------------------------------------------------------------------------------

### Passagem de argumentos

### Bibliotecas: são códifos e funções já pre-escritas em python, ao importar a 
### biblioteca estará importante o conjunto de códigos e funções para expandir 
### a potencialidade da programação. Algumas funções já estão no Python como
### len(), print(), sum(), etc., e outras funções estão em bibliotecas.

### Importar bibliotecas

import sys

argumentos = sys.argv
print(argumentos) # Fornece o caminho onde está trabalhando o Python, ou seja,
# esse é o argumento 0.

### Usando o terminal, pedemos adicionar os argumentos na linha de comando
### Devemos escrever o nome do programa Python (no meu caso, python.exe + 
### o nome do arquivo que está na pasta)

def soma(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

if argumentos[1] == 'soma':
  resp = soma(float(argumentos[2]), float(argumentos[3]))

if argumentos[1] == 'sub':
  resp = sub(float(argumentos[2]), float(argumentos[3]))
  
### arg1 = método
### arg2 = n1
### arg3 = n2

### Na linha de comando nós passamos os 3 argumentos, o nome da função
### (soma ou sub mais espaço, mais o argumento 2, espaço e argumento 3)
### Exemplo: python.exe curso_python_basico_solyd.py soma 43 67
### Então o programa retorna o valor de 43 + 67.

soma(45, 87)
sub(786, 32)

# Entrada e saída de arquivos -------------------------------------------------------------------------------------------------------------------

open('arquivo.txt') # Função open() e nome do arquivo entre aspas

open('c:\\windows\\arquivo.txt')

### O arquivo citado deve estar no diretório de trabalho, caso não,
### pode escrever o código adicionando o argumento 'w'.

open('arquivo.txt', 'w') # Abrir um novo arquivo .txt no diretório de trabalho

### O 'w' significa modo 'write'

open('arquivo.txt', 'r +') # 'r + w' significa 'read + write', modo de leitura e escrita

open('arquivo.txt', 'a') # Método de escrita no modo apend

arquivo = open('arquivo.txt', 'w')
print(arquivo)
type(arquivo)

arquivo.write('Programação em Python') # Para escrever dentro do arquivo

arquivo1 = open('arquivo.txt', 'r')
print(arquivo1.read())

### Após escrever no bloco de notas:

for linha in arquivo1:
  print(linha)

### Para ler arquivos de imagens usase 'b' de bytes e 'r' de read

image = open('logo.png', 'rb')
print(image)
print(image.read())

# Tratamento de erros e exceções ----------------------------------------------------------------------------------------------------------------

### Veja alguns exemplos que podem dar erros no Python e que mensagens são enviadas
### indicando onde está o erro

escrever strings sem objeto e aspas # sintaxe inválida
a = 'qualquer string' + 2 # podemos apenas concatenar strings e nao strings + int
b = 1200 / 0 # erro de divisão por zero

### Erros podem travar todo o andamento do programa ou travar o computador

### Uso do try e except - Para tentar executar a função com um possível erro

try:
  b = 1200 / 0
except:
  print("Divisão por zero - Impossível executar, tente outro valor")

### O código acima explica que ao executar algo com erro, este erro apresentará
### uma exceção caso ele não funcione, assim o programa pode continuar. Ele
### não travará no erro e seguirá na execução dos próximos códigos normalmente.

### Ao tratar a exceção, ela deve estar sempre correta, para não travar em outro erro.

### No except também podemos dizer o nome do erro fornecido no Python

try:
  b = 1200 / 0
except ZeroDivisionError:
  print("Divisão por zero - Impossível executar, tente outro valor")
 
### Se no except não estiver tratado com o nome correto do erro, ele
### retornará um outro erro (NameError:), e o programa trava.

try:
  kdjbfhigns
except ZeroDivisionError:
  print("Divisão por zero - Impossível executar, tente outro valor")
  
try:
  kdjbfhigns
except ZeroDivisionError:
  print("Divisão por zero - Impossível executar, tente outro valor")
except NameError:
  print('Você digitou algo errado no Except.')

### Caso não saiba o tipo de erro

try:
  fiounbeaogK
except Exception as erro:
  print('Aconteceu algum erro:', erro) # Aqui ele irá mostrar na tela qual o
  # erro do código.
  
try:
  open('algum_arquivo_inexistente.txt')
except Exception as erro:
  print('Aconteceu algum erro:', erro)

### Sempre que for acessar algo externo como sites, músicas, arquivos, etc.,
### devemos usar o try e except.

import time # Biblioteca de tempo de espera para executar um código

def abre_arquivo():
  try:
    arquivo = open('arquivo_inexistente.txt')
    return True
  except Exception as erro:
    print('Aconteceu algum erro:', erro)
    return False
  
while not abre_arquivo():
  print('Tentando abrir o arquivo')
  time.sleep(5) # Tenta abrir novamente o arquivo a cada 5 segundos
  
arquivo = open('arquivo_correto.txt')
print('Arquivo aberto')
  
# Bibliotecas, PIP e requisições web ------------------------------------------------------------------------------------------------------------

### Instalações de bibliotecas internas do Python - Exemplos:

import sys
import time

### Bibliotecas externas

### Usa-se o gerenciador de pacotes PIP para instalar bibliotecas externas.
### Essas bibliotecas já vem com códigos prontos para facilitar a execução
### de projetos.

### Uso do requests: para fazer requisições web
### Para instalar o pacote requests, usamos o comando 'pip install requests'
### no terminal do IDE ou no Prompt de comando de administrador.

### Requisições web serve para acessar sites através do Python.

### Acessa um site > clica em 'Mais ferramentas' e 'Ferramentas do desenvolvedor'
### Depois clica em 'Network' e ver as solicitações, status, etc.

import requests

requisicao_get = requests.get('https://solyd.com.br') # Para fazer requisição ao site
requisicao_post = requests.post('https://solyd.com.br') # Para fazer um post
requisicao_del = requests.delete('https://solyd.com.br')

print(requisicao_get)
print(type(requisicao_get))
requisicao_get.status_code # Para páginas de sites inexistentes veríamos o código 404
requisicao_get.text # Ver o código fonte

### É interessante colocar as requisições no try para evitar erros em grandes projetos

try:
  requisicao_g1 = requests.get('https://g1.com.br') # Site da Globo
except Exception as erro:
  print('Ocorreu um erro: ', erro)

print(requisicao_g1)
requisicao_g1.text

### Podemos usar a biblioteca Beautiful soap 4 ou BS4 para extrair partes dos textos de sites
### pip install bs4
### Site: https://putsreq.com/

try:
  requis = requests.get('https://putsreq.com/7mXA7yTXP3O11K8Beauir') 
  texto = requis.text
except Exception as erro:
  print('Ocorreu um erro: ', erro)

print(texto) # Pode modificar o texto que tme no site para ver a mudança aqui

try:
  requisi = requests.post('https://putsreq.com/7CHLKIcvPTPHw1bR92Ip') 
  texto = requisi.text
except Exception as erro:
  print('Ocorreu um erro: ', erro)

print(texto)

cabecalho = {'user-agent' : 'Windows 12',
             'Referer' : 'https://google.com.br'} # Para informar que acessou o site através do Google

meus_cookies = {'Ultima-visita' : '10-10-2020'}

dados = {'user-name' : 'Jeanne',
         'password' : '25784895d$'}

try:
  requisi = requests.post('https://putsreq.com/k8NVSIb2awKJNGm46agZ', 
                           headers = cabecalho, 
                           cookies = meus_cookies,
                           data = dados) 
  texto = requisi.text
except Exception as erro:
  print('Ocorreu um erro: ', erro)

print(texto)

# API, JSON e consulta de listas de filmes ------------------------------------------------------------------------------------------------------

### APIs (Application Programming Interfaces) são interfaces em que você se comunica com 
### outros programas, você passa parâmetros e a API retorna com as informações desses parâmetros.
### As APIs são feitas com requisições web.

### API de filmes: podemos usar o OMDb API que é uma base de dados aberta sobre filmes.
### https://www.omdbapi.com/
### Em 'Exemplos' podemos buscar as informações de um determinado filme colocando o nome
### do filme no campo de 'Title'. As informações são dadas em formato JSON na aba 'Response'.

### O formato JSON de resposta é como um dicionário do python, onde cada parâmetro apresenta
### uma informação.

### A API permite automatizar a organização dos dados, sem ele teria que formar uma tabela
### com todas as informações por linhas e colunas.

### Não esquecer de requisitar a chave (key) para visualizar o JSON e sempre colocar
### o número da chaves após o nome do filme. Exemplo:
### https://www.omdbapi.com/?t=interstellar&apikey=n_da_chave

import requests

req = requests.get('https://www.omdbapi.com/?t=black+swan&apikey=aafd493d')

print(req.text)

req = None # Caso ocorra um erro, ele nao vai instanciar

try:
  req = requests.get('https://www.omdbapi.com/?t=black+swan&apikey=aafd493d') 
except Exception as erro:
  print('Ocorreu um erro na conexão: ', erro)
  exit()

print(req.text)

import json

dicionario = json.loads(req.text)
print(dicionario) # Retorna o json em formato de dicionário

dicionario['Title']
dicionario['Year']
dicionario['Actors']
dicionario['Director']
dicionario['imdbRating']

### Informar o filme

def requisicao(titulo): # Função para selecionar um filme e retornar as informações dele através de um dicionário
  try:
    req = requests.get('https://www.omdbapi.com/?t=' + titulo + '&apikey=aafd493d')
    dicionario = json.loads(req.text)
    return dicionario
  except Exception as erro:
    print('Ocorreu um erro na conexão: ', erro)
    return None
  
def detalhes_filme(filme):
  print('Título: ', filme['Title'])
  print('Ano: ', filme['Year'])
  print('Atores: ', filme['Actors'])
  print('Diretor: ', filme['Director'])
  print('Nota IMDB: ', filme['imdbRating'])
  print('Poster: ', filme['Poster'])
  print('Prêmios: ', filme['Awards'])
  
sair = False

while not sair:
  op = input('Escreva o nome de um filme ou SAIR para fechar: ')
  
  if op == 'SAIR':
    sair = True
    print('Saindo...')
  else:
    filme = requisicao(op)
    if filme['Response'] == 'False':
      print('Filme não encontrado')
    else:
      detalhes_filme(filme)

requisicao(titulo='matrix') # Para ver em formato JSON
requisicao(titulo='titanic')
requisicao(titulo='blade runner')

'''
Criar um programa que encontre todas as páginas JSON de um filme.
Use-se o parâmetro ?s (search), o type (tipo filme) e page.
'''

### Estrutura do JSON

estrutura = {[{}, {}, {}]}

### Teste

req = requests.get('https://www.omdbapi.com/?s=black+swan&type=movie&page=1&apikey=aafd493d')
dicionario = json.loads(req.text)
print(dicionario)
print(dicionario['Search'][0]['Title'])

### Resolução do exercício

import requests
import json

### Primeiro ver a quantidade de filmes

def existe_filmes(titulo): 
    quant = 0 # Quantidade de filmes
    try:
        req = requests.get('https://www.omdbapi.com/?s=' + titulo + '&type=movie' +  '&apikey=aafd493d')
        resposta = json.loads(req.text) 
    except:
        print('Conexão falhou')
        return quant # Nesse caso, seria quantidade zero
  
    if resposta['Response'] == 'True':
        quant = resposta['totalResults'] 
    return quant # Retorna quantidade de filmes

existe_filmes(titulo='matrix')
existe_filmes(titulo='titanic')

### Depois verifica a lista de filmes

def lista_filmes(titulo): 
    lista = [] # Lista de filmes
    i = 1
    for i in range(1, 101): # No geral vai da página 1 a 100
        try:
            print('Pesquinsando na página: ', i)
            req = requests.get('https://www.omdbapi.com/?s=' + titulo + '&type=movie&page=' + str(i) + '&apikey=aafd493d')
            resposta = json.loads(req.text) 
            if resposta['Response'] == 'True':
                 for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    frase = tit + ' (' + ano + ')'
                    lista.append(frase)
            else:
                print('Fim das páginas.')
                break
        except:
            print('Conexão falhou')
    return lista 

lista_filmes(titulo='matrix')        
lista_filmes(titulo='star wars')          
lista_filmes(titulo='black swan')        
        
sair = False
while not sair:
  op = input('Pesquise um filme ou digite SAIR: ')
  if op == 'SAIR':
      sair = True
  else:
      lista_de_filmes = lista_filmes(op)
      print('Filmes encontrados: ', len(lista_de_filmes))
  for filme in lista_de_filmes:
    print(filme)

# Expressões regulares - Procurando por e-mails -------------------------------------------------------------------------------------------------

### Todos os e-mails apresentam um padrão como o uso de '@' e '.com'.
### Da mesma forma, números de telefones também apresentam um padrão
### com um, dois ou três números iniciais.

### Biblioteca para procurar expressões regulares

import re

### Pesquisar em uma string por determinado padrão

string_teste = 'O gato é bonito.'

padrao = re.search('', string_teste) # É necessário informar dois parâmetros, o primeiro se refere ao
# padrão que quer procurar e o segunda a string onde está o padrão.

print(padrao)

padrao = re.search(r'b', string_teste) # O r transforma em RAW string ou string crua
# Na string crua tudo é imprimido, inclusindo espaços e caracteres especiais
print(padrao)
print(padrao.group())

padrao = re.search(r'g', string_teste)
print(padrao)
print(padrao.group())

padrao = re.search(r'ga', string_teste)
print(padrao)
print(padrao.group())

padrao = re.search(r'gata', string_teste)
print(padrao)
print(padrao.group())

if padrao:
  print(padrao.group())
else:
  print('Padrão não encontrado.')

padrao = re.search(r'bonito', string_teste)

if padrao:
  print(padrao.group())
else:
  print('Padrão não encontrado.')
  
padrao = re.search(r'bonit.', string_teste) # O '.' indica qualquer caracter

if padrao:
  print(padrao.group())
else:
  print('Padrão não encontrado.')
  
padrao = re.search(r'gat\w', string_teste) # O '\w' indica caracter do tipo palavra,
# ou seja, não considera espaço.

if padrao:
  print(padrao.group())
else:
  print('Padrão não encontrado.')  

padrao = re.search(r'\w\w\w\w', string_teste) # Primeiras 4 letras consecutivas de palavra

if padrao:
  print(padrao.group())
else:
  print('Padrão não encontrado.') 
  
padrao = re.search(r'\d', string_teste) # Procura qualquer caracter do tipo número

if padrao:
  print(padrao.group())
else:
  print('Padrão não encontrado.')   

padrao = re.search(r'\D', string_teste) # Procura qualquer caracter que não seja número

if padrao:
  print(padrao.group())
else:
  print('Padrão não encontrado.') 
  
string_teste_1 = 'O gato, a gata, os gatos, as gatas, os gatinhos, os gatões'

padrao = re.findall(r'gat\w', string_teste_1) # Findall = encontrar tudo

if padrao:
  print(padrao) # Não usa mais group
else:
  print('Padrão não encontrado.') 

padrao = re.findall(r'gat\w+', string_teste_1) # O + repete o resto da palavra,
# pode ter uma ou mais letra após o gat

if padrao:
  print(padrao)
else:
  print('Padrão não encontrado.') 
  
string_teste_1 = 'O gato, a gata, os gatos, as gatas, os gatinhos, os gatões, o gat'

padrao = re.findall(r'gat\w*', string_teste_1) # O * indica que pode ter 0 ou
# infinitas letras após o gat

if padrao:
  print(padrao)
else:
  print('Padrão não encontrado.') 
  
padrao = re.findall(r'[gat]', string_teste_1) # Pode ter qualquer uma das letras
# que está dentro do colchetes.

if padrao:
  print(padrao)
else:
  print('Padrão não encontrado.')

padrao = re.findall(r'[gat]+', string_teste_1) # Pode ter qualquer uma das letras
# que está dentro do colchetes.

if padrao:
  print(padrao)
else:
  print('Padrão não encontrado.')  

### Pesquisando e-mails

### O que tem em um e-mail?
### 1 - Alguma palavra: \w+
### 2 - Um @
### 3 - Mais uma palavra: \w+
### 4 - Um ponto \.
### 5 - Mais uma palavra: \w+

s1 = 'snsmroi@gmail.com'
s2 = '38945701297'
s3 = 'jneriu@hotmail.com'
s4 = 'O céu é azul.'

padrao1 = re.findall(r'\w+@\w+\.\w+', s1) # Pede para encontrar estrutura de e-mail

if padrao1:
  print(padrao1)
else:
  print('Padrão não encontrado.') 

padrao2 = re.findall(r'\w+@\w+\.\w+', s2) # Pede para encontrar estrutura de e-mail

if padrao2:
  print(padrao2)
else:
  print('Padrão não encontrado.') 
  
padrao3 = re.findall(r'\w+@\w+\.\w+', s3) # Pede para encontrar estrutura de e-mail

if padrao3:
  print(padrao3)
else:
  print('Padrão não encontrado.') 

padrao4 = re.findall(r'\w+@\w+\.\w+', s4) # Pede para encontrar estrutura de e-mail

if padrao4:
  print(padrao4)
else:
  print('Padrão não encontrado.') 

### Importante: se não colocar o '\.' ele não encontra as palavras após o '.'
### Muitos e-mail também apresentam traços, pontos, underlines e outros caracteres
### que precisam ser adicionados nas expressões regulares para não passarem batido.

import requests

requisicao = requests.get('https://www.bbc.com/news')

padrao = re.findall(r'Putin', requisicao.text)

if padrao:
  print(padrao)
else:
  print('Padrão não encontrado.') 

padrao = re.findall(r'Copyright', requisicao.text) # Sempre diferencia maiúsculo de minúsculo

if padrao:
  print(padrao)
else:
  print('Padrão não encontrado.') 
  
# Consultando o clima e a cotação do dólar ------------------------------------------------------------------------------------------------------

### Site: https://docs.awesomeapi.com.br/api-de-moedas

import requests
import json

requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
print(requisicao.text)

cotacao = json.loads(requisicao.text)

print(cotacao)
print(cotacao['USDBRL']['code']) # Necessário especificar a chave USDBRL
print(cotacao['USDBRL']['codein'])
print(cotacao['USDBRL']['high'])


requisicao1 = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao1.text)

cotacao1 = json.loads(requisicao1.text)
print(cotacao1)

import time
import datetime

while True:
  requisicao1 = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
  cotacao1 = json.loads(requisicao1.text)
  
print('Cotação', ' - ', 'Dia: ', datetime.datetime.now())
print('Dólar: ',cotacao1['USDBRL']['name']) 
print('Valor Dólar: ',cotacao1['USDBRL']['high']) 
print('Euro: ',cotacao1['EURBRL']['name'])
print('Valor Euro: ',cotacao1['EURBRL']['high']) 
print('Bitcoin: ',cotacao1['BTCBRL']['name'])
print('Valor Bitcoin: ',cotacao1['BTCBRL']['high']) 
time.sleep(2) # Após 2 segundos faz a nova cotação do dia e horário

# Publicando e pesquisando no Twitter -----------------------------------------------------------------------------------------------------------

### Acessa o portal developer do Twitter, cria um novo app e copia as chaves

API_Key = 
API_Key_Secret = 

Bearer_Token = 

Access_Token = 
Access_Token_Secret = 

import oauth2
import requests
import json

consumer = oauth2.Consumer(API_Key, API_Key_Secret)
token = oauth2.Token(Access_Token, Access_Token_Secret)
cliente = oauth2.Client(consumer, token)

requisicao = cliente.request('https://api.twitter.com/2/tweets/search/recent?query=from:twitterdev')

decodificar = requisicao[1].decode()

print(type(requisicao))

objeto = json.loads(decodificar)

print(type(objeto))
print(objeto)

pprint.pprint(objeto)
