import pygame as pg
from math import cos, sin

pg.init()
screen = pg.display.set_mode((500, 500))

vertex = [[63, 63 , 63], [63, -63, 63], [-63, -63, 63], 
          [-63, 63, 63], [63, 63, -63],[63, -63, -63],
          [-63, -63, -63],[-63, 63, -63]
          ]

edges = [[0, 1], [1, 2],[2, 3],[3, 0],[4, 5],[5, 6],
         [6, 7],[7, 4],[0, 4],[1, 5],[2, 6],[3, 7]
         ]

def projection(vertex, distance_to_screen, number):
    x = (vertex[number][0] * distance_to_screen) // abs(vertex[number][2] + distance_to_screen) + 250
    y = (vertex[number][1] * distance_to_screen) // abs(vertex[number][2] + distance_to_screen) + 250

    return [x, y]

def drawing(vertex, distance_to_screen, edges):
    for num in range(len(edges)):
        start = projection(vertex, distance_to_screen, edges[num][0])
        end = projection(vertex, distance_to_screen, edges[num][1])

        pg.draw.line(screen, (173, 216, 230), start, end)

def rotation_y(vertex, angle):
    for num in range(len(vertex)):
        x_new = vertex[num][2] * sin(angle) + vertex[num][0] * cos(angle) 
        y_new = vertex[num][1]
        z_new = vertex[num][2] * cos(angle) - vertex[num][0] * sin(angle) 
        vertex[num][0] = x_new
        vertex[num][1] = y_new
        vertex[num][2] = z_new
    
    return vertex

def rotation_x(vertex, angle):
    for num in range(len(vertex)):
        x_new = vertex[num][0] 
        y_new = vertex[num][1] * cos(angle) - vertex[num][2] * sin(angle)
        z_new = vertex[num][1] * sin(angle) + vertex[num][2] * cos(angle) 
        vertex[num][0] = x_new
        vertex[num][1] = y_new
        vertex[num][2] = z_new
    
    return vertex    

def rotation_z(vertex, angle):
    for num in range(len(vertex)):
        x_new = vertex[num][0] * cos(angle) - vertex[num][1] * sin(angle)
        y_new = vertex[num][0] * sin(angle) + vertex[num][1] * cos(angle)
        z_new = vertex[num][2] 
        vertex[num][0] = x_new
        vertex[num][1] = y_new
        vertex[num][2] = z_new
    
    return vertex 

def rotation(vertex, angle_y, angle_x, angle_z):
    vertex = rotation_y(vertex, angle_y)
    vertex = rotation_x(vertex, angle_x)
    vertex = rotation_z(vertex, angle_z)

    return vertex

clock = pg.time.Clock()

k = 150

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    screen.fill((0,0,0))
    vertex = rotation(vertex=vertex, angle_y=0.01, angle_x=0, angle_z=0)
    drawing(vertex=vertex, distance_to_screen=k, edges=edges)

    clock.tick(60)
    pg.display.flip()