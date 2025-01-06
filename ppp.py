print('olá')


def função(): 
    a = input("digite um número positivo de 1 a 3")
    a = int(a)
    print('seu número é ' + str(a))
    if a < 0:
        print('seu número é negativo')
        função()
    elif a < 1:
        print('você escolheu zero')
    elif a < 2:
        print('você escolheu 1 ou 0')
    elif a < 3:
        print('você escolheu 2 ou 1 ou 0')
    else: 
        print("Seu número é grande demais para nós")
função()