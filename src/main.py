nomesList = []
teste = [{
    'nome': 'Paulo',
    'idade': 20,
    'cidade': 'Salvador/BA'
},
    {
    'nome': 'Rafael',
    'idade': 33,
    'cidade': "São Paulo"
},
    {
    'nome': 'Jose',
    'idade': 55,
    'cidade': 'Santos/SP'
}]

teste2 = {
    'nome': 'Rafael',
    'idade': 33,
    'cidade': "São Paulo"
}


for i in range(0, 3):
    nomes = teste[i]['nome']
    str(nomes)
    nomesList.append(nomes)
print(nomesList)
