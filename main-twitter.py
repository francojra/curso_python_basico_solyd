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
