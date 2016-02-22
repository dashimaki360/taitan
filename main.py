# #!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
import shogi
import gui
import TAITAN


class main:
    def __init__(self):
        self.board = shogi.Board()  # Make board
        self.game = gui.ShogiGUI()  # Make shgoi GUI
        self.turn = 1  # Brack turn

    def start(self,p):
        self.game.LoadImages()  # Load piese images
    	print(self.board.kif_str())
        hoge = self.game.ConvertSfenToBoardAndHand(self.board.sfen())
        self.game.Draw(hoge[0], hoge[1])  # draw board to gui
        if(p == 1):
            self.ai = TAITAN.ai(-1)
        elif(p == -1):
            self.ai = TAITAN.ai(1)

    	#main loop
    	while(1):
            if(self.turn == p):
                self.human_input()
            else:
                com = self.ai.attack(self.board)
                print com
                self.board.push_usi(str(com))
    		print(self.board.kif_str())
            hoge = self.game.ConvertSfenToBoardAndHand(self.board.sfen())
            self.game.Draw(hoge[0], hoge[1])  # draw board to gui
            self.turn = self.turn*-1
            if(self.board.is_checkmate() == True):
                if(self.turn != p):
                    print "You Win"
                else:
                    print "Com Win"
                break

    def human_input(self):
        while(1):
            print "Please input your move"
            shogi_input = raw_input()
            chess_input = self.convert_input_shogi2chess(shogi_input)
            if(self.input_check(chess_input) == 0):
                self.board.push_usi(chess_input)
                break

    def convert_input_shogi2chess(self, shogi_input):
        if((len(shogi_input)>5) or (len(shogi_input)<4)):
            print "input length = " + str(len(shogi_input))
            return -1
        pieses = ('P','L','N','S','G','B','R','p','l','n','s','g','b','r')
        a = shogi_input[0].isdigit() and shogi_input[1].isdigit()
        b = shogi_input[0] in pieses and shogi_input[1] == '*'
        c = shogi_input[2].isdigit()
        d = shogi_input[3].isdigit()
        if  (a or b) and c and d :
            input_dict = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','*':'*'}
            chess_input = shogi_input
            chess_input = (shogi_input[0]+input_dict[shogi_input[1]]+shogi_input[2]+input_dict[shogi_input[3]])
            if len(shogi_input) is 5:
                chess_input = chess_input + '+'
            return chess_input
        else:
            print "your input is missing"
            return -1

    def input_check(self,p_input):
        if p_input == -1:
            return -1
    	if((len(p_input)>5) or (len(p_input)<4)):
    		print "input length = " + str(len(p_input))
    		return -1
    	if((shogi.Move.from_usi(p_input) in self.board.legal_moves) == False):
    		print "your input is not legal"
    		return -1
    	return 0



if __name__ == "__main__":
    game = main()
    print "Please input b(Brack) or w(White)"
    player = raw_input()
    if(player == 'b'):
        game.start(1)
    elif(player == 'w'):
        game.start(-1)
    
