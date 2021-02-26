li=['a','b','c','d','e']

def bfs(arr,start):
        visited={}
        visited = {'a':False, 'b':False, 'c':False, 'd':False, 'e':False}
        queue = [start]
        visited[start] = True

        while queue:
                vi = queue[0]
                print(queue.pop(0), end=", ")
                for i in range(5):
                        if (arr[vi][i]==1 and not visited[li[i]]):
                                queue.append(li[i])
                                visited[li[i]] = True


arr={'a':[0,0,0,0,0],
     'b':[0,0,0,0,0],
     'c':[0,0,0,0,0],
     'd':[0,0,0,0,0],
     'e':[0,0,0,0,0]}

n = int(input("Enter number of edges: "))
for i in range(n):
        l=input()
        a=l[0]; b=int(l[2])
        arr[a][b]=1
        c=ord(a)-97
        arr[li[b]][c]=1

start=input("Enter start node: ")

bfs(arr,start)
