import pygame as p
import datetime as d
import os

p.init()
screen = p.display.set_mode((800, 600))
clock = p.time.Clock()
run = True

base_path = r'C:\Users\TriumF\Desktop\Py works\LAB7'
body_path = os.path.join(base_path, 'body')
right_arm_path = os.path.join(base_path, 'right arm')
left_arm_path = os.path.join(base_path, 'Left arm')

def choose_file(folder, extension=".png"):
    files = [f for f in os.listdir(folder) if f.endswith(extension)]
    return os.path.join(folder, files[0]) if files else None

back = p.image.load(choose_file(body_path, ".jpg"))
r_hand = p.image.load(choose_file(right_arm_path))
l_hand = p.image.load(choose_file(left_arm_path))

now = d.datetime.now()
sec = now.second
seconds = -sec * 6
minn = now.minute
minutes = -minn * 6

print(sec, minn)
image_center = (400, 300)

while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    right_hand = p.transform.rotate(r_hand, minutes)
    minutes -= 1 / 600
    right = right_hand.get_rect(center=image_center)

    left_hand = p.transform.rotate(l_hand, seconds)
    seconds -= 1 / 10
    left = left_hand.get_rect(center=image_center)

    screen.blit(back, (0, 0))
    screen.blit(right_hand, right)
    screen.blit(left_hand, left)

    p.display.flip()
    clock.tick(60)

p.quit()
