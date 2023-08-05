# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 09:03:08 2022
@author: ormondt
"""
import os
import numpy as np
import geopandas as gpd
import shapely
import pandas as pd
from tabulate import tabulate

class HurryWaveBoundaryConditions:
    def __init__(self, hw):
        self.model = hw
        self.forcing = "timeseries"
        self.gdf = gpd.GeoDataFrame()
        self.times = []

    def read(self):
        # Read in all boundary data
        self.read_boundary_points()
        self.read_boundary_time_series()
        self.read_boundary_spectra()


    def write(self):
        # Write all boundary data
        self.write_boundary_points()
        if self.forcing == "timeseries":
            self.write_boundary_conditions_timeseries()
        else:
            self.write_boundary_conditions_spectra()


    def read_boundary_points(self):
        # Read bnd file
        if not self.model.input.variables.bndfile:
            return

        file_name = os.path.join(self.model.path, self.model.input.variables.bndfile)

        # Read the bnd file
        df = pd.read_csv(file_name, index_col=False, header=None,
                         delim_whitespace=True, names=['x', 'y'])

        gdf_list = []
        # Loop through points
        for ind in range(len(df.x.values)):
            name = str(ind + 1).zfill(4)
            x = df.x.values[ind]
            y = df.y.values[ind]
            point = shapely.geometry.Point(x, y)
            d = {"name": name, "timeseries": pd.DataFrame(), "geometry": point}
            gdf_list.append(d)
        self.gdf = gpd.GeoDataFrame(gdf_list, crs=self.model.crs)


    def write_boundary_points(self):
        # Write bnd file

        if len(self.gdf.index)==0:
            return

        if not self.model.input.variables.bndfile:
            self.model.input.variables.bndfile = "hurrywave.bnd"

        file_name = os.path.join(self.model.path, self.model.input.variables.bndfile)

        if self.model.crs.is_geographic:
            fid = open(file_name, "w")
            for index, row in self.gdf.iterrows():
                x = row["geometry"].coords[0][0]
                y = row["geometry"].coords[0][1]
                string = f'{x:12.6f}{y:12.6f}\n'
                fid.write(string)
            fid.close()
        else:
            fid = open(file_name, "w")
            for index, row in self.gdf.iterrows():
                x = row["geometry"].coords[0][0]
                y = row["geometry"].coords[0][1]
                string = f'{x:12.1f}{y:12.1f}\n'
                fid.write(string)
            fid.close()

    def add_point(self, x, y, hs=None, tp=None, wd=None, ds=None, sp=None):
        # Add point

        nrp = len(self.gdf.index)
        name = str(nrp + 1).zfill(4)
        point = shapely.geometry.Point(x, y)
        df = pd.DataFrame()     

        if hs:
            # Forcing by time series
        
            if not self.model.input.variables.bndfile:
                self.model.input.variables.bndfile = "hurrywave.bnd"
            if not self.model.input.variables.bhsfile:
                self.model.input.variables.bhsfile = "hurrywave.bhs"
            if not self.model.input.variables.btpfile:
                self.model.input.variables.btpfile = "hurrywave.btp"
            if not self.model.input.variables.bwdfile:
                self.model.input.variables.bwdfile = "hurrywave.bwd"
            if not self.model.input.variables.bdsfile:
                self.model.input.variables.bdsfile = "hurrywave.bds"
                        
            new = True
            if len(self.gdf.index)>0:
                new = False
                
            if new:
                # Start and stop time
                time = [self.model.input.variables.tstart, self.model.input.variables.tstop]
            else:
                # Get times from first point
                time = self.gdf.loc[0]["timeseries"].index    
            nt = len(time)

            hs = [hs] * nt
            tp = [tp] * nt
            wd = [wd] * nt
            ds = [ds] * nt

            df["time"] = time
            df["hs"] = hs
            df["tp"] = tp
            df["wd"] = wd
            df["ds"] = ds
            df = df.set_index("time")
            
        gdf_list = []
        d = {"name": name, "timeseries": df, "geometry": point}
        gdf_list.append(d)
        gdf_new = gpd.GeoDataFrame(gdf_list, crs=self.model.crs)        
        self.gdf = pd.concat([self.gdf, gdf_new], ignore_index=True)


    def delete_point(self, index):
        # Delete boundary point by index
        if len(self.gdf.index)==0:
            return
        if index<len(self.gdf.index):
            self.gdf = self.gdf.drop(index).reset_index(drop=True)
        

    def clear(self):
        self.gdf  = gpd.GeoDataFrame()


    def read_boundary_time_series(self):
        # Read HurryWave bhs, btp, bwd and bds files

        if not self.model.input.variables.bhsfile:
            return
        if len(self.gdf.index)==0:
            return

        tref = self.model.input.variables.tref

        # Time
        
        # Hs        
        file_name = os.path.join(self.model.path, self.model.input.variables.bhsfile)
        dffile = read_timeseries_file(file_name, tref)
        # Loop through boundary points
        for ip, point in self.gdf.iterrows():
            point["timeseries"]["time"] = dffile.index
            point["timeseries"]["hs"] = dffile.iloc[:, ip].values
            point["timeseries"].set_index("time", inplace=True)

        # Tp       
        file_name = os.path.join(self.model.path, self.model.input.variables.btpfile)
        dffile = read_timeseries_file(file_name, tref)
        for ip, point in self.gdf.iterrows():
            point["timeseries"]["tp"] = dffile.iloc[:, ip].values

        # Wd
        file_name = os.path.join(self.model.path, self.model.input.variables.bwdfile)
        dffile = read_timeseries_file(file_name, tref)
        for ip, point in self.gdf.iterrows():
            point["timeseries"]["wd"] = dffile.iloc[:, ip].values

        # Ds
        file_name = os.path.join(self.model.path, self.model.input.variables.bdsfile)
        dffile = read_timeseries_file(file_name, tref)
        for ip, point in self.gdf.iterrows():
            point["timeseries"]["ds"] = dffile.iloc[:, ip].values


    def read_boundary_spectra(self):
        # Read HurryWave bhs, btp, bwd and bds files
        if not self.model.input.variables.bspfile:
            return
        if len(self.gdf.index)==0:
            return

        tref = self.model.input.variables.tref
        file_name = os.path.join(self.model.path, self.model.input.variables.bspfile)
        print("Reading " + file_name)


    def write_boundary_conditions_timeseries(self):
        if len(self.gdf.index)==0:
            return
        # First get times from the first point (times in other points should be identical)
        time = self.gdf.loc[0]["timeseries"].index
        tref = self.model.input.variables.tref
        dt   = (time - tref).total_seconds()
        
        # Hs
        if not self.model.input.variables.bhsfile:
            self.model.input.variables.bhsfile = "hurrywave.bhs"            
        file_name = os.path.join(self.model.path, self.model.input.variables.bhsfile)
        # Build a new DataFrame
        df = pd.DataFrame()
        for ip, point in self.gdf.iterrows():
            df = pd.concat([df, point["timeseries"]["hs"]], axis=1)
        df.index = dt
        # df.to_csv(file_name,
        #           index=True,
        #           sep=" ",
        #           header=False,
        #           float_format="%.3f")
        to_fwf(df, file_name)
    
        # Tp
        if not self.model.input.variables.btpfile:
            self.model.input.variables.btpfile = "hurrywave.btp"            
        file_name = os.path.join(self.model.path, self.model.input.variables.btpfile)
        # Build a new DataFrame
        df = pd.DataFrame()
        for ip, point in self.gdf.iterrows():
            df = pd.concat([df, point["timeseries"]["tp"]], axis=1)
        df.index = dt
        # df.to_csv(file_name,
        #           index=True,
        #           sep=" ",
        #           header=False,
        #           float_format="%.3f")
        to_fwf(df, file_name)

        # Wd
        if not self.model.input.variables.bwdfile:
            self.model.input.variables.bwdfile = "hurrywave.bwd"            
        file_name = os.path.join(self.model.path, self.model.input.variables.bwdfile)
        # Build a new DataFrame
        df = pd.DataFrame()
        for ip, point in self.gdf.iterrows():
            df = pd.concat([df, point["timeseries"]["wd"]], axis=1)
        df.index = dt
        # df.to_csv(file_name,
        #           index=True,
        #           sep=" ",
        #           header=False,
        #           float_format="%.3f")
        to_fwf(df, file_name)

        # Ds
        if not self.model.input.variables.bdsfile:
            self.model.input.variables.bdsfile = "hurrywave.bds"            
        file_name = os.path.join(self.model.path, self.model.input.variables.bdsfile)
        # Build a new DataFrame
        df = pd.DataFrame()
        for ip, point in self.gdf.iterrows():
            df = pd.concat([df, point["timeseries"]["ds"]], axis=1)
        df.index = dt
        # df.to_csv(file_name,
        #           index=True,
        #           sep=" ",
        #           header=False,
        #           float_format="%.3f")
        to_fwf(df, file_name)

        
    def write_boundary_conditions_spectra(self):
        # Write HurryWave bsp file

        import xarray as xr

        file_name = os.path.join(self.model.path, self.model.input.variables.bspfile)

        times = self.boundary_point[0].data.point_spectrum2d.coords["time"].values
        #        tref  = np.datetime64(self.input.tref)
        #        times = np.single((times-tref)/1000000000)

        sigma = self.boundary_point[0].data.point_spectrum2d.coords["sigma"].values
        theta = self.boundary_point[0].data.point_spectrum2d.coords["theta"].values

        sp2 = np.zeros([len(times), len(self.boundary_point), len(theta), len(sigma)])

        points = []
        xs = np.zeros([len(self.boundary_point)])
        ys = np.zeros([len(self.boundary_point)])
        for ip, point in enumerate(self.boundary_point):
            points.append(point.name)
            xs[ip] = point.geometry.x
            ys[ip] = point.geometry.y
            sp2[:, ip, :, :] = point.data.point_spectrum2d.values

        # Convert to single
        xs = np.single(xs)
        ys = np.single(ys)
        sp2 = np.single(sp2)

        ds = xr.Dataset(
            data_vars=dict(point_spectrum2d=(["time", "stations", "theta", "sigma"], sp2),
                           station_x=(["stations"], xs),
                           station_y=(["stations"], ys),
                           ),
            coords=dict(time=times,
                        stations=points,
                        theta=theta,
                        sigma=sigma)
        )

        dstr = "seconds since " + self.input.tref.strftime("%Y%m%d %H%M%S")

        ds.to_netcdf(path=file_name,
                     mode='w',
                     encoding={'time': {'units': dstr}})
#        ds.to_netcdf(path=file_name,
#                     mode='w')

def read_timeseries_file(file_name, ref_date):
    # Returns a dataframe with time series for each of the columns
    df = pd.read_csv(file_name, index_col=0, header=None,
                     delim_whitespace=True)
    ts = ref_date + pd.to_timedelta(df.index, unit="s")
    df.index = ts
    return df

def to_fwf(df, fname, floatfmt=".3f"):
    indx = df.index.tolist()
    vals = df.values.tolist()
    for it, t in enumerate(vals):
        t.insert(0, indx[it])
    content = tabulate(vals, [], tablefmt="plain", floatfmt=floatfmt)
    open(fname, "w").write(content)
    