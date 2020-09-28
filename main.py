import pygame
import sys
import random
import time

last_frame = 0

def Random_Vector():
    random_bool = random.randint(0, 1)
    if random_bool == 0:
        random_bool = -1
    return random_bool

pygame.init()

#Set favicon & title
favicon = pygame.image.load("images/favicon.png")
pygame.display.set_icon(favicon)
pygame.display.set_caption('PONG!')

#Set screen dimentions (scaleable)
screen_width = 512
screen_height = 256

display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.update()

white = (255, 255, 255)
black = (0,0,0)

speed = (screen_width / 2560) * (screen_width / 512)


myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Paddle:
    position_y = screen_height / 2
    offset = 50
    height = 100
    width = 10
    score = 0
    vertical_multiplier = 0

    def Draw(self, _color, _position_x):
        pygame.draw.rect(display, _color, (_position_x, self.position_y, 10, 100), 4)

class Ball:
    height = 10
    width = 10

    position_x = screen_width / 2
    position_y = screen_height / 2
    vector_horizontal = Random_Vector()
    vector_vertical = Random_Vector()

    def Draw(self, _color):
        pygame.draw.rect(display, _color, (self.position_x, self.position_y, 10, 10), 4)
        self.Move()
        self.Collision()

    def Collision(self):
        #Right Hand Paddle Collision
        if self.position_x > screen_width - paddle_2.offset - self.width and self.position_x < screen_width - paddle_2.offset + 0.1 and self.position_y > paddle_2.position_y and self.position_y < paddle_2.position_y + paddle_2.height:
            self.vector_horizontal = -self.vector_horizontal
        #Left hand paddle Collision
        if self.position_x <= paddle_1.offset + self.width and self.position_x >= paddle_1.offset + self.width - 0.1 and self.position_y > paddle_1.position_y and self.position_y < paddle_1.position_y + paddle_1.height:
            self.vector_horizontal = -self.vector_horizontal
        #Bottom wall
        if(self.position_y >= screen_height - self.height):
            self.vector_vertical = -self.vector_vertical
        #Top wall
        if self.position_y < 0 :
            self.vector_vertical = -self.vector_vertical

        if self.position_x < 0 or self.position_x > screen_width:
            self.position_x = screen_width / 2
            self.position_y = screen_height / 2
            self.vector_horizontal = Random_Vector()
            self.vector_vertical = Random_Vector()

    def Move(self):
        self.position_x += self.vector_horizontal * speed / 7
        self.position_y += self.vector_vertical * speed / 7 

paddle_1 = Paddle()
paddle_2 = Paddle()

ball = Ball()

while True:
    display.fill(white)
    #pygame.draw.rect(display, black, (paddle_1.offset, paddle_1.position_y, 10, 100), 4)
    paddle_1.Draw(black, paddle_1.offset)
    paddle_2.Draw(black, screen_width - paddle_2.offset)
    ball.Draw(black)


    pygame.display.update()

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit(); sys.exit();
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_s):
                paddle_1.vertical_multiplier = 1
            if(event.key == pygame.K_w):
                paddle_1.vertical_multiplier = -1
            if(event.key == pygame.K_DOWN):
                paddle_2.vertical_multiplier = 1
            if(event.key == pygame.K_UP):
                paddle_2.vertical_multiplier = -1
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_s):
                paddle_1.vertical_multiplier = 0
            if(event.key == pygame.K_w):
                paddle_1.vertical_multiplier = 0
            if(event.key == pygame.K_DOWN):
                paddle_2.vertical_multiplier = 0
            if(event.key == pygame.K_UP):
                paddle_2.vertical_multiplier = 0


    #cap paddle position
    if(paddle_1.position_y >= screen_height - paddle_1.height):
        paddle_1.position_y = screen_height - paddle_1.height
    if(paddle_1.position_y <= 0):
        paddle_1.position_y = 0
    if(paddle_2.position_y <= 0):
        paddle_2.position_y = 0
    if(paddle_2.position_y >= screen_height - paddle_2.height):
        paddle_2.position_y = screen_height  - paddle_2.height
    
        

    
    #paddle Movement
    paddle_1.position_y += paddle_1.vertical_multiplier * speed / 5 
    paddle_2.position_y += paddle_2.vertical_multiplier * speed / 5