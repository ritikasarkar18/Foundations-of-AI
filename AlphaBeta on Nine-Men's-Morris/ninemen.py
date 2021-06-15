from minmax import *
from alphabeta import *
from heuristics import *

max = float('-inf')
min = float('inf')
d = 3 #depth

class Board:
    def __init__(self,b=[],p=0):
        self.board = b
        self.pos = p
        # board initialisation
        if (not self.board):
            for i in range(24):
                self.board.append("x")
        
        
    
    #play
    def play(self, heuristic_stage1, heuristic_stage23,choice):
        for i in range(9):
            print("\n---Placing piece: ",i)
            fin = False
            while not fin:
                try:
                    self.pos = int(input("Enter Position to place 1st player's piece: "))
                    if (self.board[self.pos]=="x"):
                        self.board[self.pos] = '1' #placed if position blank
                        bcopy = deepcopy(self.board)
                        bpos = deepcopy(self.pos)
                        print("Checking Mill Formed")
                        if (isMill(bpos,bcopy)): #does it form a mill
                            print("Mill formed!")
                            self.remove('2')
                            print("Removed Piece 2")
                    
                        fin = True #player 1 finished placing
                    else:
                        print("Cannot place piece for player 1, position already occupied") 

                except Exception as e:
                    print(e)
            print("---Board after placing piece of player1 - user---")
            self.printboard()
            
            #minmax
            #print("Starting MinMax")

            self.evaluate(True,heuristic_stage1,choice)
            print("++Board after placing piece of player2 - program++")
            self.printboard()

        self.move(False,heuristic_stage23,choice)

    def move(self, fin, heuristic_stage23,choice):
        endfin = fin
        while not endfin:
            print("---Board before moving---")
            self.printboard()
            moved = False
            while not moved:
                try:
                    self.pos = int(input("Enter Position of player 1 piece to move: "))
                    while(self.board[self.pos]!='1'):
                        self.pos = int(input("Enter \"correct\" Position of player 1 piece to move: "))
                    placed = False
                    while not placed: 
                        newp = int(input("Enter Position to move player 1 piece to: "))
                        if self.board[newp] == 'x':
                            self.board[self.pos] = 'x'
                            self.board[newp] = '1'
                            self.pos = newp
                            bcopy = deepcopy(self.board)
                            bpos = deepcopy(self.pos)
                            if isMill(bpos,bcopy):
                                print("Mill formed!")
                                self.remove('2')
                            
                            placed = True
                            moved = True
                            print("Moved player 1 piece")
                        else:
                            print("Position occupied, can't move there")
                
                except Exception:
                    print("Invalid position")
        
            ##winning condition
            if self.getEvaluationStage23() == float('inf'):
                print("You Win!")
                exit(0)

            #print("Starting Minmax")

            #minmax
            self.evaluate(False,heuristic_stage23,choice) 
            print("++Board after moving piece of player2 - program++")
            self.printboard()



    def evaluate(self,isStage1,heuristic,choice): 
        bcopy = deepcopy(self.board)
        if choice==1:
            ev = minmax(bcopy,d,False,max,min,isStage1,heuristic)
        else:
            ev = alphabeta(bcopy,d,False,max,min,isStage1,heuristic)
        if ev.eval == float('-inf'):
            print('You Lost')
            exit(0)
        else:
            self.board = ev.board



    def getEvaluationStage23(self): 
        numWhite = self.board.count("1")
        numBlack = self.board.count("2")
        mills = getPossibleMillCount(self.board, "1")

        evaluation = 0

        board_list = stage23Moves(self.board)

        numBlackMoves = len(board_list)

        if numBlack <= 2 or numBlack == 0:
            return float('inf')
        elif numWhite <= 2:
            return float('-inf')
        else:
            return 0


    

    def remove(self,player):
        placed = False # to remove other player's piece
        while not placed:
            try:
                self.pos = int(input("Enter Position to remove 2nd player's piece: "))
                # check whether position occupied by other player and does not form a mill, or it forms a mill
                bcopy = deepcopy(self.board)
                bpos = deepcopy(self.pos)
                if self.board[self.pos] == player and not isMill(bpos,bcopy) or (isMill(bpos,bcopy) and bcopy.count("1")>=3):
                    self.board[self.pos] = "x" #removed
                    placed = True
                else:
                    print("Invalid choice of position")

            except Exception:
                print("Input not valid")




    def printboard(self):
        print()

        print(self.board[0]+"(00)----------------------"+self.board[1]+"(01)----------------------"+self.board[2]+"(02)")
        print("|                           |                           |")
        print("|       "+self.board[8]+"(08)--------------"+self.board[9]+"(09)--------------"+self.board[10]+"(10)     |")
        print("|       |                   |                    |      |")
        print("|       |                   |                    |      |")
        print("|       |        "+self.board[16]+"(16)-----"+self.board[17]+"(17)-----"+self.board[18]+"(18)       |      |")
        print("|       |         |                   |          |      |")
        print("|       |         |                   |          |      |")
        print(self.board[3]+"(03)---"+self.board[11]+"(11)----"+self.board[19]+"(19)               "+self.board[20]+"(20)----"+self.board[12]+"(12)---"+self.board[4]+"(04)")
        print("|       |         |                   |          |      |")
        print("|       |         |                   |          |      |")
        print("|       |        "+self.board[21]+"(21)-----"+self.board[22]+"(22)-----"+self.board[23]+"(23)       |      |")
        print("|       |                   |                    |      |")
        print("|       |                   |                    |      |")
        print("|       "+self.board[13]+"(13)--------------"+self.board[14]+"(14)--------------"+self.board[15]+"(15)     |")
        print("|                           |                           |")
        print("|                           |                           |")
        print(self.board[5]+"(05)----------------------"+self.board[6]+"(06)----------------------"+self.board[7]+"(07)")

        print()

