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