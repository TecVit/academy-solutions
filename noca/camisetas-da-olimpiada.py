def main():
  n = int(input())
  l = list(map(int, input().split()))

  p = int(input())
  m = int(input())

  sp = l.count(1)
  sm = l.count(2)

  if sp < p or sm < m:
    print("N")
  else:
    print("S")

  return 0

if __name__ == "__main__":
  main()