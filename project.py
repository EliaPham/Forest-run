import pygame
import os

pygame.init()

#Settings
Screen_Height = 600
Screen_Width = 1100
Screen = pygame.display.set_mode(Screen_Width, Screen_Height)

Running = [pygame.image.load(os.path.join("Girl_run1.png")), 
           pygame.image.load(os.path.join("Girl_run2.png"))]
Jumping = pygame.image.load(os.path.join("Girl_stand_jump.png"))
Ducking = [pygame.image.load(os.path.join("Girl_duck1.png")), 
           pygame.image.load(os.path.join("Girl_duck2.png"))]

Small_Log = pygame.image.load(os.path.join("LogSmall.png"))
Large_Cactus = pygame.image.load(os.path.join("LogLarge.png"))
Snail = pygame.image.load(os.path.join("Snail.png"))

Bird = [pygame.image.load(os.path.join("Bird1.png")), 
           pygame.image.load(os.path.join("Bird2.png"))]
Vine = pygame.image.load(os.path.join("Vine.png"))

Background = pygame.image.load(os.path.join("Setting_background.png"))
Foreground = pygame.image.load(os.path.join("Setting_foreground.png"))