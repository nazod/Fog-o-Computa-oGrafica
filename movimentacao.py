import numpy as np
import pygame
from pygame.locals import *
from copy import copy

from OpenGL.GL import *
from OpenGL.GLU import *

import keyboard
import math



# right = true or false
def move_target(eye, target, right):
    
    #translada a câmera para a origem
    t0 = target - eye

    #Ignora a componente Y
    t0[1] = 0

    #Calcula o raio do círculo
    r = math.sqrt(t0[0] * t0[0] + t0[2] * t0[2])
    
    #Calcula o seno e o cosseno e a tangente do ângulo que o vetor faz com o eixo X
    sin_alfa = t0[2]/r
    cos_alfa = t0[0]/r
    if cos_alfa == 0:
        if sin_alfa == 1:
            alfa  = math.pi/2
        else:
            alfa  = - math.pi/2
    else:
        tg_alfa = sin_alfa/cos_alfa

        #Calcula o arco cuja tangente é calculada no passo anterior
        alfa = np.arctan(tg_alfa)

        # Como o retorno de arctan varia somente entre -pi/2 e pi/2, testar o cosseno para 
        # calcular o ângulo correto
        if cos_alfa < 0:
            alfa = alfa -  math.pi
    
    if right:
        signal = 1
    else:
        signal = -1

    # Varia o ângulo do alvo (target)
    alfa = alfa + 0.1 * signal
    
    # Calcula o novo alvo (sobre o eixo Y)
    t0[0] = r * math.cos(alfa)
    t0[2] = r * math.sin(alfa)
    
    n_target = eye + t0

    return n_target

def move_can(eye, target, ahead):

    #equação paramétrica
    a = np.zeros(3)
    delta = 0.1
    p0 = eye
    p1 = target
    a = p1 - p0
    print('------------------------')    
    print(p1)
    print(p0)
    print(a)

    if ahead:
        signal = 1
    else:
        signal = -1
    p0 = p0 + delta * a * signal
    #p1 = p1 + delta * a * signal

    #Câmera sobre o plano (X, Z)
    #p0[1] = 0


    return p0, p1

def retornaMovimentacao(ty, tx, target, eye, up, up_angle, rot_angle):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif  event.type == pygame.KEYDOWN :
		# Movimentação do cubo
                if event.key==K_w:
                    ty = ty + 0.5
                elif event.key==K_z:
                    ty = ty - 0.5
                elif event.key==K_a:
                    tx = tx - 0.5
                elif event.key==K_s:
                    tx = tx + 0.5

		# Movimentação da direção da câmera 
		# nos eixos X e Y (olho)
                elif event.key==K_UP:
                    target[1] = target[1] + 0.5
                elif event.key==K_DOWN:
                    target[1] = target[1] - 0.5

                #move_target(eye, target, right):
                elif event.key==K_RIGHT:
                    target = move_target(eye, target, True)
                elif event.key==K_LEFT:
                    target = move_target(eye, target, False)

                elif event.key==K_PAGEUP:
                    #Mover para frente
                    eye, target = move_can(eye, target, True)
                    #eye[2] = eye[2] - 0.5
                elif event.key==K_PAGEDOWN:
                    #Mover para trás
                    eye, target = move_can(eye, target, False)
                    #eye[2] = eye[2] + 0.5

                elif event.key==K_t:
                    eye[0] = eye[0] - 0.5
                elif event.key==K_g:
                    eye[0] = eye[0] + 0.5

		# Movimentação da parte de cima da câmera (UP vector)
                elif event.key==K_PERIOD:
                    up_angle += 0.05
                    up[1] = math.sin(up_angle)
                    up[0] = math.cos(up_angle)
                elif event.key==K_COMMA:
                    up_angle -= 0.05
                    up[1] = math.sin(up_angle)
                    up[0] = math.cos(up_angle)


            elif event.type == pygame.MOUSEBUTTONDOWN:
                #eye_dist = math.sqrt(eye[0]*eye[0] + eye[1]*eye[1] +eye[2]*eye[2])
                eye_dist = math.sqrt(eye[0]*eye[0]  +eye[2]*eye[2])
                #print(eye, eye_dist)
                if event.button == 4:
                    rot_angle += 0.02
                    eye[2] = eye_dist * math.sin(rot_angle)
                    eye[0] = eye_dist * math.cos(rot_angle)

                if event.button == 5:
                    rot_angle -= 0.02
                    eye[2] = eye_dist * math.sin(rot_angle)
                    eye[0] = eye_dist * math.cos(rot_angle)
        
        
        return ty, tx, target, eye, up, up_angle, rot_angle
