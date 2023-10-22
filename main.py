from veiculo import Veiculo

caminhao_rosa = Veiculo('rosa', 6, 'Ford') # Cor, nome da marca e número de rodas
print(caminhao_rosa)
print(type(caminhao_rosa)) # Criou um novo tipo de classe

### Agora podemos criar objetos do tipo 'veículo'

### Veja as opções que aparecem ao digitar 'caminhao_rosa.'

caminhao_rosa.

print(caminhao_rosa.cor)
print(caminhao_rosa.rodas)
print(caminhao_rosa.marca)

print('Cor:', caminhao_rosa.cor, 
'Número de rodas:', caminhao_rosa.rodas,
'Marca:', caminhao_rosa.marca)

carro_azul = Veiculo('azul', 4, 'bmw')

carro_azul.marca

print('Cor:\n', carro_azul.cor, 
'\nNúmero de rodas:\n', carro_azul.rodas,
'\nMarca:\n', carro_azul.marca)

### Organizando

print('Caminhão Rosa:')

print('Cor:\n', caminhao_rosa.cor, 
'\nNúmero de rodas:\n', caminhao_rosa.rodas,
'\nMarca:\n', caminhao_rosa.marca)

print(' ')

print('Carro Azul:')

print('Cor:\n', carro_azul.cor, 
'\nNúmero de rodas:\n', carro_azul.rodas,
'\nMarca:\n', carro_azul.marca)

from cliente import Cliente

maria = Cliente('Maria', 30, 'Google', 14000) 
print(maria)
print(type(maria)) 

maria.

print(maria.nome)
print(maria.idade)
print(maria.empresa)
print(maria.salario)

print('Cliente Maria:')

print('Nome:\n', maria.nome, 
'\nIdade:\n', maria.idade,
'\nEmpresa:\n', maria.empresa,
'\nSalário:\n', maria.salario)

maria.ganho(3000)
print('Salário:\n', maria.salario)

from carro import Carro

carro_lilas = Carro('lilás', 7, 'Ferrari')

print(carro_lilas)
print(type(carro_lilas))

print('Carro Lilás:')

print('Cor:\n', carro_lilas.cor, 
'\nNúmero de rodas:\n', carro_lilas.rodas,
'\nMarca:\n', carro_lilas.marca)

from cliente import Cliente
from conta import Conta

cliente1 = cliente()
