def main():
  n, m = map(int, input().split())

  gaiolas = [False] * m

  for i in range(0, m, 4 + 1):
    gaiolas[i] = True

  qtd = gaiolas.count(True)

  if qtd >= n:
    print("S")
  else:
    print("N")

  return 0

if __name__ == "__main__":
  main()