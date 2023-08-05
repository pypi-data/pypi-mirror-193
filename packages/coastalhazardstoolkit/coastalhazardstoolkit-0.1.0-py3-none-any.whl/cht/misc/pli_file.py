# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 12:08:35 2021

@author: ormondt
"""

#from cht.geometry import Polyline as polyline
import cht.misc.tekal as tek

class Polyline:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class PliFile:
    
    def __init__(self, file_name):
        
        self.file_name=file_name
        self.read()

    def read(self):
        
        D = tek.tekal(self.file_name)
        D.info()
        m=D.read(0)
        x = m[0,:,0]
        y = m[1,:,0]        
        self.x = x
        self.y = y

def read_pli_file(file_name):
    
    polylines = []

    D = tek.tekal(file_name)
    D.info()
    for j in range(len(D.blocks)):
        m=D.read(j)
        x = m[0,:,0]
        y = m[1,:,0]
        polylines.append(Polyline(x, y))
        
    return polylines    
        