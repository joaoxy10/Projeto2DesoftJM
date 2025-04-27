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

def calcula_pontos_regra_simples(lista):
    numero={1:0,2:0,3:0,4:0,5:0,6:0}
    for chave in numero.keys():
        i=0
        while i <len(lista):
            if chave==lista[i]:
                numero[chave]=numero[chave]+lista[i]
            i=i+1
    return numero

def calcula_pontos_soma(lista):
    soma=0
    i=0
    while i < len(lista):
        soma=soma+lista[i]
        i=i+1
    return soma

def calcula_pontos_sequencia_baixa(lista):
    i=0
    lista_org=[]
    numero=[1,2,3,4,5,6]
    while i<len(numero):
        i2=0
        while i2 <len(lista):
            if lista_org==[1,2,3,4] or lista_org==[2,3,4,5] or lista_org==[3,4,5,6]:
                break
            if numero[i]==lista[i2]:
                if  not lista[i2] in lista_org :
                    lista_org.append(lista[i2])
            i2=i2+1
        i=i+1
    if lista_org==[1,2,3,4] or lista_org==[2,3,4,5] or lista_org==[3,4,5,6]:
        return 15
    else:
        return 0
