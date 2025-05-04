#jogo
from funcoes import *
max_rounds = 12
jogadas_possiveis = [0, 1, 2, 3, 4]
cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

#SO TEM UM JOGADOR!!!!!!!!! EU ACHEI Q TINHA Q ALTERNAR PLAYER 1 E PLAYER 2 IGUAL NO EP1!!!!!!!!!!!!!!!! QUE VIDA BOA!!!!!!!!!!!!!!!!!!!!!!!
dados = rolar_dados(5)
estoque = []
rolagens = 2
jogadas = 0





while jogadas < max_rounds:      #while principal!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    
    print(f'Dados rolados: {dados}')
    print(f'Dados guardados: {estoque}')
    
    
    ordem = input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    
    try:
        ordem_int = int(ordem)
        if ordem_int in jogadas_possiveis:
            ordem_valida = True
        else:
            ordem_valida = False
    except:
         ordem_valida = False
    finally:
        ordem_valida = True


    
        if ordem_valida == True:
            #rodar o jogo normalmente
            ordem = int(ordem)

            #guardar dado
            if ordem == 1:
                dado_a_guardar = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
                
                result_guardar = guardar_dado(dados, estoque, dado_a_guardar)
                
                dados = result_guardar[0]
                estoque = result_guardar[1]
                

            #remover dado
            if ordem == 2:
                dado_a_remover = int(input("Digite o índice do dado a ser removido (0 a 4):"))

                result_remover = remover_dado(dados, estoque, dado_a_remover)

                dados = result_remover[0]
                estoque = result_remover[1]



            #rolar dados dnv
            if ordem == 3:
                if rolagens > 0:
                    dados = rolar_dados(len(dados))
                    rolagens -=1
                else:
                    print("Você já usou todas as rerrolagens.")




            #mostrar a tabela
            if ordem == 4:
                imprime_cartela(cartela_de_pontos)



            #fazer a jogada
            if ordem == 0:
                categoria = input("Digite a combinação desejada:") #verificar se o espaco depois do : importa ou nao!!!!!!!!!!!!
                in_avancado = False
                in_simples = False


                #verificar se esta dentro de 
                if categoria in cartela_de_pontos['regra_avancada']:
                    in_avancado = True
                    classe = 'regra_avancada'
                try:
                    categoria_int = int(categoria)
                except:
                    in_simples = False
                else:
                    if categoria_int in cartela_de_pontos['regra_simples']:
                        in_simples = True
                        classe = 'regra_simples'
                
                

                #verificar se eh valido
                while in_avancado == False and in_simples == False:
                    
                    print("Combinação inválida. Tente novamente.")
                    categoria = input()
                

                #verificar se combinacao ja esta usada
                
                if categoria in cartela_de_pontos['regra_avancada']:
                    in_avancado = True
                    classe = 'regra_avancada'
                try:
                    categoria_int = int(categoria)
                except:
                    in_simples = False
                else:
                    if categoria_int in cartela_de_pontos['regra_simples']:
                        in_simples = True
                        classe = 'regra_simples'
                    
                    
                    
                while cartela_de_pontos[classe][categoria] != -1:
                        
                                            
                    print("Essa combinação já foi utilizada.")
                    categoria = input()
                    if categoria in cartela_de_pontos['regra_avancada']:
                        classe = 'regra_avancada'
                    elif int(categoria) in cartela_de_pontos['regra_simples']:
                        classe = 'regra_simples'
                        categoria = int(categoria)


            
                
                #transplantar os dados pra um so estoque
                i = 0
                while i < len(estoque):
                    dados.append(estoque[i])
                    i +=1


                
                    
                cartela_de_pontos = faz_jogada(dados, categoria, cartela_de_pontos) #verificar se precisa colocar o estoque junto dos dados!!!!!!!!!!!! edit: precisa
                
                
                #resetar o jogo
                dados = []
                dados = rolar_dados(5)
                estoque = []
                rolagens = 2
                invalida = False




                jogadas +=1
        else:
            print("Opção inválida. Tente novamente.")



#fim do jogo, calcular a pontuacao final


soma_simples = 0
soma_avancada = 0
bonus = 0


#soma simples
for i in cartela_de_pontos['regra_simples'].values():
    soma_simples += i


#soma avancada
for i in cartela_de_pontos['regra_avancada'].values():
    soma_avancada += i

if soma_simples >= 63:
    bonus = 35

pontuacao_final = soma_simples + soma_avancada + bonus


imprime_cartela(cartela_de_pontos)
print(f"Pontuação total: {pontuacao_final}")