
# TicTacToe




# Prints the tictactoe board


def display_board(board):
    
    print(board[1] + '|' +board[2] + '|' + board[3])
    print(board[4] + '|' +board[5] + '|' + board[6])
    print(board[7] + '|' +board[8] + '|' + board[9])

    
 
    pass







# Lets player choose X or O
def player_input():

    """
    OUTPUT = (Player 1 marker, player 2 marker)
    """   
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose X or O: ").upper()

    if marker == 'X':

        return ('X', 'O')

    else:

        return ('O', 'X')



# This function allows the player to choose where on the board they should put X or O
def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    # WIN TIC TAC TOE

    # ALL ROWS, and check to see if they all share the same marker
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[7] == mark and board[8] == mark and board[9] == mark) or # across the bottom
    (board[1] == mark and board[4] == mark and board[7] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
    # ALL COLUMNS, check to see if marker matches
    # 2 diagonals, check to see match


import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'



def space_check(board, position):

   return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
        # Board is fulll if we return True
    return True



def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))

    return position


def replay():

    choice = input('Play again? Enter yes or no')

    return choice == 'Yes'



# WHILE LOOP TO KEEP RUNNING THE GAME

print('Welcome to TIC TAC TOE')

while True:

    # Play the game

    # Set everything up (Board, whos first, choose markers)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    
    turn = choose_first()
    print(turn + ' Will go first')

    play_game = input('Ready to play? y or n?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        

    # GAME PLAY

    while game_on:

        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place marker on position
            place_marker(the_board, player1_marker,position)
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
                     # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place marker on position
            place_marker(the_board, player2_marker,position)
            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie')
                    game_on = False
                else:
                    turn = 'Player 1'
            # or check if there is a tie

            # no tie an no win? next player turn

 




    if not replay():
        break


# BREAK OUT OF THE WHILE LOOP ON replay()
