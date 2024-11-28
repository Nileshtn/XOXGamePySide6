class Player:
    def __init__(self, symbol, name) -> None:
        self.symbol = symbol
        self.name = name
        self.score = 0
        
    def get_symbol(self):
        return self.symbol
    
    def _check_board_occ(self, on, board):
        if board.board[on[0],on[1]] != "-":
            return 0
        return 1
    
    def play(self,board, pos, retry=False):
        check = self._check_board_occ(pos, board)
        if check:
            return check, board.board_interact(pos, self)
        
        return check, None

    def set_score(self, score:int):
        self.score += score
        
    def get_score(self):
        return self.score
    
    def reset_score(self):
        self.score = 0