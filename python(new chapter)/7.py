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
    try:
            a=int(input('enter a number between 1 and 9 :  '))
    except:
            print('enter a number !! ')
    else :
            while True:
                if int(a) in range(1,10):
                    return int(a)
                else:
                    print('enter a number in range 1 , 10') 
                    break


def marker():
    while True:
        b=input('do you want to be x or o ? ')
        if b=='x' or b=='o':
            return b
        else:
            print('enter x or o ')
    
            


def place_marker(board , marker , position):
        board[position]=marker
        return board
# print(place_marker(board,marker(),player_input()))

def win_check(board):
    if board[1] and board[2] and board[3] =='o':
        return True
    elif board[4] and board[5] and board[6] =='o':
        return True
    elif board[7] and board[8] and board[9] =='o':
        return True
    elif board[1] and board[4] and board[7] =='o':
        return True
    elif board[2] and board[5] and board[8] =='o':
        return True
    elif board[3] and board[6] and board[9] =='o':
        return True
    elif board[1] and board[5] and board[9] =='o':
        return True
    elif board[3] and board[5] and board[7] =='o':
        return True
    elif board[1] and board[2] and board[3] =='x':
        return True
    elif board[4] and board[5] and board[6] =='x':
        return True
    elif board[7] and board[8] and board[9] =='x':
        return True
    elif board[1] and board[4] and board[7] =='x':
        return True
    elif board[2] and board[5] and board[8] =='x':
        return True
    elif board[3] and board[6] and board[9] =='x':
        return True
    elif board[1] and board[5] and board[9] =='x':
        return True
    elif board[3] and board[5] and board[7] =='x':
        return True
    else :
        return False


def choose_first():
    c=randint(1,2)
    if c == 1 :
        return True
    else :
        return False


def space_chekck_x(board , position):
    if board[position]=='o':
        return False
    else:
        return True


def space_chekck_o(board , position):
    if board[position]=='x':
        return False
    else:
        return True
# space_chekck_x(board,player_input())


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
    board=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
    pp=input('enter the first players name: ')
    pp2=input('enter second players name: ')
    while True:
        if choose_first()==True:
            print(f'{pp} starts! ')
        else:
            print(f'{pp2} starts! ')
        while True:
            display_board(board)
            marker()
            # player_input() #position
            while True:
                player_input() #position
                if marker()=='x' and space_chekck_x(board,player_input())==True:
                    print('you cant put it there ')
                    continue
                elif marker()=='o' and space_chekck_o(board,player_input())==True:
                    print('you cant put it there ')
                    continue
                else:
                    break
            place_marker(board,marker(),player_input())
            if win_check(board)==True or full_board_check(board)==True:
                break
        break
    countinue()
    if countinue()==False:
        break