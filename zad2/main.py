import sys

import math

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

distance = 0.0
triangle_angle = 0.0

display = (800, 600)

colors = [
    (41.0/255.0, 128.0/255.0, 185.0/255.0),
    (243.0/255.0, 156.0/255.0, 18.0/255.0),
    (39.0/255.0, 174.0/255.0, 96.0/255.0),
    (155.0/255.0, 89.0/255.0, 182.0/255.0),
    (241.0/255.0, 196.0/255.0, 15.0/255.0),
    (192.0/255.0, 57.0/255.0, 43.0/255.0)
]

def drawTriangle(offset: tuple, color: tuple, isRotated: bool):
    glPushMatrix()
    glTranslatef(1 + offset[0], 1 + offset[1], 0)
    if isRotated:
        glRotatef(triangle_angle, 0, 0, 1)

    # Triangles
    glColor4f(color[0], color[1], color[2], 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-1, -1)
    glVertex2f( 2, -1)
    glVertex2f(-1,  2)
    glEnd()

    # Lines
    glColor4f(0, 0, 0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-1, -1)
    glVertex2f( 2, -1)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-1, -1)
    glVertex2f(-1,  2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f( 2, -1)
    glVertex2f(-1,  2)
    glEnd()
    glPopMatrix()


def drawQuarter(angle: float):
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    drawTriangle((0, 0), colors[0], True)
    drawTriangle((3, 0), colors[1], True)
    drawTriangle((0, 3), colors[2], True)
    drawTriangle((6, 0), colors[3], False)
    drawTriangle((3, 3), colors[4], False)
    drawTriangle((0, 6), colors[5], False)
    glPopMatrix()


# Main
pygame.init()
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 1.0, 64.0)

glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -28.0)
glRotated(-45, 1, 0, 0)

moveAway = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit(0)

    if distance <= 0:
        moveAway = True
    elif distance >= 9:
        moveAway = False

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glRotated(1, 0, 0, 1)

    drawQuarter(0)
    # drawQuarter(90)
    # drawQuarter(180)
    # drawQuarter(270)

    triangle_angle += -3

    # if moveAway:
    #     distance += 1/3600 * 9
    # else:
    #     distance -= 1/3600 * 9

    # print('Distance:', distance, 'Rotation:', round(distance * 10 / 9))

    pygame.display.flip()
    pygame.time.wait(10)
