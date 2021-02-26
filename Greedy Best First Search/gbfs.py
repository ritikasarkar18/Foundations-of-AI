# li = [[u,v,w],[u1,v1,w1]]
# using queue like bfs for giving shortest path
from queue import PriorityQueue as PQ

def gbfs(li,src,dst,e,n):
    #pass
    visited = [False]*n
    visited[0] = True
    q=PQ()
    q.put(0,src)
    while q.empty() == False:
        node = q.get()[1] #get the node
        print(node, end=", ")
        if node == dst:
            break

        
    
    

if __name__='__main__':
    n=int(input("Enter the number of nodes"))
    e=int(input("Enter number of edges"))
    print("Enter the edges and the cost")
    li = []
    for i in range(e):
        a = list(map(int,input().strip().split()))
        li.append(a)

    
    print(li)
    src=int(input("Enter the source node"))
    dst=int(input("Enter the destination node"))
    gbfs(li,src,dst,e,n)
