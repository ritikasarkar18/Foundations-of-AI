#Works in alphabetical order for the level - causes problem if order changed

li=['a','b','c','d','e']
f=0

def dls(arr,start,visited,depth,goal,children):
    print(start, end=", ")
    visited[start] = True

    if (start==goal):
        #global f
        #f=1
        return True

    if (depth<=0):
        return False

    if (children>5):
        children=5
    for i in range(children):
        if li[i]==start:
            continue
        if (arr[start][i]==1 and not visited[li[i]]):
            if (dls(arr,li[i],visited,depth-1,goal,children)):
                #print("Success")
                return True
    return False



def iddfs(arr,start,depth,goal):
    visited={}
    for i in range(1,depth+1):
        visited = {'a':False, 'b':False, 'c':False, 'd':False, 'e':False}
        if (dls(arr,start,visited,i,goal,int(pow(2,i))-1)):
            return True
        print("\n")
    return False


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
goal=input("Enter goal node: ")
depth=int(input("Enter the depth: "))

if (iddfs(arr,start,depth,goal)): #not f
    print("\nSuccess")
else:
    print("\nNot found")
