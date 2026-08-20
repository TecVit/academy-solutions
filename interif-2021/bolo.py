def main():
  n = int(input())
  precos = list(map(float, input().split()))  # precos[0] = preço de 1 pedaço, precos[1] = 2 pedaços, ...

  # dp[i] = menor custo para conseguir i pedaços
  # dp[0] = 0 (zero pedaços custa zero)
  # o resto começa "infinito" pra garantir que o min() sempre atualize

  INF = float('inf')
  dp = [INF] * (n + 1)
  dp[0] = 0

  for i in range(1, n + 1):
    for j in range(1, i + 1):
      # j = tamanho do "último pedido" que eu testo
      # precos[j-1] porque a lista é 0-indexada (precos[0] é o preço de 1 pedaço)
      custo = dp[i - j] + precos[j - 1]
      if custo < dp[i]:
        dp[i] = custo

  print(f"{dp[n]:.2f}")

if __name__ == "__main__":
  main()