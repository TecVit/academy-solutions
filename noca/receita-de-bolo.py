def main():
  a, b, c = map(int, input().split())

  a /= 2
  b /= 3
  c /= 5

  print(int(min([a, b, c])))

  return 0

if __name__ == "__main__":
  main()