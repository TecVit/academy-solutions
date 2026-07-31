def main():
  p_cu, p_zn, m_total = map(float, input().split())

  t_cu = p_cu * (m_total * 0.7)
  t_zn = p_zn * (m_total * 0.3)

  total = t_cu + t_zn

  print(f'''COBRE: {(m_total * 0.7):.2f} KG
ZINCO: {(m_total * 0.3):.2f} KG
CUSTO TOTAL: R$ {total:.2f}''')
  
  return 0

if __name__ == "__main__":
  main()