def main():
    n = int(input())
    fila = list(map(int, input().split()))
    idosos = 0

    i = 0

    for k in range(len(fila)):
        pessoa = fila[k]
        if pessoa >= 60:
            idosos += 1
            i = k

    if idosos == 0:
        print(0)
        return 0

    i += 1
    j = idosos

    mr = i - j

    print(max(mr, 0))

    return 0

if __name__ == "__main__":
    main()