import pygame
import os
import random

pygame.init()

#Settings
Screen_Height = 600
Screen_Width = 1100
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

Running = [pygame.image.load(os.path.join("CS_project", "Girl_run1.png")), 
           pygame.image.load(os.path.join("CS_project", "Girl_run2.png"))]
Jumping = pygame.image.load(os.path.join("CS_project", "Girl_stand_jump.png"))
Ducking = [pygame.image.load(os.path.join("CS_project", "Girl_duck2.png")), 
           pygame.image.load(os.path.join("CS_project", "Girl_duck1.png"))]

Small_Log = pygame.image.load(os.path.join("CS_project", "LogSmall.png"))
Large_Cactus = pygame.image.load(os.path.join("CS_project", "LogLarge.png"))
Snail = pygame.image.load(os.path.join("CS_project", "Snail.png"))

Bird = [pygame.image.load(os.path.join("CS_project", "Bird1.png")), 
           pygame.image.load(os.path.join("CS_project", "Bird2.png"))]
Vine = pygame.image.load(os.path.join("CS_project", "Vine.png"))

Background = pygame.image.load(os.path.join("CS_project", "Setting_background.png"))
Foreground = pygame.image.load(os.path.join("CS_project", "Setting_foreground.png"))

class Girl:
    X_Pos = 80
    Y_Pos = 310
    Y_Pos_Duck = 328
    Jump_Velocity = 8.5

    def __init__(self):
        self.duck_img = Ducking
        self.run_img = Running
        self.jump_img = Jumping

        self.girl_duck = False
        self.girl_run = True
        self.girl_jump = False

        self.step_index = 0
        self.jump_vel = self.Jump_Velocity
        self.image = self.run_img[0]
        self.girl_rect = self.image.get_rect()
        self.girl_rect.x = self.X_Pos
        self.girl_rect.y = self.Y_Pos

    def update(self, userInput):
        if self.girl_duck:
            self.duck()
        if self.girl_run:
            self.run()
        if self.girl_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_UP] and not self.girl_jump:
            self.girl_duck = False
            self.girl_run = False
            self.girl_jump = True
        elif userInput[pygame.K_DOWN] and not self.girl_jump:
            self.girl_duck = True
            self.girl_run = False
            self.girl_jump = False
        elif not (self.girl_jump or userInput[pygame.K_DOWN]):
            self.girl_duck = False
            self.girl_run = True
            self.girl_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.girl_rect = self.image.get_rect()
        self.girl_rect.x = self.X_Pos
        self.girl_rect.y = self.Y_Pos_Duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.girl_rect = self.image.get_rect()
        self.girl_rect.x = self.X_Pos
        self.girl_rect.y = self.Y_Pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.girl_jump:
            self.girl_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.Jump_Velocity:
            self.girl_jump = False
            self.jump_vel = self.Jump_Velocity


    def draw(self, Screen):
        Screen.blit(self.image, (self.girl_rect.x, self.girl_rect.y))


def main():
    global game_speed, x_pos_set, y_pos_set
    run = True
    clock = pygame.time.Clock()
    player = Girl()
    game_speed = 14
    x_pos_set = 0
    y_pos_set = 240

    def background():
        global x_pos_set, y_pos_set
        image_width = Background.get_width()
        Screen.blit(Background, (x_pos_set, y_pos_set))
        Screen.blit(Background, (image_width + x_pos_set, y_pos_set))
        if x_pos_set <= -image_width:
            Screen.blit(Background, (image_width + x_pos_set, y_pos_set))
            x_pos_set = 0
        x_pos_set -= game_speed - 10

    def foreground():
        global x_pos_set, y_pos_set
        image_width = Foreground.get_width()
        Screen.blit(Foreground, (x_pos_set, y_pos_set))
        Screen.blit(Foreground, (image_width + x_pos_set, y_pos_set))
        if x_pos_set <= -image_width:
            Screen.blit(Foreground, (image_width + x_pos_set, y_pos_set))
            x_pos_set = 0
        x_pos_set -= game_speed

    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Screen.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        background()
        foreground()
        
        player.draw(Screen)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    main()