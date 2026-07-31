def main():
  while True:
    try:
      c, m = map(int, input().split())
    except EOFError:
      break
    
    total = 0
    for _ in range(c):
      n, p = input().split()
      total += int(p)
    
    print(3 * m - total)

if __name__ == "__main__":
  main()