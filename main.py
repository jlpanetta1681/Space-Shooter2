import pygame
import os
import time
import random

pygame.font.init()

width, height = 750,750
WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption("Super Spacy Invaders")

# get our images into the file
RED_SPACE_SHIP = pygame.image.load(os.path.join("../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "pixel_ship_blue_small.png"))

# Yellow ship is player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "pixel_ship_yellow.png"))

# Lasers images
RED_LASER = pygame.image.load(os.path.join("../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "pixel_laser_yellow.png"))

# game backdrop
BG = pygame.transform.scale(pygame.image.load(os.path.join(
    "../../Desktop/Space-Shooter-Tutorial (1)/Space Shooter Tutorial/assets", "background-black.png")), (WIDTH, HEIGHT))
