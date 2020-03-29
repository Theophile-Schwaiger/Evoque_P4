# -*- coding: utf-8 -*-

#ext_forces.py
#@author: Olivier Lantsoght
#
#Created on 23/05/2019
#Last update on 23/05/2019
#
#Copyright 2019 Universite Catholique de Louvain


import numpy as np
from math import cos, pi


def user_ExtForces(PxF,RxF,VxF,OMxF,AxF,OMPxF,mbs,tsim,ixF):
    """ Compute the external force for a given force point

    :param PxF: the position of the point
    :param RxF: the rotation matrix of the point
    :param VxF: the velocity vector of the point
    :param OMxF: the angular velocity of the point
    :param AxF: the acceleration vector of the point
    :param OMPxF: the angular acceleration of the point
    :param mbs: the Data structure
    :param tsim: the simulation time
    :param ixF: the index of the force point
    
    """
    Kp = mbs.user_model['Fext']['K']
    Dp = mbs.user_model['Fext']['D']
    R0 = mbs.user_model['Fext']['R0']
 
    
    Fz = 0.0
    Fx=0.0
    Fy=0.0
    Fz=0.0
    Mx=0.0
    My=0.0
    Mz=0.0
    
    
    kroul = mbs.user_model['BAR']['kroul'] #N/degres ou N/rad
    li = mbs.user_model['BAR']['li'] #m
    lj = mbs.user_model['BAR']['lj'] #m
    
    kbad = kroul/((li + lj)**2) #N/m c est bizarre avec kroul
    
    
    if ixF == mbs.extforce_id["ExtForce_0"]:
        e = PxF[3] - (RxF[2,2]*R0)
#        print(tsim)
#        print(mbs.sensors[0].P)
#        print(mbs.sensors[1].P)
#        print(mbs.sensors[2].P)
#        print(mbs.sensors[3].P)
        #e = PxF[3] - R0
 
        ed = VxF[3]
        
        diff = mbs.sensors[1].P[3]-mbs.sensors[0].P[3] #verifier que c est dans le bon sens la force
        Fzbar = kbad * diff #N
        
        if mbs.process == 2:
            
            if e < 0:
                Fz = Kp*abs(e) + Dp*abs(ed) + Fzbar
            if e > 0:
            
                Fz = -(Kp*abs(e) + Dp*abs(ed)) + Fzbar
        
        else:
            
            if e < 0:
                
                #Fz = -Kp*e - Dp*ed 
                Fz = -Kp*e + Dp*abs(ed) + Fzbar

                
            else:
                
                Fz = 0 + Fzbar
                
    if ixF == mbs.extforce_id["ExtForce_1"]:
        e = PxF[3] - (RxF[2,2]*R0)
        #e = PxF[3] - R0
 
        ed = VxF[3]
        
        diff = mbs.sensors[1].P[3]-mbs.sensors[0].P[3] #verifier que c est dans le bon sens la force
        Fzbar = kbad * diff #N
        
        if mbs.process == 2:
            
            if e < 0:
                Fz = Kp*abs(e) + Dp*abs(ed) + Fzbar
            if e > 0:
            
                Fz = -(Kp*abs(e) + Dp*abs(ed)) + Fzbar
        
        else:
            
            if e < 0:
                
                #Fz = -Kp*e - Dp*ed 
                Fz = -Kp*e + Dp*abs(ed) + Fzbar

                
            else:
                
                Fz = 0 + Fzbar
                
    if ixF == mbs.extforce_id["ExtForce_2"]:
        e = PxF[3] - (RxF[2,2]*R0)
        #e = PxF[3] - R0
 
        ed = VxF[3]
        
        diff = mbs.sensors[1].P[3]-mbs.sensors[0].P[3] #verifier que c est dans le bon sens la force
        Fzbar = kbad * diff #N
        
        if mbs.process == 2:
            
            if e < 0:
                Fz = Kp*abs(e) + Dp*abs(ed) + Fzbar
            if e > 0:
            
                Fz = -(Kp*abs(e) + Dp*abs(ed)) + Fzbar
        
        else:
            
            if e < 0:
                
                #Fz = -Kp*e - Dp*ed 
                Fz = -Kp*e + Dp*abs(ed) + Fzbar

                
            else:
                
                Fz = 0 + Fzbar
                
    if ixF == mbs.extforce_id["ExtForce_3"]:
        e = PxF[3] - (RxF[2,2]*R0)
        #e = PxF[3] - R0
 
        ed = VxF[3]
        
        diff = mbs.sensors[1].P[3]-mbs.sensors[0].P[3] #verifier que c est dans le bon sens la force
        Fzbar = kbad * diff #N
        
        if mbs.process == 2:
            
            if e < 0:
                Fz = Kp*abs(e) + Dp*abs(ed) + Fzbar
            if e > 0:
            
                Fz = -(Kp*abs(e) + Dp*abs(ed)) + Fzbar
        
        else:
            
            if e < 0:
                
                #Fz = -Kp*e - Dp*ed 
                Fz = -Kp*e + Dp*abs(ed) + Fzbar

                
            else:
                
                Fz = 0 + Fzbar
                
    
    #idpt=mbs.xfidpt[ixF]
    #dxF = mbs.dpt[1:,idpt]
    dxF=np.array([0,0,-(PxF[3]/RxF[2,2])])
    Swr=np.zeros(9+1)
    Swr[1:]=np.r_[Fx,Fy,Fz,Mx,My,Mz,dxF]
        
    return Swr
