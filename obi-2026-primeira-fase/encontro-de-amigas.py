def main():
  a_inicio = int(input())
  a_fim = int(input())

  b_inicio = int(input())
  b_fim = int(input())

  c_inicio = int(input())
  c_fim = int(input())

  inicio_conjunto = max(a_inicio, b_inicio, c_inicio)
  fim_conjunto = min(a_fim, b_fim, c_fim)

  resultado = (fim_conjunto - inicio_conjunto) + 1

  if resultado < 0:
    print(0)
  else:
    print(resultado)

  return 0

if __name__ == "__main__":
    main()