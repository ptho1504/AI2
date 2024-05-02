import random

pieceScore = {"K": 900, "Q": 90, "R": 50, "B":30, "N":30, "p":10}

whiteKnightScores = [
                    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
                    [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
                    [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
                    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
                    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
                    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
                    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                ]  
        
blackKnightScores = [
                    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
                    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
                    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
                    [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
                    [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
                    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
                    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                ]


whiteBishopScores=[
                    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
                    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
                    [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
                    [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
                    [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
                    [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
                    [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
                    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
             ]

blackBishopScores=[
                    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
                    [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
                    [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
                    [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
                    [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
                    [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
                    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
                    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
             ]  

whiteQueenScores=[
                    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
                    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
                    [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
                    [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
                    [ 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
                    [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
                    [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
                    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
            ]

blackQueenScores=[
                    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
                    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.5,  0.0, -1.0],
                    [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.5, -1.0],
                    [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0,  0.0],
                    [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
                    [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
                    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
                    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
            ]

whiteRookScores=[
                    [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  0.0],
                    [ 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,  0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [ 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0,  0.0],
            ]

blackRookScores=[
                    [ 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0,  0.0],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
                    [ 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,  0.5],
                    [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  0.0],
            ]

whitePawnScores=[
                    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
                    [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
                    [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
                    [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
                    [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
                    [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
                    [0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5],
                    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
                ]

blackPawnScores =[
                [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
                [0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5],
                [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
                [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
                [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
                [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
                [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
                [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            ]

whiteKingScore = [
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
                [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
                [ 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
                [ 2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
]

blackKingScore = [
                [ 2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0],
                [ 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
                [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
                [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
                [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
]


piecePositionScores = {"wN": whiteKnightScores,"bN": blackKnightScores, 
                       "wQ": whiteQueenScores, "bQ" : blackQueenScores, 
                       "wB": whiteBishopScores, "bB": blackBishopScores, 
                       "wR": whiteRookScores, "bR": blackRookScores,
                       "bp":blackPawnScores, "wp": whitePawnScores,
                       "wK": whiteKingScore, "bK": blackKingScore,
                       }

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3

def findRandomMove(validMoves):
    return validMoves[random.randint(0,len(validMoves)-1)]

def findLevel(gs, validMoves, level):
    if level == 1:
        return findRandomMove(validMoves)
    else:
        return findBestMoveMinMax(gs, validMoves, level)
        
def findBestMove(gs, validMoves):
     turnMultiplier = 1 if gs.whiteToMove else -1
     opponentMinMaxScore = CHECKMATE 
     bestPlayerMove = None
     random.shuffle(validMoves)
     
     for playerMove in validMoves:
         gs.makeMove(playerMove)
         opponentsMoves = gs.getValidMoves()
         if gs.staleMate:
             opponentsMaxScore = STALEMATE
         elif gs.checkMate:
             opponentsMaxScore = -CHECKMATE
         else:
             opponentsMaxScore = -CHECKMATE
             for opponentsMove in opponentsMoves:
                gs.makeMove(opponentsMove)
                gs.getValidMoves()
                if gs.checkMate:
                    score = CHECKMATE 
                elif gs.staleMate:
                    score = STALEMATE
                else:
                    score = scoreMaterial(gs.board) * -turnMultiplier
                if  score > opponentsMaxScore:
                    opponentsMaxScore = score
                gs.undoMove()
         if opponentsMaxScore < opponentMinMaxScore:
            opponentMinMaxScore = opponentsMaxScore
            bestPlayerMove = playerMove
         gs.undoMove()
     return bestPlayerMove


    

def findBestMoveMinMax(gs, validMoves, level):
    global nextMove, counter
    nextMove = None
    counter = 0
    random.shuffle(validMoves)
    # findMoveMinMax(gs,validMoves, DEPTH, gs.whiteToMove)
    # findMoveMinMaxAlphaBeta(gs,validMoves, level, -CHECKMATE, CHECKMATE, gs.whiteToMove, level)
    # findMoveNegaMax(gs,validMoves, DEPTH, 1 if gs.whiteToMove else -1)
    findMoveNegaMaxAlphaBeta(gs,validMoves, level, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1,level)
    print("Game State Counter: ",counter)
    
    return nextMove

def findMoveMinMax(gs, validMoves, depth, whiteToMove):
    global nextMove,counter
    counter += 1
    if depth == 0:
        return scoreBoard(gs)

    if whiteToMove:
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMax(gs, nextMoves, depth-1, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return maxScore
    else:
        minSCore = CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMax(gs, nextMoves, depth-1, True)

            if score < minSCore:
                minSCore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return minSCore

def findMoveMinMaxAlphaBeta(gs,validMoves, depth, alpha, beta, whiteToMove, maxDepth):
    global nextMove,counter
    counter += 1
    if depth == 0:
        return scoreBoard(gs)

    if whiteToMove:
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMaxAlphaBeta(gs, nextMoves, depth-1,alpha,beta, False,maxDepth)
            if score > maxScore:
                maxScore = score
                if depth == maxDepth:
                    nextMove = move
            gs.undoMove()
            if maxScore > alpha:
                alpha = maxScore
            if beta <= alpha:
                break
        # print(nextMove, score)
        return maxScore
    else:
        minSCore = CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMaxAlphaBeta(gs, nextMoves, depth-1,alpha,beta, True,maxDepth)

            if score < minSCore:
                minSCore = score
                if depth == maxDepth:
                    nextMove = move
            gs.undoMove()
            if minSCore < beta:
                beta = minSCore
            if beta <= alpha:
                break
        # print(nextMove, score)
        return minSCore

def findMoveNegaMax(gs, validMoves, depth, turnMultiplier):
    global nextMove,counter
    counter += 1
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)
    
    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        score = -findMoveNegaMax(gs,nextMoves,depth-1, -turnMultiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        gs.undoMove()
    return maxScore

def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier, maxLevel):
    global nextMove,counter
    counter += 1
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)
    #move ordering 
    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(gs,nextMoves,depth-1,-beta, -alpha, -turnMultiplier,maxLevel)
        if score > maxScore:
            maxScore = score
            if depth == maxLevel:
                nextMove = move
        gs.undoMove()
        if maxScore > alpha: #prune happens
            alpha = maxScore
        if alpha >= beta:
            break
    # print(nextMove, score)
    return maxScore
  
  
  
  
'''
    A positive score is good for white, a negative score is good for black
'''

# Function 1
# def scoreBoard(gs):
    
#     if gs.checkMate:
#         if gs.whiteToMove:
#             return -CHECKMATE #black wins
#         else:
#             return CHECKMATE #white wins
#     elif gs.staleMate:
#         return STALEMATE
#     score = 0
#     for row in gs.board:
#         for square in row:
#             if square[0] == 'w':
#                 score += pieceScore[square[1]]
#             elif square[0] == 'b':
#                 score -= pieceScore[square[1]]
#     return score


# Function 2
def scoreBoard(gs):
    
    if gs.checkMate:
        if gs.whiteToMove:
            return -CHECKMATE #black wins
        else:
            return CHECKMATE #white wins
    elif gs.staleMate:
        return STALEMATE
    score = 0
    
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            square = gs.board[row][col]
            if square != "--":
                # Score it positionally
                piecePositionScore = 0
                # if square[1] != "K":
                #     if square[1] == "p":
                piecePositionScore = piecePositionScores[square][row][col]
                    # else:
                        # piecePositionScore = piecePositionScores[square[1]][row][col]
                
                if square[0] == 'w':
                    score += pieceScore[square[1]] + piecePositionScore 
                elif square[0] == 'b':
                    score -= pieceScore[square[1]] + piecePositionScore 
    return score

def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
    return score