def soma(numero1, numero2):
  return numero1 + numero2

def subtracao(numero1, numero2):
  return numero1 - numero2

def divisao(numero1, numero2):
  if numero2 == 0:
    return 0
  else:
    return numero1 / numero2



################## TESTS ##########################
def test_soma_dois_numeros():
  resultado = soma(15, 30)
  assert resultado == 45

def test_subtracao_dois_numero():
  resultado = subtracao(50, 15)
  assert resultado == 35

def test_divisao_dois_numeros():
  resultado = divisao(20, 5)
  assert resultado == 4

def test_divisao_com_divisor_0():
  resultado = divisao(50, 0)
  assert resultado == 0