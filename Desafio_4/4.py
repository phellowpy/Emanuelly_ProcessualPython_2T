numeros = [i for i in range(1, 101)] 
for num in numeros:
    is_primo = True
    if num < 2:
        is_primo = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_primo = False
                break
    if is_primo:
        print(f"{num}: número primo")
    if num % 2 == 0:
        print(f"{num}: divisível por 2")