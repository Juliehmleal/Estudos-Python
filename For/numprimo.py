num = int(input("Digite um numero: "))
contador = 0

for c in range (1,num):
    if(num % c == 0):
        contador = contador + 1
    
if contador > 2:
    print("Numero não primo")
else:
    print("Numero primo")
