def place_mines(x,y, no_mines, board):
    
    mine_places = []
    
    for i in range(no_mines):
        while(1):
            mine_cell_x = rand() % x
            mine_cell_y = rang() % y
            
            if [mine_cell_x, mine_cell_y] not in mine_places:
                mine_places.append([mine_cell_x, mine_cell_y])
                adacent_cells = generate_cells_around(mine_cell_x, mine_cell_y)
                for cell in adacent_cells:
                    board[cell[0]][cell[y]] = board[cell[0]][cell[y]] + 1
                    
                break
                
            
        
    return mine_places, board
    
    
def check_mine(x,y,mine_places):
    if [x,y] in mine_places:
        return True
        
    else:
        return False
    
    

def generate_no_mines(x,y):
    return board[x][y]
