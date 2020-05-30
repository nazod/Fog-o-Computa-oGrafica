import numpy as np
import pygame
from pygame.locals import *
from copy import copy

from OpenGL.GL import *
from OpenGL.GLU import *

import keyboard
import math


def retornaIluminacao():
    luzAmbiente=[0.1,0.1,0.1,1.0]
    luzDifusa=[0.7, 0.7, 0.7,1.0]     # "cor" 
    luzEspecular=[1.0, 1.0, 1.0, 1.0] # "brilho" 

    posicaoLuz=[5.0, 0.0, 0.0, 1.]

    # Capacidade de brilho do material
    especularidade =[1.0,1.0,1.0,1.0]
    # 1 a 128
    especMaterial = 1


    # Especifica que a cor de fundo da janela será preta
    glClearColor(0.1, 0.1, 0.1, 0.)

    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)

    # Define a refletância do material 
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    # Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente 
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )


    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )


    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    # Habilita a luz de número 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()