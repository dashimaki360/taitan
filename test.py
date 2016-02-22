# #!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
import shogi
import random

board = shogi.Board()
moves = []
for move in board.legal_moves:
    moves.append(move)
print moves 
print board.legal_moves
print shogi.Move.from_usi("5g5f") in board.legal_moves
#print str(shogi.Move.from_usi("5g5f"))
moves = []
for move in board.legal_moves:
    moves.append(move)
next_move = random.choice(moves)
print moves