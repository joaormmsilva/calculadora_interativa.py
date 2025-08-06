def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

cont = 0
num1 = float(input('digite seu valor: '))
num2 = float(input('digite outro valor: '))

while True:
    
    print('Qual operação deseja')
    operacao = int(input('''
[0] soma 
[1] subtração 
[2] multiplicação 
[3] divisão
opção: '''))
    

    if cont != 0:
        if operacao == 0:
            res = soma(res,num2)
            print(f'{num1} + {num2} = {res}')
        if operacao == 1:
            res = subtracao(res,num2)
            print(f'{num1} - {num2} = {res}')
        if operacao == 2:
            res = multiplicacao(res,num2)
            print(f'{num1} * {num2} = {res}')
        if operacao == 3:
            res = divisao(res,num2)
            print(f'{num1} / {num2} = {res}')
    else:
        if operacao == 0:
            res = soma(num1,num2)
            print(f'{num1} + {num2} = {res}')
        if operacao == 1:
            res = subtracao(num1,num2)
            print(f'{num1} - {num2} = {res}')
        if operacao == 2:
            res = multiplicacao(num1,num2)
            print(f'{num1} * {num2} = {res}')
        if operacao == 3:
            res = divisao(num1,num2)
            print(f'{num1} / {num2} = {res}')
    
    verificador = input('Deseja continuar com outra operação usando o mesmo resultado? [s/n]').lower().strip()
    if verificador == 'n':
        verificador = input('\nDeseja fazer outra conta? [s/n]').lower().strip()
        if verificador == 'n':
            break
        else:
            num1 = int(input('digite seu valor: '))
            num2 = int(input('digite outro valor: '))
            continue
    
    num2 = int(input('digite o novo numero: '))
    cont += 1

verificador = input('Deseja fazer outra conta? [s/n]').lower().strip()

