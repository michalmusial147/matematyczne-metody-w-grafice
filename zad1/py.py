import sys

import pygame
from pygame.locals import *

import OpenGL.GL
import OpenGL.GLU

m_transX = 0
m_transY = 0
m_angle1 = 0
m_angle2 = 0

display = (800, 600)

RedSurface = ( 1.0, 0.0, 0.0, 1.0)
GreenSurface = (0.0, 1.0, 0.0, 1.0)
BlueSurface = (0.0, 0.0, 1.0, 1.0)
LightAmbient = (0.1, 0.1, 0.1, 0.1)
LightDiffuse = (0.7, 0.7, 0.7, 0.7)
LightSpecular = (0.0, 0.0, 0.0, 0.1)
LightPosition = (5.0, 5.0, 5.0, 0.0)

vertices = [
    (-1, -1,  1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1,  1,  1),
    (-1, -1, -1),
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1)
]

colors = [
    BlueSurface,
    GreenSurface,
    RedSurface,
    RedSurface,
    GreenSurface,
    BlueSurface
]

indices = [
    4, 5, 6, 7,
    0, 4, 7, 3,
    0, 1, 5, 4,
    3, 2, 6, 7,
    1, 5, 6, 2,
    0, 1, 2, 3
]

normals = [
    ( 0,  0, -1),
    (-1,  0,  0),
    ( 0, -1,  0),
    ( 0,  1,  0),
    ( 1,  0,  0),
    ( 0,  0,  1)
]

def drawCube():
    glPushMatrix()
    glRotated(-m_angle2, 1, 0, 0)
    glRotated(-m_angle1, 0, 1, 0)
    glTranslatef(m_transX / 1000, m_transY / 1000, 0)
    for row in range(0, 6):
        glNormal3fv(normals[row])
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, colors[row])

        glBegin(GL_POLYGON)
        for col in range(0, 4):
            vertex = vertices[indices[row * 4 + col]]
            glVertex3f(vertex[0], vertex[1], vertex[2])
        glEnd()
    glPopMatrix()


# Main
pygame.init()
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 1.0, 10.0)

glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -5.0)

glDrawBuffer(GL_BACK)

glEnable(GL_LIGHTING)
glEnable(GL_DEPTH_TEST)

m_RightDownPos = (0, 0)
m_LeftDownPos = (0, 0)
m_RightButtonDown = False
m_LeftButtonDown = False

glLight(GL_LIGHT0, GL_POSITION, LightPosition)
glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmbient)
glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiffuse)
glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpecular)
glEnable(GL_LIGHT0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEMOTION:
            if m_LeftButtonDown:
                m_angle1 += m_LeftDownPos[0] - event.pos[0]
                m_angle2 += m_LeftDownPos[1] - event.pos[1]
                m_LeftDownPos = event.pos
            elif m_RightButtonDown:
                m_transX -= m_RightDownPos[0] - event.pos[0]
                m_transY += m_RightDownPos[1] - event.pos[1]
                m_RightDownPos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                m_LeftButtonDown = True
                m_LeftDownPos=event.pos
            elif event.button == 3:
                m_RightButtonDown = True
                m_RightDownPos=event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                m_LeftButtonDown = False
            elif event.button == 3:
                m_RightButtonDown = False

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glRotated(1, 3, 1, 1)

    drawCube()

    pygame.display.flip()
    pygame.time.wait(10)
