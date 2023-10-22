class Conta:
  def __init__(self, cliente, saldo, limite, sacar): # Método construtor, constroi o objeto
      self.cliente = cliente
      self.saldo = saldo
      self.limite = limite
      self.sacar = sacar
      
  def depositar(self, quantidade):
    if quantidade > 0:
      self.saldo += quantidade # Vai pegar a quantidade depositada e somar ao saldo
    else:
      print('Erro no depósito')

  def consulta_saldo(self):
    return sefl.saldo

