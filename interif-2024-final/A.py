def main():
  target = int(input())
  n = int(input())
  vetor = []

  for _ in range(n):
    x = int(input())
    vetor.append(x)

  sums = {}

  for i in range(n):
    x = vetor[i]

    if x in sums:
      print(sums[x], i)
      break

    sums[target - x] = i

  return 0

if __name__ == "__main__":
  main()