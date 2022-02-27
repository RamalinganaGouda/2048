import pygame
import time
import random

WINDOW = 400
TILESIZE = 100
HEIGHT = WINDOW
WIDTH = WINDOW

grid = []

background = (0,0,0)
boundaries = (20,20,20)
tile = ((20,20,20), #2 tile
        (40,40,40), #4 tile
        (60,60,60), #8 tile
        (80,80,80), #16 tile
        (100,100,100), #32 tile
        (120,120,120), #64 tile
        (160,160,160), #128 tile
        (180,180,180), #256 tile
        (200,200,200), #512 tile
        (220,220,220), #1024 tile
        (240,240,240)) #2048 tile
rows = int(WINDOW / TILESIZE)
columns = rows

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(background)
pygame.display.set_caption('2048')


class Tile():
    def __init__(self, x, y, tilesize):
        self.x = x
        self.y = y
        self.number = 0
        self.color = background
        self.rect = 0
        self.neighbors = []
        self.tilesize = tilesize
        self.display = display #not efficient

    def show(self):
        self.rect = pygame.Rect(self.x * self.tilesize,
                                self.y * self.tilesize,
                                self.tilesize,
                                self.tilesize)
        if(self.number == 0):
            pygame.draw.rect(display, boundaries, self.rect, 5)
        if(self.number == 2):
            pygame.draw.rect(display, tile[0], self.rect, 0)
        if (self.number == 4):
            pygame.draw.rect(display, tile[1], self.rect, 0)
        if (self.number == 8):
            pygame.draw.rect(display, tile[2], self.rect, 0)
        if (self.number == 16):
            pygame.draw.rect(display, tile[3], self.rect, 0)
        if (self.number == 32):
            pygame.draw.rect(display, tile[4], self.rect, 0)
        if (self.number == 64):
            pygame.draw.rect(display, tile[5], self.rect, 0)
        if (self.number == 128):
            pygame.draw.rect(display, tile[6], self.rect, 0)
        if (self.number == 256):
            pygame.draw.rect(display, tile[7], self.rect, 0)
        if (self.number == 512):
            pygame.draw.rect(display, tile[8], self.rect, 0)
        if (self.number == 1024):
            pygame.draw.rect(display, tile[9], self.rect, 0)
        if (self.number == 2048):
            pygame.draw.rect(display, tile[10], self.rect, 0)

        if(self.number != 0):
            display.blit(pygame.font.SysFont('Arial', 25).render(ascii(self.number), True, (255, 255, 255)),
                         (self.x * self.tilesize + int(self.tilesize / 2) - 12,
                          self.y * self.tilesize + int(self.tilesize / 2) - 12))
        else:
            display.blit(pygame.font.SysFont('Arial', 25).render('', True, (255, 255, 255)),
                         (self.x * self.tilesize + int(self.tilesize / 2) - 12,
                          self.y * self.tilesize + int(self.tilesize / 2) - 12))

def genRadomTile():
    retry = 0
    while retry < rows*columns:
        row = random.randrange(0, rows, 1)
        col = random.randrange(0, columns, 1)
        if grid[row][col].number == 0:
            grid[row][col].number = (random.randrange(1, 2, 1)*2)
            return
        retry += 1

def processUp(grid):
    #hard coding this part
    for i in range(columns):
        list = []
        for j in range(rows):
            list.append(grid[j][i].number)

        for j in range(rows - 1):
            if ((list[j] != 0) and (list[j] == list[j + 1])):
                list[j] *= 2
                del list[j + 1]
                list.append(0)

        list = [k for k in list if k != 0]
        for _ in range(rows - len(list)):
            list.append(0)

        for j in range(rows):
            grid[j][i].number = list[j]


def processDown(grid):
    #hard coding this part
    for i in range(columns):
        list = []
        for j in range(rows):
            list.append(grid[j][i].number)

        for j in range(rows - 1):
            if ((list[j] != 0) and (list[j] == list[j + 1])):
                list[j] *= 2
                del list[j + 1]
                list.append(0)

        list = [k for k in list if k != 0]
        list.reverse()
        for _ in range(rows - len(list)):
            list.append(0)

        list.reverse()
        for j in range(rows):
            grid[j][i].number = list[j]
def processLeft(grid):
    #hard coding this part
    for i in range(rows):
        list = []
        for j in range(columns):
            list.append(grid[i][j].number)

        for j in range(columns - 1):
            if ((list[j] != 0) and (list[j] == list[j + 1])):
                list[j] *= 2
                del list[j + 1]
                list.append(0)

        list = [k for k in list if k != 0]
        for _ in range(columns - len(list)):
            list.append(0)

        for j in range(columns):
            grid[i][j].number = list[j]

def processRight(grid):
    #hard coding this part
    for i in range(rows):
        list = []
        for j in range(columns):
            list.append(grid[i][j].number)

        for j in range(columns - 1):
            if ((list[j] != 0) and (list[j] == list[j + 1])):
                list[j] *= 2
                del list[j + 1]
                list.append(0)

        list = [k for k in list if k != 0]
        list.reverse()
        for _ in range(columns - len(list)):
            list.append(0)
        print('before', list)
        list.reverse()
        print('after', list)

        for j in range(columns):
            grid[i][j].number = list[j]


def updateGrid(grid):
    for i in range(rows):
        for j in range(columns):
            grid[i][j].show()

def main():

    #create grid
    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(Tile(j, i, TILESIZE))
        grid.append(row)

    for i in range(rows):
        for j in range(columns):
            grid[i][j].show()

    genRadomTile()
    genRadomTile()

    while True:
        updateGrid(grid)
        pygame.display.update()
        time.sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left")
                    processLeft(grid)
                if event.key == pygame.K_RIGHT:
                    print("right")
                    processRight(grid)
                if event.key == pygame.K_UP:
                    print("up")
                    processUp(grid)
                if event.key == pygame.K_DOWN:
                    print("down")
                    processDown(grid)

                genRadomTile()
                display.fill(background)











if __name__ == "__main__":
    main()