n = int(input())
r = int(n ** (1 / 2))

while r * r > n:
  r -= 1

while (r + 1) * (r + 1) <= n:
  r += 1

print(r * r)