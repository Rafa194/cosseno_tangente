print('O que você gostaria de calcular?')
opcao = int(input('(1) Seno // (2) Cosseno // (3) Tangente: '))
while opcao > 3 or opcao < 1:
    print('Digite um numero entre 1 e 3:')
    opcao = int(input('(1) Seno // (2) Cosseno // (3) Tangente: '))

if opcao == 1:
    co = float(input('Digite o valor do Cateto Oposto: '))
    h = float(input('Digite o valor da Hipotenusa: '))
    seno = (co / h)
    print('o seno é: {:.2f}'.format(seno))

elif opcao == 2:
    adj = float(input('Digite o valor do Cateto Adjacente: '))
    h = float(input('Digite o valor da Hipotenusa: '))
    cosseno = (adj / h)
    print('O cosseno é {:.2f}'.format(cosseno))

elif opcao == 3:
    co = float(input('Digite o valor do Cateto Oposto: '))
    adj = float(input('Digite o valor do Cateto Adjacente: '))
    tangente = (co / adj)
    print('A tangente é {:.2f}'.format(tangente))



# CALCULADORA DE SENO, COSSENO OU TANGENTE
# - a pessoa escolhe o item a ser calculado
# se seno... / se cosseno... / se tg ....
# S-OH // C-AH/ T-OA

