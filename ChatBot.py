def Greet():    
    while True:   
        try:
            nome = input("1ºNome: ")
            print(f"Olá {nome}!")

            idade = int(input("Idade: "))
            print(f"Parabéns pelos seus {idade} anos! " )

            apelido = input("Apelido: ")
            print(f"Prazer, {nome} {apelido}!")
            break
        except ValueError:
            print("Erro! Deve introduzir um numero!")
            
            

