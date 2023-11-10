from twitter import Twitter

consumer_key = 
cosumer_secret = 

token_key = 
token_secret = 

twitter = Twitter(consumer_key, cosumer_secret, token_key, token_secret)

print(twitter) # Retorna a conexão

### Função para fazer postagens no Twitter

twitter.tweet('Vamos testar nossa lib') # Colocar entre aspas o que quer postar

### A farse 'Vamos postar nossa lib' aparecerá automaticamente no Twitter.

for i in range(1, 50): # Posta a frase abaixo de 1 até 50 vezes
    twitter.tweet('Nova postagem no Twitter' + str(i))
    time.sleep(1) # Novas postagem a cada 1 segundo

resp = twitter.tweet('Vamos testar nossa lib novamente')

print(resp) # Para ver detalhes da postagem e saber se deu certo

pesquisa = twitter.search('Solyd', 'pt') # Informa o que quer pesquisar e em qual língua

for resultado in pesquisa:
  print(resultado['text']) # Irá imprimir apenas o texto
  print(resultado['user']['screen_name']) # Imprime o nome do usuário
