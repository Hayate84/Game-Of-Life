from Engine import *

from Game_of_life import *

class Game(Engine):

    """ Class that visualizes Conway's Game of Life """

    BLACK = (255, 255, 255)
    WHITE = (0, 0, 0)
    
    def __init__(self, width, height, size_of_rectangles):

        window_data = WindowData("assets/images/logo32x32.png", "Game of Life")

        super().__init__(width, height, window_data)

        self._init_constants(size_of_rectangles)

        # More than 3 frames per second felt too fast
        self._FPS = 3
        
        self._rect_list = self._init_rectangle_list(self._width, self._height, self.SIZE_OF_RECTANGLES)

        self._game_of_life = Game_of_life(self.CELLS_HEIGHT, self.CELLS_WIDTH)

    def mainLoop(self):
    
        """ Main loop for drawing the dead alive cells in each frame """

        while self._running:

            self._clock.tick(self._FPS)

            self._handleEvents()

            self._Game_of_life_logic()
         
            pygame.display.flip()
            
        pygame.quit()

    def _Game_of_life_logic(self):

        """ The logic is: We map the 0,1 values of the 2x2 board to rectangles on the screen.
            Black (1) for alive cells 0 for dead """

        for i in range(self.CELLS_HEIGHT):
            for j in range(self.CELLS_WIDTH):

                current_rectangle = self._rect_list[i][j]
                    
                if self._game_of_life._board[i][j]:

                    pygame.draw.rect(self._screen, self.WHITE, current_rectangle)

                else:
                        
                    pygame.draw.rect(self._screen, self.BLACK, current_rectangle)

        # after drawing the screen compute the next timestep to draw
        self._game_of_life.next_time_step()

    def _init_rectangle_list(self, width, height, size):
        
        """ Method to map a 2x2 binary list into rectangles. Fills a 2x2 list with rectangles """
        
        rect_list = []

        # rows in screen are the y values of a pixel
        y = 0
        for i in range(height):
            
            rect_row = []

            # for every x column in the screen
            x = 0
            for j in range(width):
                
                r = pygame.Rect(x, y, size, size)
                
                rect_row.append(r)
                
                # offset the next value size rectangle
                x = x + size
                
            rect_list.append(rect_row)

            y = y + size
            
        return rect_list
                  
    def _keyboardControls(self, event):

        """ Controls for the game are: 
            r: To restart the simulation
            q: To quit """  

        if event.key == pygame.K_r:
            
            self._game_of_life = Game_of_life(self.CELLS_HEIGHT, self.CELLS_WIDTH)
            
        elif event.key == pygame.K_q:
            
            self._running = False
            
        else:
            
            return
        
    def _init_constants(self, size_of_rectangles):
        
        """ Class to compute the constants we use in the program. Similar to a C++ initializer list """
        
        # Computations to fit the whole resolution with rectangles. Works best for remainder zero 
        self.CELLS_WIDTH  = self._width     // size_of_rectangles
        self.CELLS_HEIGHT = self._height    // size_of_rectangles

        # Size of rectangles must feel like a constant
        self.SIZE_OF_RECTANGLES = size_of_rectangles
        
if __name__== "__main__":

    """ Driver main """
    
    # In testing we liked a lot those values
    WIDTH  = 800
    HEIGHT = 600

    SIZE_OF_RECTANGLES = 10

    game = Game(WIDTH, HEIGHT, SIZE_OF_RECTANGLES)

    game.mainLoop()
