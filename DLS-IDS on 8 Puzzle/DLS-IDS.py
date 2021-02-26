from Puzzle import EightPuzzle, Node

def dls(puzzle, depth):
    start = Node(puzzle)
    boardnode = [] # using stack like dfs
    boardnode.append(start)
    
    while True:
        
        if not boardnode: #empty board
            return None
        
        actual = boardnode.pop(0)
        actual.printBoard(actual) #printing the current state
        
        if actual.goalState(): #check goal
            print("Success")
            print("Depth: ",actual.depth)
            return actual
        
        elif actual.depth is not depth: #check whether depth reached
            succ = actual.successor() #expand to new states, returns queue
            while not succ.empty():
                boardnode.append(succ.get()) #store the new states
    

def ids(puzzle):
    depth = 0
    result = None
    while result == None: #like an infinite loop
        result = dls(puzzle, depth)
        depth +=1  #incrementing depth until goal reached
    print("Depth", depth)
    return result



if __name__=='__main__':
    p = EightPuzzle(int(input("Enter the board size (preferably 3 here): ")))
    p.createStates(int(10)) #creating a random starting board
    p.printPuzzle()
    algo = int(input("Enter 1. DLS and 2. IDS: "))
    if algo==1:
        depth = int(input("Enter the depth for DLS: "))
        print("Depth Limited Search... ", dls(p, depth))
        
    elif algo==2:
        print("Iterative Deepening Search: ", ids(p))
        
    else:
        print("Invalid entry for algorithm choice")



