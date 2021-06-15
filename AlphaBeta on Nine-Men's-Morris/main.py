from ninemen import *
from heuristics import *

if __name__=="__main__":
    print("------Nine Men's Morris------")
    b = Board()
    b.printboard()
    choice=int(input("Enter 1.Minmax or 2.Alphabeta"))
    b.play(numberOfPieces, AdvancedHeuristic,choice)
