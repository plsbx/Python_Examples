from random import randrange

border_size_x = 9 # "-" char
border_space = 3

def display_board_hor():
    print("+", "-" * border_size_x, "+", "-" * border_size_x, "+", "-" * border_size_x, "+")
    
def display_board_vert(board, y):
    print("|", " " * border_size_x, "|", " " * border_size_x, "|", " " * border_size_x, "|")
    print(  "|", " " * border_space, board[y][0], " " * border_space, \
            "|", " " * border_space, board[y][1], " " * border_space, \
            "|", " " * border_space, board[y][2], " " * border_space, \
            "|")
    print("|", " " * border_size_x, "|", " " * border_size_x, "|", " " * border_size_x, "|")

def display_board(board):
    for row in range(3):
        display_board_hor()
        display_board_vert(board, row)
    display_board_hor()

def enter_move(board, p_char):
    free_fields = make_list_of_free_fields(board)
    fix_field = (   (0,0),(0,1),(0,2),
                    (1,0),(1,1),(1,2),
                    (2,0),(2,1),(2,2),)
    choosen_field = int(input("Wybierz numer miejsca: "))
    if (choosen_field > 0 and choosen_field < 10):
        if fix_field[choosen_field-1] in free_fields:
            row = fix_field[choosen_field-1][0]
            col = fix_field[choosen_field-1][1]
            board[row][col] = p_char
        else:
            print("Podane miejsce jest zajete, podaj inne")
            enter_move(board, p_char)

    print()
#
# Funkcja, która przyjmuje parametr odzwierciedlający biężący stan tablicy,
# prosi użytkownika o wykonanie ruchu, 
# sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.
#

def make_list_of_free_fields(board):
    free_fields = ()
    free_count = 0;
    for col in range(3):
        for row in range(3):
            if ((board[row][col] != "x") and (board[row][col] != "o")):
                free_count += 1
                free_fields = (*free_fields, (row, col,))
    if free_count == 0:
        return None
    #print(free_fields)
    return free_fields
#
# Funkcja, która przegląda tablicę i tworzy listę wszystkich wolnych pól; 
# lista składa się z krotek, a każda krotka zawiera parę liczb odzwierciedlających rząd i kolumnę.
#

def victory_for(board, sign):
    win = False
    for col in range(3): # Szukanie kolumny
        if board[0][col] == sign:
            if board[1][col] == sign:
                if board[2][col] == sign:
                    win = True
    for row in range(3): # Szukanie rzedu
        if board[row][0] == sign:
            if board[row][1] == sign:
                if board[row][2] == sign:
                    win = True
    if((board[0][0] == sign) and (board[1][1] == sign) and (board[2][2] == sign) \
       or (board[0][2] == sign) and (board[1][1] == sign) and (board[2][0] == sign)):
        win = True
    return win

#
# Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
#

def draw_move(board):
    #try:
        free_fields = make_list_of_free_fields(board)
        choosen_field = randrange(len(free_fields))
        row = free_fields[choosen_field][0]
        col = free_fields[choosen_field][1]
        board[row][col] = "x"
    #except:
    #    print("Błąd, brak więcej ruchów?")
    #
    # Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.
    #

def draw_win(sign):
    print("\n"*5)
    print("Wygrały ", sign)

def start():
    player1 = "Gracz 1"
    player2 = "Gracz 2"
    board = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
    ] # 0 - none, 1 - x, 2 - o

    print("TicTacToe")
    print("Wybierz tryb:",
    "1: Gracz vs Komputer",
    "2: Gracz vs Gracza", sep="\n")
    mode = int(input())
    if ((mode != 1) and (mode != 2)):
        input("Zły tryb. Wciśnij enter aby zrestartować grę")
        return 1;
    elif mode == 1:
        player2 = "Komputer"
        who_move = player2
    elif mode == 2:
        who_move = player2
    
    print("Pierwszy ruch wykona", who_move,", będzie on miał X. Enter aby zacząć")
    input()
    while True:
        if victory_for(board, "x"):
            draw_win("x")
            break
        elif victory_for(board, "o"):
            draw_win("o")
            break
        if who_move == player2 and player2 == "Komputer":
            draw_move(board)
            #display_board(board)
            who_move = player1
        elif who_move == player2:
            display_board(board)
            enter_move(board, "x")
            who_move = player1
        else:
            display_board(board)
            enter_move(board, "o")
            who_move = player2

while True:
        exit_code = start()
        if exit_code == 0:
            break