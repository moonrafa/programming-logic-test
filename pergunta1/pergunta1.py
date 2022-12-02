# Dado o Array de inteiros abaixo, ordene-o de tal forma que os números “1” estejam à esquerda. Os itens devem ser modificados no lugar, ou seja, você não ira trocar posições e sim colocar os números “1” no inicio do Array.

def oneFirst(lista):
  # Primeiro, conta-se a quantidade de números 1 na lista
  amountOfOnes = lista.count(1)

  # Iremos então tirá-los das suas posições
  while 1 in lista:
    lista.remove(1)
    
  # E colocar-los no inicio da lista
  for i in range( 0, amountOfOnes):
    # se amountOfOnes = 4
    # i = 0, 1, 2, 3  (adicionando sempre no inicio da lista)
    lista.insert(i, 1)
  return lista

print(oneFirst([2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]))