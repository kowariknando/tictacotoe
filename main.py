# Let's create a tic tac toe game!! :)
import random


print('lets modify something just for testing')

board = [' ' for i in range(10)]
boardtotest = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
boardtotest2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print(board)

def showboard(boa):
    print(boa)
    print('the board looks like: ')
    row1 = [' ', boa[1], ' ', '|', ' ', boa[2], ' ', '|', ' ', boa[3], ' ']
    row2 = [' ', boa[4], ' ', '|', ' ', boa[5], ' ', '|', ' ', boa[6], ' ']
    row3 = [' ', boa[7], ' ', '|', ' ', boa[8], ' ', '|', ' ', boa[9], ' ']
    #linerow = ['-' for i in range(11)]
    linesrow = ['-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-']
    print(''.join(row1))
    print(''.join(linesrow))
    print(''.join(row2))
    print(''.join(linesrow))
    print(''.join(row3))

def win(boa):
    if boa[1]==boa[2]==boa[3] and boa[1]!=' ':
        print('the winner is : ', boa[1])
    if boa[4]==boa[5]==boa[6] and boa[4]!=' ':
        print('the winner is : ', boa[4])
    if boa[7]==boa[8]==boa[9] and boa[7]!=' ':
        print('the winner is : ', boa[7])
    if boa[1]==boa[4]==boa[7] and boa[1]!=' ':
        print('the winner is : ', boa[1])
    if boa[2]==boa[5]==boa[8] and boa[2]!=' ':
        print('the winner is : ', boa[2])
    if boa[3]==boa[6]==boa[9] and boa[3]!=' ':
        print('the winner is : ', boa[3])
    if boa[1]==boa[5]==boa[9] and boa[1]!=' ':
        print('the winner is : ', boa[1])
    if boa[3]==boa[5]==boa[7] and boa[3]!=' ':
        print('the winner is : ', boa[3])

def playermove(boa):
    while True:
        try:
            playermove = int(input('please enter your move'))
            if 0 < playermove < 10:
                print('your movement is correct!')
                if boa[playermove] == ' ':
                    boa[playermove] = 'x'
                else:
                    print('Move not allowed, there is a: ', boa[playermove], ' on this place')
                    continue
                break
            else:
                print('Please enter an integer BETWEEN 1 and 9')
                continue
        except ValueError:
            print("Please input INTEGER between 1 and 9: ")
            continue
    print('the player move is: ', playermove)
    return boa

def compmove(boa):
    occupied = ['x', '0']
    #first round, cheking if the center is empty, if so move there.
    if boa[5] == ' ':
        boa[5] = '0'   #computer will try first to put in the center
    else: #check if player can win or computer can win
        if (boa[2] in occupied and boa[3] in occupied) or (boa[4] in occupied and boa[7] in occupied) or (boa[5] in occupied and boa[9] in occupied):
            boa[1] ='0'
            print('NUEVO CERO EN EL 1') #Todo borrame
'''            
        if (boa[1] != ' ' and boa[3] != ' ') or (boa[5] != ' ' and boa[8] != ' '):
            boa[2] = '0'
        if (boa[1] != ' ' and boa[2] != ' ') or (boa[6] != ' ' and boa[9] != ' ') or (boa[5] != ' ' and boa[7] != ' '):
            boa[3] ='0'
'''
'''        
    elif boa[5] == 'x':
        computermove = int(random.choice(["1", "3", "7", '9'])) #if not in the center computer will try in any of the corners
        boa[computermove] == '0'
    #second round
    elif boa[5] == '0':

'''



showboard(boardtotest2)
win(boardtotest2)
newboardTEST = playermove(boardtotest2)
win(boardtotest2)
compmove(boardtotest2)
#newboardTEST = playermove(boardtotest2)
#showboard(newboardTEST)
#win(newboardTEST)

print(boardtotest2.index('x'))