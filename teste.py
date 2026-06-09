usuarios = [{"Nome": "Etelvino"}]

usuarios.insert(len(usuarios)-1, {"Nome": 'Tiago', "Saldo": 123})

nomeprocurado = input('Nome: ')
resultado = None

for c in usuarios:
    if c["Nome"] == nomeprocurado:
        resultado = c
        break

print(resultado)