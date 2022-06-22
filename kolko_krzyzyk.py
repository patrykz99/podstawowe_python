import time
class Kolko_krzyzyk:
    def __init__(self): #inicjalka
        self.user_sign = 'O'
        self.user2_sign = 'X'
        self.the_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def print_board(self): #wyswietlenie tablicy
        print(self.the_board[0] + '|' + self.the_board[1] + '|' + self.the_board[2])
        print('-' + ' ' + '-' + ' ' + '-')
        print(self.the_board[3] + '|' + self.the_board[4] + '|' + self.the_board[5])
        print('-' + ' ' + '-'+ ' '  +'-')
        print(self.the_board[6] + '|' + self.the_board[7] + '|' + self.the_board[8])
        print()

    def _user2_move(self, numer): #ruch gracza 2
        self.the_board[numer] = self.user2_sign


    def _user_move(self, field_number): #ruch gracza 1
        self.the_board[field_number] = self.user_sign

    def who_win(self): #sprawdzenie kto wygral
        result = []

        result.append(self.the_board[0] + self.the_board[1] + self.the_board[2])
        result.append(self.the_board[3] + self.the_board[4] + self.the_board[5])
        result.append(self.the_board[6] + self.the_board[7] + self.the_board[8])
        result.append(self.the_board[0] + self.the_board[3] + self.the_board[6])
        result.append(self.the_board[1] + self.the_board[4] + self.the_board[7])
        result.append(self.the_board[2] + self.the_board[5] + self.the_board[8])
        result.append(self.the_board[0] + self.the_board[4] + self.the_board[8])
        result.append(self.the_board[2] + self.the_board[4] + self.the_board[6])

        if 'XXX' in result:
            print('Gracz z krzyżykiem wygrał!!!')
            return True
        elif 'OOO' in result:
            print('Gracz z kółkiem wygrał!!!')
            return True


        return False

    def move_player1(self, field_number): # czy g1 wybral pusta pozycje

        if field_number in range(0, 9):
            if self.the_board[field_number] == 'X' or self.the_board[field_number] == 'O':
                while True:
                    player_one = int(input('Gracz z kółkiem: Podaj numer pola do ktorego wpisac kółko (od 0 - 8: )'))
                    if self.the_board[player_one] != 'O' and self.the_board[player_one] != 'X':
                        self._user_move(player_one)
                        break
            else:
                self._user_move(field_number)

    def move_player2(self, numer): # czy g2 wybral pusta pozycje
        if numer in range (0, 9):
            if self.the_board[numer] == 'X' or self.the_board[numer] == 'O':
                while True:
                    player_two = int(input('Gracz z krzyżykiem: Podaj numer pola do ktorego wpisac kółko (od 0 - 8: )'))
                    if self.the_board[player_two] != 'O' and self.the_board[player_two] != 'X':
                        self._user2_move(player_two)
                        break
            else:
                self._user2_move(numer)


    def reset(self): #reset tablicy
        self.__init__()

# wyswietlenie
gra = Kolko_krzyzyk()
gra.print_board()

while True:
    player2 = int(input('Gracz z krzyżykiem: Podaj numer pola do ktorego wpisac kółko (od 0 - 8: )'))
    gra.move_player2(player2)
    gra.print_board()
    if (gra.who_win() == True):
        # score = gra.who_win()
        print(gra.who_win())
        break
    del player2
    if ' ' in gra.the_board:
        player1 = int(input('Gracz z kółkiem: Podaj numer pola do ktorego wpisac kółko (od 0 - 8: )'))
        gra.move_player1(player1)
        gra.print_board()
        if (gra.who_win() == True):
            # score = gra.who_win()
            print(gra.who_win())
            break
        del player1
    else:
        gra.print_board()
        print('Remis!')
        break

time.sleep(15)
print('Im deleting board... ')
for i in range(5, 0, -1):
    print(f'In {i} ')
    time.sleep(1.5)
gra.reset()
gra.print_board()





