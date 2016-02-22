#!/usr/bin/env python
#coding: utf-8
# yamaguchi takuya
# gui class for taitan
import pygame
import shogi
import os
import sys
from pygame.locals import *

class ShogiGUI:
    def __init__(self,graphicStyle=1):
        os.environ['SDL_VIDEO_CENTERED'] = '1' #should center pygame window on the screen
        pygame.init()
        pygame.display.init()
        self.piece_w = 40
        self.piece_h = 45
        self.window_margin = 50
        self.window_w = self.piece_w*9 + self.window_margin*2
        self.window_h = self.piece_h*11 + self.window_margin*2
        self.screen = pygame.display.set_mode((self.window_w,self.window_h))
        pygame.display.set_caption('TaiTan')
        self.fontDefault = pygame.font.Font( None, 20 )      

    def LoadImages(self):
            # "convert()" is supposed to help pygame display the images faster.
            # It seems to mess up transparency - makes it all black!
            # And, for this chess program, the images don't need to change that fast.
            self.P = pygame.image.load(os.path.join("images","P.png")) 
            self.R = pygame.image.load(os.path.join("images","R.png"))
            self.B = pygame.image.load(os.path.join("images","B.png"))
            self.K = pygame.image.load(os.path.join("images","K.png"))
            self.G = pygame.image.load(os.path.join("images","G.png"))
            self.S = pygame.image.load(os.path.join("images","S.png"))
            self.N = pygame.image.load(os.path.join("images","N.png"))
            self.L = pygame.image.load(os.path.join("images","L.png"))
            self.P_ = pygame.image.load(os.path.join("images","P+.png"))
            self.R_ = pygame.image.load(os.path.join("images","R+.png"))
            self.B_ = pygame.image.load(os.path.join("images","B+.png"))
            self.S_ = pygame.image.load(os.path.join("images","S+.png"))
            self.N_ = pygame.image.load(os.path.join("images","N+.png"))
            self.L_ = pygame.image.load(os.path.join("images","L+.png"))
            # resize pieces image
            self.P = pygame.transform.scale(self.P,(self.piece_w,self.piece_h))
            self.R = pygame.transform.scale(self.R,(self.piece_w,self.piece_h))
            self.B = pygame.transform.scale(self.B,(self.piece_w,self.piece_h))
            self.K = pygame.transform.scale(self.K,(self.piece_w,self.piece_h))
            self.G = pygame.transform.scale(self.G,(self.piece_w,self.piece_h))
            self.S = pygame.transform.scale(self.S,(self.piece_w,self.piece_h))
            self.N = pygame.transform.scale(self.N,(self.piece_w,self.piece_h))
            self.L = pygame.transform.scale(self.L,(self.piece_w,self.piece_h))
            self.P_ = pygame.transform.scale(self.P_,(self.piece_w,self.piece_h))
            self.R_ = pygame.transform.scale(self.R_,(self.piece_w,self.piece_h))
            self.B_ = pygame.transform.scale(self.B_,(self.piece_w,self.piece_h))
            self.S_ = pygame.transform.scale(self.S_,(self.piece_w,self.piece_h))
            self.N_ = pygame.transform.scale(self.N_,(self.piece_w,self.piece_h))
            self.L_ = pygame.transform.scale(self.L_,(self.piece_w,self.piece_h))
            # rotate pieces image
            self.p = pygame.transform.rotate(self.P,180)
            self.r = pygame.transform.rotate(self.R,180)
            self.b = pygame.transform.rotate(self.B,180)
            self.k = pygame.transform.rotate(self.K,180)
            self.g = pygame.transform.rotate(self.G,180)
            self.s = pygame.transform.rotate(self.S,180)
            self.n = pygame.transform.rotate(self.N,180)
            self.l = pygame.transform.rotate(self.L,180)
            self.p_ = pygame.transform.rotate(self.P_,180)
            self.r_ = pygame.transform.rotate(self.R_,180)
            self.b_ = pygame.transform.rotate(self.B_,180)
            self.s_ = pygame.transform.rotate(self.S_,180)
            self.n_ = pygame.transform.rotate(self.N_,180)
            self.l_ = pygame.transform.rotate(self.L_,180)
        
    def ConvertToScreenCoords(self,shogiSquareTuple):
        #converts a (col,row) chessSquare into the pixel location of the upper-left corner of the square
        (col,row) = shogiSquareTuple
        screenX = self.window_w - (self.window_margin + (col)*self.piece_w)
        screenY = (self.window_margin + (row) * self.piece_h)
        return (screenX,screenY)

    def ConvertToChessCoords(self,screenPositionTuple):
        #converts a screen pixel location (X,Y) into a (col,row)
        #x is horizontal, y is vertical
        (X,Y) = screenPositionTuple
        row = (Y-self.window_margin) / self.piece_h
        col = 9 - (X-self.window_margin) / self.piece_w
        return (col,row)

    def DrawHand(self,pieseInHand):
        # Draw piece in hands
        for j in range(2):
            for i in range(7):
                if pieseInHand[j][i] > 0:
                    if j == 0:
                        (screenX,screenY) = self.ConvertToScreenCoords((9-i,10))
                    else:
                        (screenX,screenY) = self.ConvertToScreenCoords((1+i,0))
                    if j == 0 and i == 0:
                        self.screen.blit(self.P,(screenX,screenY))
                    if j == 0 and i == 1:
                        self.screen.blit(self.L,(screenX,screenY))
                    if j == 0 and i == 2:
                        self.screen.blit(self.N,(screenX,screenY))
                    if j == 0 and i == 3:
                        self.screen.blit(self.S,(screenX,screenY))
                    if j == 0 and i == 4:
                        self.screen.blit(self.G,(screenX,screenY))
                    if j == 0 and i == 5:
                        self.screen.blit(self.B,(screenX,screenY))
                    if j == 0 and i == 6:
                        self.screen.blit(self.R,(screenX,screenY))
                    if j == 1 and i == 0:
                        self.screen.blit(self.p,(screenX,screenY))
                    if j == 1 and i == 1:
                        self.screen.blit(self.l,(screenX,screenY))
                    if j == 1 and i == 2:
                        self.screen.blit(self.n,(screenX,screenY))
                    if j == 1 and i == 3:
                        self.screen.blit(self.s,(screenX,screenY))
                    if j == 1 and i == 4:
                        self.screen.blit(self.g,(screenX,screenY))
                    if j == 1 and i == 5:
                        self.screen.blit(self.b,(screenX,screenY))
                    if j == 1 and i == 6:
                        self.screen.blit(self.r,(screenX,screenY))

    def DrawBoard(self,board):
        boardSize = len(board) 
        #board should be square.
        # boardSize should be always 8 for chess, but I dislike "magic numbers" :)  
        # draw pieces
        for r in range(boardSize):
            for c in range(boardSize):
                (screenX,screenY) = self.ConvertToScreenCoords((9-c, r+1))
                if board[r][c] == 'P':
                    self.screen.blit(self.P,(screenX,screenY))
                if board[r][c] == 'R':
                    self.screen.blit(self.R,(screenX,screenY))
                if board[r][c] == 'B':
                    self.screen.blit(self.B,(screenX,screenY))
                if board[r][c] == 'K':
                    self.screen.blit(self.K,(screenX,screenY))
                if board[r][c] == 'G':
                    self.screen.blit(self.G,(screenX,screenY))
                if board[r][c] == 'S':
                    self.screen.blit(self.S,(screenX,screenY))
                if board[r][c] == 'N':
                    self.screen.blit(self.N,(screenX,screenY))
                if board[r][c] == 'L':
                    self.screen.blit(self.L,(screenX,screenY))
                if board[r][c] == 'p':
                    self.screen.blit(self.p,(screenX,screenY))
                if board[r][c] == 'r':
                    self.screen.blit(self.r,(screenX,screenY))
                if board[r][c] == 'b':
                    self.screen.blit(self.b,(screenX,screenY))
                if board[r][c] == 'k':
                    self.screen.blit(self.k,(screenX,screenY))
                if board[r][c] == 'g':
                    self.screen.blit(self.g,(screenX,screenY))
                if board[r][c] == 's':
                    self.screen.blit(self.s,(screenX,screenY))
                if board[r][c] == 'n':
                    self.screen.blit(self.n,(screenX,screenY))
                if board[r][c] == 'l':
                    self.screen.blit(self.l,(screenX,screenY))
                if board[r][c] == 'P_':
                    self.screen.blit(self.P_,(screenX,screenY))
                if board[r][c] == 'R_':
                    self.screen.blit(self.R_,(screenX,screenY))
                if board[r][c] == 'B_':
                    self.screen.blit(self.B_,(screenX,screenY))
                if board[r][c] == 'S_':
                    self.screen.blit(self.S_,(screenX,screenY))
                if board[r][c] == 'N_':
                    self.screen.blit(self.N_,(screenX,screenY))
                if board[r][c] == 'L_':
                    self.screen.blit(self.L_,(screenX,screenY))
                if board[r][c] == 'p_':
                    self.screen.blit(self.p_,(screenX,screenY))
                if board[r][c] == 'r_':
                    self.screen.blit(self.r_,(screenX,screenY))
                if board[r][c] == 'b_':
                    self.screen.blit(self.b_,(screenX,screenY))
                if board[r][c] == 's_':
                    self.screen.blit(self.s_,(screenX,screenY))
                if board[r][c] == 'n_':
                    self.screen.blit(self.n_,(screenX,screenY))
                if board[r][c] == 'l_':
                    self.screen.blit(self.l_,(screenX,screenY))
    def ConvertSfenToBoardAndHand(self,sfen):
        # return (board, hand)
        [board, hand] = [ [[0 for i in range(9)] for j in range(9)], [[0 for i in range(7)] for j in range(2)]]  # initialize
        x = 0
        y = 0
        color = 0
        piese = 0
        isNari = False
        isHand = False
        for i in range(len(sfen)):
            if not isHand:
                if sfen[i] == u' ':
                    isHand = True
                elif not isHand and sfen[i] == u"/":  # check Row change
                    y += 1
                    x = 0
                    isNari = False
                elif not isHand and sfen[i] == u'+':  # check narigoma
                    isNari = True
                elif not isHand and sfen[i].isdigit():  # check number or not
                    for empty in range(int(sfen[i])):
                        board[y][x] = u'e'
                        x += 1
                    isNari = False
                else:
                    if isNari:
                        board[y][x] = sfen[i] + u'_'
                    else:
                        board[y][x] = sfen[i]
                    x += 1
                    isNari = False
            elif isHand:
                if sfen[i] == u'P':
                    hand[0][0] = sfen[i+1]
                elif sfen[i] == u'L':
                    hand[0][1] = sfen[i+1]
                elif sfen[i] == u'N':
                    hand[0][2] = sfen[i+1]
                elif sfen[i] == u'S':
                    hand[0][3] = sfen[i+1]
                elif sfen[i] == u'G':
                    hand[0][4] = sfen[i+1]
                elif sfen[i] == u'B':
                    hand[0][5] = sfen[i+1]
                elif sfen[i] == u'R':
                    hand[0][6] = sfen[i+1]
                elif sfen[i] == u'p':
                    hand[1][0] = sfen[i+1]
                elif sfen[i] == u'l':
                    hand[1][1] = sfen[i+1]
                elif sfen[i] == u'n':
                    hand[1][2] = sfen[i+1]
                elif sfen[i] == u's':
                    hand[1][3] = sfen[i+1]
                elif sfen[i] == u'g':
                    hand[1][4] = sfen[i+1]
                elif sfen[i] == u'b':
                    if sfen[i+1].isdigit():
                        hand[1][5] = sfen[i+1]
                elif sfen[i] == u'r':
                    hand[1][6] = sfen[i+1]
        return (board, hand)

    def Draw(self, board, pieseInHand):
        self.screen.fill((0,0,0))
        self.DrawBoard(board)
        self.DrawHand(pieseInHand)       
        pygame.display.flip()

    def EndGame(self,board,hand):
        print("Press any key to exit.")
        self.Draw(board,hand) #draw board to show end game status
        pygame.event.set_blocked(MOUSEMOTION)
        while 1:
            e = pygame.event.wait()
            if e.type is KEYDOWN:
                pygame.quit()
                sys.exit(0)
            if e.type is QUIT:
                pygame.quit()
                sys.exit(0)

    def InputHand(self):
        # returns (col,row)
        IsSquareChosen = False
        while not IsSquareChosen:
            squareClicked = []
            pygame.event.set_blocked(MOUSEMOTION)
            e = pygame.event.wait()
            if e.type is MOUSEBUTTONDOWN:
                (mouseX,mouseY) = pygame.mouse.get_pos()
                squareClicked = self.ConvertToChessCoords((mouseX,mouseY))
                IsSquareChosen = True
                if squareClicked[0]<0 or squareClicked[0]>10 or squareClicked[1]<0 or squareClicked[1]>10:
                    squareClicked = [] #not a valid chess square
                    IsSquareChosen = False
            if e.type is QUIT: #the "x" kill button
                pygame.quit()
                sys.exit(0)
        return squareClicked


if __name__ == "__main__":
    #try out some development / testing stuff if this file is run directly
    testBoard = [['l','n','s','g','k','g','s','n','l'],\
                 ['e','r','e','e','e','e','e','b','e'],\
                 ['p','p','p_','p','p','p','p','p','p'],\
                 ['e','e','e','e','e','e','e','e','e'],\
                 ['e','e','e','e','e','e','e','e','e'],\
                 ['e','e','e','e','e','e','e','e','e'],\
                 ['P','P','P_','P','P','P','P','P','P'],\
                 ['e','B','e','e','e','e','e','R','e'],\
                 ['L','N','S','G','K','G','S','N','L']]

                    #   P L N S G B R   [black, white]
    testPieseInHand = [[1,1,1,0,1,1,1],\
                       [1,0,1,1,0,1,1]]
    game = ShogiGUI()
    board = shogi.Board()
    game.LoadImages()
    print board.sfen()
    hoge = game.ConvertSfenToBoardAndHand(board.sfen())
    print hoge[0]
    print hoge[1]
    game.Draw(testBoard, testPieseInHand)  # draw board to gui
    # game.Draw(testBoard, testPieseInHand)
    # game.GetClickedSquare(game.InputHand())
    print game.InputHand()
    print game.InputHand()
    print game.InputHand()
    print game.InputHand()
    game.EndGame(hoge[0],hoge[1])
