contador = 0
dia = 12
print ("contando do 12")
while contador <= 100:
    multiplicador = contador * dia
    print(contador,"* 12 =", multiplicador)
    contador +=1
    if multiplicador > 1000:
        print("maior que 1000")