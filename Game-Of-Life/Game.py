import pygame

from Game_of_life import *

class Game(object):

    WIDTH  = 800
    HEIGHT = 600

    CELLS_WIDTH  = 80
    CELLS_HEIGHT = 60

    SIZE_OF_RECTANGLES = 10

    BLACK = (255, 255, 255)
    WHITE = (0, 0, 0)

    LOGO_PATH       = "assets/images/logo32x32.png"
    WINDOW_TITLE    = "Game of Life"
    
    def __init__(self):

        pygame.init()

        self._set_window(self.LOGO_PATH, self.WINDOW_TITLE)

        self._screen = self._set_display(self.WIDTH, self.HEIGHT)

        self._running = True

        self._clock = pygame.time.Clock()
        self._FPS   = 3
        
        self._rect_list = self._init_rectangle_list(self.WIDTH, self.HEIGHT, self.SIZE_OF_RECTANGLES)

        self._game_of_life = Game_of_life(self.CELLS_HEIGHT, self.CELLS_WIDTH)

    def _set_window(self, logo_path, window_title):

        logo = pygame.image.load(logo_path)

        pygame.display.set_icon(logo)
        pygame.display.set_caption(window_title)

    def _set_display(self, width, height):

        return pygame.display.set_mode((width, height))

    def mainLoop(self):

        while self._running:

            self._clock.tick(self._FPS)

            self._handleEvents()

            self._Game_of_life_logic()
         
            pygame.display.flip()
            
        pygame.quit()

    def _Game_of_life_logic(self):

        for i in range(self.CELLS_HEIGHT):
            for j in range(self.CELLS_WIDTH):

                current_rectangle = self._rect_list[i][j]
                    
                if self._game_of_life._board[i][j]:

                    pygame.draw.rect(self._screen, self.WHITE, current_rectangle)

                else:
                        
                    pygame.draw.rect(self._screen, self.BLACK, current_rectangle)
                        
        self._game_of_life.next_time_step()

    def _init_rectangle_list(self, sum_x, sum_y, size):

        rect_list = []
        y = 0
        for i in range(sum_y):
            
            rect_row = []
            x = 0
            for j in range(sum_x):
                
                r = pygame.Rect(x, y, size, size)
                
                rect_row.append(r)
                
                x = x + size
                
            rect_list.append(rect_row)
            y = y + size
            
        return rect_list
    
    def _handleEvents(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:       self._running = False
            if event.type == pygame.KEYDOWN:    self._keyboardControls(event)
                  
    def _keyboardControls(self, event):

        if event.key == pygame.K_r:
            
            self._game_of_life = Game_of_life(self.CELLS_HEIGHT, self.CELLS_WIDTH)
            
        elif event.key == pygame.K_q:
            
            self._running = False
            
        else:
            
            return
        
if __name__== "__main__":

    game = Game()

    game.mainLoop()
