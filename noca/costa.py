def main():
    m, n = map(int, input().split())

    grid = [input() for _ in range(m)]

    c = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                se_agua = False

                if i == 0 or grid[i-1][j] == ".":
                    se_agua = True
                if i == m-1 or grid[i+1][j] == ".":
                    se_agua = True
                if j == 0 or grid[i][j-1] == ".":
                    se_agua = True
                if j == n-1 or grid[i][j+1] == ".":
                    se_agua = True

                if se_agua:
                    c += 1

    print(c)

    return 0

if __name__ == "__main__":
    main()