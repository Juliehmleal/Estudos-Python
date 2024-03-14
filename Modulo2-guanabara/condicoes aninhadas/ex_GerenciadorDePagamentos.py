valorOriginal = float(input("Digite o valor do produto: "))

print("1.dinheiro/cheque")
print("2.à vista no cartão")
print("3.2x no cartão")
print("4.3x ou mais no cartão")
op = int(input("Qual foi o metodo de pagamento? "))

if(op==1):
    print("Preço final: {}".format(round(valorOriginal-valorOriginal*0.10, 2)))
elif(op==2):
    print("Preço final: {}".format(round(valorOriginal-valorOriginal*0.05, 2)))
elif(op==3):
    print("Preço final: {}".format(round(valorOriginal, 2)))
else:
    print("Preço final: {}".format(round(valorOriginal+valorOriginal*0.2, 2)))