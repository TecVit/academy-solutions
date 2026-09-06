def main():
  qtd, capacidade = map(int, input().split())
  pesos = [0] * qtd
  valores = [0] * qtd

  for i in range(qtd):
    peso, valor = map(int, input().split())

    pesos[i] = peso
    valores[i] = valor

  mochila = [[0] * (capacidade + 1) for _ in range(qtd + 1)]

  for i in range(1, qtd + 1):
    peso = pesos[i - 1]
    valor = valores[i - 1]

    for cap in range(capacidade + 1):
      if peso <= cap:
        mochila[i][cap] = max(mochila[i - 1][cap], valor + mochila[i - 1][cap - peso])
      else:
        mochila[i][cap] = mochila[i - 1][cap]

  print(mochila[qtd][capacidade])

  return 0

if __name__ == "__main__":
  main()