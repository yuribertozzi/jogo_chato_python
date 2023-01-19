def pcchoose(n,m):

    if n <= m:
        
        return n

    else:

        resto = n % (m +1)

        if resto > 0:

            return resto

    return m

#*********

def userchoose(n,m):

    play = 0

    while play == 0:

        print()

        play = int(input("Quantas peças vai tirar? "))

        if play < 0 or play > m or play > n:

            print()

            print("Número inválido!")

            play = 0

        else:

            return play

#*********

def main():

    print()

    n = 0

    m = 0

    while m == 0 and n == 0:

        n = int(input("Qual o número de peças? "))

        m = int(input("Máximo de peças que pode tirar: "))

        if n == 0 or m == 0 or n < m:

            print()
            
            print("Número(s) inválido(s)!")

            n = 0

            m = 0

    pcturn = True

    if n % (m + 1) == 0:

        pcturn = False

        print()

        print("Você começa!")

    else:

        print()

        print("O PC começa!")

#***

    while n > 0:

        if pcturn == True:

            play = pcchoose(n,m)

            pcturn = False

            if play == 1:

                print()

                print("O PC removeu uma peça.")

            else:

                print()

                print("O PC removeu", play, "peças.")

#***

        else:

            play = userchoose(n,m)

            pcturn = True

            if play == 1:

                print()

                print("Você removeu uma peça.")

            else:
                print()

                print("Você removeu", play, "peças.")

            
        n = n - play

        if n == 1:

            print("Resta uma peça no tabuleiro.")

        else:
          
            print("Restam", n, "peças no tabuleiro.")
#***

    if pcturn == True:

        print()

        print("Você venceu!")

    else:

        print()

        print("O PC venceu!")

#***
        
main()
