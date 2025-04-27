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


dados_rolados = [1, 3, 2]
dados_no_estoque = [1, 2]
dado_para_guardar = 1

print(guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar))
