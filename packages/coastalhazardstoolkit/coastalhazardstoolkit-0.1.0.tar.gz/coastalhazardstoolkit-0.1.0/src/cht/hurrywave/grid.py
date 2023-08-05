# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 09:03:08 2022
@author: ormondt
"""
from pyproj import Transformer
import numpy as np
from matplotlib import path
import geopandas as gpd
import shapely
import math

class HurryWaveGrid:
    def __init__(self, hw):
        self.model = hw

    def build(self):
        self.x0 = self.model.input.variables.x0
        self.y0 = self.model.input.variables.y0
        self.dx = self.model.input.variables.dx
        self.dy = self.model.input.variables.dy
        self.nmax = self.model.input.variables.nmax
        self.mmax = self.model.input.variables.mmax
        self.rotation = self.model.input.variables.rotation

        cosrot = np.cos(self.rotation * np.pi / 180)
        sinrot = np.sin(self.rotation * np.pi / 180)

        # Corners
        xx = np.linspace(0.0,
                         self.mmax * self.dx,
                         num=self.mmax + 1)
        yy = np.linspace(0.0,
                         self.nmax * self.dy,
                         num=self.nmax + 1)
        xg0, yg0 = np.meshgrid(xx, yy)
        self.xg = self.x0 + xg0 * cosrot - yg0 * sinrot
        self.yg = self.y0 + xg0 * sinrot + yg0 * cosrot

        xx = np.linspace(0.5 * self.dx,
                         self.mmax * self.dx - 0.5 * self.dx,
                         num=self.mmax)
        yy = np.linspace(0.5 * self.dy,
                         self.nmax * self.dy - 0.5 * self.dy,
                         num=self.nmax)
        xg0, yg0 = np.meshgrid(xx, yy)
        self.xz = self.x0 + xg0 * cosrot - yg0 * sinrot
        self.yz = self.y0 + xg0 * sinrot + yg0 * cosrot

    def to_gdf(self):

        lines = []

        cosrot = math.cos(self.rotation*math.pi/180)
        sinrot = math.sin(self.rotation*math.pi/180)

        for n in range(self.nmax):
            for m in range(self.mmax):
                xa = self.x0 + m*self.dx*cosrot - n*self.dy*sinrot
                ya = self.y0 + m*self.dx*sinrot + n*self.dy*cosrot
                xb = self.x0 + (m + 1)*self.dx*cosrot - n*self.dy*sinrot
                yb = self.y0 + (m + 1)*self.dx*sinrot + n*self.dy*cosrot
                line = shapely.geometry.LineString([[xa, ya], [xb, yb]])
                lines.append(line)
                xb = self.x0 + m*self.dx*cosrot - (n + 1)*self.dy*sinrot
                yb = self.y0 + m*self.dx*sinrot + (n + 1)*self.dy*cosrot
                line = shapely.geometry.LineString([[xa, ya], [xb, yb]])
                lines.append(line)
        geom = shapely.geometry.MultiLineString(lines)
        gdf = gpd.GeoDataFrame(crs=self.model.crs, geometry=[geom])

        return gdf
