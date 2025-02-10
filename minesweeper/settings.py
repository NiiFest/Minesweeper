import pygame
import os


# colors
white = (255,255,255)
black = (0,0,0)
dgrey = (150,150,150)
grey = (30,30,30)
green = (0,255,0)
dgreen = (0,180,0)
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)

#screen size 
tile_size = 32
rows = 15 
cols = 15
WIDTH = tile_size * rows
HEIGHT = tile_size * cols

number_of_mines = 16
FPS = 60

tile_numbers = []
for i in range(1,9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join('games/minesweeper/Sprites',f'Tile{i}.png')), (tile_size,tile_size)))
    
tile_empty = pygame.transform.scale(
        pygame.image.load(os.path.join('games/minesweeper/Sprites',f'TileEmpty.png')), (tile_size,tile_size))

tile_exploded = pygame.transform.scale(
        pygame.image.load(os.path.join('games/minesweeper/Sprites',f'TileExploded.png')), (tile_size,tile_size))

tile_flag = pygame.transform.scale(
        pygame.image.load(os.path.join('games/minesweeper/Sprites',f'TileFlag.png')), (tile_size,tile_size))

tile_mine = pygame.transform.scale(
        pygame.image.load(os.path.join('games/minesweeper/Sprites',f'TileMine.png')), (tile_size,tile_size))

tile_unknown = pygame.transform.scale(
        pygame.image.load(os.path.join('games/minesweeper/Sprites',f'TileUnknown.png')), (tile_size,tile_size))

tile_not_mine = pygame.transform.scale(
        pygame.image.load(os.path.join('games/minesweeper/Sprites',f'TileNotMine.png')), (tile_size,tile_size))


