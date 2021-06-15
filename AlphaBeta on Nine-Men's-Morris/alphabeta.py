from minmax import *

alpha = float('-inf')
beta = float('inf')
d = 3 #depth
count=0 # for alphabeta
prune=0

def alphabeta(board, d, player1, alpha, beta, isStage1,heuristic):
    final = Evaluate()
    global count
    count+=1
    if d!=0:
        curr = Evaluate()
        if player1:
            if isStage1:
                successors = stage1Moves(board)
            else:
                successors = stage23Moves(board) 

        else:
            if isStage1:
                successors = generateInvertedBoardList(stage1Moves(InvertedBoard(board))) 
            else:
                successors = generateInvertedBoardList(stage23Moves(InvertedBoard(board)))


        for succ in successors:
            if len(succ)==24:
                if player1:
                    curr = alphabeta(succ,d-1,False,alpha, beta, isStage1, heuristic)
                    if curr.eval>alpha:
                        alpha = curr.eval
                        final.board = succ
                else:
                    curr = alphabeta(succ,d-1,True,alpha, beta, isStage1, heuristic)
                    if curr.eval<beta:
                        beta = curr.eval
                        final.board = succ

            if alpha>=beta:
                global prune
                prune+=1
                print("Pruned branches uptill now: ",prune)
                break

        if player1:
            final.eval = alpha
        else:
            final.eval = beta
    
    else:
        if player1:
            final.eval = heuristic(board, isStage1)
        else:
            final.eval = heuristic(InvertedBoard(board), isStage1)

    return final
