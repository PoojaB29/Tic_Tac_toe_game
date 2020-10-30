#global variables
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

#if game is still going 
game_still_going = True

#who won or tie
winner = None

#whose turn is it
current_player ='X'

#display board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def play_game():
    #display initial board
    display_board()

    while game_still_going:
        
        #handle a single turn of an arbitrary player 
        handle_turn(current_player)

        #check if the game has ended 
        check_if_game_over()

        #flip to other player 
        flip_player()

    #The game has ended 
    if winner == "X" or winner =="O":
        print(winner +' won.')
    elif winner == None:
        print('Tie.')

def handle_turn(player):

    print(player + "'s turn.")
    position = input('Choose a position from 1-9: ')
    valid = False
    while  not valid:
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Choose a position from 1-9: ')

        position = int(position)-1

        if board[position] == '-':
            valid = True
        else:
            print('You cant go there. Go again.')
    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner 
    #check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else :
        winner = None
    return

def check_rows():
    global game_still_going
    #check if any of the rows have all the same value
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():
    global game_still_going
    #check if any of the rows have all the same value
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'

    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    #check if any of the rows have all the same value
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2 :
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player =='X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return 


play_game()