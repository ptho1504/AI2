import pygame as p 
import ChessEngine 

WIDTH = HEIGHT = 512
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
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock  = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False # flag v when a move is made
    loadImages()
    running = True
    sqSelected = () # No sq is selected, keep track of the last click of the user
    playerClicks = [] # Keep track of player clicks ([(6,4)->(4,4)])
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False 
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                
                if sqSelected == (row,col): # double click on same square
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
                    if move in validMoves:
                        # print("Move valids", validMoves)
                        # print("")
                        gs.makeMove(move)
                        moveMade = True
                        # print(gs.board)
                        sqSelected = ()  # Reset the sqSelected value.
                        playerClicks = []  # Reset the playerClicks list.
                    else:
                        playerClicks = [sqSelected]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #Undo with press 'z'
                    gs.undoMove()
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()
            # print(validMoves)
            moveMade = False
            
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()



def drawGameState(screen, gs):
    drawBoard(screen) # Draw square on board
    drawPieces(screen, gs.board) # Draw piece
    
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

 


if __name__ == "__main__":
    main()