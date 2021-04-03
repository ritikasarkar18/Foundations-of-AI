from puzzle import EightPuzzle, Node
import time
import sys

def dls(puzzle, depth):
    start = Node(puzzle)
    boardnode = [] # using stack like dfs
    boardnode.append(start)
    
    while True:
        
        if not boardnode: #empty board
            return None
        
        actual = boardnode.pop(0)
        #actual.printBoard(actual) #printing the current state
        
        if actual.goalState():
            print("Success!")
            print("Goal board is ")
            actual.printBoard(actual)
            print("Depth: ",actual.depth)
            
            return actual
        
        elif actual.depth is not depth: 
            succ = actual.successor() 
            while succ:
                for s in succ:
                    boardnode.append(s)
                    succ.remove(s)
    

def ids(puzzle):
    depth = 0
    result = None
    start_time = time.time()
    while result == None: 
        result = dls(puzzle, depth) 
        depth +=1
    print('Total time is: %2f' % (time.time() - start_time))
    return result




def Astar(w,puzzle): 
    listopen=[] 
    listclose=[]
    iters=0
    
    snode = Node(puzzle,w) 
    snode.calculate_h()
    snode.calculate_f()

    listopen.append(snode) #start node added

    start_time = time.time()

    while listopen:
        
        cnode=listopen[0]
        iters+=1
        
        for node in listopen:
            if node.fp < cnode.fp:
                cnode=node

            if node.fp == cnode.fp:
                if node.h < cnode.h:
                    cnode=node

        listopen.remove(cnode)
        listclose.append(cnode) #added to path as it has lowest f
        cnode.printBoard(cnode)
        
        #goal found
        if cnode.goalState():
    
            print("Goal reached!")
            print("Goal board is ")
            cnode.printBoard(cnode)
            print('Total number of moves: %d' % iters)
            print("Cost = ",iters*w) 
            print('Total time is: %2f' % (time.time() - start_time))
            exit()

        #children or successors to be generated
        succ = cnode.successor() #returns list

        #applying the heuristics
        for ch in range(len(succ)):
            for closech in listclose:
                if ch == closech:
                    continue

            succ[ch].calculate_costs()            

            if node in listopen:
                if succ[ch] == node and succ[ch].g>node.g: 
                    continue

            listopen.append(succ[ch]) 

    else:
        print("Failed to find path")




if __name__=="__main__":
    print("Weighted A star algorithm ...")
    start = []
    goal = []
    print("Enter starting board :")
    for i in range(3):
        start.append(list(map(int,input().strip().split())))
        
    zero=tuple(map(int,input("Enter row and col of blank cell or 0: ").strip().split()))
    
    print("Enter goal board :")
    for i in range(3):
        goal.append(list(map(int,input().strip().split())))

    w = int(input("Enter the weight: "))
    
    p = EightPuzzle(start,goal,zero)

    print("\n\n...Iterative Deepening Search...")
    ids(p)
    print("\n\n")
    print("...Astar search...")
    Astar(w,p) 
    
