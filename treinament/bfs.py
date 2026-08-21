def bfs(n, m, g):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # achar inicio e fim
  inicio = fim = -1
  for i in range(n):
    for j in range(m):
      if g[i][j] == 'x':
        inicio = (i, j)
      elif g[i][j] == 'y':
        fim = (i, j)

  if inicio == -1 or fim == -1:
    return -1
  
  distancias = [([-1] * m) for _ in range(n)]

  fila = []
  fila.append(inicio)

  vi, vj = inicio
  distancias[vi][vj] = 0

  while len(fila) > 0:
    i, j = fila.pop(0)

    if (i, j) == fim:
      break

    for k in range(4):
      ni, nj = i + dx[k], j + dy[k]

      if 0 <= ni < n and 0 <= nj < m:
        if distancias[ni][nj] == -1 and g[ni][nj] != "#":
          distancias[ni][nj] = distancias[i][j] + 1
          fila.append((ni, nj))

  fi, fj = fim
  if distancias[fi][fj] == -1:
    return -1

  return distancias[fi][fj]

def main():
  n, m = map(int, input().split())

  g = [([''] * m) for _ in range(n)]

  for i in range(n):
    r = str(input())

    for j in range(m):
      g[i][j] = r[j]

  resultado = bfs(n, m, g)

  print(resultado)

  return 0

main()