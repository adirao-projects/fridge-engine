from numba import jit, njit, vectorize
import random

import pygame
import sys
import pywavefront
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import * 
import numpy as np
import pandas as pd
import fuzzywuzzy as fw


verts = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)    
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),    
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

faces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),    
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1)
    )


class Entity:
    def __init__(self):
        self.verts
        
    def texture(self):
        pass
    
    def render(self):
        pass
    
    
    
def Cube():
    glBegin(GL_QUADS)
    for face in faces:
        x=0
        #glColor3fv((0,0,1))
        for vert in face:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verts[vert])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        glColor3fv((1,1,1))
        for vert in edge:
            glVertex3fv(verts[vert])
            
    glEnd()
    
    
scene = pywavefront.Wavefront('shoot.obj', collect_faces=True)

scene_box = (scene.vertices[0], scene.vertices[0])
for vertex in scene.vertices:
    min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
    scene_box = (min_v, max_v)

scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 5
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

def Model():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)

    for mesh in scene.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*scene.vertices[vertex_i])
        glEnd()

    glPopMatrix() 

def main():
    pygame.init()
    display= (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    glTranslatef(0.0, 0.0, -5)
    
    glRotatef(0, 0 ,0 ,0)
    
    #285, 107
    #799, 141
    #540:180
    
    
    while True:
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            x_new, y_new = pygame.mouse.get_pos()
            
            if x_new!=x:
               glRotatef(((x_new-x)/3),0,1,0)
               x=x_new
               
            if y_new!=y:
                glRotatef(((y_new-y)/3),1,0,0)
                y=y_new
                
                
            print("X:", x, "Y:", y)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    glTranslate(-0.1, 0, 0)
                    
                if event.key == pygame.K_LEFT:
                    glTranslate(0.1, 0, 0)
                    
                if event.key == pygame.K_UP:
                    glTranslate(0, 0, 0.1)
        
                if event.key == pygame.K_DOWN:
                    glTranslate(0, 0, -0.1)
                    
                if event.key == pygame.K_SPACE:
                    glTranslate(0, 0.1, 0)
                    
                if event.key == pygame.K_RCTRL:
                    glTranslate(0, -0.1, 0)
                    
                if event.key == pygame.K_q:
                    glRotatef(3,0,0,1)
                    
                if event.key == pygame.K_e:
                    glRotatef(3,1,0,-1)
 
        #glRotatef(1, 3 ,1 ,1)
        
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Model()
        Cube()  
        pygame.display.flip()
        pygame.time.wait(10)
        
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    