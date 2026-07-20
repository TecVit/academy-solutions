def main():
  g1, g2, g3, g4 = map(int, input().split())

  mesas = 0

  mesas += max(g4, 0)

  while g3 != 0 and g1 != 0:
    g3 -= 1
    g1 -= 1

    mesas += 1
  
  mesas += max(g3, 0)

  while g2 >= 2:
    g2 -= 2

    mesas += 1

  if g2 == 1:
    g2 -= 1
    g1 -= 2

    mesas += 1
  
  mesas += g1 // 4

  if (g1 % 4) != 0:
    mesas += 1
  
  g1 -= (4 * (g1 // 4)) + (g1 % 4)
  
  print(mesas)

  return 0

if __name__ == "__main__":
    main()