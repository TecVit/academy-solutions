def main():
  n, m = map(int, input().split())

  medalhas = [[0, 0, 0, i + 1] for i in range(n)]

  for _ in range(m):
    o, p, b = map(int, input().split())

    medalhas[o - 1][0] += 1
    medalhas[p - 1][1] += 1
    medalhas[b - 1][2] += 1

  medalhas.sort(key=lambda x: (-x[0], -x[1], -x[2]))

  for r in medalhas:
    print(r[-1], end=" ")

  return 0

main()