soma=0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        soma += c
print("A soma é: {}".format(soma))
print("fim")