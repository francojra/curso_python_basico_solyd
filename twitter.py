### Criando bibliotecas

import oauth2

class Twitter:
  
  def __init__(self, consumer_key, cosumer_secret, token_key, token_secret):
      self.conexao(consumer_key, cosumer_secret, token_key, token_secret)
    
  def conexao(self, consumer_key, cosumer_secret, token_key, token_secret):
      self.consumer = oauth2.Consumer(consumer_key, cosumer_secret)
      self.token = oauth2.Token(token_key, token_secret)
      self.cliente = oauth2.Client(self.consumer, self.token)
      return self.cliente
 
