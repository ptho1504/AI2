import pygame as p 
import ChessEngine 
import SmartMoveFinder


WIDTH = HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = HEIGHT
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

IMAGES = {}


def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ" ]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece +".png"), (SQ_SIZE, SQ_SIZE))
    

def main():
    p.init()
    screen = p.display.set_mode((WIDTH + 1*MOVE_LOG_PANEL_WIDTH, HEIGHT))
    clock  = p.time.Clock()
    # Rect = p.Rect(MOVE_LOG_PANEL_WIDTH, 0, WIDTH, HEIGHT)
    screen.fill(p.Color("white"))
    moveLogFont = p.font.SysFont("Arial", 16, False, False)
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False # flag v when a move is made
    animate = False
    loadImages()
    running = True
    sqSelected = () # No sq is selected, keep track of the last click of the user
    playerClicks = [] # Keep track of player clicks ([(6,4)->(4,4)])
    gameOver = False
    playerOne = False # A human is playing white, then this will true. If AI playing, then False
    playerTwo = False # Same as above but for black
    
    while running:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False 
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    
                    if sqSelected == (row,col) or col >= 8: # double click on same square
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row,col)
                        # print(sqSelected)
                        playerClicks.append(sqSelected)
                        if gs.board[playerClicks[0][0]][playerClicks[0][1]] == "--":
                            sqSelected = ()  # Reset the sqSelected value.
                            playerClicks = []  # Reset the playerClicks list.
                        
                    if len(playerClicks) == 2:
                        move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                        print(move.getChesNotation())
                        for i in range(len(validMoves)):
                            
                            if move == validMoves[i]:
                                # print("")
                                # print("out side")
                                # print(gs.board)
                                # print("Move out side", move)
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                animate = True
                                # print(gs.board)
                                sqSelected = ()  # Reset the sqSelected value.
                                playerClicks = []  # Reset the playerClicks list.
                        if not moveMade:
                            playerClicks = [sqSelected]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #Undo with press 'z'
                    gs.undoMove()
                    moveMade = True
                    animate = False
                    gameOver = False
                if e.key == p.K_r: #Reset the board press 'r'
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False
                    
        # AI move finder
        if not gameOver and not humanTurn:
            if   gs.whiteToMove: # White use Level 1
                AIMove = SmartMoveFinder.findLevel(gs,validMoves,3)
                if AIMove is None:
                    AIMove = SmartMoveFinder.findRandomMove(validMoves)
                gs.makeMove(AIMove)
                moveMade = True
                animate = True
            elif not   gs.whiteToMove: # Black use Level 2
                AIMove = SmartMoveFinder.findLevel(gs, validMoves, 2)
                # AIMove = SmartMoveFinder.findBestMoveMinMax(gs, validMoves, 2)
                if AIMove is None:
                    AIMove = SmartMoveFinder.findRandomMove(validMoves)
                gs.makeMove(AIMove)
                moveMade = True
                animate = True
            
        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            validMoves = gs.getValidMoves()
            # print(validMoves)
            moveMade = False
            animate = False
            
        drawGameState(screen, gs, validMoves, sqSelected, moveLogFont)
        
        if gs.checkMate or gs.staleMate:
            gameOver = True
            if gs.staleMate:
                text = "Stalemate"
            else:
                if gs.whiteToMove:
                    text = "Black wins by checkmate Press R to reset"
                    # drawEndGameText(screen, "Black wins by checkmate Press R to reset")
                else:
                    text = "White wins by checkmate Press R to reset"
                    # drawEndGameText(screen, "White wins by checkmate Press R to reset")
            drawEndGameText(screen,text)
            
            
            
        
        clock.tick(MAX_FPS)
        p.display.flip()


def highlightSquares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            # highlight selected square
            s = p.Surface((SQ_SIZE,SQ_SIZE))
            s.set_alpha(100) # transparent value -> 0
            s.fill(p.Color('blue'))
            screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
            #hightlight move from that square
            s.fill(p.Color('yellow'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (SQ_SIZE*move.endCol, SQ_SIZE*move.endRow))
            
def drawGameState(screen, gs, validMoves, sqSelected, moveLogFont ):
    drawBoard(screen) # Draw square on board
    drawPieces(screen, gs.board) # Draw piece
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawMoveLog(screen, gs, moveLogFont)
    # drawInstruction(screen, gs, moveLogFont )
    
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawMoveLog(screen, gs, font):
    moveLogRect = p.Rect(WIDTH, 0, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT)
    p.draw.rect(screen, p.Color("black"), moveLogRect)
    moveLog = gs.moveLog
    moveTexts = []
    
    for i in range(0, len(moveLog), 2):
        moveString = str(i//2 + 1) + ". " + str(moveLog[i]) + " "
        if i + 1 < len(moveLog):
            moveString += str(moveLog[i+1]) + "   "
        moveTexts.append(moveString)
    
    movesPerRow = 3
    padding = 5
    textY = padding
    lineSpacing = 2
    for i in range(0, len(moveTexts), movesPerRow):
        text = ""
        for j in range(movesPerRow):
            if i + j < len(moveTexts):
                text += moveTexts[i+j]
        textObject = font.render(text, True, p.Color('white'))
        textLocation = moveLogRect.move(padding, textY)
        screen.blit(textObject, textLocation)
        textY += textObject.get_height() + lineSpacing

def drawInstruction(screen, gs, instruction):
    moveLogRect = p.Rect(MOVE_LOG_PANEL_WIDTH+WIDTH, 0, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT)
    
    p.draw.rect(screen, p.Color("red"), moveLogRect)
    
    
def animateMove(move, screen, board, clock):
    colors = [p.Color("white"), p.Color("gray")]
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 10
    frameCount = (abs(dR) + abs(dC))*framesPerSquare
    for frame in range(frameCount + 1):
        r,c = (move.startRow + dR*frame/frameCount,move.startCol + dC*frame/frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        #erase the piece move from its ending
        color = colors[(move.endRow + move.endCol)%2]
        endSquare = p.Rect(move.endCol*SQ_SIZE, move.endRow*SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, color, endSquare)
        #draw capture piece
        # if move.pieceCaptured != "--":
        #     if move.isEnpassantMove:
        #         enPassantRow = (move.endRow + 1) if move.pieceCaptured[0] == 'b' else (move.endRow-1)
        #         endSquare = p.Rect(move.endCol*SQ_SIZE, enPassantRow*SQ_SIZE, SQ_SIZE, SQ_SIZE)
        #     screen.blit(IMAGES[move.pieceMoved], endSquare)
        #draw moving piece
        screen.blit(IMAGES[move.pieceMoved], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        p.display.flip()
        clock.tick(60)
        
def drawEndGameText(screen, text):
    font = p.font.SysFont("Helvitca", 32, True, False)
    textObject = font.render(text, 0, p.Color('Gray'))
    textLocation = p.Rect(0,0,WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject, textLocation)
    textObject = font.render(text, 0, p.Color("Black"))
    screen.blit(textObject, textLocation.move(2,2))



if __name__ == "__main__":
    main()