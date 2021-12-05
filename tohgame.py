# -*- coding: utf-8 -*-
"""


@author: Sanjana
"""

import pygame
from random import randint #to give random position to coven members
import time
from menu import MainMenu

class Game:
    
    def __init__(self):
        pygame.init()
        self.running,self.playing,self.music_playing = True, False,False
        self.moveUp,self.moveDown,self.moveRight,self.moveLeft,self.move_init,self.START_KEY = False,False,False,False,False,False
        self.height,self.width = 500,500
        #self.display = pygame.Surface((self.height,self.width))
        self.window = pygame.display.set_mode((self.height,self.width))
        self.window_rect = self.window.get_rect()
        pygame.display.set_caption("HOOOOOOOOOTY")
        self.font_name = pygame.font.get_default_font()
        self.cover = pygame.Surface(self.window.get_size())
        self.cover = self.cover.convert()
        self.Black,self.White = (0,0,0),(255,255,255)
        self.curr_menu = MainMenu(self) # the game object passes itself to mainmenu
        self.score = 0
       
        
        
    def gameplay(self):
        self.check_event()
        
        
        print("gameplay")
        
        self.cover.fill(self.Black)  # lets you fill the board in any color
        self.window.blit(self.cover, (0,0)) #lets you kinda stick an image on the board
        pygame.display.update() #important: lets you refresh the screen. everytime you blit something you need to refresh the screen so it appears
        self.reset_keys()
        pygame.mixer.init() # initialize for sound
        step = 23
        #score = 0
        length = 2
        speed = 80
        x_hoot_position = [0] #horizonatal
        y_hoot_position = [0] #vertical
            
        for i in range(0,1000):
            x_hoot_position.append(-100)
            y_hoot_position.append(-100)
                
        heads = pygame.image.load("resources/head.png").convert_alpha() #hooty's beautiful evervescent face
        head = pygame.transform.scale(heads, (35,35)) #can't have his face toooo big
        print ("head",head)
        body_part_1_o = pygame.image.load("resources/hoopy.jpg").convert_alpha()
        body_part_1 = pygame.transform.scale(body_part_1_o,(35,35))
             
        covens = pygame.image.load("resources/coven.png").convert_alpha()
        coven = pygame.transform.scale(covens, (35,35))
    
    #storing the head and coven coords in variables
    
        pos_1 = head.get_rect() # get_rect pffttt ahem lets you get the coords of a given object
        pos_coven = coven.get_rect()
    
        print("pos",pos_coven)
    #storing the coords in the list we made before
    
        x_hoot_position[0] = pos_1.x
        y_hoot_position[0] = pos_1.y
    
    #giving random coords to the first coven members
    
        pos_coven.x = randint(2,10)*step
        pos_coven.y = randint(2,10)*step
    
    
        pygame.mixer.music.load("resources/bgm.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(loops = -1)
            
        while self.playing == True:
            print("true")
            self.check_event()
            self.window.blit(body_part_1,(-5,5))
            self.window.blit(head,(0,0))
                #print("blit")
                #moving each part of the body by giving them new coords
    
                #this loop makes sure that each part of the snake will take the pos before it. so we give updated coords to the entire list
            for i in range(length-1,0,-1):
                
                    #print("loop")
                x_hoot_position[i] = x_hoot_position[(i-1)]
                y_hoot_position[i] = y_hoot_position[(i-1)]
    
    #fill the screen with color to erase hooty
           
            self.cover.fill((0,0,0))
                
                
            for i in range(1,length):
                self.cover.blit(body_part_1, (x_hoot_position[i], y_hoot_position[i]))
            #print("image??")
            self.check_event()
            if self.moveUp:
            
                y_hoot_position[0] = y_hoot_position[0] - step
                self.window.blit(self.cover,(0,0))
                self.window.blit(head, (x_hoot_position[0],y_hoot_position[0]))
    
            if self.moveDown:
                y_hoot_position[0] = y_hoot_position[0] + step
                self.window.blit(self.cover, (0,0))
                self.window.blit(head, (x_hoot_position[0], y_hoot_position[0]))
            
            if self.moveRight:
                x_hoot_position[0] = x_hoot_position[0] + step
                self.window.blit(self.cover, (0,0))
                self.window.blit(head, (x_hoot_position[0],y_hoot_position[0]))
            
            if self.moveLeft:
                x_hoot_position[0] = x_hoot_position[0] - step
                self.window.blit(self.cover, (0,0))
                self.window.blit(head, (x_hoot_position[0], y_hoot_position[0]))
            if x_hoot_position [0] < self.window_rect.left:
                self.playing = False
                #menu(score)
            if x_hoot_position [0] +35 > self.window_rect.right:
                self.playing = False
                         #menu(score)
            if y_hoot_position[0] < self.window_rect.top:
                self.playing = False
                     #menu(score)
            if y_hoot_position[0] +35 > self.window_rect.bottom:
                self.playing = False
                    #menu(score)
                    
            if self.collision(x_hoot_position[0],y_hoot_position[0],x_hoot_position[i],y_hoot_position[i],0,0) and (self.move_init == True):
                self.playing = False
                pygame.mixer.music.pause()  
                time.sleep(10)
                    
            self.window.blit(coven, pos_coven)
        
        #call collision fnc to check if hoot collides with coven
        
            if self.collision(x_hoot_position[0],y_hoot_position[0], pos_coven.x,pos_coven.y,35,35):
                pos_coven.x = randint(1,20)* step
                pos_coven.y - randint(1,20)* step
                    
                for j in range(0,length):
                    while self.collision (pos_coven.x, pos_coven.y, x_hoot_position[j],y_hoot_position[j],35,35):
                        pos_coven.x=randint(1,20)*step
                        pos_coven.y=randint(1,20)*step
                    
                length = length + 1
                self.score = self.score + 1
                if(self.score ==10):
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('resources/trauma.mp3'), maxtime=600)
                    speed = 60
                if(self.score == 19):
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('resources/trauma.mp3'), maxtime=2500)
                    speed = 60
                if(self.score >= 20):
                    speed = 50
                if(self.score == 30):
                    speed = 45
                    pygame.mixer.music.load("resources/extreme.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play()
                    
            self.display_score(self.score)
        
            pygame.display.flip()
            time.sleep (speed / 1000)
            print(self.playing)
            if self.playing == False:
                pygame.mixer.music.pause()  
                self.curr_menu.display_menu()
                #self.text_display("Thanks for playing",20,self.height/2,self.width/2) 
                #time.sleep(20)
        
    def check_event(self):
        print("check state")
        #while (self.playing == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running,self.playing = False,False
                self.curr_menu.run_display = False
                pygame.quit()
             #if a key is being pressed   
            if event.type == pygame.KEYDOWN:
                
                
                if event.key == pygame.K_UP:
                    
                    
                    if self.moveUp == False and self.move_init == True:
                        
                        if self.moveDown == True:
                            
                            self.moveUp == False
                            
                        else:
                            
                            self.moveDown = self.moveRight = self.moveLeft = False
                            self.moveUp = self.move_init = True
                
                if event.key == pygame.K_DOWN:
                    if self.moveDown == False:
                        if self.moveUp == True:
                            self.moveDown == False
                        
                        else:
                            self.moveRight = self.moveLeft = self.moveUp = False
                            self.moveDown = self.move_init = True
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                    print("return key")
                            
                if event.key == pygame.K_RIGHT:
                    if self.moveRight == False:
                        if self.moveLeft == True:
                            self.moveRight == False
                        else:
                            self.moveLeft = self.moveUp = self.moveDown = False
                            self.moveRight = self.move_init = True
                
                if event.key == pygame.K_LEFT:
                    
                    if self.moveLeft == False:
                        if self.moveRight == True:
                        
                            
                    #if the snake is already going right them it cant go left so we invalidate the move by assigning moveLeft False
                            self.moveLeft == False
                        else:
                            self.moveRight = self.moveDown = self.moveUp = False #if its not moving right then set everything else to false and moveLeft to true
                            self.moveLeft = self.move_init = True
                            
                #if event.type == pygame.MOUSEBUTTONDOWN: 
                 #   self.button.on_click(event)
        
    def reset_keys(self):
        self.moveUp,self.moveDown,self.moveRight,self.moveLeft,self.move_init,self.START_KEY = False,False,False,False,False,False
        
    #passing x and y coords of two objects. if they collide it returns true else false
    def collision(self,x_coord_1,y_coord_1,x_coord_2,y_coord_2,hooty_size,coven_size):
        if((x_coord_1 + hooty_size >= x_coord_2) or (x_coord_1 >= x_coord_2)) and x_coord_1 <= x_coord_2 + coven_size:
            if ((y_coord_1 > y_coord_2) or (y_coord_1 + hooty_size > y_coord_2)) and y_coord_1 <= y_coord_2 + coven_size:
                return True
        #return False  # if only an x coord collides and not y that means theyre touching and not colliding so return false

    def display_score(self,score):
        font = pygame.font.SysFont("comicsansms", 15)
        text = font.render("Score: "+str(score), True,(250,250,250))
        self.window.blit(text,(400,0))
        
    def text_display(self,text,size,x,y):
        font = pygame.font.SysFont("calibri", 25)
        text_sur = font.render(text, True,(250,250,250))
        text_rect=text_sur.get_rect()
        text_rect.center=(x,y)
        self.cover.blit(text_sur,text_rect)
        
        
        
        
        

        
        
        
        
        