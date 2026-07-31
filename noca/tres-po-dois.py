def main():
  n = int(input())
  l = [int(input()) for _ in range(n)]

  if n < 3:
    print(sum(l))
    return 0

  l.sort(reverse=True)

  r = 0
  for i in range(2, n, 3):
    r += l[i]

  print(sum(l) - r)

  return 0

if __name__ == "__main__":
  main()