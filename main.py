import pygame
import sys

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

paddle2_position_y = screen_height / 2
paddle_position_y = screen_height / 2
paddle_offset = 50

paddle_height = 100
paddle_width = 10

vertical1 = 0
vertical2 = 0

ball_height = 10
ball_width = 10

ball_position_x = screen_width / 2
ball_position_y = screen_height / 2
ball_vector_horizontal = 1
ball_vector_vertical = 1

speed = (screen_width / 2560) * (screen_width / 512)

paddle_1_score = 0
paddle_2_score = 0

myfont = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = myfont.render(str(paddle_1_score), False, black)
display.blit(text_surface, dest=(screen_width / 2,screen_height / 2))

while True:
    display.fill(white)
    pygame.draw.rect(display, black, (paddle_offset, paddle_position_y, 10, 100), 4)
    pygame.draw.rect(display, black, (screen_width - paddle_offset, paddle2_position_y, 10, 100), 4)
    pygame.draw.rect(display, black, (ball_position_x, ball_position_y, 10, 10), 4)
    pygame.display.update()

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit(); sys.exit();
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_s):
                vertical1 = 1
            if(event.key == pygame.K_w):
                vertical1 = -1
            if(event.key == pygame.K_DOWN):
                vertical2 = 1
            if(event.key == pygame.K_UP):
                vertical2 = -1
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_s):
                vertical1 = 0
            if(event.key == pygame.K_w):
                vertical1 = 0
            if(event.key == pygame.K_DOWN):
                vertical2 = 0
            if(event.key == pygame.K_UP):
                vertical2 = 0

    #Right Hand Paddle Collision
    if(ball_position_x > screen_width - paddle_offset - ball_width and ball_position_y > paddle2_position_y - paddle_height):
        ball_vector_horizontal = -ball_vector_horizontal
    #Left hand paddle Collision
    if(ball_position_x < paddle_offset + ball_width and ball_position_y > paddle_position_y - paddle_height):
        ball_vector_horizontal = -ball_vector_horizontal
    #Bottom wall
    if(ball_position_y >= screen_height - ball_height):
        ball_vector_vertical = -ball_vector_vertical
    #Top wall
    if(ball_position_y < 0):
        ball_vector_vertical = -ball_vector_vertical


    #cap paddle position
    if(paddle_position_y >= screen_height - paddle_height):
        paddle_position_y = screen_height - paddle_height
    if(paddle_position_y <= 0):
        paddle_position_y = 0
    if(paddle2_position_y <= 0):
        paddle2_position_y = 0
    if(paddle2_position_y >= screen_height - paddle_height):
        paddle2_position_y = screen_height  - paddle_height

    
    #paddle Movement
    paddle_position_y += vertical1 * speed / 5
    paddle2_position_y += vertical2 * speed / 5
    ball_position_x += ball_vector_horizontal * speed / 7
    ball_position_y += ball_vector_vertical * speed / 7