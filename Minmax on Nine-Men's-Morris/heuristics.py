from minmax import *


#heuristic_stage1
def numberOfPieces(board, isStage1):
    
    numP1 = board.count("1")
    numP2 = board.count("2")

    moveP2 = 0

    if not isStage1:
        moveBlack = len(stage23Moves(board)) #number stage2 or 3 moves possible by p2

    if not isStage1:
        if numP2 <= 2 or moveBlack == 0:
            evaluation = float('inf') #p1 wins
        elif numP1 <= 2:
            evaluation = float('-inf') #p1 loses
        else:
            evaluation = 200 * (numP1 - numP2)
    else:
        evaluation = 100 * (numP1 - numP2) #because we want p1 to win

    return evaluation


##not required
def potentialMills(board, isStage1):

    evaluation = 0

    numP1 = board.count("1")
    numP2 = board.count("2")

    possibleMillP1 = getPossibleMillCount(board, "1")
    possibleMillP2 = getPossibleMillCount(board, "2")

    moveP2 = 0

    if not isStage1:
        moveBlack = len(stage23Moves(board))

    potentialMillP1 = getPotentialMill(board, "1")
    potentialMillP2 = getPotentialMill(board, "2")

    if not isStage1:
        if numP2 <= 2 or moveBlack == 0:
            evaluation = float('inf')
        elif numP1 <= 2:
            evaluation = float('-inf')
        else:
            if (numP1 < 4):
                evaluation += 100 * possibleMillP1
                evaluation += 200 * potentialMillP2
            else:
                evaluation += 200 * possibleMillP1
                evaluation += 100 * potentialMillP2
    else:
        if numP1 < 4:
            evaluation += 100 * possibleMillP1
            evaluation += 200 * potentialMillP2
        else:
            evaluation += 200 * possibleMillP1
            evaluation += 100 * potentialMillP2

    return evaluation


##not required
def numOfMoveablePieces(board, isStage1):
    
    evaluation = 0

    numP1 = board.count("1")
    numP2 = board.count("2")

    #moveablePiecesPlayer1 = 0
    moveP2 = 0

    if not isStage1:
        moveBlack = len(stage23Moves(board))

    if not isStage1:
        if numP2 <= 2 or moveBlack == 0:
            evaluation = float('inf')
        elif numP1 <= 2:
            evaluation = float('-inf')
        else:
            evaluation = 100 * (numP1 - numP2)
            evaluation -= 50 * moveBlack
    else:
        evaluation = 100 * (numP1 - numP2)
        evaluation -= 50 * moveP2

    return evaluation


###heuristic_stage23
def AdvancedHeuristic(board, isStage1):
    evaluation = 0

    numP1 = board.count("1")
    numP2 = board.count("2")

    #count number of places that are now blank but mill can be formed on placing another similar piece
    possibleMillP1 = getPossibleMillCount(board, "1")
    possibleMillP2 = getPossibleMillCount(board, "2")

    #moveablePiecesPlayer1 = 0
    moveP2 = 0

    if not isStage1:
        moveBlack = len(stage23Moves(board))#number stage2 or 3 moves possible by p2

    #count number of places where, for eg '1' is there but if we could place '2' mill can be formed
    potentialMillP1 = getPotentialMill(board, "1")
    potentialMillP2 = getPotentialMill(board, "2")

    if not isStage1:
        if numP2 <= 2 or moveBlack == 0:
            evaluation = float('inf') #p2 loses
        elif numP1 <= 2:
            evaluation = float('-inf') #p1 loses
        else:
            if (numP1 < 4): # when it becomes stage 3 Moves for p1, chances of winning for p1 are less so heuristic values reversed
                evaluation += 100 * possibleMillP1
                evaluation += 200 * potentialMillP2
            else:
                evaluation += 200 * possibleMillP1
                evaluation += 100 * potentialMillP2
            evaluation -= 25 * moveBlack #subtracting counter moves by p2
            evaluation += 50 * (numP1 - numP2) #because we want p1 to win
    else:
        if numP1 < 4:
            evaluation += 100 * possibleMillP1
            evaluation += 200 * potentialMillP2
        else:
            evaluation += 200 * possibleMillP1
            evaluation += 100 * potentialMillP2
        evaluation -= 25 * moveP2
        evaluation += 50 * (numP1 - numP2) 

    return evaluation
