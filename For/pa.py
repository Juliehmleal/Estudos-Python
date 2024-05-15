termo1 = int(input("Digite o primeiro termo da p.a: "))
razao = int(input("Digite a razão da p.a: "))

print ("primeiros 10 termos da p.a:")
for c in range(0,10):
    if c == 0:
        print(termo1)
    else:
        termo1 = termo1 + razao
        print(termo1)
    
