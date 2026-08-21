def main():
  n = int(input())
  alturas = list(map(int, input().split()))

  maior = alturas[-1]
  c = 0

  for i in range(n - 2, -1, -1):
    atual = alturas[i]

    if maior >= atual:
      c += 1
    else:
      maior = atual

  print(c)

  return 0

if __name__ == "__main__":
  main()