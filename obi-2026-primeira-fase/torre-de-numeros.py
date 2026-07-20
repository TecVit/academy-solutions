def main():
  n = input().strip()
  torre = [int(n)]

  while True:
    topo = str(torre[-1]).zfill(4)
    digitos = sorted(topo)

    menor = int("".join(digitos))
    maior = int("".join(digitos[::-1]))
    x = maior - menor

    if x in torre:
      break

    torre.append(x)

  for numero in torre:
    print(numero)

if __name__ == "__main__":
    main()