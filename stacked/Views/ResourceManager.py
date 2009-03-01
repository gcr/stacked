#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import pygame

"""
    This manages handling and loading of our images, sounds, etc.
"""
RESOURCE_PATH = "."
IMAGE_PATH = os.path.join(RESOURCE_PATH, "img")
IMAGE_UI_PATH = os.path.join(IMAGE_PATH, "UI")

def load_ui_image(iname):
    return pygame.image.load( os.path.join( 
        IMAGE_UI_PATH, iname + ".png"
    ))

