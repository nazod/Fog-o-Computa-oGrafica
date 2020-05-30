import numpy as np
import pygame
from pygame.locals import *
from copy import copy

from OpenGL.GL import *
from OpenGL.GLU import *

import keyboard
import math

verticies = (
    ( 1, -1, -1), # 0
    ( 1,  1, -1), # 1
    (-1,  1, -1), # 2
    (-1, -1, -1), # 3

    ( 1, -1,  1), # 4
    ( 1,  1,  1), # 5
    (-1, -1,  1), # 6
    (-1,  1,  1)  # 7
    )


faces = (
    # Z negativo = (0, 1, 2, 3)
    (0, 1, 2, 3),
    # Z positivo = (4, 5, 6, 7)
    (4, 5, 7, 6),
    # Y negativo = (0, 3, 4, 6)
    (0, 3, 6, 4),
    # Y positivo = (1, 2, 5, 7)
    (1, 2, 7, 5),
    # X negativo = (2, 3, 6, 7)
    (2, 3, 6, 7),
    # X positivo = (0, 1, 4, 5)
    (0, 1, 5, 4)
    )

normals = (
    (0, 0, -1),
    (0, 0, 1),
    (0, -1, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (1, 0, 0),
)

face1 = (4, 5, 7, 6) #Z Positivo
normal1 = (0, 0, 1) #Z Positivo

face2 = (0, 1, 2, 3) #Z Negativo
normal2 = (0, 0, -1) #Z Negativo

face3 = (1, 2, 7, 5) #Y Positivo
normal3 = (0, 1, 0) #Y Positivo

face4 = (0, 3, 6, 4) #Y Negativo
normal4 = (0, -1, 0) #Y Negativo

face5 = (0, 1, 5, 4) #X Positivo
normal5 = (1, 0, 0) #X Positivo

face6 = (2, 3, 6, 7) #X Negativo
normal6 = (-1, 0, 0) #X Negativo

def retornaNovaFace(face, normal, texture = None):
    if not texture is None:
        glBindTexture(GL_TEXTURE_2D, texture)
    
    glBegin(GL_QUADS)
    texIndexes = [(1,0), (1,1), (0, 1), (0,0)] 
    glNormal3d(normal[0], normal[1], normal[2] )
    for vertex, texIndex in zip(face, texIndexes):
        if not texture is None:
             glTexCoord2f(texIndex[0], texIndex[1])  
        glVertex3fv(verticies[vertex]) 
    glEnd()


def retornaOsPesDoFogao():
    verticies = (
    ( 0.1, -0.1, -0.1), # 0
    ( 0.2,  0.1, -0.1), # 1
    (-0.1,  0.1, -0.1), # 2
    (-0.1, -0.1, -0.1), # 3

    ( 0.1, -0.1,  0.1), # 4
    ( 0.2,  0.1,  0.1), # 5
    (-0.1, -0.1,  0.1), # 6
    (-0.1,  0.1,  0.1)  # 7
    )


    glBegin(GL_QUADS)
    for face, normal in zip(faces, normals):
        glNormal3d(normal[0], normal[1], normal[2] )
        for vertex in face:
            glVertex3fv(verticies[vertex])  
    glEnd()
