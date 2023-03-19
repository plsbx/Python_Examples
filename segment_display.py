number_str = input("Podaj cyfrę: ")
number = int(number_str)
number_lst = list(number_str)
number_len = len(number_str)

char = '#'

nbrs = '''  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ### '''
            
print_string = "";

def getString(n, i): # This function is used to extract smaller strings from "nbrs"
    shift = 41
    if n == 0:
        n = 10
    #nbrs[n+(4*(n-1)):n+(4*(n-1))+4] # 1 - 0 to 3, 2 - 5 to 7, 3 - 9 to 11
    n -= 1
    start = n       + (n*3) + shift*i
    stop = n + 4    + (n*3) + shift*i
    string = nbrs[start:stop]
    #print(n, i, start, stop, string) just debugging
    return string



print_string = ""
for k in range(5): # It is for line selection
    for i in range(number_len): # It is for number selection
        print_string += getString(int(number_lst[i]), k) # It is for extraction special string
    print_string += '\n' # End line

print(print_string)