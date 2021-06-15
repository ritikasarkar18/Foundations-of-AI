from copy import deepcopy


count = 0 # number of states reached
class Evaluate:
    def __init__(self):
        self.eval = 0
        self.board = []

def minmax(board, d, player1, max, min, isStage1,heuristic):
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
            #'2' is placed here
            if isStage1:
                successors = generateInvertedBoardList(stage1Moves(InvertedBoard(board))) 
            else:
                successors = generateInvertedBoardList(stage23Moves(InvertedBoard(board)))


        for succ in successors:
            if len(succ)==24:
                if player1:
                    curr = minmax(succ,d-1,False,max, min, isStage1, heuristic)
                    # player1 variable set to False so as to set turn for player 2
                    if curr.eval>max:
                        max = curr.eval
                        final.board = succ
                else:
                    curr = minmax(succ,d-1,True,max, min, isStage1, heuristic)
                    if curr.eval<min:
                        min = curr.eval
                        final.board = succ
            else:
                print("Error in successor generation")
                exit(0)

        if player1:
            final.eval = max
        else:
            final.eval = min
    
    else:
        if player1:
            final.eval = heuristic(board, isStage1)
        else:
            final.eval = heuristic(InvertedBoard(board), isStage1)

    return final



def stage1Moves(board):
    board_list = []
    for i in range(len(board)):
        if board[i] == 'x': 
            bcopy = deepcopy(board)
            bcopy[i] = '1'
            #board = bcopy 
            if (isMill(i, bcopy)):
                board_list = removePiece(bcopy, board_list)
            else:
                board_list.append(bcopy)
    return board_list



def stage23Moves(board):
    if (board.count("1") == 3):
        # flying piece(special moves)
        return stage3Moves(board)
    else:
        # moving the pieces
        return stage2Moves(board)



def stage2Moves(board):
    board_list = []
    for i in range(len(board)):
        if (board[i] == "1"):
            adjacent_list = get_neighbours(i)

            for pos in adjacent_list:
                if (pos>=0 and board[pos] == "x"):
                    boardcopy = deepcopy(board)
                    boardcopy[i] = "x"
                    boardcopy[pos] = "1"

                    if isMill(pos, boardcopy):
                        board_list = removePiece(boardcopy, board_list)
                    else:
                        board_list.append(boardcopy)
    return board_list



def stage3Moves(board):
    board_list = []

    for i in range(len(board)):
        if (board[i] == "1"):

            for j in range(len(board)):
                if (board[j] == "x"):
                    boardcopy = deepcopy(board)

                    boardcopy[i] = "x"
                    boardcopy[j] = "1"

                    if (isMill(j, boardcopy)):
                        board_list = removePiece(boardcopy, board_list)
                    else:
                        board_list.append(boardcopy)
    return board_list


def removePiece(boardcopy, board_list):
    for i in range(len(boardcopy)):
        if (boardcopy[i] == "2"):
            #cannot move pieces from mill positions of other player
            if not isMill(i, boardcopy):
                new_board = deepcopy(boardcopy)
                new_board[i] = "x" # removing '2' piece
                board_list.append(new_board)
    return board_list



def generateInvertedBoardList(pos_list):

    result = []
    for i in pos_list:
        result.append(InvertedBoard(i))
    return result


def InvertedBoard(board):
    invertedboard = []
    for i in board:
        if i == "1":
            invertedboard.append("2")
        elif i == "2":
            invertedboard.append("1")
        else:
            invertedboard.append("x")
    return invertedboard


def getPossibleMillCount(board, player):
    count = 0
    for i in range(len(board)):
        if (board[i] == "x"):
            if checkMill([i], player, board):
                count += 1
    return count


def getPotentialMill(board, player):
    count = 0
    for i in range(len(board)):
        if (board[i] == player):
            adjacent_list = get_neighbours(i)
            for pos in adjacent_list:
                if pos>=0:
                    if (player == "1"):
                        if (board[pos] == "2"):
                            board[i] = "2"
                            if isMill(i, board):
                                count += 1
                            board[i] = player
                    else:
                        if (board[pos] == "1" and potentialMill(pos, board, "1")):
                            count += 1
    return count



def potentialMill(position, board, player):
    adjacent_list = get_neighbours(position)
    for i in adjacent_list:
        #check if '1' does not form a mill - condition for checking future safe moves by '2'
        if i>=0 and (board[i] == player) and (not checkMill([position], player, board)):
            return True
    return False



def get_neighbours(pos):
    #up down left right
    #invalid = -1
    arr = [
        [-1, 3, -1, 1], [-1, 9, 0, 2],
        [-1, 4, 1, -1], [0, 5, -1, 11],
        [2, 7, 12, -1], [3, -1, -1, 6],
        [14, -1, 5, 7], [4, -1, 6, -1],
        [-1 , 11, -1, 9], [1, 17, 8, 10],
        [-1, 12, 9, -1], [8, 13, 3, 19],
        [10, 15, 20, 4], [11, -1, -1, 14],
        [22, 6, 13, 15], [12, -1, 14, -1],
        [-1, 19, -1, 17], [9, -1, 16, 18],
        [-1, 20, 17, -1], [16, 21, 11, -1],
        [18, 23, -1, 12], [19, -1, -1, 22],
        [-1, 14, 21, 23], [20, -1, 22, -1]
    ]
    return arr[pos]



def findMill(board,player,p1,p2):
    if board[p1] == player and board[p2] == player:
        return True
    return False


def isMill(pos,board):
    player = board[pos]
    if player!='x':
        return checkMill([pos],player,board)
    return False
    

# horizontally or vertically 3 pieces in line
def checkMill(position,player,board):
    h = 0
    v = 0
    for i in position:
        # check vert
        neighbours = get_neighbours(i)
        if (neighbours[0]>=0):
            if (neighbours[1]>=0):
                v = findMill(board,player,neighbours[0],neighbours[1])
                
            else:
                farther_neighbours = get_neighbours(neighbours[0])
                if (farther_neighbours[0]>=0):
                    v = findMill(board, player,neighbours[0],farther_neighbours[0])
                    
        else:
            if (neighbours[1]>=0):
                farther_neighbours = get_neighbours(neighbours[1])
                if (farther_neighbours[1]>=0):
                    v = findMill(board, player,neighbours[1],farther_neighbours[1])
                    
        
    
        #check hori
        if (neighbours[3]>=0):
            if (neighbours[2]>=0):
                h = findMill(board, player,neighbours[2],neighbours[3])
                
            else:
                farther_neighbours = get_neighbours(neighbours[3])
                if (farther_neighbours[3]>=0):
                    h = findMill(board, player,neighbours[3],farther_neighbours[3])
                    
        else:
            if (neighbours[2]>=0):
                farther_neighbours = get_neighbours(neighbours[2])
                if (farther_neighbours[2]>=0):
                    h = findMill(board,player,neighbours[2],farther_neighbours[2])
                    


    return (h or v)
