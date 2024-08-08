import pygame
from planet import Planet
import pandas as pd

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

planets = []

def get_planets_from_csv():
    df = pd.read_csv('planet_data.csv')

    no_planets = df.shape[0]

    for i in range(no_planets):
        planets.append(Planet(df['x'][i], df['y'][i], df['velocity'][i], df['mass'][i], (df['colorR'][i], df['colorG'][i], df['colorB'][i]), df['max_width'][i], df['max_height'][i]))


def draw_planets():

    for planet in planets:
        pygame.draw.circle(win, planet.color, (planet.x, planet.y), planet.mass)

get_planets_from_csv()
print(planets[0].color)

while run:

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    draw_planets()
    pygame.display.update()
    

pygame.quit()