# -*- coding: utf-8 -*-
"""


@author: Sans08
"""

#from pygame.locals import *
#import pygame
#from random import randint #to give random position to coven members
#import time

import pygame
import time


class Menu():
    def __init__(self,game):
        self.game = game #access to all variabkes in game object
        self.mid_w,self.mid_h = self.game.height/2,self.game.width/2
        self.run_display = True # tells the menu to keep running
        
        self.cursor_rect = pygame.Rect(0,0,20,20) #cursor to select
        self.offset = -100 #souldnt go on text so set offset
        
    def draw_cursor(self):
        self.game.text_display('*',15,self.cursor_rect.x,self.cursor_rect.y)
        print("draw cursor")
    
    #blit menu on screen    
    def blit_screen(self):
        print("blit")
        self.game.window.blit(self.game.cover, (0,0)) #lets you kinda stick an image on the board
        pygame.display.update()
        self.game.reset_keys()
        #time.sleep(20)
#put menu as a parameter. this tells mainmenu to inherit the menu class      
class MainMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w,self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w,self.mid_h + 50
        self.quitx, self.quity = self.mid_w,self.mid_h + 70
        #assign starting position to cursor (will allign asterisk with text)
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        
#display menu function
    def display_menu(self):
        print("inside display_menu")
        self.run_display = True #to make sure menu disp is always true
        while self.run_display and self.game.playing ==False:
            self.game.check_event()
            #self.check_input()
           
            self.game.cover.fill(self.game.Black)
            print("post fill black")
            self.game.text_display("MAIN MENU",20,self.game.width / 2, self.game.height / 2 - 20)
            self.game.text_display("SCORE: " +str(self.game.score),20,self.game.width / 2, self.game.height / 2 - 60)
            self.game.text_display("PLAY",20,self.startx,self.starty)
            self.game.text_display("OPTIONS",20,self.optionsx,self.optionsy)
            self.game.text_display("QUIT",20,self.quitx,self.quity)
            self.draw_cursor()
            self.check_input()
            self.blit_screen()
            #to make sure everything is on the screen
       # time.sleep(20)
            
            
    def move_cursor(self):
        print("defualt state",self.state)
        if self.game.moveDown:
            if self.state == 'Start': #if the state is start and we press down it goes to options and so on
                self.cursor_rect.midtop = (self.optionsx +self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.quitx +self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.startx +self.offset, self.starty)
                self.state = 'Start'
            
        if self.game.moveUp:
            if self.state == 'Start': #if the state is start and we press down it goes to options and so on
                self.cursor_rect.midtop = (self.optionsx +self.offset, self.optionsy)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.quitx +self.offset, self.quity)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx +self.offset, self.starty)
                self.state = 'Start'
                    
    def check_input(self):
        self.move_cursor() # to check if the player wanted to move the cursor
        if self.game.START_KEY:
            print("state",self.state)
            if self.state == 'Start':
                self.game.playing = True
                self.game.score=0
                self.game.gameplay()
                
                print(self.game.playing)
            elif self.state == 'Options':
                self.game.playing = True
                #pygame.quit()
            elif self.state == 'Quit':
                self.game.playing = False
                pygame.quit()
            self.run_display = False
            
            
                
    
        
    
    
    
    


  
