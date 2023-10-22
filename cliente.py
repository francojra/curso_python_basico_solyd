class Cliente:
  def __init__(self, nome, idade, empresa, salario): # Método construtor, constroi o objeto
      self.nome = nome
      self.idade = idade
      self.empresa = empresa
      self.salario = salario

  def __str__(self):
     return "Nome: " + self.nome + "\nIdade: " + str(self.idade) + "\nEmpresa: " + self.empresa + "\nSalário: " + str(self.salario)

