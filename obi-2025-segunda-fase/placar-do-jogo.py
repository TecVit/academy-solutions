def main():
  p = list(map(int, input().split()))
  p, ps = p[0], p[1:]

  c = list(map(int, input().split()))
  c, cs = c[0], c[1:]

  gols = []

  for i in range(p):
    gols.append(('paulo', ps[i]))
  
  for i in range(c):
    gols.append(('camila', cs[i]))

  gols.sort(key=lambda x: (x[1]))

  total = {
    'paulo': 0,
    'camila': 0,
  }
  
  print(0, 0)
  for pessoa, minuto in gols:
    total[pessoa] += 1
    print(total['paulo'], total['camila'])

  return 0

if __name__ == "__main__":
  main()