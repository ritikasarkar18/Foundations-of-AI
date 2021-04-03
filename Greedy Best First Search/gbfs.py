#priority queue selects the node with lowest cost

from queue import PriorityQueue as PQ

alpha='abcdefghijklmnopqrstuvwxyz'

def gbfs(li,src,dst,n):
    visited ={alpha[i]:False for i in range(n)}
    #print(visited)
    visited[src] = True
    q=PQ() #an empty PriorityQueue
    q.put([0,src]) #inserting source's cost and source node
    
    while q.empty() == False:
        node = q.get()[1] #get the node and remove it from q

        print(node, end=", ")

        #goal
        if node == dst:
            break

        else:
            for wnode in li[node]:
                #print(wnode)
                if not visited[wnode[0]]:
                    visited[wnode[0]] = True
                    q.put([wnode[1],wnode[0]])
            #print(q)

    

if __name__=='__main__':
    n=int(input("Enter the number of nodes: "))
    e=int(input("Enter number of edges: "))
    print("Enter the edges and the cost: ")
    nodelist=[alpha[i] for i in range(n)]
    li={key:[] for key in nodelist}
    for i in range(e):
        a = list(input().strip().split())
        #add(a[0],a[1],a[2])
        li[a[0]].append([a[1],int(a[2])]) #adjacent node,cost
        li[a[1]].append([a[0],int(a[2])])
        #print(li)
    print("The graph with costs")
    print(li)
    src=input("\nEnter the source node: ")
    dst=input("Enter the destination node: ")
    print("Greedy best first search ...")
    gbfs(li,src,dst,n)

