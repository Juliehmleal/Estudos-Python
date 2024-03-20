num=float(input("Digite o numero que deseja saber a tabuada: "))


for i in range(1, 11):
    print("{:,.2f} x {:2} = {:2,.2f}".format(num, i, num*i))
