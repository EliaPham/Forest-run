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

class Girl:
    X_Pos = 80
    Y_Pos = 310

    def __init__(self):
        self.duck_img = Ducking
        self.run_img = Running
        self.Jump_img = Jumping

        self.girl_duck = False
        self.girl_run = True
        self.girl_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.girl_rect = self.image.get_rect()
        self.girl_rect.x = self.X_Pos
        self.girl_rect.y = self.Y_Pos

def main():
    run = True
    clock = pygame.time.Clock()
    player = Girl()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Screen.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(Screen)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    main()