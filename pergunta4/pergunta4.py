# Dado o array [9, 2, 3, 1, 4] encontre todos os números que estão faltando para completar o intervalo 0 a n, onde n é o maior número dentro do array. Adicione os números faltando dentro do array.
def intervalo(lista):
  # Se a lista não for vazia
  if (lista):
    # Seleciona o n (maior número da lista)
    maxNum = max(lista)
    # Um for loop de 0 até o maior número
    for i in range(0, maxNum):
      # Se não tiver o número que está no intervalo, o adiciona no da lista
      if (lista.count(i) == 0):
        lista.append(i)
  return lista

lista = [9, 2, 3, 1, 4]

print(intervalo(lista))

# Caso queira imprimir ordenada:
print(intervalo(sorted(list(lista))))
