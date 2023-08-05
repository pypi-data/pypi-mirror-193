# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:16:54 2022

@author: roelvink

BEWARE runup & flooding calculation
"""
import pandas as pd
import numpy as np
import xarray as xr
import pathlib
from scipy import stats
import os
import netCDF4 as nc
import mat73
from scipy import io
# from sklearn import neighbors
import array as ar
#import datetime as dt
from scipy import interpolate as intp
import time
import sys
import datetime

import cht.misc.misc_tools

class BEWARE:
    
    def __init__(self, input_file):               
       
        self.input = BewareInput()

        # Get the path of beware.inp
        self.path = os.path.dirname(input_file)
        self.read_input_file(input_file)
        
        self.flow_boundary_point = []
        self.wave_boundary_point = []
        self.testprofs = []
        
        if os.path.isabs(self.input.profsfile) is False:
            self.input.profsfile= os.path.join(self.path, self.input.profsfile)

        self.read_profile_characteristics()              
        self.read_wave_boundary_points()
        self.read_flow_boundary_points()
                       
    def run(self, Hs, Tp, WL, betab, testprofs, xbFile, match_runup=None, match_flooding=None):
        self.Hs = Hs
        self.Tp = Tp
        self.WL = WL
        self.betab = betab
            
        # Initialize: load matching for runup / flooding and initialize input / output vars
        BWvars=["Hs", "Tp", "WL", "betab", 'BWprof']
        outvars1 = []
        if match_runup is not None and self.input.runup==1:
            matchrunup = io.loadmat(match_runup, simplify_cells=True)
            BWvars.extend(["R2pIndex", "runupComponents"])
            outvars1.extend(["R2", "R2_wl", "R2_setup", 'R2_vlf', "R2_ig", "R2_hf",  r"R2_tot"])
        if match_flooding is not None and self.input.flooding==1:
            matchflooding = io.loadmat(match_flooding, simplify_cells=True)
            BWvars.extend([r"obs_05m.fp", r"obs_05m.infra_m0", r"obs_05m.fsplit",  r"obs_05m.gauss_scale", r"obs_05m.Hm0_HF", r"obs_05m.setup"])
            outvars1.extend([r"fsplit",  r"scale", r"fp", r"Hhf", r"setup", r"m0"])

        # Load XB results        
        ds = nc.Dataset(xbFile)
        BWdata={}
        for var in BWvars:
            BWdata[str(var)]=np.array(ds[str(var)][:].data, ndmin=2)

        # Initialize BEWARE profile output
        outvars2= [r"Prof", r"Xc",  r"Yc", r"Xo", r"Yo"]
        self.out={}
        for var in outvars1:
            a = np.empty((len(testprofs), len(Hs)))
            a[:] = np.nan
#            self.out[str(var)]= np.nan((len(testprofs), (len(Hs))))
            self.out[str(var)]= a
        for var in outvars2:
            a = np.empty((len(testprofs)))
            a[:] = np.nan
            self.out[str(var)]= a
#            self.out[str(var)]= np.nan((len(testprofs)))

        error=[]
        # Initialize profile id naming
        if match_runup is not None:
            profid= np.zeros(len(matchrunup['ProbNS3']['profid']))
            for i in range(len(matchrunup['ProbNS3']['profid'])):
                profid[i]= matchrunup['ProbNS3']['profid'][i]
        else:
            profid= np.zeros(len(matchflooding['ProbNS3']['profid']))
            for i in range(len(matchflooding['ProbNS3']['profid'])):
                profid[i]= matchflooding['ProbNS3']['profid'][i]
            
        for inputprof in range(len(testprofs)):                            
            print(inputprof)
            # t = time.time()
            ID = np.argwhere(testprofs[inputprof]==profid)[0][0]

            # Load forcing file into dictionary
            if np.shape(self.Hs)[0] == 1:
                forcing=np.array(np.concatenate((self.Hs[:, inputprof], self.Tp[:, inputprof], self.WL[:, inputprof],self.betab[inputprof]*np.ones(np.shape(self.Hs)[0]))), ndmin=2)
            else:
                forcing=np.transpose((self.Hs[:, inputprof], self.Tp[:, inputprof], self.WL[:, inputprof],self.betab[inputprof]*np.ones(np.shape(self.Hs)[0])))

            # Runup
            if match_runup is not None and self.input.runup==1:
                prob=matchrunup['ProbNS3']['ProbtoCR2'][ID]            # Get matching % of input profile to BW profiles
                idx= [i for i,v in enumerate(prob) if v > 0.01]             # Delete profiles with less than 1% matching
                
                bwProfiles= matchrunup['ProbNS3']['CR2repProf'][idx]             # Get id of matched bwprofiles
                prob=prob[idx] / sum(prob[idx])                             # correct probability of matching for deleted profiles
            
                # try:
                if len(prob)>=1:
    
                    savevars= ["R2", "R2_wl", "R2_setup", 'R2_vlf', "R2_ig", "R2_hf",  r"R2_tot", r"fsplit",  r"scale", r"fp", r"Hhf", r"setup",  r"m0"]
                    save={}
                    for var in savevars:
                        save[str(var)]= np.zeros((len(self.Hs),len(prob)))
                    
                    # intpData=np.zeros((16, 4))
        
                    for iforcings in range(np.shape(forcing)[0]): # Loop through forcing conditions
                            
    
                        for iprof in range(len(bwProfiles)): # Loop through matched BEWARE profiles range(len(prob))
                            if np.isnan(forcing).any():
                                cont=1   
                            else:
    
                                profval= np.where(bwProfiles[iprof]==BWdata['BWprof'])[0][0]
                                BWforcing=np.transpose((BWdata['Hs'][:,profval], BWdata['Tp'][:,profval],
                                                                            BWdata['WL'][:,profval], BWdata['betab'][:,profval])) 
                        
                                # Find nearest conditions (same for all profiles so only run once per forcing condition)  
                                df = forcing[iforcings,:]-BWforcing
                                lims=[]
                                for ilim in range(4):
                                    lims.append(BWforcing[df[:,ilim]>=0, ilim].max())
                                    lims.append(BWforcing[df[:,ilim]<0, ilim].min())
                                BWinds=np.where(np.all(((BWforcing[:,0]==lims[0]) | (BWforcing[:,0]==lims[1]), (BWforcing[:,1]==lims[2]) | (BWforcing[:,1]==lims[3]), 
                                    (BWforcing[:,2]==lims[4]) | (BWforcing[:,2]==lims[5]),(BWforcing[:,3]==lims[6]) | (BWforcing[:,3]==lims[7])), axis=0))
                                    
                                # lims=[] # nearest upper and lower values
                                # for ilim in range(4):
                                #     uniquelist= list(set(BWforcing[:,ilim]))
                                #     lims.append(next(uniquelist[i-1] for i,v in enumerate(uniquelist) if v>forcing[iforcings, ilim]))
                                #     lims.append(next(uniquelist[i]  for i,v in enumerate(uniquelist) if v>forcing[iforcings, ilim]))
                                # lims=np.array(lims)                                

                                # BWinds=[]
                                # for itmp in range(2):
                                #     for itmp2 in range(2):
                                #         for itmp3 in range(2):
                                #             for itmp4 in range(2):
                                #                 BWinds.append(np.argwhere(np.all((BWforcing[:,0]==lims[0+itmp], BWforcing[:,1]==lims[2+itmp2], BWforcing[:,2]==lims[4+itmp3], BWforcing[:,3]==lims[6+itmp4]), axis=0)))                     
                                # BWinds= np.squeeze(BWinds)

                                limsdim=[lims[1]-lims[0], lims[3]-lims[2], lims[5]-lims[4], lims[7]-lims[6]] # distance between BW conditions        
                                intpData= np.zeros((np.shape(BWinds)[1], 4))
                                intpData[0:np.shape(BWinds)[1], 0:4]= BWforcing[BWinds,:]
                            
                                # Calculate normalized geometric mean inverse distance
                                NGM= (1-abs((forcing[iforcings,:] - intpData) / (limsdim)))
                                NGMiD=np.prod(NGM, axis=1)**(1/len(intpData[0]))
                                P= NGMiD/ sum(NGMiD)
                                
                                R2= np.squeeze(BWdata['R2pIndex'][BWinds, profval])
                                R2comp= np.squeeze(BWdata['runupComponents'][BWinds, :, profval])
    
                                save['R2'][iforcings, iprof]=np.sum(R2*P*prob[iprof])
                                save['R2_wl'][iforcings, iprof]= np.sum(R2comp[:,0]*P*prob[iprof]) 
                                save['R2_setup'][iforcings,iprof]= np.sum(R2comp[:,1]*P*prob[iprof]) 
                                save['R2_vlf'][iforcings,iprof]= np.sum(R2comp[:,2]*P*prob[iprof]) 
                                save['R2_ig'][iforcings,iprof]= np.sum(R2comp[:,3]*P*prob[iprof]) 
                                save['R2_hf'][iforcings,iprof]= np.sum(R2comp[:,4]*P*prob[iprof]) 
                                save['R2_tot'][iforcings,iprof]= np.sum(R2comp[:,5]*P*prob[iprof]) 
                            
                    self.out['R2'][inputprof,:]       = np.sum(save['R2'],1)
                    self.out['R2_wl'][inputprof,:]    = np.sum(save['R2_wl'],1)
                    self.out['R2_setup'][inputprof,:] = np.sum(save['R2_setup'],1)
                    self.out['R2_vlf'][inputprof,:]   = np.sum(save['R2_vlf'],1)
                    self.out['R2_ig'][inputprof,:]    = np.sum(save['R2_ig'],1)
                    self.out['R2_hf'][inputprof,:]    = np.sum(save['R2_hf'],1)
                    self.out['R2_tot'][inputprof,:]   = np.sum(save['R2_tot'],1)
                    # print(np.squeeze(forcing[0:3,:]))
                    # self.out['BWForcing'][inputprof,:,:] = np.squeeze(forcing[:,0:3])
                    self.out['Prof'][inputprof]        =  int(matchrunup['ProbNS3']['profid'][ID])    
                    # self.out['Xc'][inputprof]        = self.input.profs['x_coast'][PRoutid]
                    # self.out['Yc'][inputprof]        = profs['y_coast'][PRoutid]
                    # self.out['Xo'][inputprof]        = profs['x_off'][PRoutid]
                    # self.out['Yo'][inputprof]        = profs['y_off'][PRoutid]
           
                # except:
                #     error.append(inputprof)
                #     print('error')
                    
                
            # Flooding
            if match_flooding is not None and self.input.flooding==1:
                prob=matchflooding['ProbNS3']['ProbtoCR2'][ID]            # Get matching % of input profile to BW profiles
                idx= [i for i,v in enumerate(prob) if v > 0.01]             # Delete profiles with less than 1% matching
                
                bwProfiles= matchflooding['ProbNS3']['CR2repProf'][idx]             # Get id of matched bwprofiles
                prob=prob[idx] / sum(prob[idx])                             # correct probability of matching for deleted profiles
                  
                try:
                    if len(prob)>=1:
        
                        savevars= [r"fsplit",  r"scale", r"fp", r"Hhf", r"setup",  r"m0"]
                        save={}
                        for var in savevars:
                            save[str(var)]= np.zeros((len(self.Hs),len(prob)))
                        
                        intpData=np.zeros((16, 4))
            
                        for iforcings in range(np.shape(forcing)[0]): # Loop through forcing conditions
                                
        
                            for iprof in range(len(bwProfiles)): # Loop through matched BEWARE profiles range(len(prob))
                                if np.isnan(forcing).any():
                                   cont=1   
                                else:
        
                                    profval= np.where(bwProfiles[iprof]==BWdata['BWprof'])[0][0]
                                    BWforcing=np.squeeze(np.array(np.transpose([BWdata['Hs'][:,profval], BWdata['Tp'][:,profval],
                                                                                BWdata['WL'][:,profval], BWdata['betab'][:,profval]]))) # faster?
                           
                                    # Find nearest conditions
                                    df = forcing[iforcings,:]-BWforcing
                                    lims=[]
                                    for ilim in range(4):
                                        lims.append(BWforcing[df[:,ilim]>=0, ilim].max())
                                        lims.append(BWforcing[df[:,ilim]<0, ilim].min())
                                    BWinds=np.where(np.all(((BWforcing[:,0]==lims[0]) | (BWforcing[:,0]==lims[1]), (BWforcing[:,1]==lims[2]) | (BWforcing[:,1]==lims[3]), 
                                        (BWforcing[:,2]==lims[4]) | (BWforcing[:,2]==lims[5]),(BWforcing[:,3]==lims[6]) | (BWforcing[:,3]==lims[7])), axis=0))

                                    # lims=[] # nearest upper and lower values
                                    # for ilim in range(4):
                                    #     uniquelist= list(set(BWforcing[:,ilim]))
                                    #     lims.append(next(uniquelist[i-1] for i,v in enumerate(uniquelist) if v>forcing[iforcings, ilim]))
                                    #     lims.append(next(uniquelist[i]  for i,v in enumerate(uniquelist) if v>forcing[iforcings, ilim]))
                                    # lims=np.array(lims)                                
                                                                
                                    # BWinds=[]
                                    # for itmp in range(2):
                                    #     for itmp2 in range(2):
                                    #         for itmp3 in range(2):
                                    #             for itmp4 in range(2):
                                    #                 BWinds.append(np.argwhere(np.all((BWforcing[:,0]==lims[0+itmp], BWforcing[:,1]==lims[2+itmp2], BWforcing[:,2]==lims[4+itmp3], BWforcing[:,3]==lims[6+itmp4]), axis=0)))
                                                            
                                    # BWinds= np.squeeze(BWinds)
                                    limsdim=[lims[1]-lims[0], lims[3]-lims[2], lims[5]-lims[4], lims[7]-lims[6]] # distance between BW conditions        
                                    intpData[0:16,0:4]= BWforcing[BWinds,:]
                                
                                    # Calculate normalized geometric mean inverse distance
                                    NGM= (1-abs((forcing[iforcings,:] - intpData) / (limsdim)))
                                    NGMiD=np.prod(NGM, axis=1)**(1/len(intpData[0]))
                                    P= NGMiD/ sum(NGMiD)
                                    
                                    # R2= np.squeeze(BWdata['R2pIndex'][BWinds, profval])
                                    # R2comp= np.squeeze(BWdata['runupComponents'][BWinds, :, profval])
                                                                    
                                    save['fsplit'][iforcings, iprof]= np.sum(np.squeeze(BWdata[r'obs_05m.fsplit'][BWinds, profval])*P*prob[iprof]) 
                                    save['scale'][iforcings, iprof]= np.sum(np.squeeze(BWdata[r'obs_05m.gauss_scale'][BWinds, profval])*P*prob[iprof]) 
                                    save['m0'][iforcings, iprof]= np.sum(np.squeeze(BWdata[r'obs_05m.infra_m0'][BWinds, profval])*P*prob[iprof])          
                                    save['fp'][iforcings, iprof]= np.sum(np.squeeze(BWdata[r'obs_05m.fp'][BWinds, profval])*P*prob[iprof]) 
                                    save['Hhf'][iforcings, iprof]= np.sum(np.squeeze(BWdata[r'obs_05m.Hm0_HF'][BWinds, profval])*P*prob[iprof])                        
                                    save['setup'][iforcings, iprof]= np.sum(np.squeeze(BWdata[r'obs_05m.setup'][BWinds, profval])*P*prob[iprof])        
                                    
                        # self.out['BWForcing'][inputprof,:,:] = np.squeeze(forcing[:,0:3])
                        # self.out['Prof'][inputprof]        =  int(match['ProbNS3']['profid'][ID][12:])    
                        # self.out['Xc'][inputprof]        = self.input.profs['x_coast'][PRoutid]
                        # self.out['Yc'][inputprof]        = profs['y_coast'][PRoutid]
                        # self.out['Xo'][inputprof]        = profs['x_off'][PRoutid]
                        # self.out['Yo'][inputprof]        = profs['y_off'][PRoutid]
        
                        self.out['fp'][inputprof,:]  = 0.5*np.sum(save['fsplit'],1)
                        self.out['m0'][inputprof,:]      = np.sum(save['m0'],1)
                        self.out['scale'][inputprof,:]   = np.sum(save['scale'],1)
                        self.out['setup'][inputprof,:]   = np.sum(save['setup'],1)
    
                except:
                    error.append(inputprof)  
        # self.output=self.out
                        
    def write_flow_boundary_points(self, file_name=None):
    
        # Write BEWARE profs file
        if not file_name:
            if not self.input.bndfile:
                return
            file_name = os.path.join(self.path,
                                     self.input.bndfile)
        if not file_name:
            return

        fid = open(file_name, "w")
        for point in self.flow_boundary_point:
            if point.data is not None:
                string = f'{point.geometry.x:12.1f}{point.geometry.y:12.1f}'
                fid.write(string + r' ' + str(point.name) + '\n')
        fid.close()    

    def write_wave_boundary_points(self, file_name=None):
    
        # Write BEWARE profs file
        if not file_name:
            if not self.input.bwvfile:
                return
            file_name = os.path.join(self.path,
                                     self.input.bwvfile)
            
        if not file_name:
            return
            
        fid = open(file_name, "w")
        for point in self.wave_boundary_point:
            if point.data is not None:
                string = f'{point.geometry.x:12.1f}{point.geometry.y:12.1f}'
                fid.write(string + r' ' + str(point.name) + '\n')
        fid.close()  

    def read_profile_characteristics(self):

        df = pd.read_csv(self.input.profsfile, index_col=False,
            delim_whitespace=True)

        self.input.betab= df.beachslope.values
        self.input.xc= df.x_coast.values
        self.input.yc= df.y_coast.values
        self.input.xo= df.x_off.values
        self.input.yo= df.y_off.values
        self.input.coasttype= df.coasttype.values
        self.input.profid= df.profid.values

    def read_flow_boundary_points(self):
        
        # Read BEWARE profs file
        from cht.sfincs.sfincs import FlowBoundaryPoint
        
        prof_file = os.path.join(self.path, self.input.profsfile)
        # Read the bnd file
        # df = pd.read_csv(prof_file, index_col=False, header=None,
        #      delim_whitespace=True, names=['x', 'y', 'profs', 'type'])
        df = pd.read_csv(prof_file, index_col=False,
             delim_whitespace=True)
        
        # Loop through points
        for ind in range(len(df.x_off.values)):
            name = df.profid.values[ind]
            point = FlowBoundaryPoint(df.x_off.values[ind],
                                      df.y_off.values[ind],
                                       name=r'transect_' + str(int(name)))
                                      # name= str(int(name))) 
            self.flow_boundary_point.append(point)
            self.testprofs.append(name)
            
    def read_wave_boundary_points(self):
        
        # Read BEWARE profs file
        from cht.sfincs.sfincs import FlowBoundaryPoint

                
        prof_file = os.path.join(self.path, self.input.profsfile)
        
        # Read the bnd file
        df = pd.read_csv(prof_file, index_col=False,
             delim_whitespace=True)
        
        # Loop through points
        for ind in range(len(df.x_off.values)):
            name = df.profid.values[ind]
            point = FlowBoundaryPoint(df.x_off.values[ind],
                                      df.y_off.values[ind],
                                       name=r'transect_' + str(int(name)))
                                      # name= str(int(name))) 
            self.wave_boundary_point.append(point)             
        
    def write_wave_boundary_conditions(self, file_name=None):

        file_name = os.path.join(self.path,
                                 self.input.bwvfile)
                 
        # Build a new DataFrame

        file_name = os.path.join(self.path,
                                 'beware.bhs')
        self.bhsfile = file_name
        
        point_data = []
        for point in self.wave_boundary_point:
            if point.data is not None:
                # df = pd.concat([df, point.data['hm0']], axis=1)
                point_data.append(point.data['hm0'])
        df = pd.concat(point_data, axis=1)
        
        tmsec = pd.to_timedelta(df.index - self.input.tref, unit="s")
        df.index = tmsec.total_seconds()
        # df=df.replace(np.NaN, 0.1)
        df.to_csv(file_name,
                  index=True,
                  sep=" ",
                  header=False,
                  float_format="%0.3f")
        
        file_name = os.path.join(self.path,
                                 'beware.btp')
        self.btpfile = file_name

        point_data = []
        for point in self.wave_boundary_point:
            if point.data is not None:
                point_data.append(point.data['tp'])
        df = pd.concat(point_data, axis=1)
        df.index = tmsec.total_seconds()
        df=df.replace(np.NaN, 5.0)        
        df.to_csv(file_name,
                  index=True,
                  sep=" ",
                  header=False,
                  float_format="%0.3f")
        
    def write_flow_boundary_conditions(self, file_name=None):

        file_name = os.path.join(self.path,
                                 self.input.bzsfile)
        self.input.bzsfile = file_name

        # Build a new DataFrame
        point_data = []
        for point in self.flow_boundary_point:
            point_data.append(point.data)
            # df = pd.concat([df, point.data], axis=1)
            
        df = pd.concat(point_data, axis=1)
        print('write flow data')

        tmsec = pd.to_timedelta(df.index - self.input.tref, unit="s")
        df.index = tmsec.total_seconds()
        df.to_csv(file_name,
                  index=True,
                  sep=" ",
                  header=False,
                  float_format="%0.3f")
        print('Finish write flow data')
        
    def read_input_file(self, inputfile):
        
        # Reads beware.inp
        
        
        fid = open(inputfile, 'r')
        lines = fid.readlines()
        fid.close()
        for line in lines:
            str = line.split("=")
            if len(str)==1:
               # Empty line
               continue
            name = str[0].strip()
            val  = str[1].strip()
            try:
                # First try to convert to int
                val = int(val)
            except ValueError:
                try:
                    # Now try to convert to float
                    val = float(val)
                except:
                    pass
            if name == "tref":
                try:
                    val = datetime.datetime.strptime(val.rstrip(), '%Y%m%d %H%M%S')
                except:
                    val = None
            if name == "tstart":
                try:
                    val = datetime.datetime.strptime(val.rstrip(), '%Y%m%d %H%M%S')
                except:
                    val = None
            if name == "tstop":
                try:
                    val = datetime.datetime.strptime(val.rstrip(), '%Y%m%d %H%M%S')
                except:
                    val = None
            setattr(self.input, name, val)

    def read_data(self, input_file=None):
        if not input_file:
            output_path = os.path.join(self.cycle_path, "output\\")
            input_file= os.path.join(output_path, 'BEWARE_output.nc')

        ds = nc.Dataset(input_file)
        self.R2p=np.nan_to_num(ds[r"R2_tot"][:].data, copy=False, nan=0.0)
        self.setup=np.nan_to_num(ds[r"R2_set"][:].data, copy=False, nan=0.0)
        self.Hs=np.nan_to_num(ds[r"Hs"][:].data, copy=False, nan=0.0)
        self.Tp=np.nan_to_num(ds[r"Tp"][:].data, copy=False, nan=0.0)
        self.WL=np.nan_to_num(ds[r"R2_wl"][:].data, copy=False, nan=0.0)
        self.filename=ds[r"Profiles"][:].data
        self.swash=self.R2p-self.setup-self.WL

        self.xp=ds[r"x_coast"][:].data
        self.yp=ds[r"y_coast"][:].data
        
        self.xo=ds[r"x_off"][:].data
        self.yo=ds[r"y_off"][:].data
        
        if not self.input.tstart:
            ttt = ds["time"][:]
            dt  = datetime.timedelta(seconds=ttt[0])
            tout = datetime.datetime(1970,1,1) + dt
            self.input.tstart = tout
        
#     def write_to_geojson(self, output_path, scenario):
#         from geojson import Point, Feature, FeatureCollection, dump
#         from pyproj import Transformer

#         features = []
#         transformer = Transformer.from_crs(self.crs,
#                                            'WGS 84',
#                                            always_xy=True)
        
#         for ip in range(len(self.filename)):
#             x, y = transformer.transform(self.xp[ip],
#                                          self.yp[ip])
#             point = Point((x, y))
#             name = 'Loc nr: ' +  str(self.filename[ip])
                        
#             id = np.argmax(self.R2p[ip,:])                                                                       
#             features.append(Feature(geometry=point,
#                                     properties={"LocNr":int(self.filename[ip]),
#                                                 "Lon":x,
#                                                 "Lat":y,                                                
#                                                 "Setup":round(self.setup[ip, id],2),
#                                                 "Swash":round(self.swash[ip, id],2),
#                                                 "TWL":round(self.R2p[ip, id],2)}))
        
#         feature_collection = FeatureCollection(features)
        
#         if features:
#             feature_collection = FeatureCollection(features)
#             output_path_runup =  os.path.join(output_path, 'extreme_runup_height\\')
#             os.mkdir(output_path_runup)
#             file_name = os.path.join(output_path_runup,
#                                     "extreme_runup_height.geojson.js")
#             cht.misc.misc_tools.write_json_js(file_name, feature_collection, "var runup =")
            
#         features = []
            
#         for ip in range(len(self.filename)):
#             x, y = transformer.transform(self.xo[ip],
#                                          self.yo[ip])
#             point = Point((x, y))
#             name = 'Loc nr: ' +  str(self.filename[ip])
                        
#             id = np.argmax(self.R2p[ip,:])                                                                       
#             features.append(Feature(geometry=point,
#                                     properties={"LocNr":int(self.filename[ip]),
#                                                 "Lon": x,
#                                                 "Lat": y,
#                                                 "Hs":round(self.Hs[ip, id],2),
#                                                 "Tp":round(self.Tp[ip, id],1),
#                                                 "WL":round(self.WL[ip, id],2)}))
        
#         feature_collection = FeatureCollection(features)
        
#         if features:
#             feature_collection = FeatureCollection(features)
#             output_path_waves =  os.path.join(output_path, 'extreme_sea_level_and_wave_height\\')
#             os.mkdir(output_path_waves)
#             file_name = os.path.join(output_path_waves,     
#                                     "extreme_sea_level_and_wave_height.geojson.js")
#             cht.misc.misc_tools.write_json_js(file_name, feature_collection, "var swl =")
#         # with open(output_path + r"\\" + scenario + '.TWL.geojson.js', 'w') as fl:
#         #     fl.write('const point_' + scenario + '_TWL = ')
#         #     dump(feature_collection, fl)
#         #     fl.write("  \n   \n")
#         #     fl.write('pt_' + scenario + '_' + 'BT' + '_TWL.addData(point_' + scenario + '_TWL);')
    
        
#     def write_to_csv(self, output_path, scenario):
#         from geojson import Point, Feature, FeatureCollection, dump
#         from pyproj import Transformer

#         transformer = Transformer.from_crs(self.crs,
#                                            'WGS 84',
#                                            always_xy=True)
#         features = []
            
#         for ip in range(len(self.filename)):
#             x, y = transformer.transform(self.xp[ip],
#                                          self.yp[ip])
#             point = Point((x, y))
#             name = 'Loc nr: ' +  str(self.filename[ip])
                        
#             obs_file = "extreme_runup_height." + self.runid + "." +str(self.filename[ip]) + ".csv.js"
                                                          
#             features.append(Feature(geometry=point,
#                                     properties={"name":int(self.filename[ip]),
#                                                 "LocNr":int(self.filename[ip]),
#                                                 "Lon":x,
#                                                 "Lat":y,
#                                                 "model_name":self.name,
#                                                 "model_type":self.type,
#                                                 "TWL":  np.round(np.max(self.R2p[ip,:]),2),
#                                                 "obs_file": obs_file}))
#             d= {'WL': self.WL[ip,:],'Setup': self.setup[ip,:], 'Swash': self.swash[ip,:], 'Runup': self.R2p[ip,:]}       
#             v= pd.DataFrame(data=d, index =  pd.date_range(self.input.tstart, periods=len(self.swash[ip,:]), freq= '0.5H'))
    
#             local_file_path = os.path.join(output_path,  "timeseries",
#                                                obs_file)
# #            local_file_path = os.path.join(output_path,  
# #                                           obs_file)
#             s= v.to_csv(path_or_buf=None,
#                          date_format='%Y-%m-%dT%H:%M:%S',
#                          float_format='%.3f',
#                          header= False, index_label= 'datetime')        
            
#             cht.misc.misc_tools.write_csv_js(local_file_path, s, "var csv = `date_time,wl,setup,swash,runup")
                             
#         if features:
#             feature_collection = FeatureCollection(features)
#             runup_file = os.path.join(output_path,
#                                     "twls.geojson.js")
#             cht.misc.misc_tools.write_json_js(runup_file, feature_collection, "var TWL =")
            

class BewareInput():
    def __init__(self):
        self.xc = []
        self.yc = []
        self.xo = []
        self.yo = []
        self.betab = []
        self.coasttype = []
        self.profid = []
        
        self.tref = []
        self.tstart = []
        self.tstop = []
        self.folder = []
        self.dT = []
        self.runup = []
        self.flooding = []
        self.profsfile = "beware.profs"
        