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

def calcula_pontos_sequencia_alta(lista):
    i=0
    lista_org=[]
    numero=[1,2,3,4,5,6]
    while i<len(numero):
        i2=0
        while i2 <len(lista):
            if lista_org==[1,2,3,4,5] or lista_org==[2,3,4,5,6]:
                break
            if numero[i]==lista[i2]:
                if  not lista[i2] in lista_org :
                    lista_org.append(lista[i2])
            i2=i2+1
        i=i+1
    if lista_org==[1,2,3,4,5] or lista_org==[2,3,4,5,6]:
        return 30
    else:
        return 0

def calcula_pontos_full_house(lista):
    lista3i=[]
    lista2i=[]
    i=0
    iguais1=0
    while i<len(lista):
        i2=0
        while i2<len(lista):
            if lista[i] == lista[i2]:
                iguais1=iguais1+1
                lista3i.append(lista[i2])
            if len(lista3i)==3:
                if lista3i[0]!=lista3i[1] or lista3i[2]!=lista3i[1]:
                    lista3i=[]
                    iguais1=0
                    break
            i2=i2+1
        if len(lista3i) == 3:
                break
        lista3i=[]
        i=i+1 
    i3=0
    while i3 <len(lista):
        if not lista[i3] in lista3i:
            lista2i.append(lista[i3]) 
        i3=i3+1
    soma=0 
    if len(lista3i)==3 and len(lista2i): 
        if lista3i[0]==lista3i[1] and lista3i[2]==lista3i[1]:
            if lista2i[0]==lista2i[1]:
                soma=lista3i[0]+lista3i[1]+lista3i[2]+lista2i[0]+lista2i[1]
    return soma