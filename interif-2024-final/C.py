from decimal import Decimal, getcontext

getcontext().prec = 50

def main():
  qtd_alunos, orcamento, valor_unitario = map(Decimal, input().split())

  if qtd_alunos <= 0:
    print(0)
  elif valor_unitario == 0:
    print(1)
  else:
    print(int((orcamento / qtd_alunos) / valor_unitario))

  return 0

if __name__ == "__main__":
  main()