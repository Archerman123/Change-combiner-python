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
from CurrencyList import CAN_CUR
from FontHandler import *

def game(currency = CAN_CUR):

    gameGrid = Grid.grid()

    pygame.init()

    WINDOW_LENGHT = gameGrid.getTileMargin() + gameGrid.getRowLenght() * (gameGrid.getTileWidth() + gameGrid.getTileMargin()) + 400

    WINDOW_HEIGHT = gameGrid.getTileMargin() + gameGrid.getColumnLenght() * (gameGrid.getTileHeight() + gameGrid.getTileMargin())

    score = 0

    # Set the width and height of the screen [width, height]
    WINDOW_SIZE = [WINDOW_LENGHT , WINDOW_HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Grid game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    MARGIN = gameGrid.getTileMargin()
    WIDTH = gameGrid.getTileWidth()
    HEIGHT = gameGrid.getTileHeight()
    font = UIFONT
    fontC = makeFont(gameGrid.getTileWidth()/3)
    selCur = currency #selected currency

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
                score += gameGrid.combine(row,column,selCur)
                gameGrid.unselectAll()

            if dragging:
                if row < gameGrid.getRowLenght():
                    if column < gameGrid.getColumnLenght():
                        if gameGrid.isSelect(row,column) == False:
                            gameGrid.setSelect(row,column,True)
            #print("Click ", pos, "Grid coordinates: ", row, column)


    # Set the screen background
        screen.fill(BLACK)




        # grid physics
        for row in range(gameGrid.getRowLenght()-1,-1,-1):
            for column in range(gameGrid.getColumnLenght()-1,-1,-1):
                if gameGrid.getTileValue(row,column) > 0:
                    fallCoin = gameGrid.getTileValue(row,column)
                    if row < gameGrid.getColumnLenght()-1:
                        if gameGrid.getTileValue(row+1,column) == 0:
                            gameGrid.setTileValue(row+1,column,fallCoin)
                            gameGrid.setTileValue(row,column,0)

        # Generate raindom coins at the top
        for column in range(gameGrid.getColumnLenght()):
            if gameGrid.getTileValue(0,column) == 0:
                randCoin = random.randrange(5)
                gameGrid.setTileValue(0,column,randCoin)

        # Draw the grid
        for row in range(gameGrid.getRowLenght()):
            for column in range(gameGrid.getColumnLenght()):
                if gameGrid.isSelect(row,column) == True:
                    color = YELLOW
                    pygame.draw.rect(screen,
                                color,
                                [(WIDTH + MARGIN) * column,
                                (HEIGHT + MARGIN) * row,
                                WIDTH + MARGIN *2,
                                HEIGHT + MARGIN*2])
                coin = selCur.getCoinById(gameGrid.getTileValue(row,column))
                color = coin.getCol()


                if not selCur.getCoinById(gameGrid.getTileValue(row,column)).getImg() == "":
                    color = WHITE

                    pygame.draw.rect(screen,
                                    color,
                                    [(MARGIN + WIDTH) * column + MARGIN,
                                    (MARGIN + HEIGHT) * row + MARGIN,
                                    WIDTH,
                                    HEIGHT])
                    img = selCur.getCoinById(gameGrid.getTileValue(row,column)).getImg()
                    img = pygame.transform.scale(img, (WIDTH, HEIGHT))
                    screen.blit(img,[(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
                else:
                    if gameGrid.getTileValue(row,column) == 0:
                        color = WHITE

                    pygame.draw.rect(screen,
                                    color,
                                    [(MARGIN + WIDTH) * column + MARGIN,
                                    (MARGIN + HEIGHT) * row + MARGIN,
                                    WIDTH,
                                    HEIGHT])
                if not gameGrid.getTileValue(row,column) == 0:
                    if coin.getVal() >= 100:
                        curType = selCur.getNType()
                        textC = fontC.render(str(coin.getVal()/100) + curType, True, BLACK,None)
                    else:
                        curType = selCur.getType()
                        textC = fontC.render(str(coin.getVal()) + curType, True, BLACK,None)
                    textRect = textC.get_rect()
                    textRect.center = (((MARGIN + WIDTH) * column + MARGIN ) + WIDTH/2, ((MARGIN + HEIGHT) * row + MARGIN) + HEIGHT/2)
                    screen.blit(textC, textRect)




        # Draw info

        X = WINDOW_LENGHT - 400 + 200
        Y = 20
        selMoney = str(gameGrid.getSelectedValue(selCur) / 100)
        nt = selCur.getNType()
        text = font.render('Score: ' + str(score / 100)  + nt, True, WHITE,BLACK)
        textRect = text.get_rect()
        textRect.center = (X, Y)
        screen.blit(text, textRect)
        text = font.render('Current selection value: ' + selMoney + nt, True, WHITE,BLACK)
        textRect = text.get_rect()
        textRect.center = (X, Y + 50)
        screen.blit(text, textRect)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(30)


if __name__ == "__main__":
    game()