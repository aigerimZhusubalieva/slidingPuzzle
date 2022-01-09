import os, random
path = os.getcwd()
NUM_ROWS = 4
NUM_COLS = 4
RESOLUTION = 800
TILE_WIDTH = RESOLUTION/NUM_COLS
TILE_HEIGHT = RESOLUTION/NUM_ROWS

class Tile:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.v = r * NUM_ROWS + c
        self.img = loadImage(path + "/images/" + str(self.v) + ".png")
    
    def display(self):
        image(self.img, self.c * TILE_WIDTH, self.r * TILE_HEIGHT)
        noFill()
        stroke(0, 0, 0)
        strokeWeight(5)
        rect(self.c * TILE_WIDTH, self.r * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        

class Puzzle(list):
    def __init__(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r,c))
    
    def display_tiles(self):
        for t in self:
            t.display()
        
        row = mouseY//TILE_WIDTH
        col = mouseX//TILE_HEIGHT
        stroke(0, 255, 0)
        noFill()
        rect(col * TILE_WIDTH, row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        

puzzle = Puzzle()

def setup():
    size(RESOLUTION, RESOLUTION)
    background(0, 0, 0)
    
def draw():
    background(0, 0, 0)
    puzzle.display_tiles()

    
    
