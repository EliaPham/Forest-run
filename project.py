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

Small_Log = [pygame.image.load(os.path.join("CS_project", "LogSmall.png"))]
Large_Log = [pygame.image.load(os.path.join("CS_project", "LogLarge.png"))]
Snail = [pygame.image.load(os.path.join("CS_project", "Snail.png"))]

Bird = [pygame.image.load(os.path.join("CS_project", "Bird1.png")), 
        pygame.image.load(os.path.join("CS_project", "Bird2.png"))]
Vine = [pygame.image.load(os.path.join("CS_project", "Vine.png"))]

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

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = Screen_Width

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
                obstacles.pop()

    def draw(self, Screen):
        Screen.blit(self.image[self.type], self.rect)

class SmallLog(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeLog(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 300

class Birds(Obstacle):
    def __init__(self, image):
        super().__init__(image, 0)
        self.rect.y = 250
        self.index = 0

    def draw(self, Screen):
        if self.index >= 9:
            self.index = 0
        Screen.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_set, y_pos_set, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Girl()
    game_speed = 14
    x_pos_set = 0
    y_pos_set = 240
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        Screen.blit(text, textRect)
    

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

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallLog(Small_Log))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeLog(Large_Log))
            elif random.randint(0, 2) == 2:
                obstacles.append(Birds(Bird))

        for obstacle in obstacles:
            obstacle.draw(Screen)
            obstacle.update()
            if player.girl_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
                
        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        Screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key ro Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (Screen_Width // 2, Screen_Height // 2 + 50)
            Screen.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (Screen_Width // 2, Screen_Height // 2)
        Screen.blit(text, textRect)
        Screen.blit(Running[0], (Screen_Width // 2 - 20, Screen_Height // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


if __name__ == "__main__":
    menu(death_count=0)