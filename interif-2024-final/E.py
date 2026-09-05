import sys

def main():
  data = sys.stdin.read().split('\n')
  n = int(data[0])
  saida = []

  for i in range(1, n + 1):
    palavra = data[i]
    resultado = []
    c = 0
    length = len(palavra)

    while c < length:
      ch = palavra[c]
      if ch == ' ':
        resultado.append(' ')
        c += 1
      elif ch.isalpha():
        resultado.append(ch)
        c += 1
      elif ch == '9':
        num = int(palavra[c:c + 2])
        resultado.append(chr(num))
        c += 2
      elif ch == '1':
        num = int(palavra[c:c + 3])
        resultado.append(chr(num))
        c += 3
      else:
        resultado.append(ch)
        c += 1

    saida.append("".join(resultado))

  sys.stdout.write("\n".join(saida) + "\n")

if __name__ == "__main__":
  main()