import numpy as np
from player import Player

class Board:
    def __init__(self) -> None:
        self.board = np.full((3, 3), "-", dtype=str)
        self.current_player = None
        
    def reset_board(self):
        self.board = np.full((3, 3), "-", dtype=str)
        self.current_player = None
        
    def _check_elements(self, elements):
        count = 0
        for element in elements:
            if element != self.current_player:
                break
            count += 1
            
        if count==3:
            return 1
        else:
            return 0
        
    def _check_dim(self):
        if not self.current_player:
            return 0
        
        for i in range(3):
            if self._check_elements(self.board[i,...]):
                return 1
            
            elif self._check_elements(self.board[...,i]):
                return 1
        
        if self._check_elements(self.board.diagonal()):
            return 1
        
        elif self._check_elements(np.fliplr(self.board).diagonal()):
            return 1
        
        else:
            return 0
        
    def board_interact(self, on:tuple, player:Player):
        self.current_player = player.get_symbol()
        self.board[on[0], on[1]] = self.current_player
        return self._check_dim()