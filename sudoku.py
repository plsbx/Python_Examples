set1 = """295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""

set2 = """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""

def sudoku(set):
    set = set.replace("\n", "")
    #Sprawdzenie rzędów
    for row in range(9):
        row_pass = False
        for number in range(9):
            row_pass = set.find(chr(number+49), row*9, row*9+9)
            #print("Debug: ", row, number, chr(number+49), row_pass, set[row*9:row*9+9])
            if row_pass < 0:
                return False
    for col in range(9):
        col_pass = False
        for number in range(9):
            col_pass = set.find(chr(number+49), col, col+81)
            if row_pass <= 0:
                return False
    #Sprawdzanie kwadratów
    #0 3 6
    #27 30 33
    #54 57 60
    for square_sel in range(9):
        shift = 0
        if square_sel >= 3:
            shift = 1
        elif square_sel >= 6:
            shift = 2
        if square_sel == 0 or square_sel == 3 or square_sel == 6:
            square = 0
        elif square_sel == 1 or square_sel == 4 or square_sel == 7:
            square = 1
        elif square_sel == 2 or square_sel == 5 or square_sel == 8:
            square = 2
        sqrt_start = 3*square + 27*shift
        sqrt_stop = sqrt_start+3
        square_str = set[sqrt_start:sqrt_stop] + set[sqrt_start+9:sqrt_stop+9] + set[sqrt_start+18:sqrt_stop+18]
        for number in range(9):
            square_pass = square_str.find(chr(number+49))
            if square_pass < 0:
                #print("Debug: ", square, number, chr(number+49), sqrt_start, square_str)
                return False

    return True
#--------------------------------

print(sudoku(set1))
print(sudoku(set2))
