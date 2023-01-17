def campeonato():

  usuario = 0

  computador = 0

  x = 1

  for _ in range(3):

    print("\n**** Rodada {} ****\n".format(x))
    
    x = x + 1
    
    vencedor = partida()
    
    if vencedor == 1:
    
        usuario = usuario + 1
        
    else:
    
        computador = computador + 1
        
  print("\n**** Final do campeonato! ****\n")

  print("Placar: Você {} x {} Computador".format(usuario, computador))


def computador_escolhe_jogada(n, m):

  if n <= m:
  
    return n
    
  else:

    quantia = n % (m+1)
    
    if quantia > 0:
    
        return quantia
        
  return m


def usuario_escolhe_jogada(n, m):

  jogada = 0

  while jogada == 0:

    jogada = int(input("Quantas peças você vai tirar? "))
    
    if jogada > n or jogada < 1 or jogada > m:
    
        print("\nOops! Jogada inválida! Tente de novo.\n")
        
        jogada = 0
        
  return jogada


def partida():

  n = int(input("Quantas peças? "))

  m = int(input("Limite de peças por jogada? "))

  is_computer_turn = True

  if n % (m+1) == 0: 

    is_computer_turn = False
    
    print("\nVocê começa!\n")
    
  else:

    print("\nComputador começa!\n")

  while n > 0:

    if is_computer_turn:
    
        jogada = computador_escolhe_jogada(n, m)
        
        is_computer_turn = False
        
        if(jogada == 1):
        
            print("\nO computador tirou uma peça.")
            
        else:
        
            print("\nO computador tirou {} peças.".format(jogada))
            
    else:
    
        jogada = usuario_escolhe_jogada(n, m)
        
        is_computer_turn = True
        
        if(jogada == 1):
        
            print("\nVocê tirou uma peça.")
            
        else:
        
            print("\nVocê tirou {} peças.".format(jogada))


    n = n - jogada

    if(n == 1):
    
        print("Agora resta apenas uma peça no tabuleiro.\n")
        
    elif(n > 1):
    
        print("Agora restam {} peças no tabuleiro.\n".format(n))

  if is_computer_turn:

    print("Fim do jogo! Você ganhou!")
    
    return 1
    
  else:

    print("Fim do jogo! O computador ganhou!")
    
    return 0


tipo_jogo = 0
    
while tipo_jogo == 0:

  tipo_jogo = (int(input("Bem-vindo ao jogo do NIM! Escolha: \n\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato ")))
    
  if ( tipo_jogo == 1 ):
        
    print("\nVoce escolheu partida isolada!")
        
    partida()
        
    break
    
  elif ( tipo_jogo == 2):
        
    print("\nVoce escolheu um campeonato!")
        
    campeonato()
        
    break
    
  else:
            
    print("Opção inválida!")
        
    tipo_jogo = 0
