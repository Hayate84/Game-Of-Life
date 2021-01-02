import pygame

class WindowData(object):
    
    """ Struct type Class for defining a pygame window """

    def __init__(self, logo_path, window_title):

        self.logo_path      = logo_path
        self.window_title   = window_title

class Engine(object):

    """ Base Class for a pygame program game """

    def __init__(self, width, height, window_data):

        pygame.init()

        self._width     = width
        self._height    = height

        self._set_window(window_data)

        self._screen = self._set_display()

        self._running = True

        self._clock = pygame.time.Clock()
        self._FPS   = 60

    def mainLoop(self):

        """ A pygame program has a main loop """

        while self._running:

            self._clock.tick(self._FPS)

            self._handleEvents()
         
            pygame.display.flip()
            
        pygame.quit()

    def _handleEvents(self):
        
        """ Method for handling inside the main loop various events """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:       self._running = False
            if event.type == pygame.KEYDOWN:    self._keyboardControls(event)

    def _keyboardControls(self, event):

        """ Method for handling keyboard presses """

        if event.key == pygame.K_ESCAPE:
            
            self._running = False
            
        else:
            
            return
        
    def _set_display(self):

        """ Method for setting the screen """

        return pygame.display.set_mode((self._width, self._height))

    def _set_window(self, window_data):
       
        """ Method for setting the window """    
    
        logo = pygame.image.load(window_data.logo_path)

        pygame.display.set_icon(logo)
        pygame.display.set_caption(window_data.window_title)
