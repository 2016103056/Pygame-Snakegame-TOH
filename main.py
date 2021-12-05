# -*- coding: utf-8 -*-
"""


@author: Sanjana
"""

from tohgame import Game

g= Game()
while g.running:
    
    g.curr_menu.display_menu()
    #g.playing = True
    #
    g.gameplay()