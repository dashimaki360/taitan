# #!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

import shogi
import random

class ai:
    def __init__(self,p):
        self.color = p

    def random_attack(self,board):
    	moves = []
    	for move in board.legal_moves:
	    	moves.append(move)
		next_move = random.choice(moves)
    	return next_move

    def attack(self,board):
    	moves = []
    	for move in board.legal_moves:
	    	moves.append(move)
	    	
	    	
	    	
	    	
		next_move = random.choice(moves)
    	return next_move
 
