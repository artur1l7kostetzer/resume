cpf = int(input('Digite um CPF sem hífens nem pontos: '))
multiplicador = 11
print(len(cpf))
while True:
  for i in range(0,9):
    if i == 0:
    multiplicador = 10
    soma += cpf[i]*multiplicador
    multiplicador -= 1
    continue
    if 11-soma%11 != cpf[9]:
      break
    else:
      
      
