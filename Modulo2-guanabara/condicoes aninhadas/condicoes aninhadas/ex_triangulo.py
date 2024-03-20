l1 = float(input("Digite a medida do lado 1 triângulo: "))
l2 = float(input("Digite a medida do lado 2 triângulo: "))
l3 = float(input("Digite a medida do lado 3 triângulo: "))

if(l1 < l2+l3 and l3 < l1+l2 and l2 < l1+l3):
    print('{:2} {:2} {:2}'.format(l1, l2, l3))
    print('Triângulo obedece as condições de existências formando um triângulo: ', end='')

    if(l1==l2==l3):
        print('EQUILÁTERO')
    elif(l1!=l2!=l3):
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print("Triângulo não obedece condições de existência")