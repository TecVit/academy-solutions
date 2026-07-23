def main():
  alfabeto = "abcdefghijklmnopqrstuvwxyz"

  n = int(input())

  for _ in range(n):
    palavra = str(input())
    resultado = ""

    c = 0
    num = 0

    while c < len(palavra):
      letra = palavra[c]
      if letra in alfabeto:
        c += 1
      else:
        if letra == "9":
          num = int(letra + palavra[c + 1])
          letra = alfabeto[num - 97]
          c += 2
        elif letra == "1":
          num = int(letra + palavra[c + 1] + palavra[c + 2])
          letra = alfabeto[num - 97]
          c += 3

      resultado += letra

    print(resultado)

  return 0

if __name__ == "__main__":
  main()