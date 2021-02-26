from queue import Queue
from copy import deepcopy
from random import randint

class EightPuzzle:
    def __init__(self,size):
        self.size=size #size of board
        self.puzzle=[] 
        self.zero=(0,0) #position of 0 (or the empty space)
        #directions permissible for movement
        self.moves=["U","D","L","R"] #up, down, left, right 
        count=1
        
        #creating the board
        for i in range(0,size):
            self.puzzle.append([])
            #filling every position like
            # 1 2 3
            # 4 5 6
            # 7 8 9
            for j in range(0,size):
                self.puzzle[i].append(count)
                count+=1
                
        self.puzzle[size-1][size-1]=0 #setting the bottom-right-corner to 0
        # The puzzle now :
        # 1 2 3
        # 4 5 6
        # 7 8 0
        self.zero=(size-1,size-1)

    #check whether goal reached 
    def checkPuzzle(self):
        count=1
        n=self.size
        for i in range(0,n):
            for j in range(0,n):
                if self.puzzle[i][j]!=(count%(n*n)):
                    return False
                count+=1
        return True

    
    def swap(self,first,second):
        x1, y1 = first
        x2, y2 = second
        temp=self.puzzle[x1][y1]
        self.puzzle[x1][y1]=self.puzzle[x2][y2]
        self.puzzle[x2][y2]=temp

    #defining the moves
    def up(self):
        if (self.zero[0]!=0):
            self.swap((self.zero[0]-1,self.zero[1]),self.zero)
            self.zero=(self.zero[0]-1,self.zero[1])
    def down(self):
        if (self.zero[0]!=self.size-1):
            self.swap((self.zero[0]+1,self.zero[1]),self.zero)
            self.zero=(self.zero[0]+1,self.zero[1])

    def left(self):
        if (self.zero[1]!=0):
            self.swap((self.zero[0],self.zero[1]-1),self.zero)
            self.zero=(self.zero[0],self.zero[1]-1)


    def right(self):
        if (self.zero[1]!=self.size-1):
            self.swap((self.zero[0],self.zero[1]+1),self.zero)
            self.zero=(self.zero[0],self.zero[1]+1)

    
    def printPuzzle(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                print(self.puzzle[i][j], end=" ")
            print("\n")
        print("\n")
            

    def doMove(self,move):
        if move=="U":
            self.up()
        if move=="D":
            self.down()
        if move=="L":
            self.left()
        if move=="R":
            self.right()
    
    def createStates(self,num):
        for i in range(0,num):
            #randomly choose one of the four moves
            self.doMove(self.moves[randint(0,3)]) 
    
    

class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle #EightPuzzle object
        self.parent = parent
        self.depth = 0
        if parent is None: #root node
            self.depth = 0
            self.moves = move 
        else:
            self.depth = parent.depth+1
            self.moves = parent.moves + move

    def printBoard(self, puzzle):
        op = deepcopy(puzzle.state)
        op.printPuzzle()

    def successor(self):
        succs = Queue()
        for m in self.state.moves: #try moving every possible direction
            p = deepcopy(self.state)
            p.doMove(m)
            #keep adding new nodes where the position of zero is different
            #from the current one and set the new node's parent
            if p.zero is not self.state.zero:
                succs.put(Node(p, self, m))
        #return all the nodes expanded till now
        return succs

    def goalState(self):
        return self.state.checkPuzzle()

