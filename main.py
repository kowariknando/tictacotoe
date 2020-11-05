# Let's create a tic tac toe game!! :)
import random

def showboard(boa):
    #print(boa) #todo borrame esto es solo para test
    #print('the board looks like: ')
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
        #print('the winner is : ', boa[1])
        return False
    if boa[4]==boa[5]==boa[6] and boa[4]!=' ':
        #print('the winner is : ', boa[4])
        return False
    if boa[7]==boa[8]==boa[9] and boa[7]!=' ':
        #print('the winner is : ', boa[7])
        return False
    if boa[1]==boa[4]==boa[7] and boa[1]!=' ':
        #print('the winner is : ', boa[1])
        return False
    if boa[2]==boa[5]==boa[8] and boa[2]!=' ':
        #print('the winner is : ', boa[2])
        return False
    if boa[3]==boa[6]==boa[9] and boa[3]!=' ':
        #print('the winner is : ', boa[3])
        return False
    if boa[1]==boa[5]==boa[9] and boa[1]!=' ':
        #print('the winner is : ', boa[1])
        return False
    if boa[3]==boa[5]==boa[7] and boa[3]!=' ':
        #print('the winner is : ', boa[3])
        return False
    return True
def boardisfull(boa):
    if boa.count(' ') > 1:
        return True
    else:
        print('the board is full, TIE GAME!!')
        return False
def playermove(boa):
    while True:
        try:
            playermove = int(input('please enter your move'))
            if 0 < playermove < 10:
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
    return boa
def player2move(boa):
    while True:
        try:
            playermove = int(input('please enter your move'))
            if 0 < playermove < 10:
                if boa[playermove] == ' ':
                    boa[playermove] = '0'
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
    return boa
def compMoveAvailable(boa, pos):
    if boa[pos] == ' ':
        return True
    else:
        False
def compmove(boa):
    #computer will try first to put in the center boa[5] if it is free
    if compMoveAvailable(boa, 5) == True:
        boa[5] = '0'
        print('Computer placed a 0 in the position 5 :')
        return boa
    #computer will check if any positibility that with a move the computer or the player can win.
    availables =[]
    for compmoves in ['1', '2', '3', '4', '6', '7', '8', '9']:
        if compMoveAvailable(boa, int(compmoves)) == True:
            availables.append(compmoves)
    for compmoves in availables:
        boa[int(compmoves)] = '0' #computer is checking if they can win moving to any of the available places
        if win(boa) == False:
            print('Computer placed a 0 in the position: ', int(compmoves))
            return boa
        boa[int(compmoves)] = 'x' #computer is checking if player can win moving to any of the available places
        if win(boa) == False:
            boa[int(compmoves)] = '0'
            print('Computer placed a 0 in the position: ', int(compmoves))
            return boa
        boa[int(compmoves)] = ' '  #if no possibility they 'clean' the space letting it empty and it continues executing the script
    #now computer check if the corners are free
    cornersfree = []
    for compmoves in ['1', '3', '7', '9']:
        if compMoveAvailable(boa, int(compmoves)) == True:  #if any of the corners are free they store it on cornersfree[]
             cornersfree.append(compmoves)
    if len(cornersfree) > 0: #if there are more than 0 corners free then computer choose one random corner and move there
        computermove = random.choice(cornersfree)
        boa[int(computermove)] = '0'
        print('Computer placed a 0 in the position: ', int(computermove))
        return boa
    #now computer check if there are any middle possitions free
    centersfree = []
    for compmoves in ['2', '4', '6', '8']: #like with the corners above it check if there are any available free middle possition
        if compMoveAvailable(boa, int(compmoves)) == True:
            centersfree.append(compmoves)
    if len(centersfree) > 0: #It stores on centersfree the free centers positions and it choose one randomly
        computermove = random.choice(centersfree)
        boa[int(computermove)] = '0'
        print('Computer placed a 0 in the position: ', int(computermove))
        return boa

board = [' ' for i in range(10)]  #creating the main board empty
boardtotest = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#boardtotest2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']



print('Welcome to TicTacoToe, the game is very simple')
showboard(boardtotest)
print('you have to select a position to place an X or an 0 from 1-9 and if you connect 3 you will be the winner')
print('You can play with a friend of versus the computer')
numberofplayers = 0
showboard(board)
#asking if you want to play VS the computer or with 2 players
while True:
    try:
        answer = int(input('please enter 1 to play versus the computer or 2 to play with a friend'))
        if (answer == 1) or (answer == 2):
            numberofplayers= answer
            break
        else:
            print('Please enter 1 or 2')
            continue
    except ValueError:
        print("Please 1 or 2: ")
    continue

#this is to play versus the computer
if numberofplayers == 1:
    print('Great you will play versus the computer, good luck!!')
    while True:
        ronda1p = playermove(board)
        if win(ronda1p) == False:
            print('Congratulations you are the winer!')
            break
        if boardisfull(ronda1p) == False:
            break
        showboard(ronda1p)
        ronda1comp = compmove(ronda1p)
        if win(ronda1comp) == False:
            print('oooh sorry, you loose!')
            break
        showboard(ronda1comp)
        board = ronda1comp
        continue
    print('the game is over')
    showboard(board)
#this is to play versus other player
if numberofplayers == 2:
    player1 = input('Please enter the name of the player 1: ')
    player2 = input('Please enter the name of the player 2: ')
    while True:
        print(player1, ', it s your turn')
        ronda1p = playermove(board)
        if win(ronda1p) == False:
            print('Congratulations ', player1, ' you are the winer!')
            break
        if boardisfull(ronda1p) == False:
            break
        showboard(ronda1p)
        print(player2, ', it s your turn')
        ronda1comp = player2move(ronda1p)
        if win(ronda1comp) == False:
            print('Congratulations ', player2, ' you are the winer!')
            break
        showboard(ronda1comp)
        board = ronda1comp
        continue
    print('the game is over')
    showboard(board)




input('press enter to finish')


