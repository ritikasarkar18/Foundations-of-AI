import copy

class State:  #Represents an NxN board instance
    def __init__(self, d, board):
        self.queen_count = 0
        self.d = d  #Next column to insert queen [1:n]
        self.board = board


    def _goal_check(self):
        #Number of queens should be the same as k
        if self.queen_count != k:
            return False
        return True

    def is_square_safe(self, r, c):
        x = [-1, 1,  0, 0, 1,  1, -1, -1]
        y = [ 0, 0, -1, 1, 1, -1,  1, -1]

        for k in range(0, 8): #Check all 8 directions from current coordinates
            i=1
            try:
                while True:
                    if self.board[r+i*x[k]][c+i*y[k]] == 1: #if queen
                        return False
                    if self.board[r+i*x[k]][c+i*y[k]] == 2: #if obstacle
                        break
                    i+=1
            except IndexError as e:
                pass

        return True  #when no obstacle or queen


class Node:
    def __init__(self, d, board, parent=None):
        self.state = State(d=d, board=board) #create a state object and initialize state using constructor
        self.parent = parent


    #Check if current state is the goal state
    def is_goal(self):
        return self.state._goal_check()


def printer(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print("\n")
    return



def BFS(board,n,k,node):
    queue = []
    visited = []
    queue.append(node)
    
    while True:
        if len(queue) == 0:
                return False
                exit()
        node = queue.pop(0)
        visited.append(node)
        
        while node.state.d < ((int(k/n)+1)* n): #for accommodating number of queens more or less than the size of board
            
            c = node.state.d%n  #column to place queen
            for r in range(n):
                if (node.state.board[r][c] != 0 or not node.state.is_square_safe(r,c)) : #not free slot or danger ahead
                    continue

                #Create a child Node
                child = copy.deepcopy(node) #create a mutable copy of the object
                child.state.board[r][c] = 1 #place queen
                child.state.queen_count = node.state.queen_count + 1 
                child.state.d = node.state.d + 1 #next position to place
                child.parent = node
                
                if child.is_goal(): #when all queens are placed
                    printer(child.state.board,n)
                    exit()
                else:
                    queue.append(child)
            
            node.state.d += 1 #next position
            
        
    
    


        
def DFS(board,n,k,node):
    while node.state.d < ((int(k/n)+1)* n): #for accommodating number of queens more or less than the size of board
        c = node.state.d%n  #column to place queen
        for r in range(n):
            if node.state.board[r][c] != 0 or not node.state.is_square_safe(r,c): #not free slot or danger ahead
                continue
            
            #Create a child Node
            child = copy.deepcopy(node) #create a mutable copy of the object
            child.state.board[r][c] = 1  #place queen
            child.state.queen_count = node.state.queen_count + 1 
            child.state.d = (node.state.d + 1) # next position to place
            child.parent = node 

            if child.is_goal(): #when all queens are placed
                 printer(child.state.board,n)
                 exit()
                 
            else:
                 DFS(board,n,k,child) #backtrack

        node.state.d += 1 #next position

    return False #if no path exists

def printgraph(board,n,k,node,algo):

    if algo == 2:
        print("BFS....")
        BFS(board,n,k,node)
    else:
        print("DFS....")
        if(not DFS(board,n,k,node)):
            print("No solution")
    


if __name__=='__main__':
    rows= tuple(open("input.txt",'r'))
    rows= [l.strip() for l in rows]
    n=int(input("Enter size of board: "))
    k=int(input("Enter number of queens: "))
    algo=int(input("Enter 1. DFS 2. BFS... Your Choice = "))
    if algo>2:
        print("Invalid input for searching algorithm")
        exit()
    board=[]
    for i in range(n):
        r=[]
        r.extend(list(map(int,input().strip().split())))
        board.append(r)
    print("The input board: ")
    
    for i in range(n):
        print(board[i])

    node=Node(d=0, board = board) #create a node object with start point and initialize node using constructor
    printgraph(board,n,k,node,algo)

