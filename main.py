import pygame, sys, math, random
from pygame import Vector2

height = 900
width = 1000
fps = 60

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def line(start_pos, end_pos, w = 1, col = 'brown'):
    pygame.draw.line(screen, col, start_pos, end_pos, w)
    pygame.display.flip()


def circle(cent, rad, col = 'white', w = 1):
    pygame.draw.circle(screen, col, cent, rad, w)

def draw_main_branch():
    stp = [width/2, height]
    enp = [width/2, height-180]
    line(stp, enp, 10)

def draw_fractal_tree(stp, angle, len, w, angle_count):

    if len < 5:
        return

    angle = (angle + 1) % 360

    vec = len * math.cos(math.radians(angle) + math.radians(angle_count)), len * -math.sin(math.radians(angle) + math.radians(angle_count))
    enp = stp[0] + vec[0], stp[1] + vec[1]

    line(stp, enp, w, 'green' if w == 1 and len <= 7 else 'brown')
    draw_fractal_tree(enp, angle, int(len*0.825), int(w*0.9) if w > 1 else 1, angle_count + angle)

    vec = len * math.cos(-math.radians(angle) + math.radians(angle_count)), len * -math.sin(-math.radians(angle) + math.radians(angle_count))
    enp = stp[0] + vec[0], stp[1] + vec[1]

    line(stp, enp, w, 'green' if w == 1 and len <= 7 else 'brown')
    draw_fractal_tree(enp, angle, int(len*0.825), int(w*0.9) if w > 1 else 1, angle_count - angle)

angle = 15

screen.fill('white')

draw_main_branch()
draw_fractal_tree([width/2, height-180], angle, int(180*0.55), 10, 90)

pygame.image.save(screen, "tree_demo.png")

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()