import random

pieceScore = {"K": 0, "Q": 10, "R": 5, "B":3, "N":3, "p":1}

knightScores = [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]

bishopScores=[
                [4, 3, 2, 1, 1, 2, 3, 4],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [4, 3, 2, 1, 1, 2, 3, 4]]

queenScores=[   
                [1, 1, 1, 3, 1, 1, 1, 1],
                [1, 2, 3, 3, 3, 1, 1, 1],
                [1, 4, 3, 3, 3, 4, 2, 1],
                [1, 2, 3, 3, 3, 2, 2, 1],
                [1, 2, 3, 3, 3, 2, 2, 1],
                [1, 4, 3, 3, 3, 4, 2, 1],
                [1, 1, 2, 3, 3, 1, 1, 1],
                [1, 1, 1, 3, 1, 1, 1, 1]]

rookScores=[
                [4, 3, 4, 4, 4, 4, 3, 4],
                [4, 4, 4, 4, 4, 4, 4, 4],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 1, 2, 2, 2, 2, 1, 1],
                [4, 4, 4, 4, 4, 4, 4, 4],
                [4, 3, 4, 4, 4, 4, 3, 4]]

whitePawnScores =[
                [8, 8, 8, 8, 8, 8, 8, 8],
                [8, 8, 8, 8, 8, 8, 8, 8],
                [5, 6, 6, 7, 7, 6, 6, 5],
                [2, 3, 3, 5, 5, 3, 3, 2],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [1, 1, 1, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0]]

blackPawnScores =[
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 1, 1, 1],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [2, 3, 3, 5, 5, 3, 3, 2],
                [5, 6, 6, 7, 7, 6, 6, 5],
                [8, 8, 8, 8, 8, 8, 8, 8],
                [8, 8, 8, 8, 8, 8, 8, 8]]




piecePositionScores = {"N": knightScores, "Q": queenScores, "B": bishopScores, "R": rookScores, "bp":blackPawnScores,
                        "wp": whitePawnScores
                       }

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 2

def findRandomMove(validMoves):
    return validMoves[random.randint(0,len(validMoves)-1)]

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


def findBestMoveMinMax(gs, validMoves):
    global nextMove, counter
    nextMove = None
    counter = 0
    random.shuffle(validMoves)
    # findMoveMinMax(gs,validMoves, DEPTH, gs.whiteToMove)
    # findMoveMinMaxAlphaBeta(gs,validMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    # findMoveNegaMax(gs,validMoves, DEPTH, 1 if gs.whiteToMove else -1)
    findMoveNegaMaxAlphaBeta(gs,validMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
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

def findMoveMinMaxAlphaBeta(gs,validMoves, depth, alpha, beta, whiteToMove):
    global nextMove,counter
    counter += 1
    if depth == 0:
        return scoreBoard(gs)

    if whiteToMove:
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMaxAlphaBeta(gs, nextMoves, depth-1,alpha,beta, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
            if maxScore > alpha:
                alpha = maxScore
            if beta <= alpha:
                break
        return maxScore
    else:
        minSCore = CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMaxAlphaBeta(gs, nextMoves, depth-1,alpha,beta, True)

            if score < minSCore:
                minSCore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
            if minSCore < beta:
                beta = minSCore
            if beta <= alpha:
                break
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

def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier):
    global nextMove,counter
    counter += 1
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)
    #move ordering 
    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(gs,nextMoves,depth-1,-beta, -alpha, -turnMultiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        gs.undoMove()
        if maxScore > alpha: #prune happens
            alpha = maxScore
        if alpha >= beta:
            break
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
                if square[1] != "K":
                    if square[1] == "p":
                        piecePositionScore = piecePositionScores[square][row][col]
                    else:
                        piecePositionScore = piecePositionScores[square[1]][row][col]
                
                if square[0] == 'w':
                    score += pieceScore[square[1]] + piecePositionScore * .1
                elif square[0] == 'b':
                    score -= pieceScore[square[1]] + piecePositionScore * .1
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