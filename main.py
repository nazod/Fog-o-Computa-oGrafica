#Feito por Hudson e Gabriel


import numpy as np
import pygame
from pygame.locals import *
from copy import copy

from OpenGL.GL import *
from OpenGL.GLU import *

import keyboard
import math

from carregaTextura import retornaTextura
from movimentacao import retornaMovimentacao
from iluminacao import retornaIluminacao
from fogao import *


fogaoTextura = [ "", "", "", "", "", ""]

	
def main():
    # Translação do cubo verde
    tx = 0
    ty = 0

    #UP vector angle = Pi/2 (90o) 
    up_angle = 3.1415/2

    
    rot_angle = 3.1415/2

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    retornaIluminacao()

    gluPerspective(45, (display[0]/display[1]), 0.1, 20.0)

    # eye = (0, 0, 10)
    eye = np.zeros(3)
    eye[2] = 10

    # target = (0, 0, 0)
    target = np.zeros(3)

    # up = (1, 0, 0)
    up = np.zeros(3)
    up[0] = 0
    up[1] = 1
    up[2] = 0

    up[1] = math.sin(up_angle)
    up[0] = math.cos(up_angle)


    fogaoTextura[0] = retornaTextura('Imagens/fogao-front.jpg')
    fogaoTextura[1] = retornaTextura('Imagens/fogao-left-right.jpg')
    fogaoTextura[2] = retornaTextura('Imagens/fogao-up.jpg')
    fogaoTextura[3] = retornaTextura('Imagens/fogao-left-right.jpg')
    fogaoTextura[4] = retornaTextura('Imagens/fogao-left-right.jpg')
    fogaoTextura[5] = retornaTextura('Imagens/fogao-left-right.jpg')
    
    while True:

        ty, tx, target, eye, up, up_angle, rot_angle = retornaMovimentacao(ty, tx, target, eye, up, up_angle, rot_angle)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        gluLookAt(eye[0], eye[1], eye[2], 
                target[0], target[1], target[2], 
	    	    up[0], up[1], up[2] )

        glPushMatrix()
        glTranslatef(tx,ty, 0.) #Monta as Faces do Fogão
        retornaNovaFace(face1, normal1, fogaoTextura[0]) # Z Positivo
        retornaNovaFace(face2, normal2, fogaoTextura[1]) # Z Negativo
        retornaNovaFace(face3, normal3, fogaoTextura[2]) # Y Positivo
        retornaNovaFace(face4, normal4, fogaoTextura[3]) # Y Negativo
        retornaNovaFace(face5, normal5, fogaoTextura[4]) # X Positivo
        retornaNovaFace(face6, normal6, fogaoTextura[5]) # X Negativo
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx,ty+2, 0.)
        retornaNovaFace(face2, normal2, fogaoTextura[5]) #Tampa do Fogão
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx-0.9,ty-1.1, 0.9)
        retornaOsPesDoFogao() #Pés do fogão
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx+0.9,ty-1.1, 0.9)
        glRotatef (180.0, 0.0, 1.0, 0.0)
        retornaOsPesDoFogao() #Pés do fogão
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx-0.9,ty-1.1, -0.9)
        retornaOsPesDoFogao() #Pés do fogão
        glPopMatrix()

        glPushMatrix()
        glTranslatef(tx+0.9,ty-1.1, -0.9)
        glRotatef (180.0, 0.0, 1.0, 0.0)
        retornaOsPesDoFogao() #Pés do fogão
        glPopMatrix()


        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()
