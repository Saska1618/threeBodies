import pygame
from planet import Planet
import pandas as pd
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

planets = []
trail_length = 200

def get_planets_from_csv():
    df = pd.read_csv('planet_data.csv')

    no_planets = df.shape[0]

    for i in range(no_planets):
        planets.append(Planet(df['x'][i], df['y'][i], df['velocity_x'][i], df['velocity_y'][i], df['mass'][i], (df['colorR'][i], df['colorG'][i], df['colorB'][i]), df['max_width'][i], df['max_height'][i]))

def draw_trails():
        for i in range(len(planets)):
            trail_color = (planets[i].color[0] // 2, planets[i].color[1] // 2, planets[i].color[2] // 2)
            if len(planets[i].trail) == trail_length:
                for j in range(len(planets[i].trail)-1):
                    #prev_x = planets[i].x - planets[i].trail[j - 1][0]
                    #prev_y = planets[i].y - planets[i].trail[j - 1][1]
                    pygame.draw.line(win, trail_color, (planets[i].trail[j][0], planets[i].trail[j][1]), (planets[i].trail[j+1][0], planets[i].trail[j+1][1]), 3)



def draw_planets():

    for planet in planets:
        pygame.draw.circle(win, planet.color, (planet.x, planet.y), planet.mass*10)

def update_planets():
    for i in range(len(planets)):
        total_force_x, total_force_y = 0, 0

        for j in range(len(planets)):
            if i != j:
                force_x, force_y = planets[i].get_gravitational_force(planets[j])

                total_force_x += force_x
                total_force_y += force_y

        planets[i].update_position(total_force_x, total_force_y)
        planets[i].trail.insert(0, (planets[i].x, planets[i].y))

        if len(planets[i].trail) >= trail_length:
            planets[i].trail = planets[i].trail[:trail_length]


get_planets_from_csv()

while run:

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    update_planets()

    draw_trails()
    draw_planets()
    pygame.display.update()
    

pygame.quit()