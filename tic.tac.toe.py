import string
from random import randint
board=[0,'',' ','','',' ','',' ','',' ']
def display_board(board):
    print('   |       |   ')
    print(f'{board[1]}  |   {board[2]}   | {board[3]} ')
    print('   |       |   ')
    print('--------------')
    print('   |       |   ')
    print(f'{board[4]}  |   {board[5]}   | {board[6]} ')    
    print('   |       |   ')
    print('--------------')
    print('   |       |   ')    
    print(f'{board[7]}  |   {board[8]}   | {board[9]} ')  
    print('   |       |   ')  




def player_input():
    while True:
        a=input('enter a number between 1 and 9 : ')
        if a.isdigit():
            if int(a) in range(1,10):
                return int(a)
            else:
                print('enter a number that is between 1 and 9 !')
                continue

        else:
            print('please enter number! ')
            continue
     


def marker():
    while True:
        b=input('do you want to be x or o ? ').lower()
        if b=='x' or b=='o':
            return b.lower()
        else:
            print('enter x or o ')
    
            


def place_marker(board , marker , position):
        board[position]=marker
        return board

def win_check(board):
    if board[1]=='o' and board[2]=='o' and board[3] =='o':
        return True
    elif board[4]=='o' and board[5]=='o' and board[6] =='o':
        return True
    elif board[7]=='o' and board[8]=='o'and board[9] =='o':
        return True
    elif board[1] =='o'and board[4]=='o' and board[7] =='o':
        return True
    elif board[2]=='o' and board[5]=='o' and board[8] =='o':
        return True
    elif board[3]=='o' and board[6] =='o'and board[9] =='o':
        return True
    elif board[1]=='o' and board[5] =='o'and board[9] =='o':
        return True
    elif board[3]=='o' and board[5]=='o' and board[7] =='o':
        return True
    elif board[1]=='x' and board[2]=='x' and board[3] =='x':
        return True
    elif board[4] =='x'and board[5]=='x' and board[6] =='x':
        return True
    elif board[7] =='x'and board[8] =='x'and board[9] =='x':
        return True
    elif board[1] =='x'and board[4]=='x' and board[7] =='x':
        return True
    elif board[2]=='x' and board[5] =='x'and board[8] =='x':
        return True
    elif board[3] =='x'and board[6] =='x'and board[9] =='x':
        return True
    elif board[1]=='x' and board[5] =='x'and board[9] =='x':
        return True
    elif board[3]=='x' and board[5]=='x' and board[7] =='x':
        return True
    else :
        return False


def choose_first():
    c=randint(1,2)
    if c == 1 :
        return True
    else :
        return False


def space_chekck_x_o(board , position):
    if board[position]==' ':
        return True



def full_board_check(board):
    sum=0
    for i in range (1,10):
        if board[i]!=' ':
            sum+=1
        else:
            pass
    if sum==9:
        return True
    else:
        return False

def countinue():
    while True :
        d=input('do you want to continue (y/n)? ').lower()
        if d =='y' :
            print('OK !')
            break
        elif d=='n' :
            print('BYE ! ')
            break
        else :
            print('pleas anwser with y/n ')
            continue
    if d=='n':
        return False



while True:
    board = [' '] * 10
    pp = input('enter the first players name: ')
    pp2 = input('enter second players name: ')
    turn = pp if choose_first() else pp2
    print(f"{turn} starts!")
    player1_marker = marker()  
    player2_marker = 'o' if player1_marker == 'x' else 'x'
    while True:
        display_board(board)
        current_marker = player1_marker if turn == pp else player2_marker
        while True:
            pos = player_input()
            if space_chekck_x_o(board, pos):
                break
            else:
                print("You cannot put it there!")

        place_marker(board, current_marker, pos)

        if win_check(board) or full_board_check(board):
            display_board(board)
            print(f"{turn} wins!" if win_check(board) else "Tie!")
            break
        turn = pp if turn == pp2 else pp2
    if countinue() == False:
        break
