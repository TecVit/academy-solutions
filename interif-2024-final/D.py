def main():
  n = int(input())
  arr = list(map(int, input().split()))

  max_val = max(arr) if arr else 0
  largura = len(bin(max_val)[2:])

  contagem = [0] * largura

  for i in range(n):
    x = arr[i]
    binario = bin(x)[2:].zfill(largura)

    for pos in range(largura):
      contagem[pos] += int(binario[pos])

  print("chave:", end=" ")

  qtd_contagem = largura
  conta = 0

  for i in range(qtd_contagem):
    numero = contagem[i]

    if numero == 0:
      continue

    print(f"{numero}*2^{qtd_contagem - 1 - i}", end="")

    if i + 1 != qtd_contagem:
      print("+", end="")

    conta += numero * (2 ** (qtd_contagem - 1 - i))

  print(f"={conta}")

  return 0

if __name__ == "__main__":
  main()