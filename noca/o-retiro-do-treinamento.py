def main():
    d, n = map(float, input().split())

    p = d * n

    if n <= 8:
        p += 8 * n
    else:
        p += 5 * n
    
    print(f"{p:.2f}")

    return 0

if __name__ == "__main__":
    main()