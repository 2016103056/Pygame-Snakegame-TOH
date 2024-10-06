# -*- coding: utf-8 -*-
"""


@author: Sans08
"""

from tohgame import Game

g= Game()
while g.running:
    
    g.curr_menu.display_menu()
    #g.playing = True
    #
    g.gameplay()
