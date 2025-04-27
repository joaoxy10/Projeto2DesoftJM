import random

def rolar_dados(Quantia):
    lista=[]
    i=0
    while i<Quantia:
        numero=random.randint(1,6)
        lista.append(numero)
        i=i+1
    return lista

def guardar_dado(rolados,estoque,guardar):
    novo_rolados=[]
    resposta=[]
    i=0
    while i < len(rolados):
        if i == guardar:
            estoque.append(rolados[i])
        else:
            novo_rolados.append(rolados[i])
        i=i+1
    resposta.append(novo_rolados)
    resposta.append(estoque)
    return resposta

def remover_dado(rolados,estoque,remover):
    novo_estoque=[]
    i=0
    while i <len(estoque):
        if i==remover:
            rolados.append(estoque[i])
        else:
            novo_estoque.append(estoque[i])
        i=i+1
    resposta=[]
    resposta.append(rolados)
    resposta.append(novo_estoque)
    return resposta

