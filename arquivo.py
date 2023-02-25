class Arquivo():
  def __init__(self, nome, tipo, tamanho, posicao):
    self.nome =  nome
    self.tipo = tipo
    self.tamanho = tamanho
    self.posicao = posicao
  def cria_arquivo(self):
    self.nome = self.nome + 1 #adiciona mais um arquivo
    self.tipo = self.tipo + 1
    self.tamanho = self.tamanho + 1
    self.posicao = self.posicao + 1
    print(f'O arquivo {self.nome} foi adicionado')
  def atualiza_arquivo(self):
    #primeiro printa lista e depois seleciona o arquivo específico
    self.nome = self.nome - 1
    self.nome = self.nome + 1
    self.tipo = self.tipo - 1
    self.tipo = self.tipo + 1
    self.tamanho = self.tamanho - 1
    self.tamanho = self.tamanho + 1
    self.posicao = self.posicao - 1
    self.posicao = self.posicao + 1

    print(f' Arquivo atualizado:\nNome: {self.nome}\nTipo: {self.tipo}\nTamanho: {self.tamanho}\nPosicao:{self.posicao}\n')

  def remove_arquivo(self):
    self.nome = self.nome - 1 #remove um arquivo
    self.tipo = self.tipo - 1
    self.tamanho = self.tamanho - 1
    self.posicao = self.posicao - 1
      
  def aloca_arquivo(self):
    self.posicao = self.posicao + 1 #adiciona uma posicao a frente
    print(f'a nova posicao eh: {self.posicao}')

  

