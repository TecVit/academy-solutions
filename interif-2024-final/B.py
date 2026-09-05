def medianaDeUmArray(arr):
  arr.sort()

  tamanho = len(arr)

  if tamanho % 2 == 0:
    mediana = arr[tamanho // 2] + arr[(tamanho // 2) + 1] / 2
  else:
    mediana = arr[tamanho // 2]

  return mediana

def main():
  x, y = map(int, input().split())
  arr = list(map(int, input().split()))

  z = x - y

  avisos = 0

  for i in range(z):
    start, end = i, i + y

    mediana = medianaDeUmArray(arr[start:end])
    operacao = arr[end]

    if operacao >= (mediana * 2):
      avisos += 1

  print(avisos)

  return 0

if __name__ == "__main__":
  main()