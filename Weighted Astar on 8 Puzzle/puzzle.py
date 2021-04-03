#from queue import Queue
from copy import deepcopy
from random import randint

class EightPuzzle:
    def __init__(self,start,goal,zero=(0,0)):
        self.size=3
        self.puzzle=start
        self.goal=goal 
        self.zero=zero #position of 0 (or the empty space)
        #directions permissible for movement
        self.moves=["U","D","L","R"] #up, down, left, right 
        count=1


    #check whether goal reached 
    def checkPuzzle(self):
        count=1
        n=self.size
        for i in range(0,n):
            for j in range(0,n):
                if self.puzzle[i][j]!=self.goal[i][j]:
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

    

class Node:
    def __init__(self, puzzle, w=0, parent=None, move=""):
        self.state = puzzle #EightPuzzle object
        self.parent = parent
        self.fp=0 
        self.f=0
        self.g=0
        self.h=0
        self.w=w
        self.depth=0
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
        succs = []  
        for m in self.state.moves: #try moving every possible direction
            p = deepcopy(self.state)
            p.doMove(m)
            #keep adding new nodes where the position of zero is different
            #from the current one and set the new node's parent
            if p.zero is not self.state.zero:
                succs.append(Node(p, self.w, self, m))
        #return all the nodes expanded till now
        return succs
    
    def calculate_h(self):
        h_value = 0
        for i in range(self.state.size):
            for j in range(self.state.size):
                if self.state.goal[i][j] != 0 and self.state.puzzle[i][j] != self.state.goal[i][j]:
                    for k,v in enumerate(self.state.puzzle):
                        if self.state.goal[i][j] in v:
                            a = i #row
                            b = v.index(self.state.goal[i][j])
                            h_value += abs(a - i) + abs(b - j) #manhattan distance
                            print("h: ", h_value, "+=",a,"-",i," + ", b, "-", j)
        self.h = h_value

    def calculate_g(self):
        # g value
        parent = self.parent
        self.g = parent.g + 1

    def calculate_f(self):
        # f value
        self.fp = self.g + self.w * self.h  #weight mutliplied
        self.f = self.g + self.h

    def calculate_costs(self):
        self.calculate_h()
        self.calculate_g()
        self.calculate_f()


    def goalState(self):
        return self.state.checkPuzzle()

