import pygame as p

p.init()
screen = p.display.set_mode((800, 600))
clock = p.time.Clock()
run = True

ball_x, ball_y = 400, 300
ball_radius = 25
ball_speed = 20

while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    pressed = p.key.get_pressed()
    if pressed[p.K_UP] and ball_y - ball_radius - ball_speed >= 0:
        ball_y -= ball_speed
    if pressed[p.K_DOWN] and ball_y + ball_radius + ball_speed <= 600:
        ball_y += ball_speed
    if pressed[p.K_LEFT] and ball_x - ball_radius - ball_speed >= 0:
        ball_x -= ball_speed
    if pressed[p.K_RIGHT] and ball_x + ball_radius + ball_speed <= 800:
        ball_x += ball_speed

    screen.fill((255, 255, 255))
    p.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
    p.display.flip()
    clock.tick(60)

p.quit()
