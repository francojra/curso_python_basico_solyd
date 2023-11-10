### Criando bibliotecas

import oauth2
import urllib.parse
import json

class Twitter:
  
  def __init__(self, consumer_key, cosumer_secret, token_key, token_secret):
      self.conexao(consumer_key, cosumer_secret, token_key, token_secret)
    
  def conexao(self, consumer_key, cosumer_secret, token_key, token_secret):
      self.consumer = oauth2.Consumer(consumer_key, cosumer_secret)
      self.token = oauth2.Token(token_key, token_secret)
      self.cliente = oauth2.Client(self.consumer, self.token)
    
  def tweet(self, novo_tweet):
      query_codificada = urllib.parse.quote(novo_tweet, safe = '')
      requisicao = self.cliente.request('https://......')
      decodificar = requisicao[1].decode()
      objeto = json.loads(decodificar)
      return objeto
    
  def search(self, query, lang):
      query_codificada = urllib.parse.quote(novo_tweet, safe = '')
      requisicao = self.cliente.request('https://......' + query_codificada
      + '&lang=' + lang)
      decodificar = requisicao[1].decode()
      objeto = json.loads(decodificar)
      twittes = objeto['statuses']
      return twittes # Retorna uma coleção de tweets
