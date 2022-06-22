import getpass
import os

#getpass zeby nie zobaczyl co gracz wpisal :D
mozliwosci = ['Kamien','Papier','Nozyce']
punkty1 = 0
punkty2 = 0

def clearConsole(): #czyszczenie konsoli
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def wybor_graczy(ktory_gracz): # wybieranie gracza
    # gracz = input(f'Gracz {ktory_gracz}: ')
    gracz = getpass.getpass(f'Gracz {ktory_gracz}: ') # ukrywa slowa zeby nie bylo widoczne co wybral gracz (dziala tylko w terminalu)
    gracz = gracz.capitalize()

    while not gracz in mozliwosci:
        print('Zle slowo! Wybierz ponownie: papier, kamien albo nozyce!')
        # gracz = input(f'Gracz {ktory_gracz}: ')
        gracz = getpass.getpass(f'Gracz {ktory_gracz}: ')
        gracz = gracz.capitalize()

    return gracz


def warunki_kto_zdobywa_pkt(gracz1,gracz2): #zliczanie kto zdobywa pkt
    pkt1 = 0
    pkt2 = 0
    if (gracz1 == 'Kamien' and gracz2 == 'Nozyce') or (gracz1 == 'Papier' and gracz2 == 'Kamien') \
    or (gracz1 == 'Nozyce' and gracz2 == 'Papier'):
        print('Gracz 1 zdobywa punkt!')
        pkt1 = pkt1 + 1
        return pkt1
    elif (gracz1 == gracz2):
        print('Remis! Gracze nie otrzymuja punktow!')
    else:
        print('Gracz 2 zdobywa punkt!')
        pkt2 = pkt2 + 2
        return pkt2

if __name__ == "__main__":
    while (True): #petla glowna
        print("Prosta gierka kamien, papier, nozyce dla dwoch graczy :)")
        Gracz1 = wybor_graczy('Pierwszy')
        Gracz2 = wybor_graczy('Drugi')
        suma = warunki_kto_zdobywa_pkt(Gracz1,Gracz2)

        if suma == 1:
            punkty1 += 1
        elif suma == 2:
            punkty2 += 1

        print(f'Obecny wynik: {punkty1} do {punkty2}')

        if punkty1 == 3:
            print('Wygral Gracz 1!')
            break
        elif punkty2 == 3:
            print('Wygral Gracz 2!')
            break












