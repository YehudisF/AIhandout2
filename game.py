import copy
import math
import random
VIC = 2**10 # The value of a winning board (for max)
LOSS = -VIC # The value of a losing board (for max)
TIE = None # The value of a tie
SIZE = 8 # The length of a winning sequence
#COMPUTER=SIZE+1 # Marks the computer's cells on the board
COMPUTER = 2 # Marks the computer's cells on the board
HUMAN = 1 # Marks the human's cells on the board

'''
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
   the comp's cells = COMPUTER and the human's = HUMAN
1. The heuristic value of the state.
2. Who's turn is it: HUMAN or COMPUTER
3. number of empty cells
'''
def create():
#Returns an empty board. The human plays first.
    # board = []
    # for i in range(8):
    #      board = board + [8 * [0]]
    # print(board)
    # return [board, 0.00001, HUMAN, 9]
    # creates an 8*8 board with random numbers between -20 to 20
    #board = [['', '', 1, 2, 3, 4, 5, 6, 7, 8], [' ' for i in range(10)], [int(random.randint(-20, 21)) for i in range(8)] for j in range(8)]
    board = [[int(random.randint(-20, 21)) for i in range(8)] for j in range(8)]
    # for i in range(8):
    #     board[i].insert(0, ' ')
    #     board[i].insert(0, i+1)
    # board.insert(0, [' ' for i in range(10)])
    # board.insert(0, [' ', ' ', 1, 2, 3, 4, 5, 6, 7, 8])
    # print(listush)
    #
    #print(board)
    # returns beginning state- each state is[the board, humans score, computers score, the next row/column, who's next]
    return [board, 0.0, 0.0, int(random.randint(0, 9)), HUMAN, 0]





def printState(s):
#Prints the board. The empty cells are printed as numbers = the cells name(for input)
#If the game ended prints who won.
    # for r in range(len(s[0])):
    #     print("\n -- -- --\n|", end="")
    #     for c in range(len(s[0][0])):
    #         if s[0][r][c]==COMPUTER:
    #             print("X |", end="")
    #         elif s[0][r][c]==HUMAN:
    #             print("O |", end="")
    #         else:
    #             print(r*3+c,"|", end="")

    print('{:>2} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} \n'.format(*['', 1, 2, 3, 4, 5, 6, 7, 8]))

    for i in s[0]:
        print('{}  {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} '.format(s[0].index(i)+1, *i))
        #print(*i)
    print("\n -- -- --\n Human score:{}\t Computer score:{}\n".format(s[1], s[2]))
    if isFinished(s):
        if s[2] > s[1]:
            print("Ha ha ha I won!")
        elif s[2] < s[1]:
            print("You did it!")
        else:
            print("It's a TIE")

def isFinished(s):
#Returns True if the game ended
   # return s[1] in [LOSS, VIC, TIE]

  # for i in s[0]:
    if s[4] == HUMAN:
        if any(s[0][s[3]]):
            return False
    else:
        for row in s[0]:
            if row[s[3]]:
                return False
    return True

def value(s):
#Returns the heuristic value of s
    if isFinished(s):
        if s[2] > s[1]:
            return math.pow(2, 10)
        elif s[2] < s[1]:
            return -math.pow(2, 10)
        else:
            return None
    else:
        return s[2] - s[1]



def isHumTurn(s):
#Returns True if it the human's turn to play
    return s[4]==HUMAN

def whoIsFirst(s):
#The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you. : ")) == 1:
        s[4] = COMPUTER
    else:
        s[4] == HUMAN

def checkSeq(s,r1,c1,r2,c2):
# r1, c1 are in the board. if r2,c2 not on board returns 0.
# Checks the seq. from r1,c1 to r2,c2. If all X returns VIC. If all O returns LOSS.
# If no Os (and at least 1 X) returns 1.
# If no Xs (and at least 1 O) returns -1, Othewise returns 0.
    if r2<0 or c2<0 or r2>=len(s[0]) or c2>=len(s[0][0]):
        return 0 #r2, c2 are illegal
    dr=(r2-r1)//(SIZE-1) #the vertical step from cell to cell
    dc=(c2-c1)//(SIZE-1) #the horizontal step from cell to cell
    sum=0
    for i in range(SIZE):#summing the values in the seq.
        sum+=s[0][r1+i*dr][c1+i*dc]
    if sum==COMPUTER*SIZE:
        return VIC
    if sum==HUMAN*SIZE:
        return LOSS
    if sum>0 and sum<COMPUTER:
        return -1
    if sum>0 and sum%COMPUTER==0:
        return 1
    return 0

def makeMove(s,r,c):
# Puts mark (for huma. or comp.) in r,c
# switches turns
# and re-evaluates the heuristic value.
# Assumes the move is legal.
    s[s[4]] += s[0][r][c]  # adds value from tile to current player
    s[0][r][c] = None  # marks the board
    if s[4] == HUMAN:
        s[3] = c
    else:
        s[3] = r
    #s[3] -= 1  # one less empty cell
    s[2]=COMPUTER+HUMAN-s[2] # switches turns
    # dr=[-SIZE+1, -SIZE+1, 0, SIZE-1] # the next lines compute the heuristic val.
    # dc=[0, SIZE-1, SIZE-1, SIZE-1]
    # s[1]=0.00001 # to distinguish from TIE, which is 0
    # for row in range(len(s[0])):
    #     for col in range(len(s[0][0])):
    #         for i in range(len(dr)):
    #             t=checkSeq(s,row,col,row+dr[i],col+dc[i])
    #             if t in [LOSS,VIC]:
    #                 s[1]=t
    #                 return
    #             else:
    #                 s[1]+=t
    # if s[3]==0:
    #     s[1]=TIE
    s[5] = value(s)

    
   
def inputMove(s):
# Reads, enforces legality and executes the user's move.
    printState(s)
    flag=True
    while flag:
        c=int(input("Enter column choice in row {}".format(s[3])))-1
        r=s[3]
        if c<0 or c>=SIZE-1  or s[0][r][c]==None:
            print("Ilegal move reenter please.")
        else:
            flag=False
            makeMove(s,r,c)
        
def getNext(s):
# returns a list of the next states of s
    ns=[]
    forced = s[3]
    if s[4] == HUMAN:
        for choice in range(SIZE):
            if s[0][forced][choice]!=None:
                tmp=copy.deepcopy(s)
                makeMove(tmp,forced,choice)
                ns+=[tmp]
    else:
        for choice in range(SIZE):
            if s[0][choice][forced] != None:
                tmp = copy.deepcopy(s)
                makeMove(tmp, choice, forced)
                ns += [tmp]
    return ns
    
#print(isFinished(create()))
#create()
printState(create())