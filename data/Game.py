"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""
import sys
sys.path.append('pygame')
import pygame
sys.path.append('data')
sys.path.append('data/font')
import Currency
import Grid
from Colors import *
import random
from CurrencyList import CUR_LIST
from FontHandler import *
import Vue

TILE_IMG_ONE = pygame.image.load("data/img/Tile1.png")
TILE_IMG_TWO = pygame.image.load("data/img/Tile2.png")

class game():
    def __init__(self,options):
        self.showText = options["Text Overlay"]
        self.currency = CUR_LIST[int(options["Currency"])]
        self.gameGrid = Grid.grid()
        
        pygame.init()

        self.score = 0
        self.play()

    def play(self):
        WINDOW_LENGHT = self.gameGrid.getTileMargin() + self.gameGrid.getRowLenght() * (self.gameGrid.getTileWidth() + self.gameGrid.getTileMargin()) + 400

        WINDOW_HEIGHT = self.gameGrid.getTileMargin() + self.gameGrid.getColumnLenght() * (self.gameGrid.getTileHeight() + self.gameGrid.getTileMargin())

        # Set the width and height of the screen [width, height]
        WINDOW_SIZE = [WINDOW_LENGHT , WINDOW_HEIGHT]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        self.vue = Vue.vue(screen,self.gameGrid)
        pygame.display.set_caption("Coin combiner: Level-1")

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        MARGIN = self.gameGrid.getTileMargin()
        WIDTH = self.gameGrid.getTileWidth()
        HEIGHT = self.gameGrid.getTileHeight()
        font = UIFONT
        fontC = makeFont(self.gameGrid.getTileWidth()/3)
        selCur = self.currency #selected self.

        dragging = False
        while not done:
            for event in pygame.event.get():  # User did something
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                if event.type == pygame.QUIT:  # If user clicked close
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    dragging = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    dragging = False
                    self.score += self.gameGrid.combine(row,column,selCur)
                    self.gameGrid.unselectAll()

                if dragging:
                    if row < self.gameGrid.getRowLenght():
                        if column < self.gameGrid.getColumnLenght():
                            if self.gameGrid.isSelect(row,column) == False:
                                self.gameGrid.setSelect(row,column,True)
                #print("Click ", pos, "Grid coordinates: ", row, column)


        # Set the screen background
            screen.fill(BLACK)




            # grid physics
            for row in range(self.gameGrid.getRowLenght()-1,-1,-1):
                for column in range(self.gameGrid.getColumnLenght()-1,-1,-1):
                    if self.gameGrid.getTileValue(row,column) > 0:
                        fallCoin = self.gameGrid.getTileValue(row,column)
                        if row < self.gameGrid.getColumnLenght()-1:
                            if self.gameGrid.getTileValue(row+1,column) == 0:
                                self.gameGrid.setTileValue(row+1,column,fallCoin)
                                self.gameGrid.setTileValue(row,column,0)

            # Generate raindom coins at the top
            for column in range(self.gameGrid.getColumnLenght()):
                if self.gameGrid.getTileValue(0,column) == 0:
                    randCoin = random.randrange(5)
                    self.gameGrid.setTileValue(0,column,randCoin)

            # Draw the grid
            for row in range(self.gameGrid.getRowLenght()):
                for column in range(self.gameGrid.getColumnLenght()):
                    if self.gameGrid.isSelect(row,column) == True:
                        color = YELLOW
                        pygame.draw.rect(screen,
                                    color,
                                    [(WIDTH + MARGIN) * column,
                                    (HEIGHT + MARGIN) * row,
                                    WIDTH + MARGIN *2,
                                    HEIGHT + MARGIN*2])
                    coin = selCur.getCoinById(self.gameGrid.getTileValue(row,column))
                    color = coin.getCol()
                    showText = self.showText
                    if not selCur.getCoinById(self.gameGrid.getTileValue(row,column)).getImg() == "":

                        self.vue.printEmptySquare(column,row)

                        if not self.gameGrid.getTileValue(row,column) == 0:
                            coin = selCur.getCoinById(self.gameGrid.getTileValue(row,column))
                            imgC = coin.getImg()
                            scale = coin.getScale()/100
                            imgC = pygame.transform.scale(imgC,(WIDTH,HEIGHT))
                            screen.blit(imgC,
                                            [
                                                ((MARGIN + WIDTH)* column + MARGIN),
                                                ((MARGIN + HEIGHT ) * row+ MARGIN),
                                            ])
                    else:
                        if self.gameGrid.getTileValue(row,column) == 0:
                            color = WHITE
                        pygame.draw.rect(screen,
                                        color,
                                        [(MARGIN + WIDTH) * column + MARGIN,
                                        (MARGIN + HEIGHT) * row + MARGIN,
                                        WIDTH,
                                        HEIGHT])
                        showText = "True"
                    if not self.gameGrid.getTileValue(row,column) == 0:
                        if coin.getVal() >= 100:
                            curType = selCur.getNType()
                            textC = fontC.render(str(coin.getVal()/100) + curType, True, BLACK,None)
                        else:
                            curType = selCur.getType()
                            textC = fontC.render(str(coin.getVal()) + curType, True, BLACK,None)
                        if showText == "True":
                            textRect = textC.get_rect()
                            textRect.center = (((MARGIN + WIDTH) * column + MARGIN ) + WIDTH/2, ((MARGIN + HEIGHT) * row + MARGIN) + HEIGHT/2)
                            screen.blit(textC, textRect)

            # Draw info

            X = WINDOW_LENGHT - 400 + 200
            Y = 20
            selMoney = str(format(self.gameGrid.getSelectedValue(selCur) / 100,'.2f'))
            nt = selCur.getNType()
            text = font.render('Score: ' + str(format(self.score / 100,'.2f'))  + nt, True, WHITE,BLACK)
            textRect = text.get_rect()
            textRect.center = (X, Y)
            screen.blit(text, textRect)
            text = font.render(selMoney + nt, True, WHITE,BLACK)
            textRect = text.get_rect()
            textRect.center = (pos[0]+20, pos[1] - 10)
            screen.blit(text, textRect)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)


#if __name__ == "__main__":
    #game()