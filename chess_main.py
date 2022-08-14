#main drive file
from operator import truediv
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
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
              running = False
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