#f(n)=g(n)+h(n)

direction=[[0,-1],
           [0,1],
           [-1,0],
           [1,0]]  #diagonal not allowed

class Node:
    def __init__(self,parent=None,pos=None):
        self.parent=parent
        self.pos=pos #a list - [row,col]
        #defining the f, g, h terms
        self.f=0
        self.g=0
        self.h=0


def Astar(maze,start,goal): 
    listopen=[] #will contain the nodes to explore
    listclose=[] #will contain the final confirmed path
    #initialise start and goal node
    snode=Node(None,start) #no parent
    gnode=Node(None,goal) #no parent as of now

    listopen.append(snode) #start node added

    while listopen:
        #assign the first element to the current node
        cnode=listopen[0]
        #check for lowest f
        for node in listopen:
            if node.f < cnode.f:
                cnode=node

        listopen.remove(cnode)
        listclose.append(cnode) #added to path as it has lowest f
        #print(cnode.pos)
        
        #goal found
        if cnode.pos==gnode.pos:
            #backtrack for getting path
            path=[]
            curr=cnode
            while(curr is not None):
                path.append(curr.pos)
                curr=curr.parent
            return path


        children=[] #list of node objects which are children of cnode
        #find children in the adjacent nodes
        for p in direction:
            newpos=[cnode.pos[0]+p[0],cnode.pos[1]+p[1]]

            #invalid position
            if newpos[0] not in range(0,len(maze)) or newpos[1] not in range(0,len(maze)):
                continue
            #obstacle
            if maze[newpos[0]][newpos[1]]!=0:
                continue

            newnode=Node(cnode,newpos)
            #if (newnode is not cnode.parent):
            children.append(newnode)

        #applying the heuristics
        for ch in children:
            for closech in listclose:
                if ch == closech:
                    continue
            #set the f g h vals
            ch.g=cnode.g+1 #since its only one step away from the parent
            #straight line square distance from the goal
            ch.h= ((ch.pos[0]-gnode.pos[0])**2) +((ch.pos[1]-gnode.pos[1])**2)

            ch.f = ch.g + ch.h #estimated cost

            for node in listopen:
                if ch == node and ch.g>node.g: #if the cost is higher ignore
                    continue
            #add child to end of list if its not there in openlist already or the nodes of openlist have a smaller g
            listopen.append(ch) 

    else:
        print("Failed to find path")




if __name__=="__main__":
    print("A star algorithm on a 10x10 maze...")
    maze=[]
    for i in range(10):
        maze.append(list(map(int,input().strip().split())))
        #print(maze[i])
    
    start=list(map(int,input("Enter starting row and column: ").strip().split()))
    goal=list(map(int,input("Enter goal row and column: ").strip().split()))
    print("The final path is...")
    #reverse the path
    path=Astar(maze,start,goal)[::-1]

    for i in range(len(maze)):
        for j in range(len(maze)):
            if [i,j] in path:
                print(">",end="")
            else:
                print(maze[i][j],end="")
        print("\n")
    
