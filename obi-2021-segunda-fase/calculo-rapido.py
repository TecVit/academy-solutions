def somarDigitos(numero):
  numero = str(numero)
  s = 0

  for digito in numero:
    s += int(digito)

  return s

def main():
  s = int(input())
  a = int(input())
  b = int(input())

  c = 0

  for i in range(a, b + 1):
    si = somarDigitos(i)

    if si == s:
      c += 1

  print(c)
  return 0

if __name__ == "__main__":
  main()