#main drive file
from operator import truediv
from pickle import TRUE
import pygame as p
# from chess 
import chess_engine

WIDTH = HEIGHT = 400
DIMENSION = 8 #dimension of the board is 8*8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initializing a global dictionary of images, onyl once
'''

def loadImages():
    pieces = ['bN','bP','bK','bB','bQ','bR','wP','wB','wK','wN','wQ','wR']
    for piece in pieces:
        IMAGES[piece] =  p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE ))
'''

'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = chess_engine.GameState()
    loadImages()

    valid_moves = gs.getValidMoves()
    moveMade = False #flags variable when a move is made
    running = True
    sqSelected = () # no squares is selected
    playerClicks = []#keeps track of player clicks
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
              running = False
            #mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()#x y location of mouse
                col = location[0]//SQ_SIZE
                row =location[1]//SQ_SIZE
                if sqSelected == (row,col): #the user clicked the same space
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append for both first and secnd click
                if len(playerClicks) == 2: #after two clicks
                    move = chess_engine.Move(playerClicks[0],playerClicks[1], gs.board)
                    #print(move.getChessNotation)
                    if move in valid_moves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = () #resets rows
                    playerClicks = []
            #key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_a: # undo moves when z is presse
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            valid_moves = gs.getValidMoves
            moveMade = False 
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


#draws squares
def drawBoard(screen):
    colors= [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
#draws pieces on current game state
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)

main()