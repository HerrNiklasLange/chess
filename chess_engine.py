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
    
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.move.append(move) # logs move
        self.whiteToMove = not self.whiteToMove #switches turns
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
        self.startRow = startSq[1]
        self.endRow = endSq[0]
        self.endRow = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return  self.getRankFile(self.startRow, self.startRow) + self.getRankFile(self.endRow,self.endCol)
    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks