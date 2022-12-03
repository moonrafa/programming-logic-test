# Dada a seguinte arvore binária de palavras, faça uma função que busque nessa arvore pela palavra-chave. O output da sua função deve ser o caminho até chegar no item procurado. Por exemplo, se o input de buscar for “goiaba” o output deve ser uma string “Maça -&gt; morango -&gt; Goiaba”.

# Criando a árvore binária

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    
# Função para verificar se há um caminho da raiz até o item pesquisado e para popular uma lista com o caminho, caso exista 

def hasPath(root, lista, item):
  # Retorna falso caso esse nó seja do tipo None
  if (not root):
    return False
  # Adiciona o valor do nó que faz parte do caminho que está sendo checado atualmente
  lista.append(root.data)    
  
  # Se o valor pesquisado for encontrado, retorna verdadeiro
  if (root.data == item):    
    return True
    
  # Se não, continua a procura nos subnós recursivamente, se encontrar retorna verdadeiro
  if (hasPath(root.left, lista, item) or hasPath(root.right, lista, item)):
    return True
    
  # Se o item pesquisado não se encontra no nó esquerdo nem direito do nó atual, remove o item da lista e retorna falso, pois não foi encontrado nesse caminho
  lista.pop(-1)
  return False

# Função para imprimir o caminho até o item, caso encontrado
def imprimirPath(root, item):    
  caminho = []
  string = []
  # Um for loop para imprimir o caminho caso tenha um
  if (hasPath(root, caminho, item)):
    for i in range(len(caminho) - 1):
      string.append(caminho[i])
    string.append(caminho[len(caminho) - 1])
  return string


# Populando a árvore de acordo com a questão

root = Node('Maçã')
root.left = Node('Morango')
root.right = Node('Pera')
root.left.left = Node('Goiaba')
root.left.right = Node('Limão')
root.right.left = Node('Abacaxi')
root.right.left.left = Node('Laranja')
root.right.left.left.left = Node('Banana')
root.right.left.left.right = Node('Cebola')

# Visualmente:
'''      Maçã
        /    \
  Morango      Pera 
  /    \        |
Goiaba  Limão  Abacaxi
                |
              Laranja
              /    \ 
          Banana  Cebola
  '''

# Pesquisando o caminho até o item"
def search(item):
  # Como não tinha nada na questão sobre isso, possibilitei que possa ser pesquisado com palavras em uppercase, lowercase e capitalized
  item = item.capitalize()
  if(imprimirPath(root, item)):
    return' -> '.join(imprimirPath(root, item))
  else:
    return 'Item não encontrado'
# ex: Goiaba, output: "Maçã -> Morango -> Goiaba
print(search('Goiaba'))
