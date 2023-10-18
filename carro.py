from veiculo import Veiculo

class Carro(Veiculo):
  
  def __init__(self, cor, rodas, marca):
    Veiculo.__init__(self, cor, rodas, marca)

