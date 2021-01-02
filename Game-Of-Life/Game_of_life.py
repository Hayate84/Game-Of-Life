from random import randint

class Game_of_life(object):

    """ Class that implements the rules of Conway's Game of Life """

    def __init__(self, rows, cols):

        self.ALIVE = 1
        self.DEAD  = 0
        
        #World is a 2x2 board with cell in position i, j 
        self._board = []

        self._rows  = rows
        self._cols  = cols

        for _ in range(rows):
            
            #create the initial cells a random 
            row = [randint(self.DEAD, self.ALIVE) for _ in range(cols)]
            self._board.append(row)

    def _get_neighbors(self, i, j):
        
        """ Count the neighbors of a cell in i, j position in the 2x2 board/world """

        board = self._board

        rows = self._rows 
        cols = self._cols 

        total_neighbors = 0
	
        if i + 1 < rows: total_neighbors += board[i + 1][j]
        if j + 1 < cols: total_neighbors += board[i][j + 1]
        
        if i - 1 >= 0:   total_neighbors += board[i - 1][j]
        if j - 1 >= 0:   total_neighbors += board[i][j - 1]

        if i - 1 >= 0   and j - 1 >= 0:    total_neighbors += board[i - 1][j - 1]
        if i + 1 < rows and j - 1 >= 0:    total_neighbors += board[i + 1][j - 1]
        if i + 1 < rows and j + 1 < cols:  total_neighbors += board[i + 1][j + 1]
        if i - 1 >= 0   and j + 1 < cols:  total_neighbors += board[i - 1][j + 1]

        return total_neighbors

    def get_board(self):

        """ Get method to get the 2x2 grid """

        return self._board

    def next_time_step(self):

        """ Update all the cells based on the rules """

        new_board = []
        old_board = self._board

        for i in range(self._rows):

            new_row = []
            
            for j in range(self._cols):

                current_neighbors = self._get_neighbors(i, j)

                cell = self._rules(old_board[i][j], current_neighbors)

                new_row.append(cell)

            new_board.append(new_row)

        self._board = new_board
                
    def _rules(self, cell, neighbors):
    
        """ Method to get the rules of the game based on if a cell is alive or dead """

        if cell == self.ALIVE: return self._alive_rules(neighbors)
        else:                  return self._dead_rules(neighbors)
              
    def _alive_rules(self, neighbors):
	
        """ Rules in case a cell is alive """

        if neighbors == 3 or neighbors == 2:    return self.ALIVE
        else:                                   return self.DEAD

    def _dead_rules(self, neighbors):

        """ Rules in case a cell is dead """

        if neighbors == 3:  return self.ALIVE
        else:               return self.DEAD
