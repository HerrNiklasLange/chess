# Thus class is responsible for string the information about the current state of a chess game.


class GameState():
    def __init__(self):
        # board is 8 * 8 2d list, each elemt of the list has 2 characters,
        # the first character represents the color w or b
        # the second character represents the type of piece

        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]

        self.whiteToMove = True
        self.moveLog = []
    #Takes amvoe as a parameter and executes it (this will) not work got castling)
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # logs move 
        self.whiteToMove = not self.whiteToMove #switches turns
    #undo last move it is not working
    def undoMove(self):
        if len(self.moveLog) != 0:  # make sure that there is a move to undo
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove  # swap players


    #all moves considering check
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    # all moves without considering
    def getAllPossibleMoves(self):
        moves = [Move((6,4),(4,4),self.board)]
        for r in range(len(self.board)): #number of rows
            for c in range(len(self.board[r])): #number of cols
                turn = self.board[r][c][0]
                if (turn == "w" and self.whiteToMove) and (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == "P":
                        self.getPawnMoves(r,c,moves)
                    elif piece == "R":
                        self.getRookMoves(r,c,moves)
        return moves
                   
                   
    '''
    Get all the moves
    '''
    #get pawn moves
    def getPawnMoves(self,r,c, moves):
        pass
    #get rook moves     
    def getRookMoves(self,r,c, moves):
        pass
class Move():
    #maps keys to values
    # key : value
    rankToRows = {"1":7,"2":6,"3":5,"4":4,
                "5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v:k for k,v in rankToRows.items()}#reverse row
    
    fileToCols = {"a": 0,"b":1,"c":2,"d":3,"e":4,
                "f":5,"g":6,"h":7}
    colsToFiles = {v: k for k, v in fileToCols.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol *100 + self.endRow * 10 + self.endCol

    '''
    Overriding the equals method
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        return  self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow,self.endCol)
    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]