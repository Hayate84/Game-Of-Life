from random import randint

class Game_of_life(object):

    def __init__(self, rows, cols):

        self.ALIVE = 1
        self.DEAD  = 0

        self._board = []

        self._rows  = rows
        self._cols  = cols

        for _ in range(rows):

            row = [randint(self.DEAD, self.ALIVE) for _ in range(cols)]
            self._board.append(row)

    def _get_neighbors(self, i, j):
        
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

        return self._board

    def next_time_step(self):

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

        if cell == self.ALIVE:
            return self._alive_rules(neighbors)
        else:
            return self._dead_rules(neighbors)
              
    def _alive_rules(self, neighbors):

        if neighbors == 3 or neighbors == 2:    return self.ALIVE
        else:                                   return self.DEAD

    def _dead_rules(self, neighbors):

        if neighbors == 3:  return self.ALIVE
        else:               return self.DEAD
