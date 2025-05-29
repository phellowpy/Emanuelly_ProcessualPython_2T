def validar_nome(nome):
    for char in nome:
        if not (char.isalpha() or char.isspace()):
            return False
    return True

print("A seguir coloque 10 nomes:")
erro_encontrado = False

nome1 = input("Coloque um nome:")
if not validar_nome(nome1):
    print(f"Erro: O nome '{nome1}' contém caracteres inválidos.")
    erro_encontrado = True

if not erro_encontrado:
    nome2 = input("Coloque um nome:")
    if not validar_nome(nome2):
        print(f"Erro: O nome '{nome2}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    nome3 = input("Coloque um nome:")
    if not validar_nome(nome3):
        print(f"Erro: O nome '{nome3}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    nome4 = input("Coloque um nome:")
    if not validar_nome(nome4):
        print(f"Erro: O nome '{nome4}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    nome5 = input("Coloque um nome:")
    if not validar_nome(nome5):
        print(f"Erro: O nome '{nome5}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    nome6 = input("Coloque um nome:")
    if not validar_nome(nome6):
        print(f"Erro: O nome '{nome6}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    nome7 = input("Coloque um nome:")
    if not validar_nome(nome7):
        print(f"Erro: O nome '{nome7}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    nome8 = input("Coloque um nome:")
    if not validar_nome(nome8):
        print(f"Erro: O nome '{nome8}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    nome9 = input("Coloque um nome:")
    if not validar_nome(nome9):
        print(f"Erro: O nome '{nome9}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    nome10 = input("Coloque um nome:")
    if not validar_nome(nome10):
        print(f"Erro: O nome '{nome10}' contém caracteres inválidos.")
        erro_encontrado = True

if not erro_encontrado:
    lista = [nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8, nome9, nome10]
    lista.sort()

    for nome in lista:
        num_letras = len(nome.replace(" ", ""))
        print(f"O nome '{nome}' tem {num_letras} letras.")