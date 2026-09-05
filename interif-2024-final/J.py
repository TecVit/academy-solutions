import queue

def main():
  qtd_alunos, qtd_amizades = map(int, input().split())

  # Amizades vai ser um grafo pois os
  # vertices conectados diretamente sao amigos
  amizades = { i: set() for i in range(1, qtd_alunos + 1)}

  for _ in range(qtd_amizades):
    i, j = map(int, input().split())

    if i in amizades:
      amizades[i].add(j)

    if j in amizades:
      amizades[j].add(i)

  equipes = []

  visitados = set()

  fila = queue.Queue()

  for i in range(1, qtd_alunos + 1):
    equipe = set()
    fila.put(i)

    while fila.qsize() > 0:
      atual = fila.get()

      if atual in visitados:
        continue
      
      # print(f"{atual} -> ", end="")
      visitados.add(atual)
      equipe.add(atual)

      for vizinho in amizades[atual]:
        fila.put(vizinho)

    if equipe:
      equipes.append(equipe)

  # print()
  print(len(equipes))
  # print(equipes)
  # print(amizades)

  return 0

if __name__ == "__main__":
  main()