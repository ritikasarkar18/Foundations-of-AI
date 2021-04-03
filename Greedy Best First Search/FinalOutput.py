Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: E:\F drive\VIT Sem 4\AI\Lab\19BAI1031\Lab 3\Greedy Best First Search\gbfs.py
Enter the number of nodes: 14
Enter number of edges: 13
Enter the edges and the cost: 
a b 3
a c 6
a d 5
b e 9
b f 8
c g 12
c h 14
d i 7
i j 5
i k 6
j l 1
j m 10
j n 2
The graph with costs
{'a': [['b', 3], ['c', 6], ['d', 5]], 'b': [['a', 3], ['e', 9], ['f', 8]], 'c': [['a', 6], ['g', 12], ['h', 14]], 'd': [['a', 5], ['i', 7]], 'e': [['b', 9]], 'f': [['b', 8]], 'g': [['c', 12]], 'h': [['c', 14]], 'i': [['d', 7], ['j', 5], ['k', 6]], 'j': [['i', 5], ['l', 1], ['m', 10], ['n', 2]], 'k': [['i', 6]], 'l': [['j', 1]], 'm': [['j', 10]], 'n': [['j', 2]]}

Enter the source node: a
Enter the destination node: j
Greedy best first search ...
a, b, d, c, i, j, 
>>> 