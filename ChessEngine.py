"""
    Store all information about the current state of a chess game. It will be also responsible for determining valid moves at 
    current state. It keep a move log
"""

class GameState():
    def __init__(self):
        # Board as 8x8, each element has 2 characters
        # First character has 'b' or 'w'
        # Second character reprensent type 'K', 'Q', 'R', 'B', 'N' or  'p' 
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR" ],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp" ],
            ["--", "--", "--", "--", "--", "--", "--", "--" ],
            ["--", "--", "--", "--", "--", "--", "--", "--" ],
            ["--", "--", "--", "--", "--", "--", "--", "--" ],
            ["--", "--", "--", "--", "--", "--", "--", "--" ],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp" ],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR" ],
        ]
        self.moveFunction = {'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves, 
                             'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K':self.getKingMoves}
        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingLocation = (7,4)
        self.blackKingLocation = (0,4)
        self.checkMate = False
        self.staleMate = False
        self.enpassantPossible= () #coordinate for the square whene en passant capture is possible
        self.enpassantPossibleLog = [self.enpassantPossible]
        self.currentCastlingRight = CastleRights(True,True,True,True)
        self.castleRightsLog = [CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                             self.currentCastlingRight.wqs, self.currentCastlingRight.bqs)]
        
        
        
    def makeMove(self, move):
        # print(move.startRow, move.startCol)
        # print(move.endRow, move.endCol)
        
        # print("makemove", move.pieceMoved)
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove
        
        #update king moves
        if move.pieceMoved == "wK":
            self.whiteKingLocation = (move.endRow, move.endCol)
        if move.pieceMoved == "bK":
            self.blackKingLocation = (move.endRow, move.endCol)
        
        #Pawn promotion
        if move.isPawnPromotion:
            promotedPiece = 'Q'
            self.board[move.endRow][move.endCol] = move.pieceMoved[0] + promotedPiece
        # print("Move in side", move.pieceMoved, "|", move)
        
        #enpassant move
        if move.isEnpassantMove:
            self.board[move.startRow][move.endCol] = "--" #Capture the pawn
        
        #update enpassantPossible variable
        if move.pieceMoved[1] == 'p' and abs(move.startRow - move.endRow) == 2:
            self.enpassantPossible = ((move.startRow + move.endRow)//2, move.startCol)
        else:
            self.enpassantPossible = ()

        #castle move
        if move.isCastleMove:
            if move.endCol - move.startCol == 2: # King Side
                self.board[move.endRow][move.endCol-1] = self.board[move.endRow][move.endCol+1] # Rook
                self.board[move.endRow][move.endCol+1] = "--" # erase rook
            else : # Queen side
                self.board[move.endRow][move.endCol+1] = self.board[move.endRow][move.endCol-2] # Rook
                self.board[move.endRow][move.endCol-2] = "--" # erase rook
        
        #update enpassant log
        self.enpassantPossibleLog.append(self.enpassantPossible)
        
        #update castle rights - whenever it is a rock or a king move
        self.updateCastleRight(move)
        self.castleRightsLog.append(CastleRights
                                            (self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                             self.currentCastlingRight.wqs, self.currentCastlingRight.bqs)) 
        # print("in side makeMove", move)
        # print(self.board)
        # print("") 
           
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
            # updateking location
            if move.pieceMoved == "wK":
                self.whiteKingLocation = (move.startRow, move.startCol)
            if move.pieceMoved == "bK":
                self.blackKingLocation = (move.startRow, move.startCol)
            # undo en passant move
            if move.isEnpassantMove:
                self.board[move.endRow][move.endCol] = '--'
                self.board[move.startRow][move.endCol] = move.pieceCaptured
                # self.enpassantPossible = (move.endRow, move.endCol)
            self.enpassantPossibleLog.pop() 
            self.enpassantPossible = self.enpassantPossibleLog[-1]
            # undo a 2 square pawn advance
            # if move.pieceMoved[1] == 'p' and abs(move.startRow - move.endRow) == 2:
            #      self.enpassantPossible = ()
                 
                 
            # undo castling rights
            self.castleRightsLog.pop()     
            newRights = self.castleRightsLog[-1]
            self.currentCastlingRight = CastleRights(newRights.wks, newRights.bks, newRights.wqs, newRights.bqs)
            
            # undo castle move
            if move.isCastleMove:
                if move.endCol - move.startCol == 2: # King Side
                    self.board[move.endRow][move.endCol+1] = self.board[move.endRow][move.endCol-1]
                    self.board[move.endRow][move.endCol-1] = "--"
                else:
                    self.board[move.endRow][move.endCol-2] = self.board[move.endRow][move.endCol+1]
                    self.board[move.endRow][move.endCol+1] = "--"
            
            #ADD THESE
            self.checkMate = False
            self.staleMate = False
            
            
    # update the castle rights given the move
    def updateCastleRight(self, move):
        if move.pieceMoved == 'wK':
            # print("Nive in updateCastleRight", move)
            # print(self.board)
            # print("1")
            self.currentCastlingRight.wks = False
            self.currentCastlingRight.wqs = False
        elif move.pieceMoved == 'bK':
            # print("2")
            self.currentCastlingRight.bks = False
            self.currentCastlingRight.bqs = False
        elif move.pieceMoved == 'wR':
            # print("3")
            if move.startRow == 7:
                if move.startCol == 0: # left rook
                    self.currentCastlingRight.wqs = False
                elif move.startCol == 7: # right rook
                    self.currentCastlingRight.wks = False
        elif move.pieceMoved == 'bR':
            if move.startRow == 0:
                if move.startCol == 0: # left rook
                    self.currentCastlingRight.bqs = False
                elif move.startCol == 7: # right rook
                    self.currentCastlingRight.bks = False
                    
        #if a rook is captured
        if move.pieceCaptured == 'wR':
            if move.endRow == 7 :
                if move.endCol == 0:
                    self.currentCastlingRight.wqs = False
                elif move.endCol == 7:
                    self.currentCastlingRight.wks = False
        elif move.pieceCaptured == 'bR':
            if move.endRow == 0:
                if move.endCol == 0:
                    self.currentCastlingRight.bqs = False
                elif move.endCol == 7:
                    self.currentCastlingRight.bks = False
         
    def getValidMoves(self):
        tempEnpassantPossible = self.enpassantPossible
        tempCastleRights = CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                        self.currentCastlingRight.wqs, self.currentCastlingRight.bqs)
        # for log in self.castleRightsLog:
        #     print(log.wks, log.wqs, log.bks, log.bqs, end = ", ")
        # print()
        #1 Generate all possible move
        moves = self.getAllPossibleMoves()
        
        # print(tempCastleRights.wks, tempCastleRights.bks, tempCastleRights.wqs, tempCastleRights.bqs)
        
        if self.whiteToMove:
            self.getCastleMoves(self.whiteKingLocation[0], self.whiteKingLocation[1], moves)
        else:
            self.getCastleMoves(self.blackKingLocation[0], self.blackKingLocation[1], moves)
        #2 for each move, make move
        for i in range(len(moves)-1, -1, -1):
            self.makeMove(moves[i])
            #3 generate all openent move
            #4 for each your oppent move, see if they attack your kings
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
                #5 if they attack your king, it invalid
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undoMove()
            
        if len(moves) == 0:
            if self.inCheck():
                self.checkMate = True
            else:
                self.staleMate = True
        else:
            self.checkMate = False
            self.staleMate = False
        
        self.enpassantPossible = tempEnpassantPossible  
        self.currentCastlingRight = tempCastleRights 
        
        return moves

    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])
        
    def squareUnderAttack(self, r, c):
        self.whiteToMove = not self.whiteToMove
        oppMoves = self.getAllPossibleMoves()
        for move in oppMoves:
            if move.endRow == r and move.endCol == c:
                self.whiteToMove = not self.whiteToMove
                return True
        self.whiteToMove = not self.whiteToMove
        return False

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0] # First character 'black' or 'white' or '-'
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1] # piece 
                    self.moveFunction[piece](r, c, moves)
        return moves
    # Get All posible of piece
    def getPawnMoves(self, r, c,moves):
        if self.whiteToMove: # White Turn
            if self.board[r-1][c] == "--": #1 square pawn advance
                moves.append(Move((r,c), (r-1,c), self.board))
                if r == 6 and self.board[r-2][c] == "--": #2 square pawn advance
                    moves.append(Move((r,c),(r-2,c),self.board))
            
            if c-1 >= 0: # capture left
                if self.board[r-1][c-1][0] == 'b': # enemy
                    moves.append(Move((r,c),(r-1,c-1),self.board))
                elif (r-1,c-1) == self.enpassantPossible:
                    moves.append(Move((r,c),(r-1,c-1),self.board, isEnpassantMove=True))
                   
            if c+1 < 8: # capture right
                if self.board[r-1][c+1][0] == 'b': # enemy
                    moves.append(Move((r,c),(r-1,c+1),self.board))
                elif (r-1,c+1) == self.enpassantPossible:
                    moves.append(Move((r,c),(r-1,c+1),self.board, isEnpassantMove=True))
            # print("in side")
            # print(self.board)
        else: # Black TUrn
            if self.board[r+1][c] == "--": #1 square pawn advance
                moves.append(Move((r,c), (r+1,c), self.board))
                if r == 1 and self.board[r+2][c] == "--": #2 square pawn advance
                    moves.append(Move((r,c),(r+2,c),self.board))
            if c-1 >= 0: # capture left
                if self.board[r+1][c-1][0] == 'w': # enemy
                    moves.append(Move((r,c),(r+1,c-1),self.board))
                elif (r+1,c-1) == self.enpassantPossible:
                    moves.append(Move((r,c),(r+1,c-1),self.board, isEnpassantMove=True))
                    
            if c+1 < 8: # capture right
                if self.board[r+1][c+1][0] == 'w': # enemy
                    moves.append(Move((r,c),(r+1,c+1),self.board))
                elif (r+1,c+1) == self.enpassantPossible:
                    moves.append(Move((r,c),(r+1,c+1),self.board, isEnpassantMove=True))
                
    def getRookMoves(self, r, c, moves):
        directions = ((-1,0),(0,-1),(1,0),(0,1))
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1,8):
                endRow = r + d[0]*i
                endCol = c + d[1]*i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        # print("me", (r,c),endPiece[0])
                        # print(endRow, endCol)
                        # print("enemy", enemyColor)
                        # print(endPiece)
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                    elif endPiece[0] == enemyColor:
                        # print("me", (r,c),endPiece[0])
                        # print(endRow, endCol)
                        # print("enemy", enemyColor)
                        # print(endPiece)
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                        break
                    else:
                        break
                else:
                    break
        
    
    def getKnightMoves(self, r, c, moves):
        KnightMoves = ((-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1))
        meColor = "w" if self.whiteToMove else "b"
        for m in KnightMoves:
            endRow = r + m[0]
            endCol = c + m[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != meColor:
                    moves.append(Move((r,c),(endRow,endCol),self.board))
            
    
    def getBishopMoves(self, r, c, moves):
        directions = ((-1,1),(1,-1),(1,1),(-1,-1))
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1,8):
                endRow = r + d[0]*i
                endCol = c + d[1]*i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                    elif endPiece[0] == enemyColor:
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                        break
                    else:
                        break
                else:
                    break
    
    def getKingMoves(self, r, c, moves):
        KingMoves = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        meColor = "w" if self.whiteToMove else "b"
        for i in range(8):
            endRow = r + KingMoves[i][0]
            endCol = c + KingMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != meColor:
                    moves.append(Move((r,c),(endRow,endCol),self.board)) 
        # self.getCastleMoves(r,c, moves, meColor)
    def getQueenMoves(self, r, c, moves):
        self.getRookMoves(r,c,moves)
        self.getBishopMoves(r,c,moves)
    
    # Generate all valid castle move for the king at (r,c) and add them to the list moves
    
    def getCastleMoves(self,r,c,moves):
        if self.squareUnderAttack(r,c):
            return # can't castle while we are in check
        if (self.whiteToMove and self.currentCastlingRight.wks) or (not self.whiteToMove and self.currentCastlingRight.bks):
            self.getKingsideCastleMoves(r,c,moves)
        if (self.whiteToMove and self.currentCastlingRight.wqs) or (not self.whiteToMove and self.currentCastlingRight.bqs):
            self.getQueensideCastleMoves(r,c,moves)
        
    def getKingsideCastleMoves(self, r, c, moves):
        if self.board[r][c+1] == "--" and self.board[r][c+2] == "--":
            if not self.squareUnderAttack(r,c+1) and not self.squareUnderAttack(r,c+2):
                moves.append(Move((r,c), (r,c+2), self.board, isCastleMove = True))
    
    def getQueensideCastleMoves(self, r, c, moves):
        if self.board[r][c-1] == "--" and self.board[r][c-2] == "--" and self.board[r][c-3] == "--":
            if not self.squareUnderAttack(r,c-1) and not self.squareUnderAttack(r,c-2):
                moves.append(Move((r,c), (r,c-2), self.board, isCastleMove = True))
    
class CastleRights():
    def __init__(self, wks, bks, wqs, bqs):
        self.wks = wks
        self.bks = bks
        self.wqs = wqs
        self.bqs = bqs
    
class Move():
    ranksToRows = {
        "1": 7, "2": 6, "3": 5, "4": 4,
        "5": 3, "6": 2, "7": 1, "8": 0,
    }
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {
        "a": 0, "b": 1, "c": 2, "d": 3,
        "e": 4, "f": 5, "g": 6, "h": 7
    }
    
    colsToFiles = {v: k for k, v in filesToCols.items()}
    
    def __init__(self, startSq, endSq, board, isEnpassantMove = False,isCastleMove= False):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        #Pawn promotion
        self.isPawnPromotion = False
        if (self.pieceMoved == 'wp' and self.endRow == 0) or (self.pieceMoved == 'bp' and self.endRow == 7):
            self.isPawnPromotion = True
        
        #Enpassant    
        self.isEnpassantMove = isEnpassantMove
        if self.isEnpassantMove:
            self.pieceCaptured = 'wp' if self.pieceCaptured == 'bp' else 'bp'
        
        #Castle Move
        self.isCastleMove = isCastleMove    
            
        self.isCapture = self.pieceCaptured != '--'
        self.moveID = self.startRow * 1000 + self.startCol*100 + self.endRow*10 + self.endCol
        
    def __repr__(self) -> str:
        return(f"[Start{self.startRow, self.startCol}, End{self.endRow, self.endCol}]")    

    def getChesNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
        

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False
    
    def __str__(self) -> str:
        if self.isCastleMove:
            return "O-O" if self.endCol == 6 else "O-O-O"
        
        endSquare = self.getRankFile(self.endRow, self.endCol)
        
        if self.pieceMoved[1] == 'p':
            if self.isCapture:
                return self.colsToFiles[self.startCol] + "x" + endSquare
            else:
                return endSquare
            
            
        
        
        moveString = self.pieceMoved[1]
        if self.isCapture:
            moveString += 'x'
        return moveString + endSquare