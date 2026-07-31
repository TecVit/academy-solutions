def acharPontoDaIlha(m):
  y, x = 0, 0

  for i in range(len(m)):
    r = m[i]
    if r.count("#") > 0:
      y = i
      x = r.index("#")
      break

  return y, x

def main():
  l, c = map(int, input().split())

  m = [['.'] * (c + 2)]

  for _ in range(l):
    row = list(map(str, input()))

    m.append(['.'] + row + ['.'])

  m.append(['.'] * (c + 2))

  fila = []

  while True:
    y, x = acharPontoDaIlha(m)

    if y == x == 0:
      break

    fila.append((y, x))

    while len(fila) > 0:
      yi, xi = fila.pop(0)

      

  print(y, x)

  return 0

if __name__ == "__main__":
  main()