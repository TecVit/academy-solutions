def main():
  m, n, k = map(int, input().split())

  inteiro = m // n
  resto = m % n

  if k == 0:
    print(inteiro)
    return

  digitos = []
  for _ in range(k):
    resto *= 10
    digitos.append(resto // n)
    resto %= n

  parte_decimal = ''.join(str(d) for d in digitos)
  print(f"{inteiro}.{parte_decimal}")

if __name__ == "__main__":
  main()