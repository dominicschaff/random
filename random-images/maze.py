# create a CellStack (LIFO) to hold a list of cell locations
# set TotalCells = number of cells in grid
# choose a cell at random and call it CurrentCell
# set VisitedCells = 1

# while VisitedCells < TotalCells
#     find all neighbors of CurrentCell with all walls intact
#     if one or more found
#         choose one at random
#         knock down the wall between it and CurrentCell
#         push CurrentCell location on the CellStack
#         make the new cell CurrentCell
#         add 1 to VisitedCells
#     else
#         pop the most recent cell entry off the CellStack
#         make it CurrentCell
#     endIf
# endWhile
import random
from PIL import Image,ImageDraw

WIDTH,HEIGHT=150,100
NORTH,WEST,EAST,SOUTH=1,2,4,8
OPPOSITE = {
    NORTH:SOUTH,
    SOUTH:NORTH,
    WEST:EAST,
    EAST:WEST
}
DIRECTION_NAMES = {
    NORTH:"NORTH",
    SOUTH:"SOUTH",
    WEST:"WEST",
    EAST:"EAST"
}
CELL_SIZE=10

cellStack = []
cells = [[0 for y in xrange(HEIGHT)] for x in xrange(WIDTH)]
totalCells = WIDTH*HEIGHT
x,y = random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)
visitedCells = 1

while visitedCells < totalCells:
    openCells = []

    if y - 1 > -1 and cells[x][y-1] == 0:
        openCells.append([x,y-1, SOUTH])

    if x + 1 < WIDTH and cells[x+1][y] == 0:
        openCells.append([x+1,y, EAST])

    if x - 1 > -1 and cells[x-1][y] == 0:
        openCells.append([x-1,y, WEST])

    if y + 1 < HEIGHT and cells[x][y+1] == 0:
        openCells.append([x,y+1, NORTH])

    if len(openCells) > 0:
        newCell = random.choice(openCells)
        cells[x][y] |= newCell[2]
        cells[newCell[0]][newCell[1]] |= OPPOSITE[newCell[2]]
        cellStack.append([x,y])
        visitedCells+=1
        # print "Knock Down: @(%d,%d) wall: %s"%(x,y,DIRECTION_NAMES[newCell[2]])
        x,y = newCell[0],newCell[1]
        # print "Knock Down: @(%d,%d) wall: %s"%(x,y,DIRECTION_NAMES[OPPOSITE[newCell[2]]])
    else:
        x,y = cellStack.pop()

image = Image.new("RGB", (CELL_SIZE * (WIDTH+2), CELL_SIZE * (HEIGHT+2)), (0,0,0))
draw = ImageDraw.Draw(image)

for j in xrange(HEIGHT):
    for i in xrange(WIDTH):
        if cells[i][j] & SOUTH == SOUTH:
            draw.line((CELL_SIZE + i*CELL_SIZE, CELL_SIZE + j*CELL_SIZE) + (CELL_SIZE + i*CELL_SIZE + CELL_SIZE, CELL_SIZE + j*CELL_SIZE), fill=(0,0,255))
        if cells[i][j] & EAST == EAST:
            draw.line((CELL_SIZE + i*CELL_SIZE+CELL_SIZE, CELL_SIZE + j*CELL_SIZE) + (CELL_SIZE + i*CELL_SIZE+CELL_SIZE, CELL_SIZE + j*CELL_SIZE+ CELL_SIZE), fill=(0,0,255))
        if cells[i][j] & WEST == WEST:
            draw.line((CELL_SIZE + i*CELL_SIZE, CELL_SIZE + j*CELL_SIZE) + (CELL_SIZE + i*CELL_SIZE, CELL_SIZE + j*CELL_SIZE + CELL_SIZE), fill=(0,0,255))
        if cells[i][j] & NORTH == NORTH:
            draw.line((CELL_SIZE + i*CELL_SIZE, CELL_SIZE + j*CELL_SIZE + CELL_SIZE) + (CELL_SIZE + i*CELL_SIZE + CELL_SIZE, CELL_SIZE + j*CELL_SIZE + CELL_SIZE), fill=(0,0,255))

image.show("Title", "eom")